# Register / Contact Admin (Liên hệ đăng ký)

## 1. Screen Overview
- **Screen name**: Register / Liên hệ đăng ký
- **Purpose**: Provide admin contact information for account creation requests
- **Business context**: Self-registration is not allowed. Users must contact an administrator to have an account created. This screen is purely informational.

## 2. UI Structure

### Layout sections
- **Top bar**: Back button (arrow-left icon) → login
- **Header**: Phone icon in blue circle, "Liên hệ đăng ký" heading, subtitle "Vui lòng liên hệ quản trị viên để được tạo tài khoản"
- **Contact cards section**: Two cards with contact details
- **Footer**: Primary button "Quay lại đăng nhập" → login

### Components
- Back navigation button (arrow-left icon)
- Phone icon in circular blue background
- Contact card — Phone: call icon, "Số điện thoại", "0987 666 2647" with `tel:` link
- Contact card — Email: mail icon, "Email", "admin@mqhouse.vn" with `mailto:` link
- Primary button "Quay lại đăng nhập"

### Important UI patterns
- No form fields — purely informational display
- Clickable phone number (tel: protocol)
- Clickable email address (mailto: protocol)
- Back button navigates to Login

## 3. Entry Points
- Login screen → "tạo tài khoản" link
- No direct sidebar navigation or menu entry

## 4. States
- **Loading**: Not applicable (static information page)
- **Empty**: Not applicable
- **Error**: Not applicable
- **Success**: Not applicable

## 5. Business Rules
### Validation rules
- No form validation — this is an informational screen

### Permission rules
- No authentication required (accessible before login)
- No self-registration allowed — admin must create accounts via User Management (USER-02)

### Conditional rendering rules
- N/A — static page

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| AUTH-02 | (Register) | Does not exist |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Register | Login | Back button / "Quay lại đăng nhập" button |

## 8. Mapping Notes
- HTML contact page replaces what would typically be a registration form
- [STORY GAP] No AUTH-02 story exists for this screen. The register screen provides admin contact information only — no self-registration flow is supported
- [STORY GAP] Account creation is delegated to admin User Management (USER-02), which is not part of the auth story set
- [ASSUMPTION] Phone "0987 666 2647" and email "admin@mqhouse.vn" are placeholder values to be replaced with real admin contact details in production
