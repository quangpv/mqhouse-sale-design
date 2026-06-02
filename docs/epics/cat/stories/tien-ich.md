# CAT-05: Quản lý Tiện ích

- **Tên:** Quản lý danh mục tiện ích
- **Role:** Super Admin, Admin, Manager, HouseHolder (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý danh sách tiện ích với icon và khoảng cách**, So that **gắn tiện ích cho BĐS/phòng**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách: tên, mô tả, icon, khoảng cách (m), người tạo, trạng thái
- [ ] CRUD tương tự Nội thất
- [ ] Có thêm trường khoảng cách (m)

## Technical Tasks

### Backend
- CRUD `GET/POST/PUT/DELETE /api/catalog/utilities`
- Giống CAT-04

### Frontend
- Table + dialog (giống CAT-04)
