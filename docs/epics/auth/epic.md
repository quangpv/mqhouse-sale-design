# Epic 1: Xác thực & Bảo mật

**Mã Epic:** AUTH
**Business Objective:** Đảm bảo chỉ người dùng hợp lệ mới truy cập được hệ thống, bảo vệ thông tin tài khoản.
**Mô tả:** Cho phép người dùng đăng nhập, đăng ký, khôi phục mật khẩu và xác thực qua OTP.
**Dependency:** -

## Actors / Roles

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
| Xác thực & Bảo mật | CRUD | C | C | C | C | C (ĐK) |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete, ĐK = Đăng ký

## Phụ thuộc

| Phụ thuộc vào | Được phụ thuộc bởi |
|---------------|-------------------|
| - | DASH, BDS, PHONG, USER, CAT, PROFILE, NOTIF |

## Thứ tự ưu tiên

**Phase 1** (Foundation) - AUTH, CAT, USER - Nền tảng: xác thực, danh mục, người dùng
