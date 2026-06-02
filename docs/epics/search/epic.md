# Epic 3: Tìm kiếm BĐS/Phòng

**Mã Epic:** SEARCH
**Business Objective:** Giúp người dùng nhanh chóng tìm được BĐS/phòng phù hợp.
**Mô tả:** Cung cấp các chức năng tìm kiếm cơ bản, nâng cao và gợi ý.
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
| Tìm kiếm | R | R | R | R | R | R |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete, ĐK = Đăng ký, KV = Khu vực quản lý, TT = Trạng thái

---

## Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| SEARCH (Tìm kiếm) | BDS, PHONG | - |

---

## Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 3** (Experience) | SEARCH, MAP, DASH | Trải nghiệm: tìm kiếm, bản đồ, dashboard |
