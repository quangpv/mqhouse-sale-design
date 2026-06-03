# USER-08: Duyệt/Từ chối yêu cầu đăng ký

- **Tên:** Quản lý yêu cầu đăng ký
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xem danh sách yêu cầu đăng ký và duyệt hoặc từ chối**, So that **kiểm soát ai được truy cập hệ thống**

**Priority:** High

**Acceptance Criteria:**
- [ ] Tab/bộ lọc "Chờ duyệt" trong members.html
- [ ] Danh sách: SĐT, tên đăng nhập, họ tên, vai trò yêu cầu, ngày gửi, trạng thái
- [ ] Filter tabs hiển thị số lượng tương ứng: Đang hoạt động (N), Chờ duyệt (N), Đã khóa (N)
- [ ] Nút "Duyệt" trên mỗi yêu cầu
  - [ ] Bottom sheet form (tái sử dụng dialog Thêm/Sửa thành viên), pre-filled với dữ liệu yêu cầu (họ tên, SĐT, tài khoản, vai trò)
  - [ ] Admin có thể điều chỉnh vai trò, trạng thái, khu vực hoạt động trước khi duyệt
  - [ ] Duyệt → tạo user trong hệ thống (trạng thái "Đang hoạt động")
  - [ ] Gửi thông báo cho user: "Tài khoản của bạn đã được duyệt"
- [ ] Nút "Từ chối" trên mỗi yêu cầu
  - [ ] Dialog nhập lý do từ chối (bắt buộc)
  - [ ] Từ chối → cập nhật trạng thái "Bị từ chối"
  - [ ] Gửi thông báo cho user kèm lý do
- [ ] Phân trang nếu nhiều yêu cầu
- [ ] Tìm kiếm theo SĐT, họ tên
- [ ] Có thể duyệt/từ chối nhiều yêu cầu cùng lúc (bulk)
- [ ] Chỉ Admin, Super Admin mới có quyền

## Technical Tasks

### Backend
- `GET /api/auth/register-requests?status=cho_duyet&page=1&limit=20&search=` — danh sách yêu cầu
- `PUT /api/auth/register-requests/:id/approve` — duyệt + tạo user
- `PUT /api/auth/register-requests/:id/reject` — từ chối (body: ly_do)
- `POST /api/auth/register-requests/bulk-approve` — duyệt hàng loạt
- `POST /api/auth/register-requests/bulk-reject` — từ chối hàng loạt
- Khi duyệt: tạo bản ghi trong bảng `nguoi_dung`, copy thông tin từ register_request
- Khi duyệt: tạo thông báo cho user
- Khi từ chối: ghi lý do, gửi thông báo cho user

### Frontend
- Tab "Chờ duyệt" trên members.html
- Bảng danh sách yêu cầu đăng ký
- Bottom sheet form cho duyệt (tái sử dụng form Thêm/Sửa thành viên) + Dialog riêng cho từ chối (kèm textarea lý do)
- Checkbox bulk action
- Toast notification khi thành công
