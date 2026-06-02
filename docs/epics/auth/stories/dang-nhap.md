# AUTH-01: Đăng nhập

- **Role:** Người dùng (Admin, Manager, HouseHolder, Sale)
- **Mô tả:** As a **người dùng**, I want **đăng nhập bằng tên đăng nhập và mật khẩu**, So that **truy cập vào hệ thống theo quyền hạn của tôi**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form đăng nhập có: tên đăng nhập, mật khẩu, checkbox ghi nhớ
- [ ] Validate không để trống các trường
- [ ] Hiển thị lỗi khi sai tên đăng nhập hoặc mật khẩu
- [ ] Hiển thị lỗi khi tài khoản bị khóa
- [ ] Đăng nhập thành công → chuyển đến Dashboard
- [ ] Ghi nhớ đăng nhập (remember me)
- [ ] Hiển thị mật khẩu (eye toggle)
- [ ] Link "Quên mật khẩu?" dẫn đến màn hình quên mật khẩu

## Technical Tasks

### Backend
- Bảng `nguoi_dung`: id, ten_dang_nhap, mat_khau (hash), trang_thai, ngay_dang_nhap_cuoi
- `POST /api/auth/login` — nhận ten_dang_nhap, mat_khau → trả về JWT token + thông tin user
- `POST /api/auth/logout` — xóa token
- Middleware xác thực JWT, kiểm tra token hết hạn
- Gán JWT claims: user_id, role, permissions

### Frontend
- Màn hình `login1.html`: form đăng nhập (username, password, eye toggle)
- Validation: kiểm tra không để trống, định dạng tên đăng nhập, mật khẩu ≥ 6 ký tự
- Checkbox "Ghi nhớ đăng nhập", lưu token vào localStorage/sessionStorage
- Xử lý trạng thái loading (spinner) khi gọi API
- Hiển thị lỗi: sai thông tin đăng nhập, tài khoản bị khóa
- Redirect đến Dashboard sau đăng nhập thành công
- Link "Quên mật khẩu?" → forgotPassword, "Đăng ký ngay" → register
