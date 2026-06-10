# Reset Password (Đặt lại mật khẩu)

## 1. Screen Overview
- **Screen name**: Reset Password / Đặt lại mật khẩu
- **Purpose**: Create a new password after successful OTP verification
- **Business context**: Final step in the password recovery flow. Completes the reset process and redirects to login.

## 2. UI Structure

### Layout sections
- **Top bar**: Back button (arrow-left) → login
- **Header**: "Đặt lại mật khẩu" title, subtitle about creating a new password
- **Form section**: New password input, confirm password input
- **Action section**: "Xác nhận" button with check-circle-2 icon and hover scale animation

### Components
- Back navigation button
- New password input with lock icon and eye toggle — placeholder "Nhập mật khẩu mới"
- Confirm password input with lock icon and eye toggle — placeholder "Xác nhận lại mật khẩu mới"
- Primary button "Xác nhận" with check-circle-2 icon and hover scale animation

### Important UI patterns
- Eye toggle on both password inputs for visibility control
- Two-step password entry (new + confirm) to prevent typos
- Hover scale animation on submit button
- No password strength indicator visible in HTML mockup

## 3. Entry Points
- OTP Verification → Xác nhận (after valid OTP)

## 4. States
- **Loading**: Not implemented in HTML mockup
- **Empty**: Both password inputs empty on initial render
- **Error**: Not implemented in HTML mockup
- **Success**: Redirect to Login on submit

## 5. Business Rules
### Validation rules
- New password is required
- Confirm password must match new password
- Password minimum length should be enforced (see change-password for "Tối thiểu 8 ký tự" pattern)

### Permission rules
- Valid OTP must have been verified before accessing this screen

### Conditional rendering rules
- Eye toggle switches between password and text input type

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| AUTH-05 | Đặt lại mật khẩu | Specified |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Reset Password | Login | Xác nhận button / Back button |

## 8. Mapping Notes
- HTML maps directly to AUTH-05 (Đặt lại mật khẩu)
- [DESIGN GAP] No loading/error states defined in HTML. Need to handle: passwords don't match, weak password, reset link expired
- [DESIGN GAP] No password complexity requirements visibly enforced (e.g., minimum length, special characters). The change-password HTML references "Tối thiểu 8 ký tự" — this screen should have consistent rules
- [ASSUMPTION] Password hashing (bcrypt) is handled server-side after form submission
