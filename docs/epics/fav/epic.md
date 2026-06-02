# Epic 12: Yêu thích & Lịch sử

**Mã Epic:** FAV
**Business Objective:** Cho phép người dùng lưu BĐS/phòng yêu thích và xem lịch sử.
**Mô tả:** Thêm/xóa yêu thích, danh sách yêu thích, lịch sử xem BĐS.
**Dependency:** Epic 5 (Quản lý BĐS), Epic 6 (Quản lý Phòng)

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
| Yêu thích & Lịch sử | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete

---

## Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| FAV (Yêu thích) | BDS, PHONG | - |

---

## Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 4** (Engagement) | NOTIF, SHARE, FAV, PROFILE | Tương tác: thông báo, chia sẻ, yêu thích |
