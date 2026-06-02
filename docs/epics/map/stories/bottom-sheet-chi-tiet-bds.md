# MAP-04: Bottom sheet chi tiết BĐS

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **kéo lên bottom sheet hiển thị danh sách BĐS trong khu vực**, So that **có thể xem và so sánh nhiều BĐS cùng lúc**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Bottom sheet kéo từ dưới lên (draggable)
- [ ] Hiển thị danh sách BĐS trong khung bản đồ hiện tại
- [ ] Mỗi item: hình ảnh, tên, giá, địa chỉ, trạng thái phòng
- [ ] Click vào item → focus marker và mở popup
- [ ] Bottom sheet có 2 trạng thái: thu gọn (collapsed) và mở rộng (expanded)
- [ ] Pull-to-refresh danh sách

## Technical Tasks

### Frontend
- Bottom sheet component (react-spring / framer-motion)
- Danh sách BĐS trong bottom sheet
- Sync giữa bottom sheet và marker trên bản đồ
- Pull-to-refresh
