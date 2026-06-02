# FAV-02: Yêu thích phòng

- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **thêm phòng vào danh sách yêu thích**, So that **dễ dàng tìm lại sau**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Icon trái tim trên card/chi tiết phòng
- [ ] Tương tự FAV-01

## Technical Tasks

### Backend
- Database: Bảng `phong_yeu_thich`
- `POST /api/favorites/rooms/:id/toggle`

### Frontend
- Heart icon (dùng chung component)
