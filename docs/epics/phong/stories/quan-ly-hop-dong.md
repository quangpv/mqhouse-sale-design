## PHONG-08: Quản lý hợp đồng

- **Tên:** Quản lý hợp đồng thuê phòng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin**, I want **quản lý hợp đồng thuê phòng**, So that **theo dõi lịch sử cho thuê và thanh toán**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách hợp đồng (đang hiệu lực, đã hết hạn, đã hủy)
- [ ] Tạo hợp đồng mới: chọn phòng, khách hàng, ngày BĐ-KT, giá thuê, cọc
- [ ] Upload file hợp đồng (PDF)
- [ ] Gia hạn hợp đồng
- [ ] Hủy hợp đồng
- [ ] Xem chi tiết hợp đồng

## Technical Tasks

### Backend
- CRUD bảng `hop_dong` + file hợp đồng
- `GET/POST/PUT/DELETE /api/contracts` - CRUD hợp đồng
- `POST /api/contracts/:id/renew` - gia hạn
- `PUT /api/contracts/:id/cancel` - hủy
- Admin/Super Admin

### Frontend
- Màn hình quản lý hợp đồng
- Contract form, file upload
