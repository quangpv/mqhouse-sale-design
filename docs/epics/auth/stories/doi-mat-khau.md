# AUTH-06: Đổi mật khẩu

- **Role:** Người dùng đã đăng nhập (Admin, Manager, HouseHolder, Sale)
- **Mô tả:** As a **người dùng đã đăng nhập**, I want **đổi mật khẩu của tôi khi biết mật khẩu cũ**, So that **bảo vệ tài khoản khi nghi ngờ lộ thông tin**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập: mật khẩu cũ, mật khẩu mới, xác nhận mật khẩu mới
- [ ] Validate không để trống các trường
- [ ] Kiểm tra mật khẩu cũ chính xác
- [ ] Mật khẩu mới không trùng mật khẩu cũ
- [ ] Mật khẩu mới và xác nhận khớp nhau
- [ ] Đổi thành công → thông báo → có thể logout hoặc ở lại
- [ ] Không cho phép đổi nếu tài khoản bị khóa

## Technical Tasks

### Backend
- `PUT /api/auth/change-password` - nhận mật khẩu cũ + mới → verify + hash lưu
- Xác thực JWT, lấy user_id từ token

### Frontend
- Màn hình change-password.html: form đổi mật khẩu
- Validate real-time mật khẩu cũ/mới/xác nhận
- Xử lý thông báo thành công/thất bại
- Mật khẩu mới tối thiểu 6 ký tự
- Kiểm tra mật khẩu cũ đúng trước khi cập nhật
