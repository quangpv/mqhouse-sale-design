# Epic 9: Hồ sơ cá nhân

**Mã Epic:** PROFILE
**Business Objective:** Cho phép người dùng quản lý thông tin cá nhân.
**Mô tả:** Xem và chỉnh sửa hồ sơ cá nhân, đổi avatar, xem thông tin tài khoản, trang tĩnh (giới thiệu, điều khoản), liên hệ hỗ trợ.
**Dependency:** Epic 1 (Xác thực)

---

# Actors / Roles

| ID | Role | Mô tả | Quyền hạn chính |
|----|------|-------|-----------------|
| R01 | **Super Admin (Root)** | Quản trị viên cao nhất, toàn quyền hệ thống | Tất cả quyền, quản lý danh mục, phân quyền, quản lý user |
| R02 | **Admin** | Quản trị viên cấp công ty | Duyệt BĐS/phòng, quản lý user, tạo thông báo |
| R03 | **Manager** | Quản lý khu vực | CRUD BĐS/phòng trong khu vực được gán, cần duyệt khi tạo |
| R04 | **HouseHolder** | Chủ nhà / chủ BĐS | Tạo/sửa BĐS/phòng của mình, cần Admin duyệt |
| R05 | **Sale** | Nhân viên kinh doanh | Đổi trạng thái phòng (cần duyệt), xem thông tin |
| R06 | **Khách hàng** | Người thuê / người xem tin | Xem, tìm kiếm, yêu thích, không cần đăng nhập |

## Ma trận Role - Epic

| Epic | Super Admin | Admin | Manager | HouseHolder | Sale | Khách hàng |
|------|:-----------:|:-----:|:-------:|:-----------:|:----:|:----------:|
| Hồ sơ cá nhân | CRUD | CRUD | CRUD | CRUD | CRUD | - |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete

---

# Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| PROFILE (Hồ sơ) | AUTH | - |

---

# Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 4** (Engagement) | NOTIF, SHARE, FAV, PROFILE | Tương tác: thông báo, chia sẻ, yêu thích |
