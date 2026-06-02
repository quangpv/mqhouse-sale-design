## PHONG-02: Xem chi tiết phòng

- **Tên:** Xem chi tiết phòng
- **Role:** Tất cả (kể cả không đăng nhập)
- **Mô tả:** As a **người dùng**, I want **xem chi tiết phòng trong BĐS**, So that **đánh giá phòng có phù hợp để thuê**

**Priority:** High

**Acceptance Criteria:**
- [ ] Hiển thị: tên phòng, giá thuê, giá cọc, diện tích, loại phòng
- [ ] Gallery hình ảnh phòng
- [ ] Danh sách nội thất, tiện ích
- [ ] Danh sách dịch vụ kèm (giá, đơn vị)
- [ ] Trạng thái phòng hiện tại (đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống)
- [ ] Nút yêu thích, chia sẻ
- [ ] Thông tin khách thuê hiện tại (nếu đã thuê)

## Technical Tasks

### Backend
- `GET /api/rooms/:id` - chi tiết phòng
- `GET /api/rooms/:id/services` - dịch vụ kèm

### Frontend
- Màn hình room-detail.html
- Gallery, service list, status badge
- Customer info section (nếu đã thuê)
