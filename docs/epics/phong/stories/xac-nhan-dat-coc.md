## PHONG-07: Xác nhận đặt cọc

- **Tên:** Xác nhận đặt cọc phòng
- **Role:** Admin, Manager, HouseHolder, Sale
- **Mô tả:** As a **người quản lý**, I want **xác nhận đặt cọc với thông tin khách hàng đầy đủ**, So that **quản lý được thông tin khách thuê**

**Priority:** High

**Acceptance Criteria:**
- [ ] Khi đổi trạng thái → "đã cọc" → hiển thị form nhập thông tin khách
- [ ] Các trường bắt buộc: tên khách hàng, số điện thoại, hình ảnh khách
- [ ] Validate tên, SĐT
- [ ] Upload hình ảnh khách hàng (có thể chụp trực tiếp)
- [ ] Lưu thông tin khách vào bảng Khách hàng
- [ ] Hiển thị thông tin khách trên chi tiết phòng

## Technical Tasks

### Backend
- INSERT/UPDATE bảng `khach_hang`
- `POST /api/rooms/:id/deposit` - xác nhận cọc + thông tin khách
- `POST /api/customers` - tạo khách hàng

### Frontend
- Form nhập thông tin khách (room-detail.html)
- Camera capture hoặc upload từ gallery
- Validate SĐT: 10-11 số, bắt đầu 0
- Validate tên không để trống
