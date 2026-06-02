# BDS-07: Đánh dấu nổi bật

- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **đánh dấu BĐS nổi bật (featured)**, So that **BĐS được ưu tiên hiển thị và gợi ý**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Nút bật/tắt nổi bật trên chi tiết BĐS
- [ ] BĐS nổi bật hiển thị icon/vàng badge
- [ ] Ưu tiên hiển thị BĐS nổi bật trong danh sách
- [ ] BĐS nổi bật xuất hiện trong gợi ý

## Technical Tasks

### Backend
- Cập nhật trường `featured` trong bảng BĐS
- `PUT /api/properties/:id/feature` - toggle featured
- `GET /api/properties/featured` - danh sách nổi bật

### Frontend
- Featured toggle, badge UI
