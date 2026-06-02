# FAV-01: Yêu thích BĐS

- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **thêm BĐS vào danh sách yêu thích**, So that **dễ dàng tìm lại sau**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Icon trái tim trên card/chi tiết BĐS
- [ ] Click → toggle yêu thích
- [ ] Trạng thái active (đã thích) / inactive
- [ ] Animation khi toggle
- [ ] Chỉ cho user đã đăng nhập

## Technical Tasks

### Backend
- Database: Bảng `bat_dong_san_yeu_thich`
- `POST /api/favorites/properties/:id/toggle`
- `GET /api/favorites/properties/check/:id` - kiểm tra đã thích?

### Frontend
- Heart icon component
