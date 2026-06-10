# OTP Verification (Xác thực OTP)

## 1. Screen Overview
- **Screen name**: OTP Verification / Xác thực OTP
- **Purpose**: Verify the 4-digit code sent to the user's email or phone to proceed with password reset
- **Business context**: Second step in the password recovery flow. Validates identity before allowing password reset.

## 2. UI Structure

### Layout sections
- **Top bar**: Back button (arrow-left) → Forgot Password
- **Header**: "Xác nhận OTP" title, subtitle explaining the 4-digit code was sent
- **OTP inputs section**: Four individual digit input boxes, centered, large
- **Action section**: "Xác nhận" button with shield-check icon and hover scale animation
- **Footer**: "Không nhận được mã?" with "Gửi lại mã mới" link

### Components
- Back navigation button
- 4× single-character OTP inputs: `maxlength=1`, `inputmode=numeric`, `pattern=[0-9]*`
- Primary button "Xác nhận" with shield-check icon and hover scale animation
- Inline text link "Gửi lại mã mới" (no onclick handler defined)

### Important UI patterns
- Automatic focus advancement between OTP inputs (expected behavior, not implemented in static HTML)
- Numeric-only keyboard on mobile (inputmode=numeric)
- Hover scale animation on submit button
- "Gửi lại mã mới" is present but has no onclick handler in the mockup

## 3. Entry Points
- Forgot Password → Submit

## 4. States
- **Loading**: Not implemented in HTML mockup
- **Empty**: All 4 OTP inputs empty on initial render
- **Error**: Not implemented in HTML mockup
- **Success**: Redirect to Reset Password on submit

## 5. Business Rules
### Validation rules
- All 4 digits must be entered
- Each input accepts exactly 1 character (`maxlength=1`)
- Only numeric characters allowed (`pattern=[0-9]*`)

### Permission rules
- OTP is valid for 5 minutes (from Spec.md)
- OTP is exactly 4 digits (from Spec.md)

### Conditional rendering rules
- "Gửi lại mã mới" link should be disabled or show countdown during the 5-minute OTP validity window

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| AUTH-04 | Xác thực OTP | Specified |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| OTP | Reset Password | Xác nhận button |
| OTP | Forgot Password | Back button |

## 8. Mapping Notes
- HTML maps directly to AUTH-04 (Xác thực OTP)
- [DESIGN GAP] No loading/error states or invalid code feedback defined in HTML
- [DESIGN GAP] No countdown timer or cooldown mechanism shown for "Gửi lại mã mới" — the 5-minute OTP expiry is documented in Spec.md but not reflected in the mockup
- [ASSUMPTION] Auto-focus advancement between digit inputs should be implemented in JavaScript (not shown in static HTML)
- [ASSUMPTION] OTP is delivered via the contact method provided on the Forgot Password screen (email or SMS)
