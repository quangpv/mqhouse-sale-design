# AUTH-01: Đăng nhập

- **Role:** Người dùng (Admin, Manager, HouseHolder, Sale)
- **Mô tả:** As a **người dùng**, I want **đăng nhập bằng email hoặc số điện thoại và mật khẩu**, So that **truy cập vào hệ thống theo quyền hạn của tôi**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form đăng nhập có: email/SĐT, mật khẩu, eye toggle
- [ ] Validate không để trống các trường
- [ ] Validate định dạng email hợp lệ hoặc SĐT hợp lệ (10 số)
- [ ] Hiển thị loading (spinner + disabled button) khi đang gọi API
- [ ] Hiển thị thông báo lỗi chung: "Sai thông tin đăng nhập" (không tiết lộ email tồn tại)
- [ ] Hiển thị lỗi riêng khi tài khoản bị khóa
- [ ] Đăng nhập thành công → chuyển đến màn hình chính
- [ ] Token tự động hết hạn sau thời gian nhất định → redirect về login
- [ ] Link "Quên mật khẩu?" → màn hình quên mật khẩu
- [ ] Link "Đăng ký ngay" → màn hình đăng ký

## Technical Tasks

### Backend
- Bảng `nguoi_dung`: id, email, so_dien_thoai, mat_khau (hash), trang_thai, ngay_dang_nhap_cuoi
- `POST /api/auth/login` — nhận email/SĐT, mat_khau → trả về access_token + refresh_token + thông tin user
- `POST /api/auth/logout` — blacklist token
- `POST /api/auth/refresh-token` — cấp access_token mới từ refresh_token
- Middleware xác thực JWT, kiểm tra token hết hạn
- Middleware kiểm tra token blacklist
- Gán JWT claims: user_id, role, permissions
- Rate limiting: giới hạn số lần đăng nhập sai theo IP (tối đa 5 lần/phút)

### Frontend
- Màn hình `login1.html`: form đăng nhập (email/SĐT, password, eye toggle)
- Validation: không để trống, định dạng email hoặc SĐT (10 số)
- Xử lý trạng thái loading (spinner + disabled button) khi gọi API
- Hiển thị lỗi: sai thông tin đăng nhập (generic), tài khoản bị khóa
- Redirect đến màn hình chính sau đăng nhập thành công
- Xử lý 401 từ API → tự động redirect về login
- Auto-refresh token trước khi hết hạn
- Link "Quên mật khẩu?" → forgotPassword, "Đăng ký ngay" → register
