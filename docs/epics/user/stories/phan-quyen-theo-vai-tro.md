## USER-05: Phân quyền theo vai trò

- **Tên:** Phân quyền chi tiết cho vai trò
- **Role:** Super Admin
- **Mô tả:** As a **Super Admin**, I want **cấu hình quyền cho từng vai trò**, So that **kiểm soát chức năng mỗi role có thể truy cập**

**Priority:** High

**Acceptance Criteria:**
- [ ] Giao diện 3 tab role: Admin, Quản lý khu vực, Sale (permission.html)
- [ ] 12 quyền checkbox chia 3 nhóm:
  - **Duyệt:** Duyệt BĐS, Duyệt phòng trống
  - **Ghi:** Ghi BĐS, Ghi phòng, Ghi user, Ghi địa giới HC, Ghi nội thất, Ghi tiện ích, Ghi loại phòng, Ghi loại BĐS, Ghi dịch vụ
  - **Đọc:** Đọc danh sách người dùng
- [ ] Phân quyền mặc định theo role:
  - **Admin:** full 12 quyền
  - **Manager (Quản lý khu vực):** 7 quyền (Duyệt BĐS, Duyệt phòng trống, Ghi BĐS, Ghi phòng, Đọc user, Ghi nội thất, Ghi tiện ích)
  - **Sale:** 3 quyền (Ghi BĐS, Ghi phòng, Đọc user)
- [ ] Select all / Deselect all
- [ ] Lưu thay đổi → cập nhật quyền ngay

## Technical Tasks

### Backend
- Bảng `phan_quyen`: role_code + permission_code
- `GET /api/permissions/:roleId` - quyền của role
- `PUT /api/permissions/:roleId` - cập nhật quyền
- `GET /api/permissions/available` - danh sách quyền có sẵn
- Chỉ Super Admin

### Frontend
- Màn hình permission.html: 3 tab role + checkbox grid, badge phân loại (Duyệt/Ghi/Đọc)
- Select all/deselect all
- Save changes với toast notification
