# CAT-02: Quản lý Loại BĐS

- **Tên:** Quản lý loại Bất động sản
- **Role:** Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **Super Admin**, I want **quản lý danh sách loại BĐS**, So that **phân loại BĐS thống nhất**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách dạng bảng: tên loại, mô tả, trạng thái
- [ ] Thêm: tên, mô tả
- [ ] Sửa: tên, mô tả
- [ ] Xóa (nếu không có BĐS nào dùng)
- [ ] Khóa/Mở khóa

## Technical Tasks

### Backend
- CRUD `GET/POST/PUT/DELETE /api/catalog/property-types`
- Super Admin: ghi

### Frontend
- Table + dialog CRUD (catalog.html)
