# Epic 6: Quản lý Phòng

**Mã Epic:** PHONG
**Business Objective:** Quản lý chi tiết từng phòng trong BĐS, theo dõi trạng thái và khách thuê.
**Mô tả:** CRUD phòng, quản lý trạng thái, quy trình đặt cọc và hợp đồng.
**Dependency:** Epic 1 (Xác thực), Epic 5 (Quản lý BĐS)

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
| Quản lý Phòng | CRUD | CRUD+Duyệt | CRUD (KV)+đổi TT trực tiếp | CRUD (của mình)+đổi TT trực tiếp | R+đổi TT bất kỳ (qua chờ duyệt) | R |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete, ĐK = Đăng ký, KV = Khu vực quản lý, TT = Trạng thái

# Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| PHONG (Quản lý Phòng) | AUTH, BDS | DASH, SEARCH, SHARE, FAV |

# Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 2** (Core) | BDS, PHONG, NAV | Nghiệp vụ chính: quản lý BĐS và phòng |
