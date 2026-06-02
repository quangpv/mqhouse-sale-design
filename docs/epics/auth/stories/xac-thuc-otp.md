# AUTH-04: Xác thực OTP

- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng**, I want **nhập mã OTP đã được gửi qua email/SMS**, So that **xác thực danh tính để đặt lại mật khẩu**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập 6 số OTP (có thể split thành 6 ô riêng)
- [ ] Hiển thị email/SĐT đã gửi OTP (dạng ẩn: ***@gmail.com)
- [ ] Tự động focus ô tiếp theo khi nhập
- [ ] Validate mã OTP đủ 6 số
- [ ] Kiểm tra mã OTP còn hiệu lực (thời gian)
- [ ] Kiểm tra mã OTP chính xác
- [ ] Hiển thị lỗi nếu OTP sai
- [ ] Chức năng gửi lại OTP (countdown timer)
- [ ] OTP đúng → chuyển đến màn hình đặt lại mật khẩu

## Technical Tasks

### Backend
- Tạo bảng `otp` (id, identifier (email/SĐT), code, expires_at, used, created_at)
- `POST /api/auth/verify-otp` - nhận mã OTP + session_token → xác thực
- `POST /api/auth/resend-otp` - gửi lại OTP mới
- Tự động xóa OTP hết hạn (cron job)

### Frontend
- Màn hình otp.html: 6 ô nhập OTP với auto-focus
- Countdown timer cho nút "Gửi lại" (60s)
- Hiển thị thông báo lỗi/quá hạn OTP
- OTP chỉ gồm 6 chữ số
- Kiểm tra thời gian hiệu lực OTP (5 phút)
