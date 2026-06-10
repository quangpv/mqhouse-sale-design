# Phân quyền thành viên (Permissions)

## 1. Screen Overview
- **Screen name**: Phân quyền thành viên / Permissions
- **Purpose**: Assign granular permissions to roles. View and toggle individual permission flags per role.
- **Business context**: Role-based access control (RBAC) configuration screen. Super Admin and Admin users manage what each role can do (read, write, approve) across the system. 12 permissions across 3 categories.

## 2. UI Structure
### Layout sections
- **Header**: Back arrow (no target specified in HTML), title "Phân quyền thành viên", "Lưu" (Save) button with check-circle icon on the right.
- **Role selector**: 3 horizontal cards — Admin (`shield`), Quản lý khu vực (`map-pin`), Sale (`user-check`) — with icons. Active card has blue background (`bg-primary text-white`).
- **Role badge**: Text label showing the currently selected role name.
- **Permission list**: 12 checkbox rows, each containing:
  - Permission name in Vietnamese.
  - Permission code (e.g. `perm_approve_bds`) in `textSecondary`.
  - Category badge: "Duyệt" (amber), "Ghi" (blue), "Đọc" (green).
- **Select all / Deselect all**: Toggle link at top of permission list.
- **Success toast**: "Cập nhật đặc quyền thành công!" on save.

### Components
- **Role card**: Icon + role name, clickable, active state = blue fill.
- **Category badge**: Colored pill — Duyệt (amber/approve), Ghi (blue/write), Đọc (green/read).
- **Permission checkbox row**: Custom checkbox + name + code + category badge.
- **Select all toggle**: Inline link, toggles between "Chọn tất cả" and "Bỏ chọn tất cả".
- **Save button**: Header-right positioned, triggers `savePermissions()`.
- **Success toast**: Appears on save, auto-hides.

### Important UI patterns
- Horizontal card selector for roles (not a dropdown).
- Permissions grouped by category badge, not by visual section.
- Select all / deselect all as a single toggle link.
- Inline save in header (not a sticky bottom bar).

## 3. Entry Points
- Sidebar "Danh mục" → Tab 3 (Phân quyền). This screen IS Tab 3 of the Catalog section.

## 4. States
- **Loading**: Not implemented in HTML mockup.
- **Empty**: Not applicable — permission list is always populated (12 static permissions).
- **Error**: Not implemented in HTML mockup.
- **Success**: Toast "Cập nhật đặc quyền thành công!" triggered by `savePermissions()`.

## 5. Business Rules
### Validation rules
- At least one role must be selected (default: Admin).
- No validation on save — all checkbox states are saved as-is.

### Permission rules
- 12 permissions across 3 categories:
  - **Duyệt (Approve)** — amber badge: Approve properties, Approve rooms, Approve changes.
  - **Ghi (Write)** — blue badge: Create/edit properties, Create/edit rooms, Manage users (Admin only), Manage roles (Super Admin only).
  - **Đọc (Read)** — green badge: View dashboard, View properties, View rooms, View reports, View users.
- 5 roles in the system: Super Admin, Admin, Manager, HouseHolder, Sale.
- Only 3 roles are configurable in this UI: Admin, Quản lý khu vực (Manager), Sale.
- Super Admin role is not listed (managed separately or has full access by default).
- HouseHolder role is not listed (may have fixed permissions).
- Each role has a predefined permission set (mock data: 12 permission states per role).

### Conditional rendering rules
- Active role card highlighted with blue background.
- Select all / Deselect all text toggles based on current state.
- Permission checkboxes reflect the selected role's permission set.
- Save button always visible and enabled.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| USER-05 | Phân quyền theo vai trò | Specified |
| [DESIGN GAP] USER-07 | Quản lý vai trò (CRUD roles) | No dedicated UI |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Permissions | Catalog (Tab 3) | This screen IS Tab 3 of Catalog |

## 8. Mapping Notes
- HTML file: `permission.html` (277 lines).
- 3 roles × 12 permissions = 36 mock permission states in JS (`permissionData` object).
- `selectRole()`, `toggleSelectAll()`, `handleCheckboxChange()`, and `savePermissions()` are all wired in JS.
- The back button has no `onclick` handler defined — target is unspecified.
  - [DESIGN GAP] Back button navigation target is missing.
- [DESIGN GAP] USER-07 (Quản lý vai trò — CRUD for roles, e.g. create a new role, rename, delete) has no dedicated UI. Only permission assignment per existing role exists. Role management is entirely absent from the HTML mockups.
- [ASSUMPTION] Super Admin and HouseHolder roles exist but are not configurable in this screen — they likely have fixed permission sets (Super Admin = all permissions, HouseHolder = limited read-only).
- [ASSUMPTION] Changes are saved immediately on "Lưu" click; there is no confirmation dialog.
- The 3 category badges (Duyệt, Ghi, Đọc) are hardcoded in the permission data and not dynamically configurable.
