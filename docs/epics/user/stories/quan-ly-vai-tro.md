## USER-07: Quản lý vai trò

- **Tên:** Quản lý vai trò người dùng
- **Role:** Super Admin
- **Mô tả:** As a **Super Admin**, I want **thêm/sửa/xóa vai trò**, So that **linh hoạt trong quản lý phân quyền**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Danh sách vai trò (bảng)
- [ ] Thêm vai trò mới: tên, mô tả
- [ ] Sửa vai trò
- [ ] Xóa vai trò (không xóa được role mặc định)
- [ ] Gán quyền cho vai trò (dùng chung UI với USER-05)

## Technical Tasks

### Backend
- CRUD `GET/POST/PUT/DELETE /api/roles`
- Super Admin

### Frontend
- Dialog CRUD vai trò
