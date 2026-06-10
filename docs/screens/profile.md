# Hồ sơ (Profile)

## 1. Screen Overview
- **Screen name**: Hồ sơ / Profile
- **Purpose**: Display user profile summary and provide access to account management actions (edit info, change password, my properties, settings, logout).
- **Business context**: Acts as the user hub screen. All authenticated users (Sale, HouseHolder, Manager, Admin, Super Admin) access account-related features from here. Logout terminates the JWT session and redirects to Login.

## 2. UI Structure
### Layout sections
- **Avatar section**: Circular avatar (`w-20 h-20`), camera icon overlay for change, display name "Nguyễn Minh Thu", role badge "Sale" (primary blue).
- **Account actions card**: Grouped list items with chevron-right icons:
  - "Thông tin cá nhân" → navigates to User Info
  - "Đổi mật khẩu" → navigates to Change Password
  - "Bất động sản của tôi" → navigates to My Properties
- **Info & Support card**: Grouped list items with chevron-right icons:
  - "Về chúng tôi" — static, no link target
  - "Liên hệ và hỗ trợ" — static, no link target
  - "Điều khoản và chính sách" — static, no link target
  - "Xem toàn màn hình" — calls `postMessage({type: "toggleFullscreen"})`
- **Sign out section**: "Đăng xuất tài khoản" styled in error red (`text-red-500`), navigates to Login.

### Components
- **Circular avatar** with camera change icon overlay.
- **Role badge**: small primary-blue pill badge.
- **Menu item row**: icon + label + chevron-right, click navigates or triggers action.
- **Sign out row**: error-colored row with logout icon.

### Important UI patterns
- Card-based grouping for menu items (Account vs Info & Support).
- PostMessage-based fullscreen toggle (WebView bridge).
- Error color for destructive actions (logout).
- Static menu items with no navigation target are visually indistinguishable from active items.

## 3. Entry Points
- Bottom tab bar tab "Hồ sơ" (active state).

## 4. States
- **Loading**: Not implemented in HTML mockup. Assumes profile data is passed or pre-loaded.
- **Empty**: All sections always render with static mock data. No empty state.
- **Error**: Not implemented in HTML mockup.
- **Success**: Full profile display with name, avatar, and all menu groups.

## 5. Business Rules
### Validation rules
- None (no forms on this screen).

### Permission rules
- All authenticated users can view their own profile.
- [ASSUMPTION] Logout requires confirmed JWT session termination on backend.

### Conditional rendering rules
- Role badge text changes per user role (Sale / HouseHolder / Manager / Admin / Super Admin).
- Avatar camera overlay visible in all states (always editable).
- "Xem toàn màn hình" only relevant when running inside a WebView.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| PROFILE-01 | Xem hồ sơ | Specified |
| [DESIGN GAP] PROFILE-05 | Về chúng tôi | No dedicated screen |
| [DESIGN GAP] PROFILE-06 | Liên hệ và hỗ trợ | No dedicated screen |
| [DESIGN GAP] PROFILE-07 | Điều khoản và chính sách | No dedicated screen |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Profile | User Info | "Thông tin cá nhân" |
| Profile | Change Password | "Đổi mật khẩu" |
| Profile | My Properties | "Bất động sản của tôi" |
| Profile | Login | "Đăng xuất tài khoản" |

## 8. Mapping Notes
- HTML file: `profile.html` (188 lines).
- PROFILE-05, PROFILE-06, PROFILE-07 have menu items in the HTML but no corresponding screens. These are left as design gaps — the menu items are placeholders for future static pages (About, Contact, Terms).
- [ASSUMPTION] "Xem toàn màn hình" triggers a `postMessage` to the host WebView; the HTML mockup does not handle the response or toggle state.
- [ASSUMPTION] Static menu items ("Về chúng tôi", "Liên hệ và hỗ trợ", "Điều khoản và chính sách") are expected to be implemented as static HTML pages or WebView-local modals in a future iteration.
- Mock data uses "Nguyễn Minh Thu" / "Sale" — no dynamic data binding.
