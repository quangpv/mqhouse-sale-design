# Epic 11: Chia sẻ

**Mã Epic:** SHARE
**Business Objective:** Cho phép chia sẻ thông tin BĐS/phòng qua nhiều kênh.
**Mô tả:** Chia sẻ qua Zalo, Facebook, sao chép link, chia sẻ hình ảnh.
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
| Chia sẻ | R | R | R | R | R | R |

# Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| SHARE (Chia sẻ) | BDS, PHONG | - |

# Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 4** (Engagement) | NOTIF, SHARE, FAV, PROFILE | Tương tác: thông báo, chia sẻ, yêu thích |
