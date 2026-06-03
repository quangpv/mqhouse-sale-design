#!/usr/bin/env python3
"""
Sync a local story.md to Jira: update parent Story + create/update [BE]/[FE] sub-tasks.
"""
import json, re, base64, urllib.request, urllib.parse, urllib.error, os, sys, time

JIRA_USER = 'quangpv.bs@gmail.com'
JIRA_BASE = 'https://quangpvbs.atlassian.net'
SUBTASK_ISSUE_TYPE = '10022'

def load_env(env_path):
    if not os.path.exists(env_path):
        return
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, _, val = line.partition('=')
                os.environ.setdefault(key.strip(), val.strip())

def jira_call(method, path, data=None):
    url = f"{JIRA_BASE}{path}"
    token = os.environ.get('JIRA_TOKEN', '')
    auth_str = base64.b64encode(f"{JIRA_USER}:{token}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_str}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode()
            return json.loads(body) if body.strip() else None
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        print(f"  ERROR {method} {path}: {e.code}")
        print(f"  Response: {err_body[:500]}")
        raise

def parse_story_md(filepath):
    """Parse a story.md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Title: first line # AUTH-02: ...
    title_match = re.match(r'^# (\S+): (.+)$', text, re.MULTILINE)
    code = title_match.group(1) if title_match else 'UNKNOWN'
    title = title_match.group(2).strip() if title_match else ''

    # Role
    role_match = re.search(r'\*\*Role:\*\*\s*(.+?)(?:\n|$)', text)
    role = role_match.group(1).strip() if role_match else ''

    # Description (user story)
    desc_match = re.search(r'\*\*Mô tả:\*\*\s*(.+?)(?:\n|$)', text)
    description = desc_match.group(1).strip() if desc_match else ''

    # Priority
    prio_match = re.search(r'\*\*Priority:\*\*\s*(.+?)(?:\n|$)', text)
    priority = prio_match.group(1).strip() if prio_match else 'Medium'

    # Acceptance Criteria
    ac_lines = []
    in_ac = False
    for line in text.split('\n'):
        stripped = line.strip()
        if '**Acceptance Criteria:**' in stripped:
            in_ac = True
            continue
        if in_ac:
            if stripped.startswith('- [') or stripped.startswith('* ['):
                ac_lines.append(re.sub(r'^[-*]\s*\[[ x]\]\s*', '', stripped))
            elif stripped.startswith('##'):
                break

    # Technical Tasks - Backend
    be_tasks = []
    fe_tasks = []
    current_section = None
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped == '### Backend':
            current_section = 'be'
            continue
        elif stripped == '### Frontend':
            current_section = 'fe'
            continue
        elif stripped.startswith('### ') or stripped.startswith('## '):
            current_section = None
            continue
        if current_section == 'be' and stripped.startswith('-'):
            be_tasks.append(stripped.lstrip('- '))
        elif current_section == 'fe' and stripped.startswith('-'):
            fe_tasks.append(stripped.lstrip('- '))

    return {
        'code': code,
        'title': title,
        'role': role,
        'description': description,
        'priority': priority,
        'acceptance': ac_lines,
        'backend_tasks': be_tasks,
        'frontend_tasks': fe_tasks
    }

def build_description(story):
    """Build Jira description (no technical tasks)."""
    parts = [
        f"Role: {story['role']}",
        f"User Story: {story['description']}",
        f"Priority: {story['priority']}"
    ]
    if story['acceptance']:
        ac_list = '\n'.join(f"- {ac}" for ac in story['acceptance'])
        parts.append(f"Acceptance Criteria:\n{ac_list}")
    return '\n\n'.join(parts)

def build_subtask_description(tasks, label):
    """Build sub-task description from task list."""
    if not tasks:
        return f"Technical Tasks - {label}:\n- (none)"
    task_list = '\n'.join(f"- {t}" for t in tasks)
    return f"Technical Tasks - {label}:\n{task_list}"

def sync_story(story_path, target_key, dry_run=False):
    """Sync a single story.md to a Jira issue."""
    story = parse_story_md(story_path)
    print(f"\nParsed: {story['code']}: {story['title']}")
    print(f"  Backend tasks: {len(story['backend_tasks'])}")
    print(f"  Frontend tasks: {len(story['frontend_tasks'])}")
    print(f"  AC items: {len(story['acceptance'])}")

    print(f"\n=== {target_key}: {story['code']} ===")

    new_summary = f"{story['code']}: {story['title']}"
    new_desc = build_description(story)

    priority_map = {'High': '2', 'Medium': '3', 'Low': '4'}
    priority_id = priority_map.get(story['priority'], '3')

    update_payload = {
        "fields": {
            "summary": new_summary,
            "description": new_desc,
            "priority": {"id": priority_id}
        }
    }

    if dry_run:
        print(f"  [DRY-RUN] Would UPDATE {target_key}")
        print(f"    summary: {new_summary}")
        print(f"    priority: {story['priority']} (id={priority_id})")
        print(f"    description: {new_desc[:80]}...")
    else:
        jira_call('PUT', f'/rest/api/2/issue/{target_key}', update_payload)
        print(f"  UPDATED {target_key}: {new_summary}")
        time.sleep(0.3)

    existing_subtasks = {}
    if not dry_run:
        try:
            jql = f'parent={target_key} AND issuetype=Subtask'
            search = jira_call('GET', f'/rest/api/3/search/jql?jql=' + urllib.parse.quote(jql) + '&fields=summary')
            for issue in search.get('issues', []):
                s = issue['fields']['summary']
                existing_subtasks[issue['key']] = s
        except Exception as e:
            print(f"  Warning: could not search existing sub-tasks: {e}")
        time.sleep(0.3)

    summary_be = f"[BE] {story['title']}"
    summary_fe = f"[FE] {story['title']}"

    def find_existing(prefix):
        for k, v in existing_subtasks.items():
            if v.startswith(prefix):
                return k
        return None

    be_desc = build_subtask_description(story['backend_tasks'], 'Backend')
    be_key = find_existing('[BE]')
    if be_key:
        if dry_run:
            print(f"  [DRY-RUN] Would UPDATE {be_key}: {summary_be}")
        else:
            jira_call('PUT', f'/rest/api/2/issue/{be_key}', {"fields": {"summary": summary_be, "description": be_desc}})
            print(f"  UPDATED {be_key}: {summary_be}")
            time.sleep(0.3)
    else:
        be_payload = {
            "fields": {
                "project": {"key": "MS"},
                "issuetype": {"id": SUBTASK_ISSUE_TYPE},
                "summary": summary_be,
                "description": be_desc,
                "parent": {"key": target_key}
            }
        }
        if dry_run:
            print(f"  [DRY-RUN] Would CREATE: {summary_be}")
        else:
            result = jira_call('POST', '/rest/api/2/issue', be_payload)
            print(f"  CREATED {result['key']}: {summary_be}")
            time.sleep(0.3)

    fe_desc = build_subtask_description(story['frontend_tasks'], 'Frontend')
    fe_key = find_existing('[FE]')
    if fe_key:
        if dry_run:
            print(f"  [DRY-RUN] Would UPDATE {fe_key}: {summary_fe}")
        else:
            jira_call('PUT', f'/rest/api/2/issue/{fe_key}', {"fields": {"summary": summary_fe, "description": fe_desc}})
            print(f"  UPDATED {fe_key}: {summary_fe}")
            time.sleep(0.3)
    else:
        fe_payload = {
            "fields": {
                "project": {"key": "MS"},
                "issuetype": {"id": SUBTASK_ISSUE_TYPE},
                "summary": summary_fe,
                "description": fe_desc,
                "parent": {"key": target_key}
            }
        }
        if dry_run:
            print(f"  [DRY-RUN] Would CREATE: {summary_fe}")
        else:
            result = jira_call('POST', '/rest/api/2/issue', fe_payload)
            print(f"  CREATED {result['key']}: {summary_fe}")
            time.sleep(0.3)


def create_story(story_path, epic_key, dry_run=False):
    """Create a new Story in Jira under an epic, create sub-tasks, return the new key."""
    story = parse_story_md(story_path)
    print(f"\nParsed: {story['code']}: {story['title']}")
    print(f"  Backend tasks: {len(story['backend_tasks'])}")
    print(f"  Frontend tasks: {len(story['frontend_tasks'])}")

    new_summary = f"{story['code']}: {story['title']}"
    new_desc = build_description(story)

    priority_map = {'High': '2', 'Medium': '3', 'Low': '4'}
    priority_id = priority_map.get(story['priority'], '3')

    payload = {
        "fields": {
            "project": {"key": "MS"},
            "issuetype": {"id": "10024"},
            "summary": new_summary,
            "description": new_desc,
            "priority": {"id": priority_id},
            "parent": {"key": epic_key}
        }
    }

    if dry_run:
        print(f"  [DRY-RUN] Would CREATE Story: {new_summary} (epic={epic_key})")
        new_key = f"DRY-{story['code']}"
    else:
        result = jira_call('POST', '/rest/api/2/issue', payload)
        new_key = result['key']
        print(f"  CREATED {new_key}: {new_summary}")
        time.sleep(0.3)

    # Create BE sub-task
    be_desc = build_subtask_description(story['backend_tasks'], 'Backend')
    be_summary = f"[BE] {story['title']}"
    if dry_run:
        print(f"  [DRY-RUN] Would CREATE sub-task: {be_summary}")
    else:
        be_payload = {
            "fields": {
                "project": {"key": "MS"},
                "issuetype": {"id": SUBTASK_ISSUE_TYPE},
                "summary": be_summary,
                "description": be_desc,
                "parent": {"key": new_key}
            }
        }
        result = jira_call('POST', '/rest/api/2/issue', be_payload)
        print(f"  CREATED {result['key']}: {be_summary}")
        time.sleep(0.3)

    # Create FE sub-task
    fe_desc = build_subtask_description(story['frontend_tasks'], 'Frontend')
    fe_summary = f"[FE] {story['title']}"
    if dry_run:
        print(f"  [DRY-RUN] Would CREATE sub-task: {fe_summary}")
    else:
        fe_payload = {
            "fields": {
                "project": {"key": "MS"},
                "issuetype": {"id": SUBTASK_ISSUE_TYPE},
                "summary": fe_summary,
                "description": fe_desc,
                "parent": {"key": new_key}
            }
        }
        result = jira_call('POST', '/rest/api/2/issue', fe_payload)
        print(f"  CREATED {result['key']}: {fe_summary}")
        time.sleep(0.3)

    return new_key


BATCHES = {
    'auth': {
        'dir': 'auth/stories',
        'epic': None,
        'stories': [
            ('dang-nhap.md', 'MS-14'),
            ('dang-ky-tai-khoan.md', 'MS-15'),
            ('quen-mat-khau.md', 'MS-16'),
            ('xac-thuc-otp.md', 'MS-17'),
            ('dat-lai-mat-khau.md', 'MS-18'),
            ('doi-mat-khau.md', 'MS-19'),
        ]
    },
    'profile': {
        'dir': 'profile/stories',
        'epic': 'MS-9',
        'stories': [
            ('xem-ho-so.md', 'MS-62'),
            ('sua-ho-so.md', 'MS-63'),
            ('doi-avatar.md', 'MS-64'),
            ('xem-thong-tin-tai-khoan.md', 'MS-65'),
            ('ve-chung-toi.md', None),        # new story
            ('lien-he-ho-tro.md', None),       # new story
            ('dieu-khoan-chinh-sach.md', None), # new story
        ]
    },
}


def run_batch(batch_name, dry_run=False):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cfg = BATCHES.get(batch_name)
    if not cfg:
        print(f'ERROR: Unknown batch "{batch_name}". Available: {", ".join(BATCHES.keys())}')
        return

    stories_dir = os.path.join(script_dir, '..', 'epics', cfg['dir'])
    print(f'=== Syncing {len(cfg["stories"])} {batch_name.upper()} stories ===')
    print(f'  Epic: {cfg["epic"] or "N/A"}\n')

    for filename, jira_key in cfg['stories']:
        story_path = os.path.join(stories_dir, filename)
        if not os.path.exists(story_path):
            print(f'  SKIP {filename}: file not found')
            continue

        if jira_key:
            sync_story(story_path, jira_key, dry_run=dry_run)
        else:
            new_key = create_story(story_path, cfg['epic'], dry_run=dry_run)
            if not dry_run:
                print(f'  -> Created Jira key: {new_key}')

        print()

    print(f'=== {batch_name.upper()} batch done ===')


def main():
    dry_run = '--dry-run' in sys.argv

    script_dir = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(script_dir, '.env')
    load_env(dotenv_path)

    token = os.environ.get('JIRA_TOKEN', '')
    if not token:
        print('ERROR: Set JIRA_TOKEN in .env')
        sys.exit(1)

    single_file = None
    single_key = None
    batch_name = None
    for i, arg in enumerate(sys.argv):
        if arg == '--file' and i + 1 < len(sys.argv):
            single_file = sys.argv[i + 1]
        elif arg == '--key' and i + 1 < len(sys.argv):
            single_key = sys.argv[i + 1]
        elif arg == '--batch' and i + 1 < len(sys.argv):
            batch_name = sys.argv[i + 1]

    if single_file and single_key:
        sync_story(single_file, single_key, dry_run=dry_run)
    elif batch_name:
        run_batch(batch_name, dry_run=dry_run)
    else:
        run_batch('auth', dry_run=dry_run)
if __name__ == '__main__':
    main()
