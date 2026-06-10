# Change Password (Thay đổi mật khẩu)

## 1. Screen Overview
- **Screen name**: Change Password / Thay đổi mật khẩu
- **Purpose**: Allow authenticated users to change their current password
- **Business context**: Accessed from the user profile. Requires current password verification and supports client-side validation with a success toast notification.

## 2. UI Structure

### Layout sections
- **Top bar**: Back button (arrow-left) → Profile, title "Thay đổi mật khẩu"
- **Security notice**: Warning text "Không chia sẻ mật khẩu với người khác"
- **Form section**: Old password, new password, confirm password inputs
- **Sticky bottom**: "Xác nhận" submit button
- **Success toast**: Hidden by default, shows on success with check icon, auto-hides after 3 seconds

### Components
- Back navigation button
- Security notice banner
- Old password input with eye toggle — placeholder "Nhập mật khẩu hiện tại"
- New password input with eye toggle — placeholder "Tối thiểu 8 ký tự"
- Confirm password input with eye toggle — placeholder "Nhập lại mật khẩu mới"
- Sticky bottom "Xác nhận" submit button
- Success toast notification (check icon, auto-hide 3s)

### Important UI patterns
- Sticky bottom button — always visible regardless of scroll position
- Success toast with auto-dismiss (3 seconds) — no user action required
- Eye toggle on all three password fields
- New password placeholder "Tối thiểu 8 ký tự" indicates minimum length requirement
- Client-side validation: new password vs confirm password match
- `handleSubmit()` and `togglePassword()` JavaScript functions defined
- Form reset on submit

## 3. Entry Points
- Profile → "Đổi mật khẩu" option

## 4. States
- **Loading**: Not implemented in HTML mockup
- **Empty**: All three inputs empty on initial render
- **Error**: Client-side validation — new password does not match confirm password (alert)
- **Error**: Not implemented — server-side errors (wrong old password, etc.)
- **Success**: Toast notification appears (check icon), form resets, user stays on page

## 5. Business Rules
### Validation rules
- Old password is required
- New password is required, minimum 8 characters (from placeholder hint)
- Confirm password is required
- New password must match confirm password (client-side check in `handleSubmit()`)
- Old password must be correct before change is allowed (server-side)

### Permission rules
- User must be authenticated
- User must provide correct current password

### Conditional rendering rules
- Eye toggle on all three inputs switches between password/text type
- Success toast is hidden by default (`hidden` class), visible only on successful submission
- Toast auto-hides after 3 seconds (`setTimeout`)

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| AUTH-06 | Đổi mật khẩu | Specified |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Change Password | Profile | Back button |
| Change Password | Change Password | Success (stays on page, shows toast) |

## 8. Mapping Notes
- HTML maps directly to AUTH-06 (Đổi mật khẩu)
- This is the most interactive form among all auth screens — includes JavaScript with client-side validation, toast notifications, password toggle, and form reset
- [DESIGN GAP] No server-side error handling defined in HTML (e.g., wrong old password, network error). Errors currently use a simple `alert()` which should be replaced with inline error messages
- [DESIGN GAP] No loading state for the submit button (should show spinner and disable during API call)
- [ASSUMPTION] "Tối thiểu 8 ký tự" from the new password placeholder is the minimum length requirement. This should be consistent with Reset Password screen (AUTH-05)
