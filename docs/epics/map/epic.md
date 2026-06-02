# Epic 4: Bản đồ tương tác

**Mã Epic:** MAP
**Business Objective:** Trực quan hóa BĐS trên bản đồ giúp người dùng dễ dàng khám phá theo vị trí địa lý.
**Mô tả:** Tích hợp Google Maps, hiển thị marker BĐS, tìm kiếm theo bán kính.
**Dependency:** Epic 5 (Quản lý BĐS)

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
| Bản đồ | R | R | R | R | R | R |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete

## Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| MAP (Bản đồ) | BDS | - |

## Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 3** (Experience) | SEARCH, MAP, DASH | Trải nghiệm: tìm kiếm, bản đồ, dashboard |
