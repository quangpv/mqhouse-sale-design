## PHONG-09: Danh sách phòng theo BĐS

- **Tên:** Danh sách phòng theo BĐS
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **xem danh sách phòng của một BĐS dạng grid**, So that **nắm được tổng quan các phòng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Grid hiển thị: hình ảnh, tên phòng, giá, diện tích, trạng thái
- [ ] Badge trạng thái: đang trống (xanh), đã cọc (vàng), đã thuê (đỏ), sắp trống (cam)
- [ ] Lọc theo trạng thái
- [ ] Quick action: sửa, đổi trạng thái (popover/dialog)
- [ ] Click vào phòng → xem chi tiết

## Technical Tasks

### Backend
- `GET /api/properties/:id/rooms`

### Frontend
- Room grid component (property-detail.html)
- Status badge component
- Quick-update bottom sheet (edit giá + status + customer)
