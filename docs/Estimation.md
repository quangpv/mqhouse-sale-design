# Estimation — MQ Sale (6 tháng)

> **Thời gian:** 01/06/2026 → 28/11/2026
> **Team:** 2 dev
> **Sprint:** 2 tuần/sprint, 12 sprints
> **Demo:** Thứ 6 cuối mỗi sprint

---

## Tổng quan

| Hạng mục | Số lượng |
|----------|----------|
| Epic | 13 |
| User Stories | 74 |
| Sprint | 12 (24 tuần) |
| Sprint Dev | 9 (S1→S9) |
| Sprint Testing | 3 (S10→S12) |
| Demo khách hàng | 12 lần |

---

## Phân bổ effort theo Sprint

### Giai đoạn 1: Development (S1→S9 — 18 tuần)

| Sprint | Thời gian | Stories | Effort | Nhóm chính |
|--------|-----------|---------|--------|------------|
| S1 | 01/06→12/06 | AUTH-01→06 | 6 PW | Xác thực & Bảo mật |
| S2 | 15/06→26/06 | CAT-01→07, NAV-01→02 | 7 PW | Danh mục + Điều hướng |
| S3 | 29/06→10/07 | USER-01→07 | 7 PW | Người dùng & Phân quyền |
| S4 | 13/07→24/07 | BDS-01→04,08, PROFILE-01→02 | 8 PW | BĐS cơ bản + Hồ sơ |
| S5 | 27/07→07/08 | BDS-05→07, PHONG-01→02, PROFILE-03→04 | 8 PW | Duyệt BĐS + Phòng cơ bản |
| S6 | 10/08→21/08 | PHONG-03→06,09, NOTIF-01→02 | 8 PW | Quản lý phòng + Thông báo |
| S7 | 24/08→04/09 | PHONG-07→08, DASH-01→03, NOTIF-03→04 | 7 PW | Cọc, Hợp đồng, Dashboard |
| S8 | 07/09→18/09 | SEARCH-01→04, MAP-01→04 | 8 PW | Tìm kiếm + Bản đồ |
| S9 | 21/09→02/10 | NOTIF-05→06, SHARE-01→04, FAV-01→05, NAV-03→07 | 8 PW | Thông báo, Chia sẻ, Yêu thích, Giao diện |

> **PW = Person-Weck** 1 sprint = 8 PW.

### Giai đoạn 2: Testing & Release (S10→S12 — 6 tuần)

| Sprint | Thời gian | Effort | Hoạt động |
|--------|-----------|--------|-----------|
| S10 | 05/10→16/10 | 8 PW | **Internal testing** (20 người), fix bug, regression |
| S11 | 19/10→30/10 | 8 PW | **Company-wide testing** + UAT, fix critical bugs |
| S12 | 02/11→13/11 | 8 PW | **Release preparation** + Deploy staging/production |

### Giai đoạn 3: Go-live & Hypercare (2 tuần)

| Phase | Thời gian | Effort | Hoạt động |
|-------|-----------|--------|-----------|
| Go-live | 16/11→20/11 | On-call | Deploy production, monitoring, rollback stand-by |
| Hypercare | 23/11→27/11 | On-call | Support, hotfix, performance tuning, handover |

---

## Chi tiết kỹ thuật mỗi Sprint

### S1: Xác thực & Bảo mật (01/06→12/06)

**Stories:** AUTH-01 (Đăng nhập), AUTH-02 (Đăng ký), AUTH-03 (Quên mật khẩu), AUTH-04 (Xác thực OTP), AUTH-05 (Đặt lại mật khẩu), AUTH-06 (Đổi mật khẩu)

| Hạng mục | Tasks |
|----------|-------|
| **Database** | Bảng `nguoi_dung`, `otp`, session management |
| **Backend** | `POST /api/auth/login`, `/register`, `/forgot-password`, `/verify-otp`, `/reset-password`, `/change-password` |
| **Backend** | JWT middleware, token validation |
| **Frontend** | Login, Register, Forgot password, OTP, Reset/Change password screens |
| **Validation** | Username/password rules, email/SĐT format |
| **Notification** | Gửi email/SMS OTP |
| **Testing** | Test đăng nhập, đăng ký, quên mật khẩu, OTP |
| **Demo** | **12/06** — Flow đăng ký → đăng nhập → đổi mật khẩu |

### S2: Danh mục + Điều hướng (15/06→26/06)

**Stories:** CAT-01 (Địa giới HC), CAT-02 (Loại BĐS), CAT-03 (Loại phòng), CAT-04 (Nội thất), CAT-05 (Tiện ích), CAT-06 (Dịch vụ), CAT-07 (File), NAV-01 (Bottom tab bar), NAV-02 (Sidebar)

| Hạng mục | Tasks |
|----------|-------|
| **Database** | Bảng `dia_gioi_hanh_chinh`, `loai_bds`, `loai_phong`, `noi_that`, `tien_ich`, `dich_vu`, `file` |
| **Backend** | CRUD APIs cho CAT-01→07 |
| **Frontend** | Catalog management screens (tree view, tables, CRUD dialogs) |
| **Frontend** | Bottom tab bar (6 tabs), Sidebar (dynamic menu theo role) |
| **Testing** | Test CRUD danh mục, tree location |
| **Demo** | **26/06** — CRUD danh mục + điều hướng |

### S3: Người dùng & Phân quyền (29/06→10/07)

**Stories:** USER-01 (DS người dùng), USER-02 (Tạo user), USER-03 (Sửa user), USER-04 (Khóa/Mở khóa), USER-05 (Phân quyền), USER-06 (Gán khu vực), USER-07 (Quản lý vai trò)

| Hạng mục | Tasks |
|----------|-------|
| **Backend** | CRUD users, roles, permissions, area assignment |
| **Database** | Bảng `phan_quyen`, `user_area` |
| **Frontend** | Members list, user CRUD dialog, permission tab UI |
| **Testing** | Test phân quyền truy cập |
| **Demo** | **10/07** — Tạo user, phân quyền, khóa/mở khóa |

### S4: BĐS cơ bản + Hồ sơ (13/07→24/07)

**Stories:** BDS-01 (Tạo BĐS), BDS-02 (Xem chi tiết), BDS-03 (Sửa BĐS), BDS-04 (Xóa BĐS), BDS-08 (DS BĐS của tôi), PROFILE-01 (Xem hồ sơ), PROFILE-02 (Sửa hồ sơ)

| Hạng mục | Tasks |
|----------|-------|
| **Database** | Bảng `bat_dong_san` + hình ảnh, nội thất, tiện ích |
| **Backend** | CRUD BĐS, upload file, geocoding |
| **Frontend** | Add-property form (2 tabs), property detail, image gallery |
| **Frontend** | Profile view/edit |
| **Testing** | Test create + edit property |
| **Demo** | **24/07** — Tạo BĐS đầy đủ, xem chi tiết |

### S5: Duyệt BĐS + Phòng cơ bản (27/07→07/08)

**Stories:** BDS-05 (Duyệt BĐS), BDS-06 (Quản lý hết hạn), BDS-07 (Đánh dấu nổi bật), PHONG-01 (Tạo phòng), PHONG-02 (Xem chi tiết phòng), PROFILE-03 (Đổi avatar), PROFILE-04 (Xem thông tin tài khoản)

| Hạng mục | Tasks |
|----------|-------|
| **Backend** | Approve/reject property, renew, featured toggle |
| **Backend** | CRUD phòng, room types, services |
| **Frontend** | Pending approval tab, approve/reject dialog |
| **Frontend** | Room form, room detail |
| **Testing** | Test duyệt BĐS, tạo phòng |
| **Demo** | **07/08** — Duyệt BĐS + tạo phòng |

### S6: Quản lý phòng + Thông báo (10/08→21/08)

**Stories:** PHONG-03 (Sửa phòng), PHONG-04 (Xóa phòng), PHONG-05 (Đổi trạng thái), PHONG-06 (Duyệt đổi trạng thái), PHONG-09 (DS phòng theo BĐS), NOTIF-01 (DS thông báo), NOTIF-02 (Xem chi tiết TB)

| Hạng mục | Tasks |
|----------|-------|
| **Database** | Bảng `lich_su_trang_thai_phong`, `yeu_cau_doi_trang_thai`, `thong_bao` |
| **Backend** | Status change (direct + request), approval, room CRUD |
| **Backend** | Notifications list + detail |
| **Frontend** | Room grid, quick-update, status badge |
| **Frontend** | Notification list screen |
| **Testing** | Test status workflow (Sale request → approve/reject) |
| **Demo** | **21/08** — Đổi trạng thái phòng + duyệt |

### S7: Cọc, Hợp đồng, Dashboard (24/08→04/09)

**Stories:** PHONG-07 (Xác nhận đặt cọc), PHONG-08 (Quản lý hợp đồng), DASH-01 (Xem tổng quan BĐS), DASH-02 (Xem thống kê phòng), DASH-03 (Xem doanh thu), NOTIF-03 (Đánh dấu đã đọc), NOTIF-04 (Tạo TB hệ thống)

| Hạng mục | Tasks |
|----------|-------|
| **Database** | Bảng `khach_hang`, `hop_dong` |
| **Backend** | Deposit confirmation, contract CRUD, renew, cancel |
| **Backend** | Dashboard APIs (property summary, room stats, revenue) |
| **Frontend** | Customer info form, contract management |
| **Frontend** | Dashboard charts (Chart.js/Recharts) |
| **Testing** | Test deposit flow, dashboard data |
| **Demo** | **04/09** — Đặt cọc + Hợp đồng + Dashboard |

### S8: Tìm kiếm + Bản đồ (07/09→18/09)

**Stories:** SEARCH-01 (Tìm kiếm cơ bản), SEARCH-02 (Tìm kiếm nâng cao), SEARCH-03 (Lưu bộ lọc), SEARCH-04 (Gợi ý thông minh), MAP-01 (Xem bản đồ BĐS), MAP-02 (Marker & popup), MAP-03 (Tìm theo bán kính), MAP-04 (Bottom sheet)

| Hạng mục | Tasks |
|----------|-------|
| **Database** | Full-text search index |
| **Backend** | Search basic/advanced/suggest/saved filters |
| **Backend** | Map APIs (bounds query, radius search) |
| **Frontend** | Search bar, filter panel, autocomplete |
| **Frontend** | Google Maps integration, markers, clustering, bottom sheet |
| **Testing** | Test search filters, map markers |
| **Demo** | **18/09** — Tìm kiếm + Bản đồ tương tác |

### S9: Thông báo, Chia sẻ, Yêu thích, Giao diện (21/09→02/10)

**Stories:** NOTIF-05 (Auto-notify duyệt), NOTIF-06 (Xóa TB), SHARE-01 (Chia sẻ Zalo), SHARE-02 (Chia sẻ Facebook), SHARE-03 (Sao chép link), SHARE-04 (Chia sẻ hình ảnh), FAV-01 (Yêu thích BĐS), FAV-02 (Yêu thích phòng), FAV-03 (DS yêu thích), FAV-04 (Lịch sử xem), FAV-05 (Xóa lịch sử), NAV-03→07 (Chuyển màn hình, Breadcrumb, Responsive, Loading, Error)

| Hạng mục | Tasks |
|----------|-------|
| **Backend** | Auto-notify on approve/reject, schedule notification |
| **Backend** | Share data APIs, favorites toggle, history |
| **Frontend** | System notification form, scheduling |
| **Frontend** | Zalo/FB share, copy link, share images |
| **Frontend** | Heart toggle, favorites list, history |
| **Frontend** | Breadcrumb, responsive layout, skeleton, error boundary |
| **Testing** | Full regression testing |
| **Demo** | **02/10** — Full system demo |

### S10: Internal Testing (05/10→16/10)

| Hoạt động | Mô tả |
|-----------|-------|
| **Test group** | 20 người (key users từ các phòng ban) |
| **Scope** | Toàn bộ tính năng |
| **Bug fix** | Critical + High priority bugs |
| **Regression** | Re-test sau mỗi đợt fix |
| **Demo** | **16/10** — Báo cáo kết quả test + bug fixed |

### S11: Company-wide Testing + UAT (19/10→30/10)

| Hoạt động | Mô tả |
|-----------|-------|
| **Test group** | Toàn bộ công ty |
| **UAT** | User Acceptance Testing theo kịch bản |
| **Performance** | Load test, stress test |
| **Security** | Security audit |
| **Bug fix** | Chỉ critical bugs |
| **Demo** | **30/10** — UAT sign-off + kết quả |

### S12: Release preparation + Deploy (02/11→13/11)

| Hoạt động | Mô tả |
|-----------|-------|
| **Code freeze** | Đóng code, không nhận feature mới |
| **Final regression** | Regression toàn bộ hệ thống |
| **Documentation** | User guide, operation guide |
| **Deploy staging** | Final validation on staging environment |
| **Deploy production** | Cut-over, DB migration, config |
| **Demo** | **13/11** — Release announcement |

### Go-live & Hypercare (16/11→27/11)

**Stories:** Go-live, Hypercare, Handover

| Hoạt động | Tuần 1 (16/11→20/11) | Tuần 2 (23/11→27/11) |
|-----------|----------------------|----------------------|
| **Go-live** | Deploy production, monitoring, rollback stand-by | - |
| **Hypercare** | Theo dõi hệ thống, support người dùng | Hotfix, performance tuning |
| **Handover** | Bàn giao cho team vận hành | Tài liệu + training |
| **KPI** | Uptime 99.9%, response time < 2s | UAT sign-off cuối cùng |

---

## Phân bổ nguồn lực

| Vai trò | Số lượng | Trách nhiệm |
|---------|----------|-------------|
| **Backend Dev** | 2 | API, Database, Business logic |
| **Frontend Dev** | 2 | UI, Integration, State management |
| **QA** | 1 | Test case, Manual + Automation test |
| **BA/PM** | 1 (shared) | Sprint review, Demo prep, UAT coordination |

---

## Rủi ro & Giảm thiểu

| Rủi ro | Mức | Giảm thiểu |
|--------|-----|------------|
| Sprint 8 khối lượng lớn (Search + Map) | Cao | Map dùng Google Maps SDK sẵn, Search dùng full-text index |
| Sprint 9 dồn 12 stories | Cao | Các story đơn giản (SHARE, FAV, PROFILE), ưu tiên core trước |
| Bug từ S10→S11 tràn sang S12 | Trung | Chỉ fix critical, low/medium chuyển post-release |
| Phụ thuộc vào Google Maps API key | Thấp | Chuẩn bị key từ đầu dự án |

---

*Tổng số: 13 Epics, 74 User Stories, 12 Sprints, 24 tuần.*
