# Quản lý thành viên (Members)

## 1. Screen Overview
- **Screen name**: Quản lý thành viên / Members
- **Purpose**: List, search, filter, create, edit, lock/unlock, and delete system users. Assign operating areas to users.
- **Business context**: Admin-level user management screen. Supports full CRUD for users across roles. Operating area assignment determines which geographical regions a user (Sale/Manager) can operate in.

## 2. UI Structure
### Layout sections
- **Header**: Title "Quản lý thành viên" with "+" add member button (circle, primary-blue).
- **Search bar**: Search icon + text input, full width.
- **Filter tabs**: 3 horizontal tabs — "Tất cả" (All, default active), "Đang hoạt động" (Active), "Đã khoá" (Locked). Each shows a count badge.
- **Member list**: Vertical scrollable list of member cards with context menu.
- **Empty state**: Centered "Không tìm thấy thành viên nào" with users icon (`w-16 h-16`).
- **Add/Edit dialog**: Bottom sheet overlay with form, avatar, and operating area selectors.
- **Confirmation dialog**: Centered modal with warning triangle icon, cancel/confirm buttons.

### Components
- **Member card**: Avatar (48px), name, phone, username, status badge (green "Đang hoạt động" / red "Đã khoá"), role badge (colored per role), operating area chips (city/district/ward), more-vertical context menu icon.
- **Context menu**: Dropdown with Edit (pencil), Lock/Unlock (lock), Delete (trash-2, red text) options.
- **Status badge**: Green pill for active, red pill for locked.
- **Role badge**: Colored badge per role (Sale/Chủ nhà/Quản lý khu vực/Admin).
- **Add/Edit bottom sheet**:
  - Avatar with randomize (dice) and upload (upload) buttons.
  - Form inputs: Name (`type="text"`), Phone (`type="tel"`), Username (`type="text"`), Password (`type="text"` with auto-generate button and eye toggle).
  - Role dropdown (`select`): Sale / Chủ nhà / Quản lý khu vực / Admin.
  - Status dropdown (edit mode only): Active / Locked.
  - Operating area: Cascading comboboxes — Province → District (multi-select chips) → Ward (multi-select chips).
- **Confirmation dialog**: Warning icon, descriptive text, "Huỷ" (cancel, outline) and "Xác nhận" (confirm, danger red) buttons.
- **Toast**: Success/error notification after CRUD operations.

### Important UI patterns
- Bottom sheet for forms (not full-screen navigation).
- Cascading location selectors: Province → District (chips) → Ward (chips).
- Searchable combobox for province/district/ward selection.
- Context menu anchored to each card's more-vertical button.
- Tab filters update the list without navigation.
- Auto-generated password with visibility toggle.

## 3. Entry Points
- Bottom tab bar tab "Thành viên".

## 4. States
- **Loading**: Not implemented in HTML mockup.
- **Empty**: "Không tìm thấy thành viên nào" message with users icon — shown when search yields no results or no users exist.
- **Error**: Not implemented in HTML mockup.
- **Success**: Member list populated with cards (5 mock users in HTML).

## 5. Business Rules
### Validation rules
- Name: required, no length specified.
- Phone: valid Vietnamese phone number (10-11 digits).
- Username: required, must be unique.
- Password: required for new users, optionally auto-generated.
- Role: always required.
- Operating area: at least one district required for Sale and Manager roles.

### Permission rules
- Role hierarchy: Super Admin > Admin > Manager > HouseHolder > Sale.
- Super Admin can create Admin; Admin can create Manager and below.
- A user cannot delete their own account.
- Locked users cannot log in.
- Only Admin and above can access this screen.

### Conditional rendering rules
- Status dropdown only visible in edit mode.
- Password field: auto-generate button generates a random password; eye toggle shows/hides.
- Delete option in context menu hidden for self.
- Operating area cascading: District options depend on Province selection; Ward options depend on District selection.
- Filter tabs: count badges update dynamically based on filtered list.
- Empty state shown when no members match the active filter/search.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| USER-01 | Danh sách người dùng | Specified |
| USER-02 | Tạo người dùng | Specified |
| USER-03 | Sửa người dùng | Specified |
| USER-04 | Khoá/Mở khoá người dùng | Specified |
| USER-06 | Gán khu vực quản lý | Specified |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Members | — | Standalone screen, no navigation to other screens |

## 8. Mapping Notes
- HTML file: `members.html` (879 lines).
- 5 mock users with mixed roles and statuses are hardcoded in JS (`mockUsers` array).
- The cascading location selector uses static mock data for provinces (Hồ Chí Minh, Hà Nội, Đà Nẵng), districts, and wards.
- [STORY GAP] USER-05 (Phân quyền theo vai trò) has a separate screen (`permission.html`). This screen focuses on user CRUD only.
- [DESIGN GAP] No loading state — assumes instant data. In practice, a loading skeleton or spinner would be needed.
- [ASSUMPTION] Password auto-generation uses a simple random string; no configurable password policy (length, special chars) is implemented.
- [ASSUMPTION] The role dropdown does not filter available roles based on the current user's role — the HTML mockup shows all roles regardless. This would need backend validation.
