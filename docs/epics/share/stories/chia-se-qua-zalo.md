# SHARE-01: Chia sẻ qua Zalo

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **chia sẻ BĐS/phòng qua Zalo**, So that **gửi cho bạn bè/đồng nghiệp**

**Priority:** Medium

**Acceptance Criteria:
- [ ] Nút chia sẻ Zalo trên chi tiết BĐS/phòng
- [ ] Mở Zalo app/web với nội dung đã soạn sẵn
- [ ] Nội dung: tên BĐS, giá, địa chỉ, link
- [ ] Có thể chọn nội dung chia sẻ: địa chỉ, loại phòng, nội thất, tiện ích, dịch vụ

## Technical Tasks

### Backend
- `GET /api/share/:entityType/:entityId` - dữ liệu chia sẻ

### Frontend
- Zalo sharing integration (Zalo SDK / URL scheme)
- Checkbox chọn nội dung (sharing.html)
