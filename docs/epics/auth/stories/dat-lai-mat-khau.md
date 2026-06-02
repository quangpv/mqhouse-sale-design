# AUTH-05: Đặt lại mật khẩu

- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng đã xác thực OTP**, I want **nhập mật khẩu mới và xác nhận**, So that **có thể đăng nhập với mật khẩu mới**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập mật khẩu mới và xác nhận mật khẩu mới
- [ ] Validate mật khẩu không để trống, tối thiểu 6 ký tự
- [ ] Validate mật khẩu và xác nhận khớp nhau
- [ ] Mật khẩu mới không được trùng mật khẩu cũ
- [ ] Đặt lại thành công → chuyển đến màn hình đăng nhập với thông báo
- [ ] Vô hiệu hóa token OTP sau khi đặt lại thành công

## Technical Tasks

### Backend
- Cập nhật mật khẩu (hash) cho user
- `POST /api/auth/reset-password` - nhận mật khẩu mới + session_token → hash lưu

### Frontend
- Màn hình reset-password.html: form đặt lại mật khẩu
- Strength meter cho mật khẩu mới
- Thông báo thành công và redirect
- Validate độ mạnh mật khẩu
- Kiểm tra mật khẩu mới ≠ mật khẩu cũ
