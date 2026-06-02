# Epic 8: Danh mục hệ thống (Catalog)

**Mã Epic:** CAT
**Business Objective:** Quản lý các danh mục dùng chung cho toàn hệ thống.
**Mô tả:** CRUD cho Địa giới hành chính, Loại BĐS, Loại phòng, Nội thất, Tiện ích, Dịch vụ.
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
| Danh mục (Catalog) | CRUD | R | R | R | R | - |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete

---

# Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| CAT (Danh mục) | AUTH | BDS, USER |

---

# Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 1** (Foundation) | AUTH, CAT, USER | Nền tảng: xác thực, danh mục, người dùng |
