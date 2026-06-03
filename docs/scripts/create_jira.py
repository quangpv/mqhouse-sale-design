#!/usr/bin/env python3
"""
Read Epic.md and create all Epics, Sprints, and Stories in Jira.
"""
import json
import re
import base64
import urllib.request
import urllib.error
import sys
import os
import time

JIRA_TOKEN = ''
JIRA_USER = 'quangpv.bs@gmail.com'
JIRA_BASE = 'https://quangpvbs.atlassian.net'

def load_env(env_path):
    """Load .env file manually (no dependency on python-dotenv)."""
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
    auth_str = base64.b64encode(f"{JIRA_USER}:{os.environ.get('JIRA_TOKEN', '')}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_str}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        print(f"  ERROR {method} {path}: {e.code}")
        print(f"  Response: {err_body[:500]}")
        raise

def create_description(parts):
    """Convert parts list to plain text description."""
    return '\n\n'.join(parts)

def parse_epic_md(filepath):
    """Parse Epic.md and extract epics and stories."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    epics = {}
    stories = []
    current_epic = None

    epic_pattern = re.compile(r'^# Epic \d+: (.+)$', re.MULTILINE)
    story_pattern = re.compile(r'^## ([A-Z]+-\d+): (.+)$', re.MULTILINE)
    epic_code_pattern = re.compile(r'\*\*Mã Epic:\*\*\s*(\w+)')
    epic_objective_pattern = re.compile(r'\*\*Business Objective:\*\*\s*(.+?)(?:\n|$)')
    epic_desc_pattern = re.compile(r'\*\*Mô tả:\*\*\s*(.+?)(?:\n|$)')

    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]

        epic_match = re.match(r'^# Epic \d+: (.+)$', line)
        if epic_match:
            epic_name = epic_match.group(1).strip()
            j = i + 1
            epic_block = []
            while j < len(lines) and not re.match(r'^## [A-Z]+-\d+:', lines[j]) and not re.match(r'^# Epic \d+:', lines[j]):
                epic_block.append(lines[j])
                j += 1
            epic_text = '\n'.join(epic_block)
            code_match = epic_code_pattern.search(epic_text)
            obj_match = epic_objective_pattern.search(epic_text)
            desc_match = epic_desc_pattern.search(epic_text)
            if code_match:
                epic_code = code_match.group(1)
                epics[epic_code] = {
                    'name': epic_name,
                    'code': epic_code,
                    'objective': obj_match.group(1) if obj_match else '',
                    'description': desc_match.group(1) if desc_match else ''
                }
                current_epic = epic_code
            i = j
            continue

        story_match = re.match(r'^## ([A-Z]+-\d+): (.+)$', line)
        if story_match:
            story_code = story_match.group(1)
            story_title_line = story_match.group(2)
            epic_prefix = story_code.split('-')[0]
            j = i + 1
            story_lines = []
            story_section_end = j
            while j < len(lines):
                if re.match(r'^## [A-Z]+-\d+:', lines[j]) or re.match(r'^# Epic \d+:', lines[j]):
                    break
                if re.match(r'^---$', lines[j].strip()):
                    story_section_end = j
                    if j + 1 < len(lines) and re.match(r'^## [A-Z]+-\d+:', lines[j + 1]):
                        break
                    elif j + 1 < len(lines) and re.match(r'^# Epic \d+:', lines[j + 1]):
                        break
                story_lines.append(lines[j])
                j += 1
            story_text = '\n'.join(story_lines)

            title_match = re.search(r'\*\*Tên:\*\*\s*(.+?)(?:\n|$)', story_text)
            role_match = re.search(r'\*\*Role:\*\*\s*(.+?)(?:\n|$)', story_text)
            desc_match = re.search(r'\*\*Mô tả:\*\*\s*(.+?)(?:\n|$)', story_text)
            priority_match = re.search(r'\*\*Priority:\*\*\s*(.+?)(?:\n|$)', story_text)

            ac_start = story_text.find('**Acceptance Criteria:**')
            ac_end = story_text.find('**Technical Tasks:**')
            if ac_end == -1:
                ac_end = len(story_text)
            acceptance_criteria = []
            if ac_start != -1:
                ac_section = story_text[ac_start + len('**Acceptance Criteria:**'):ac_end].strip()
                for ac_line in ac_section.split('\n'):
                    ac_line = ac_line.strip()
                    if ac_line.startswith('- [') or ac_line.startswith('* ['):
                        acceptance_criteria.append(ac_line)

            story = {
                'code': story_code,
                'epic': epic_prefix,
                'title': title_match.group(1).strip() if title_match else story_title_line,
                'role': role_match.group(1).strip() if role_match else '',
                'description': desc_match.group(1).strip() if desc_match else '',
                'priority': priority_match.group(1).strip() if priority_match else 'Medium',
                'acceptance': acceptance_criteria
            }
            stories.append(story)

            while i < j and lines[i].strip() != '---':
                i += 1
            if i < j and lines[i].strip() == '---':
                i += 1
            continue

        i += 1

    return epics, stories

def create_epics(epics, dry_run=False):
    """Create all Epics in Jira."""
    epic_keys = {}
    print("\n=== Creating Epics ===")
    for code, epic in epics.items():
        summary = f"[{code}] {epic['name']}"
        desc_text = f"Business Objective: {epic['objective']}\n\nMô tả: {epic['description']}"
        payload = {
            "fields": {
                "project": {"key": "MS"},
                "issuetype": {"id": 10021},
                "summary": summary,
                "description": desc_text
            }
        }
        if dry_run:
            print(f"  [DRY-RUN] Would create Epic {code}: {summary}")
            epic_keys[code] = f'dry-run-{code}'
        else:
            try:
                result = jira_call('POST', '/rest/api/2/issue', payload)
                key = result['key']
                epic_keys[code] = key
                print(f"  Created Epic {code}: {key} - {summary}")
            except Exception as e:
                print(f"  FAILED to create Epic {code}: {e}")
            time.sleep(0.3)
    return epic_keys

def create_sprints(dry_run=False):
    """Create all 12 sprints (S1→S12) in Jira."""
    sprint_ids = {}
    print("\n=== Creating Sprints ===")
    for i in range(1, 13):
        name = f"MS Sprint {i}"
        payload = {
            "name": name,
            "originBoardId": 4,
            "goal": f"Sprint {i} implementation"
        }
        if dry_run:
            print(f"  [DRY-RUN] Would create {name}")
            sprint_ids[f'Sprint {i}'] = f'dry-run-{i}'
        else:
            try:
                result = jira_call('POST', '/rest/agile/1.0/sprint', payload)
                sid = result['id']
                sprint_ids[f'Sprint {i}'] = sid
                print(f"  Created {name}: id={sid}")
            except Exception as e:
                print(f"  FAILED to create {name}: {e}")
            time.sleep(0.3)
    return sprint_ids

STORY_SPRINT_MAP = {
    'AUTH-01': 1, 'AUTH-02': 1, 'AUTH-03': 1,
    'AUTH-04': 1, 'AUTH-05': 1, 'AUTH-06': 1,
    'CAT-01': 2, 'CAT-02': 2, 'CAT-03': 2,
    'CAT-04': 2, 'CAT-05': 2, 'CAT-06': 2, 'CAT-07': 2,
    'NAV-01': 2, 'NAV-02': 2,
    'USER-01': 3, 'USER-02': 3, 'USER-03': 3,
    'USER-04': 3, 'USER-05': 3, 'USER-06': 3, 'USER-07': 3,
    'BDS-01': 4, 'BDS-02': 4, 'BDS-03': 4, 'BDS-04': 4, 'BDS-08': 4,
    'PROFILE-01': 4, 'PROFILE-02': 4,
    'BDS-05': 5, 'BDS-06': 5, 'BDS-07': 5,
    'PHONG-01': 5, 'PHONG-02': 5,
    'PROFILE-03': 5, 'PROFILE-04': 5,
    'PHONG-03': 6, 'PHONG-04': 6, 'PHONG-05': 6, 'PHONG-06': 6, 'PHONG-09': 6,
    'NOTIF-01': 6, 'NOTIF-02': 6,
    'PHONG-07': 7, 'PHONG-08': 7,
    'DASH-01': 7, 'DASH-02': 7, 'DASH-03': 7,
    'NOTIF-03': 7, 'NOTIF-04': 7,
    'SEARCH-01': 8, 'SEARCH-02': 8, 'SEARCH-03': 8, 'SEARCH-04': 8,
    'MAP-01': 8, 'MAP-02': 8, 'MAP-03': 8, 'MAP-04': 8,
    'NOTIF-05': 9, 'NOTIF-06': 9,
    'SHARE-01': 9, 'SHARE-02': 9, 'SHARE-03': 9, 'SHARE-04': 9,
    'FAV-01': 9, 'FAV-02': 9, 'FAV-03': 9, 'FAV-04': 9, 'FAV-05': 9,
    'NAV-03': 9, 'NAV-04': 9, 'NAV-05': 9, 'NAV-06': 9, 'NAV-07': 9,
}

def get_sprint_id_for_story(story_code, sprint_ids):
    """Map story code to sprint number based on Estimation.md."""
    sprint_num = STORY_SPRINT_MAP.get(story_code)
    if sprint_num is None:
        print(f"  WARNING: No sprint mapping for {story_code}, skipping sprint assignment")
        return None
    return sprint_ids.get(f'Sprint {sprint_num}')

def create_stories(stories, epic_keys, sprint_ids, dry_run=False):
    """Create all Stories in Jira."""
    print("\n=== Creating Stories ===")
    created = 0
    failed = 0
    for story in stories:
        epic_prefix = story['epic']
        epic_key = epic_keys.get(epic_prefix)
        sprint_id = get_sprint_id_for_story(story['code'], sprint_ids)

        desc_parts = [f"User Story: {story['description']}", f"Role: {story['role']}", f"Priority: {story['priority']}"]
        if story['acceptance']:
            ac_list = []
            for ac in story['acceptance']:
                ac_clean = re.sub(r'^-\s*\[[ x]\]\s*', '', ac)
                ac_list.append(f"- {ac_clean}")
            desc_parts.append("Acceptance Criteria:\n" + '\n'.join(ac_list))
        desc_text = '\n\n'.join(desc_parts)

        payload = {
            "fields": {
                "project": {"key": "MS"},
                "issuetype": {"id": 10024},
                "summary": f"{story['code']}: {story['title']}",
                "description": desc_text,
                "parent": {"key": epic_key} if epic_key else None
            }
        }
        if payload["fields"]["parent"] is None:
            del payload["fields"]["parent"]

        if sprint_id:
            payload["fields"]["customfield_10020"] = sprint_id

        if dry_run:
            sprint_label = f" → Sprint {STORY_SPRINT_MAP.get(story['code'], '?')}" if story['code'] in STORY_SPRINT_MAP else ""
            print(f"  [DRY-RUN] Would create {story['code']}: {story['title']}{sprint_label}")
            created += 1
        else:
            try:
                result = jira_call('POST', '/rest/api/2/issue', payload)
                key = result['key']
                print(f"  Created {story['code']}: {key} - {story['title']}")
                created += 1
            except Exception as e:
                print(f"  FAILED {story['code']}: {e}")
                failed += 1
            time.sleep(0.35)

    print(f"\nDone: {created} created, {failed} failed")

def main():
    dry_run = '--dry-run' in sys.argv

    script_dir = os.path.dirname(os.path.abspath(__file__))
        dotenv_path = os.path.join(script_dir, '.env')
    load_env(dotenv_path)

    token = os.environ.get('JIRA_TOKEN', '')
    if not token:
        print("ERROR: Set JIRA_TOKEN environment variable")
        sys.exit(1)
    os.environ['JIRA_TOKEN'] = token

    epic_md_path = os.path.join(script_dir, '..', 'Epic.md')

    print("Parsing Epic.md...")
    epics, stories = parse_epic_md(epic_md_path)
    print(f"  Found {len(epics)} epics: {', '.join(epics.keys())}")
    print(f"  Found {len(stories)} stories")

    if dry_run:
        print("\n=== DRY RUN MODE — No API calls will be made ===\n")

    epic_keys = create_epics(epics, dry_run=dry_run)
    sprint_ids = create_sprints(dry_run=dry_run)
    create_stories(stories, epic_keys, sprint_ids, dry_run=dry_run)

if __name__ == '__main__':
    main()
