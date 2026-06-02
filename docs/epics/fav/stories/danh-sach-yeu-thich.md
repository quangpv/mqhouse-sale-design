# FAV-03: Danh sách yêu thích

- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem danh sách BĐS/phòng đã yêu thích**, So that **dễ dàng xem lại**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Tab: BĐS yêu thích / Phòng yêu thích
- [ ] Grid/card hiển thị: hình ảnh, tên, giá, trạng thái
- [ ] Xóa khỏi danh sách yêu thích
- [ ] Click → xem chi tiết

## Technical Tasks

### Backend
- `GET /api/favorites/properties`
- `GET /api/favorites/rooms`

### Frontend
- Tab UI + card list
