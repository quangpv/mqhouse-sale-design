# AUTH-02: Đăng ký tài khoản

- **Role:** Khách hàng, Sale, HouseHolder
- **Mô tả:** As a **người dùng mới**, I want **gửi yêu cầu đăng ký qua email**, So that **admin xem xét và tạo tài khoản cho tôi**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form chỉ có 1 trường: email
- [ ] Validate email không để trống, đúng định dạng
- [ ] Gửi yêu cầu thành công → về màn hình đăng nhập với thông báo
- [ ] Admin nhận được thông báo yêu cầu tạo tài khoản mới
- [ ] Nút quay lại màn hình đăng nhập

## Technical Tasks

### Backend
- Lưu yêu cầu đăng ký (email, trạng thái chờ duyệt)
- `POST /api/auth/register-request` - nhận email → tạo yêu cầu → thông báo admin
- `GET /api/auth/register-requests` - admin xem danh sách yêu cầu
- `PUT /api/auth/register-requests/:id/approve` - admin duyệt
- `PUT /api/auth/register-requests/:id/reject` - admin từ chối
- Gửi thông báo cho admin khi có yêu cầu mới
- Gửi email thông báo cho user khi được duyệt/từ chối

### Frontend
- Màn hình register1.html: form email + validation
- Xử lý loading, success, error states
- Validate email không để trống, đúng định dạng
