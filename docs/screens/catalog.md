# Catalog

## 1. Screen Overview
- **Screen name**: Catalog (Danh mục hệ thống)
- **Purpose**: Administrative screen for managing system taxonomies: administrative geography, real estate categories, and role-based permissions.
- **Business context**: Back-office management interface. Only accessible to users with admin/manager roles. Central place to maintain reference data used across the entire platform.

## 2. UI Structure
### Layout sections
- **Header**: "Danh mục" title with 3 tabs and animated indicator.

#### Tab 1 — Địa giới hành chính (Administrative Geography)
- Search input + "+" add province button.
- Tree view: Provinces → Districts → Wards with expand/collapse chevrons.
- Expand/collapse all button.
- Geo detail panel: Name, admin code, type badge, parent level, status.
- Action buttons: Thêm con, Sửa, Xóa.
- Bottom sheets: Tạo tỉnh, Thêm cấp con, Sửa địa giới, Xóa địa giới.
- Empty state: "Không tìm thấy địa giới hành chính".

#### Tab 2 — Bất động sản (Real Estate Categories)
- **Loại phòng** (Room types): Expandable groups with design styles, edit/delete menus.
- **Loại hình BDS** (Property types): Chips with menus.
- **Nội thất** (Furniture): Grouped chips.
- **Tiện ích** (Amenities): Grouped chips.
- **Dịch vụ** (Services): 2-column grid cards (name, type badge, price, unit/period, meter reading).
- **Modals**: action-menu, name-dialog, service-dialog.

#### Tab 3 — Phân quyền (Role Permissions)
- **Role selector**: 4 pills (Admin, Quản lý khu vực, Sale, Chủ nhà) with badge count.
- **Permission list**: 12 checkbox items with color-coded categories (Duyệt / Xem / Ghi).
- Select all / deselect all toggle.
- Toast notification on save.

### Components
- **Tree view**: Nested lists with chevron expand/collapse, indentation levels.
- **Geo detail panel**: Slide-in panel showing selected node details.
- **Bottom sheets**: Create (tạo tỉnh), add child (thêm cấp con), edit (sửa), delete (xóa) with error state if children exist.
- **Chip groups**: Multi-select toggle chips for categories, furniture, amenities.
- **Service card**: 2-column grid card with name, type badge, price, unit/period, meter reading.
- **Role pills**: Segmented control for role selection.
- **Permission checkboxes**: Grouped by category with color coding.

### Important UI patterns
- Tab switching with animated underline indicator.
- Tree view for hierarchical geographic data.
- Expand/collapse all for bulk tree manipulation.
- Action menus on long-press or "..." button for list items.

## 3. Entry Points
- Bottom tab bar "Danh mục" — visible only to admin/manager roles.
- [ASSUMPTION] Tab visibility is role-gated at the app navigation level.

## 4. States
- **Loading**: Tree view skeleton (3 levels of shimmer), chip group skeletons, permission list skeleton.
- **Empty**:
  - Geography: "Không tìm thấy địa giới hành chính" + CTA to add first province.
  - Categories: "Chưa có loại phòng / loại hình / nội thất / tiện ích / dịch vụ."
  - Permissions: Always shows roles and checkboxes (cannot be empty).
- **Error**: Toast "Không thể tải danh mục. Vui lòng thử lại." for each tab.
- **Success**: Full tree/chips/permissions rendered as described.

## 5. Business Rules
### Validation rules
- **Geography delete**: Cannot delete a node that has children — error: "Không thể xóa. Địa giới này có chứa địa giới con."
- **Province/district/ward names**: Required, max 100 characters, unique at sibling level.
- **Service price**: Must be a positive number.
- **Permission save**: At least one permission must be selected per role.

### Permission rules
- **Tab 1 (Geography)**: Admin, Quản lý khu vực can CRUD. Sale and Chủ nhà are read-only.
- **Tab 2 (Categories)**: Admin only for CRUD. All other roles view-only.
- **Tab 3 (Permissions)**: Admin only. All other roles cannot access.
- [ASSUMPTION] Tab visibility itself is gated — non-admin users may not see the Permissions tab at all.

### Conditional rendering rules
- Delete button disabled (with explanation tooltip) when node has children.
- "Thêm con" and "Xóa" buttons only visible on hover/selection of a tree node.
- Permission checkboxes disabled when viewing a role the user cannot edit.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| CAT-01 | Quản lý địa giới hành chính | Planned |
| CAT-02 | Quản lý loại phòng & kiểu phòng | Planned |
| CAT-03 | Quản lý loại hình BDS | Planned |
| CAT-04 | Quản lý nội thất & tiện ích | Planned |
| CAT-05 | Quản lý dịch vụ | Planned |
| CAT-06 | Phân quyền vai trò | Planned |
| USER-05 | Phân quyền theo vai trò | Planned |
| CAT-07 | Quản lý file (tài liệu / hình ảnh) | Not planned |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Catalog | — | No navigation to other screens (standalone management) |

## 8. Mapping Notes
- [DESIGN GAP] CAT-07 (File management) has no separate UI — files are uploaded inline in property/room forms rather than managed in a centralized catalog.
- Geography tree expects hierarchical data structure: provinces → districts → wards (3 levels max).
- [ASSUMPTION] Permission changes take effect immediately on save (no staging or approval workflow).
- [STORY GAP] No bulk import/export for geography or category data.
