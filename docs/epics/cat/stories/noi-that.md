# CAT-04: Quản lý Nội thất

- **Tên:** Quản lý danh mục nội thất
- **Role:** Super Admin, Admin, Manager, HouseHolder (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý danh sách nội thất với icon**, So that **gắn nội thất cho BĐS/phòng**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách: tên nội thất, mô tả, icon, người tạo, trạng thái
- [ ] Super Admin tạo mặc định
- [ ] Manager/HouseHolder tạo → chỉ sửa/xóa cái của mình
- [ ] Admin sửa/xóa được của Manager/HouseHolder
- [ ] Icon upload/icon picker

## Technical Tasks

### Backend
- CRUD `GET/POST/PUT/DELETE /api/catalog/furniture`
- Có filter: `?created_by=me`
- Phân quyền theo created_by

### Frontend
- Table + dialog + icon picker
