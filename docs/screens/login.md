# Login (Đăng nhập)

## 1. Screen Overview
- **Screen name**: Login / Đăng nhập
- **Purpose**: Authenticate users with email/phone and password
- **Business context**: Primary entry point for the application. All roles (Sale, HouseHolder, Manager, Admin, Super Admin) authenticate through this screen.

## 2. UI Structure

### Layout sections
- **Container**: Mobile frame, 430px max-width, `h-screen sm:h-[880px]`, `bg background`, `rounded-modal shadow`
- **Top section**: Building icon (building-2) in blue circle, "Chào mừng trở lại" heading, subtitle "Đăng nhập để tiếp tục tìm kiếm căn hộ"
- **Form section**: Account input, password input with toggle, "Quên mật khẩu?" link
- **Footer section**: "Liên hệ quản trị viên để được tạo tài khoản" with inline "tạo tài khoản" link

### Components
- Building icon within a circular blue background
- Text input with user icon (Tài khoản) — placeholder "Email hoặc số điện thoại"
- Text input with lock icon and eye toggle (Mật khẩu)
- Primary button "Đăng nhập" with arrow-right icon
- Inline text link "tạo tài khoản" styled as a button

### Important UI patterns
- Eye toggle icon for password visibility
- Arrow icon on primary action button
- Semantic onclick handlers (no `<a>` tags, uses `onclick` attributes)
- No loading, error, or success states visible — static mockup

## 3. Entry Points
- App startup (default screen for unauthenticated users)
- After successful registration (redirect from register screen)
- After password reset completion
- After logout

## 4. States
- **Loading**: Not implemented in HTML mockup
- **Empty**: Both inputs empty on initial render
- **Error**: Not implemented in HTML mockup
- **Success**: Redirect to Home/Dashboard on submit

## 5. Business Rules
### Validation rules
- Email or phone number is required
- Password is required
- Login requires email/phone + password combination

### Permission rules
- JWT authentication required
- bcrypt password hashing
- Roles: Sale, HouseHolder, Manager, Admin, Super Admin — all login via this screen

### Conditional rendering rules
- Password visibility toggles via eye icon
- "tạo tài khoản" is an inline text link, not a standalone button

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| AUTH-01 | Đăng nhập | Specified |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Login | Home/Dashboard | Đăng nhập button |
| Login | Forgot Password | "Quên mật khẩu?" link |
| Login | Register | "tạo tài khoản" link |

## 8. Mapping Notes
- HTML maps directly to AUTH-01 (Đăng nhập)
- [DESIGN GAP] No loading or error states are defined in the HTML mockup. Need to define error messages for invalid credentials, network errors, and account lockout scenarios
- [DESIGN GAP] No visual distinction between email and phone login — single input field accepts both
- [ASSUMPTION] JWT tokens and bcrypt password hashing are backend concerns not reflected in the HTML mockup
