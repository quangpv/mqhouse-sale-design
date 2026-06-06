# AGENTS.md — MQ Sale

**MQ Sale** is a Vietnamese real estate management SaaS frontend. Pure static HTML — no build tools, no package manager, no framework.

## Architecture

- **Frontend only** — This repo (`mqhouse-sale-design`) is the design/UI mockup. No backend, database, or API server code lives here. All pages are standalone `.html` files in the repo root.
- **No shared components** — Each HTML file is self-contained with its own inline `<script>` for Tailwind config, inline `<style>` for custom CSS, and CDN script tags.
- **CDN dependencies** — Tailwind CSS (`cdn.tailwindcss.com`), Lucide icons (`unpkg.com/lucide`), Inter font (Google Fonts). Nothing is installed locally.
- **Language** — All UI text, docs, and commits are in Vietnamese (`lang="vi"`).

## Design tokens

Every HTML file redeclares the same `tailwind.config` inline. When editing a file, check that its tokens match the others:

| Token | Value |
|-------|-------|
| `primary` | `#2563EB` |
| `background` | `#F8FAFC` |
| `surface` | `#FFFFFF` |
| `border` | `#E2E8F0` |
| `textPrimary` | `#0F172A` |
| `textSecondary` | `#64748B` |
| `borderRadius.card` | `16px` |
| `borderRadius.button` | `12px` |
| `borderRadius.input` | `10px` |
| `borderRadius.modal` | `20px` |

Inconsistent tokens between pages is a common source of visual drift.

## Documentation (source of truth)

- **`docs/Spec.md`** — Authoritative business rules: entities, relationships, state machines, permissions, hard constraints. Read this first before implementing any feature logic.
- **`docs/index.html`** — Interactive epic/story browser with acceptance criteria and task breakdowns.
- **`docs/Estimation.md`** — 6-month sprint plan (S1 started June 1, 2026).
- **`docs/epics/`** — Per-epic markdown files with detailed story specifications.
- **`docs/scripts/`** — Python Jira automation (`create_jira.py`, `sync_jira_story.py`). Requires `JIRA_TOKEN` in `.env`.

## Deployment

- **CNAME**: `sale.mqhouse.mywire.org` (GitHub Pages)
- **Remote**: `git@github.com:quangpv/mqhouse-sale-design.git`

## What's not here

- No `package.json`, no `node_modules`, no build step.
- No test runner, no linter, no CI configuration.
- No backend code whatsoever.

## Key constraints from docs/Spec.md

Refer to `docs/Spec.md` for the full rules, but these are hard constraints extracted from the spec:
- 5 user roles: Super Admin, Admin, Manager, HouseHolder, Sale
- Properties have 5 states: draft, pending, approved, rejected, expired
- Rooms have 8 states: empty, deposited, rented, about-to-vacate, plus 4 pending-approval variants
- Sale room status changes require approval; Admin/Manager/HouseHolder change directly
- Passwords hashed (bcrypt), JWT auth, OTP valid 5 min (4 digits)
- Max 10 images per property/room (jpg/png/webp), files max 10MB
