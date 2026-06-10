# Luồng xác thực người dùng

## 1. Flow Overview
- **Flow name**: Luồng xác thực người dùng
- **Actor**: All users (unauthenticated)
- **Description**: Quy trình đăng nhập, đăng ký, quên mật khẩu và đổi mật khẩu

## 2. Preconditions
- User chưa có session hoạt động
- Thiết bị có kết nối internet

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | login.md | User nhập email/SĐT + mật khẩu → tap "Đăng nhập" | AUTH-01 |
| 2 | dashboard.md | User được chuyển đến trang chủ | DASH-01 |
| 3 | change-password.md | User đổi mật khẩu từ profile | AUTH-06 |

### Quên mật khẩu (alternate sub-flow)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | login.md | User tap "Quên mật khẩu?" | AUTH-01 |
| 2 | forgot-password.md | User nhập email/SĐT → gửi OTP | AUTH-03 |
| 3 | otp-verification.md | User nhập mã 4 số → xác thực | AUTH-04 |
| 4 | reset-password.md | User nhập mật khẩu mới → xác nhận | AUTH-05 |
| 5 | login.md | User đăng nhập với mật khẩu mới | AUTH-01 |

## 4. Alternate Flows
- **Sai thông tin đăng nhập**: Hiển thị lỗi "Email/Mật khẩu không đúng", user ở lại màn hình login
- **OTP hết hạn**: User tap "Gửi lại mã" → OTP mới được gửi
- **Mật khẩu mới không khớp**: Validation error "Mật khẩu xác nhận không khớp"
- **Đăng ký**: User vào register.md → [ASSUMPTION] phải liên hệ admin để được cấp tài khoản (no self-registration)

## 5. Error Handling
- **Network error**: Toast "Kết nối thất bại, vui lòng thử lại"
- **Tài khoản bị khoá**: Thông báo "Tài khoản của bạn đã bị khoá. Vui lòng liên hệ quản trị viên."
- **Email/SĐT không tồn tại** (forgot password): Không thông báo tồn tại/không — chỉ báo "Nếu tài khoản tồn tại, mã OTP sẽ được gửi"
- **[ASSUMPTION] Rate limit**: Giới hạn 5 lần nhập OTP sai → khoá gửi lại trong 30 phút

## 6. Screens Involved
- login.md
- register.md
- forgot-password.md
- otp-verification.md
- reset-password.md
- change-password.md
