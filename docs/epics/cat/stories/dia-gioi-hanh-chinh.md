# CAT-01: Quản lý Địa giới hành chính

- **Tên:** Quản lý địa giới hành chính
- **Role:** Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **Super Admin**, I want **quản lý cây địa giới hành chính (Tỉnh/Quận/Phường)**, So that **cấu trúc dữ liệu vùng miền chính xác**

**Priority:** High

**Acceptance Criteria:**
- [ ] Hiển thị cây 3 cấp: Tỉnh → Quận/Huyện → Phường/Xã
- [ ] Expand/collapse từng node
- [ ] Thêm mới: chọn cấp (Tỉnh/Quận/Phường), nhập tên
- [ ] Sửa: đổi tên, slug
- [ ] Xóa: confirm, không xóa nếu đang được sử dụng
- [ ] Chọn parent khi tạo Quận/Phường
- [ ] Tìm kiếm trong cây địa giới

## Technical Tasks

### Backend
- Bảng `dia_gioi_hanh_chinh`: id, ten, slug, ma, cap, parent_id, path
- `GET /api/locations/tree` - cây địa giới
- `GET /api/locations/:id/children` - con của node
- `POST/PUT/DELETE /api/locations` - CRUD
- Super Admin: CRUD, others: R

### Frontend
- Tree component (catalog.html - tab Địa giới HC)
- CRUD dialog
- Search trong tree
