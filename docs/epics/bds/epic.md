# Epic 5: Quản lý Bất động sản

**Mã Epic:** BDS
**Business Objective:** Quản lý toàn bộ vòng đời BĐS từ tạo mới đến hết hạn.
**Mô tả:** CRUD BĐS, quy trình duyệt, quản lý hết hạn, đánh dấu nổi bật.
**Dependency:** Epic 1 (Xác thực), Epic 7 (Người dùng & Phân quyền), Epic 8 (Danh mục)

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
| Quản lý BĐS | CRUD | CRUD+Duyệt | CRUD (KV) | CRUD (của mình) | R | R |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete, KV = Khu vực quản lý

## Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| BDS (Quản lý BĐS) | AUTH, USER, CAT | DASH, SEARCH, MAP, PHONG, SHARE, FAV |

## Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 2** (Core) | BDS, PHONG, NAV | Nghiệp vụ chính: quản lý BĐS và phòng |
