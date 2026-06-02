# FAV-05: Xóa lịch sử / yêu thích

- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xóa lịch sử xem hoặc yêu thích**, So that **làm sạch danh sách**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Xóa 1 item khỏi lịch sử
- [ ] Xóa tất cả lịch sử
- [ ] Xóa 1 item khỏi yêu thích
- [ ] Confirm dialog khi xóa tất cả

## Technical Tasks

### Backend
- `DELETE /api/history/properties/:id`
- `DELETE /api/history/properties` (xóa tất cả)
- `DELETE /api/favorites/properties/:id`

### Frontend
- Delete action, confirm dialog
