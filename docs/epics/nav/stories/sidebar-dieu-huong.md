# NAV-02: Sidebar điều hướng

- **Role:** Admin, Manager, HouseHolder, Sale (người dùng đã đăng nhập)
- **Mô tả:** As a **người dùng đã đăng nhập**, I want **có sidebar menu chứa các chức năng quản lý**, So that **truy cập nhanh các tính năng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Sidebar: avatar + tên người dùng
- [ ] Menu items: Dashboard, BĐS của tôi, Người dùng, Danh mục, Cài đặt
- [ ] Hiển thị menu theo quyền (VD: Admin thấy "Người dùng", Sale không thấy)
- [ ] Toggle sidebar (mở/đóng)
- [ ] Highlight menu active
- [ ] Nút logout

## Technical Tasks

### Frontend
- Sidebar component (index.html shell)
- Dynamic menu theo role
- Toggle animation
