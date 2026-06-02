# CAT-06: Quản lý Dịch vụ

- **Tên:** Quản lý danh mục dịch vụ
- **Role:** Super Admin, Admin, Manager, HouseHolder (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý danh sách dịch vụ kèm giá và đơn vị**, So that **thêm dịch vụ cho phòng cho thuê**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách: tên, mô tả, giá, đơn vị (tháng/năm/m²), chu kỳ
- [ ] Loại: bắt buộc / tự chọn
- [ ] Chỉ số đầu (cho điện/nước)
- [ ] CRUD theo quyền tương tự Nội thất

## Technical Tasks

### Backend
- CRUD `GET/POST/PUT/DELETE /api/catalog/services`
- Theo creator

### Frontend
- Table + dialog (thêm trường price, unit, cycle, type, initialIndex)
