# SHARE-04: Chia sẻ hình ảnh

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **chia sẻ hình ảnh BĐS/phòng**, So that **gửi ảnh trực tiếp cho người khác**

**Priority:** Low

**Acceptance Criteria:
- [ ] Nút "Chia sẻ hình ảnh"
- [ ] Chọn ảnh từ gallery của BĐS/phòng
- [ ] Share ảnh qua các app (native share)
- [ ] Có thể share nhiều ảnh cùng lúc

## Technical Tasks

### Backend
- `GET /api/share/:entityType/:entityId/images` - danh sách ảnh

### Frontend
- Image picker + native share API
