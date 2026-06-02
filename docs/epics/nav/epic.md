# Epic 13: Điều hướng & Giao diện

**Mã Epic:** NAV
**Business Objective:** Cung cấp trải nghiệm điều hướng mượt mà, nhất quán trên tất cả màn hình.
**Mô tả:** Cấu trúc điều hướng, chuyển đổi màn hình, responsive layout và xử lý trạng thái.
**Dependency:** Tất cả epics

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
| Điều hướng & Giao diện | R | R | R | R | R | R |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete

---

## Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| NAV (Điều hướng) | Tất cả | - |

---

## Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 2** (Core) | BDS, PHONG, NAV | Nghiệp vụ chính: quản lý BĐS và phòng |
