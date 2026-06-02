## USER-01: Danh sách người dùng

- **Tên:** Xem danh sách người dùng
- **Role:** Admin, Super Admin, Manager
- **Mô tả:** As a **Admin/Manager**, I want **xem danh sách người dùng trong hệ thống/khu vực**, So that **quản lý được nhân sự**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách dạng bảng: avatar, họ tên, tên đăng nhập, vai trò, email, SĐT, trạng thái
- [ ] Phân trang
- [ ] Tìm kiếm theo tên, email, SĐT
- [ ] Filter theo vai trò, trạng thái
- [ ] Manager chỉ xem được user trong khu vực quản lý
- [ ] Nút: Thêm mới, Sửa, Khóa/Mở khóa

## Technical Tasks

### Backend
- `GET /api/users` - danh sách (phân trang, search, filter)
- `GET /api/users/areas` - danh sách user trong khu vực (Manager)
- Manager: lọc theo UserArea

### Frontend
- Màn hình members.html: bảng danh sách
- Search bar, filter dropdowns
- Action buttons (sửa, khóa)
