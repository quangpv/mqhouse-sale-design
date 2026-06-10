# Forgot Password (Quên mật khẩu)

## 1. Screen Overview
- **Screen name**: Forgot Password / Quên mật khẩu
- **Purpose**: Initiate password recovery by submitting email or phone number to receive a reset code
- **Business context**: First step in the password recovery flow. Triggers OTP verification before allowing password reset.

## 2. UI Structure

### Layout sections
- **Top bar**: Back button (arrow-left) → login
- **Header**: "Khôi phục mật khẩu" title, subtitle explaining that a reset link/code will be sent
- **Form section**: Single input field for email or phone number with mail icon
- **Action section**: "Quên mật khẩu" submit button with key-round icon (hover rotate animation)
- **Footer**: "Nhớ ra mật khẩu? Đăng nhập" link → login

### Components
- Back navigation button
- Text input with mail icon — placeholder for email or phone number
- Primary button "Quên mật khẩu" with key-round icon and hover rotate animation
- Inline text link "Đăng nhập"

### Important UI patterns
- Hover rotate animation on the submit button icon
- Single input field accepts either email or phone number
- No client-side validation visible in HTML mockup

## 3. Entry Points
- Login screen → "Quên mật khẩu?" link

## 4. States
- **Loading**: Not implemented in HTML mockup
- **Empty**: Input field empty on initial render
- **Error**: Not implemented in HTML mockup
- **Success**: Redirect to OTP Verification on submit

## 5. Business Rules
### Validation rules
- Email or phone number is required
- Input must correspond to an existing account

### Permission rules
- No authentication required (accessible before login)

### Conditional rendering rules
- N/A

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| AUTH-03 | Quên mật khẩu | Specified |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Forgot Password | OTP Verification | Submit ("Quên mật khẩu" button) |
| Forgot Password | Login | Back button / "Đăng nhập" link |

## 8. Mapping Notes
- HTML maps directly to AUTH-03 (Quên mật khẩu)
- [DESIGN GAP] No loading/error states defined in HTML. Need to handle: account not found, send failure, rate limiting
- [ASSUMPTION] The system sends a 4-digit OTP as the reset code (consistent with AUTH-04 OTP screen)
