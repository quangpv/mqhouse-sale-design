# BDS-08: Danh sách BĐS của tôi

- **Role:** HouseHolder, Manager, Admin, Super Admin
- **Mô tả:** As a **người dùng**, I want **xem danh sách BĐS tôi đã tạo/quản lý**, So that **dễ dàng theo dõi và quản lý**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách BĐS dưới dạng grid/card
- [ ] Filter: Tất cả, Đã duyệt, Chờ duyệt, Hết hạn, Nháp
- [ ] Mỗi card hiển thị: hình ảnh, tên, giá, trạng thái, số phòng
- [ ] Nút: Sửa, Xóa, Xem chi tiết
- [ ] Tab: "Của tôi" và "Tất cả" (Admin/Manager)
- [ ] Tìm kiếm trong danh sách
- [ ] Phân trang

## Technical Tasks

### Backend
- `GET /api/properties/my-properties` - BĐS của tôi
- `GET /api/properties/managed` - BĐS trong KV (Manager)
- `GET /api/properties/all` - tất cả (Admin)
- Lọc theo quyền: HouseHolder chỉ thấy của mình

### Frontend
- Màn hình my-properties.html: grid danh sách
- Filter tabs, search bar
- Action buttons (sửa, xóa, xem)
