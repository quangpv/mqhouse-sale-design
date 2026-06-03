# AUTH-02: Đăng ký tài khoản

- **Role:** Khách hàng, Sale, HouseHolder
- **Mô tả:** As a **người dùng mới**, I want **đăng ký tài khoản qua form và xác thực SĐT bằng Zalo OTP**, So that **admin xem xét và kích hoạt tài khoản cho tôi**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form gồm: SĐT, tên đăng nhập, mật khẩu, xác nhận mật khẩu, họ tên, vai trò mong muốn
- [ ] Validate:
  - SĐT: 10-11 số, bắt đầu bằng 0
  - Tên đăng nhập: không trùng, không khoảng trắng/ký tự đặc biệt
  - Mật khẩu: ≥6 ký tự, có chữ và số
  - Xác nhận mật khẩu: khớp với mật khẩu
  - Họ tên: không để trống
  - Vai trò mong muốn: dropdown [Sale, HouseHolder] (không cho chọn Admin/Manager)
- [ ] Sau khi nhập form → nhấn "Gửi mã OTP" → gửi OTP qua Zalo
- [ ] Màn hình nhập OTP: 4 ô nhập, auto-focus, countdown 60s resend
- [ ] OTP hợp lệ → tạo yêu cầu đăng ký (trạng thái "Chờ duyệt")
- [ ] OTP sai/hết hạn → hiển thị lỗi
- [ ] Gửi yêu cầu thành công → về màn hình đăng nhập + thông báo "Yêu cầu đã gửi, chờ admin duyệt"
- [ ] Admin nhận được thông báo yêu cầu đăng ký mới
- [ ] Nút quay lại màn hình đăng nhập

## Technical Tasks

### Backend
- Tạo bảng `register_request`:
  - id, sdt, ten_dang_nhap, mat_khau_hash, ho_ten, vai_tro_id, trang_thai [Chờ duyệt, Đã duyệt, Bị từ chối], ly_do_tu_choi, created_at, updated_at
- `POST /api/auth/send-otp` — gửi OTP qua Zalo (tham số: sdt)
- `POST /api/auth/verify-otp` — xác thực OTP (tham số: sdt, otp_code)
- `POST /api/auth/register` — tạo yêu cầu đăng ký (sau khi OTP OK)
- `GET /api/auth/register-requests` — admin xem danh sách yêu cầu
- `PUT /api/auth/register-requests/:id/approve` — admin duyệt → tạo user + gửi thông báo
- `PUT /api/auth/register-requests/:id/reject` — admin từ chối (kèm lý do) + gửi thông báo
- Gửi thông báo cho admin khi có yêu cầu mới
- Gửi thông báo cho user khi được duyệt/từ chối (in-app)

### Frontend
- Màn hình register1.html: form 6 trường + validation
- Trường SĐT: mask phone number
- Trường mật khẩu: eye toggle
- Dropdown vai trò: chỉ Sale, HouseHolder
- Màn hình nhập OTP (gộp trong register1.html)
- Loading/success/error states
