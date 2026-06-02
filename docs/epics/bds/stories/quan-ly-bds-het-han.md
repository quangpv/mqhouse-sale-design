# BDS-06: Quản lý BĐS hết hạn

- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin**, I want **xem và quản lý BĐS sắp hết hạn/hết hạn**, So that **gia hạn kịp thời hoặc gỡ tin**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách BĐS sắp hết hạn (trong 7 ngày)
- [ ] Danh sách BĐS đã hết hạn
- [ ] Nút "Gia hạn" → cập nhật ngày hết hạn mới
- [ ] Tự động chuyển trạng thái "hết hạn" khi đến ngày
- [ ] Thông báo cho chủ BĐS trước khi hết hạn
- [ ] Filter: Tất cả / Sắp hết hạn / Đã hết hạn

## Technical Tasks

### Backend
- Cron job / scheduler kiểm tra và cập nhật trạng thái hết hạn
- `GET /api/properties/expiring` - BĐS sắp hết hạn
- `GET /api/properties/expired` - BĐS đã hết hạn
- `PUT /api/properties/:id/renew` - gia hạn
- Gửi thông báo nhắc hết hạn

### Frontend
- Tab quản lý hết hạn
- Nút gia hạn
