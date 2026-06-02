# AUTH-03: Quên mật khẩu

- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng quên mật khẩu**, I want **nhập email/số điện thoại để nhận OTP**, So that **có thể đặt lại mật khẩu**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập email hoặc số điện thoại đã đăng ký
- [ ] Validate trường nhập không để trống
- [ ] Kiểm tra email/số điện thoại tồn tại trong hệ thống
- [ ] Hiển thị thông báo lỗi nếu không tìm thấy tài khoản
- [ ] Gửi OTP thành công → chuyển sang màn hình OTP
- [ ] Nút quay lại màn hình đăng nhập

## Technical Tasks

### Backend
- Query kiểm tra email/SĐT tồn tại
- `POST /api/auth/forgot-password` - nhận email/SĐT → tạo OTP → gửi OTP → trả về mã xác thực tạm
- Tích hợp dịch vụ gửi email/SMS
- Gửi email/SMS chứa mã OTP

### Frontend
- Màn hình forgot-password.html: form nhập email/SĐT
- Xử lý chuyển màn hình sau khi gửi OTP thành công
- Validate email/SĐT theo đúng định dạng
