# Epic & Stories

> Tài liệu này mô tả toàn bộ Epic và User Stories cho hệ thống MQ Sale, được phân tích từ 21 file HTML prototype.
> Format: Mỗi story tuân theo "As a <role>, I want <feature>, So that <benefit>" với đầy đủ tiêu chí chấp nhận và phân rã tác vụ kỹ thuật.

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
| Xác thực & Bảo mật | CRUD | C | C | C | C | C (ĐK) |
| Dashboard & Thống kê | R | R | R | R | R | - |
| Tìm kiếm | R | R | R | R | R | R |
| Bản đồ | R | R | R | R | R | R |
| Quản lý BĐS | CRUD | CRUD+Duyệt | CRUD (KV) | CRUD (của mình) | R | R |
| Quản lý Phòng | CRUD | CRUD+Duyệt | CRUD (KV)+đổi TT trực tiếp | CRUD (của mình)+đổi TT trực tiếp | R+đổi TT bất kỳ (qua chờ duyệt) | R |
| Người dùng & Phân quyền | CRUD | CRUD (cấp dưới) | R | R | R | - |
| Danh mục (Catalog) | CRUD | R | R | R | R | - |
| Hồ sơ cá nhân | CRUD | CRUD | CRUD | CRUD | CRUD | - |
| Thông báo | CRUD | CRUD | R | R | R | R |
| Chia sẻ | R | R | R | R | R | R |
| Yêu thích & Lịch sử | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD |
| Điều hướng & Giao diện | R | R | R | R | R | R |

> **Chú thích:** C = Create, R = Read, U = Update, D = Delete, ĐK = Đăng ký, KV = Khu vực quản lý, TT = Trạng thái

---

# Sơ đồ quan hệ

```
Epic 1: Xác thực & Bảo mật ─────────────────────────────────────
  ├── AUTH-01: Đăng nhập
  ├── AUTH-02: Đăng ký tài khoản
  ├── AUTH-03: Quên mật khẩu
  ├── AUTH-04: Xác thực OTP
  ├── AUTH-05: Đặt lại mật khẩu
  └── AUTH-06: Đổi mật khẩu

Epic 2: Dashboard & Thống kê ────── phụ thuộc: Epic 1, 5, 6 ──
  ├── DASH-01: Xem tổng quan BĐS
  ├── DASH-02: Xem thống kê phòng
  └── DASH-03: Xem doanh thu

Epic 3: Tìm kiếm BĐS/Phòng ──────── phụ thuộc: Epic 5, 6 ─────
  ├── SEARCH-01: Tìm kiếm cơ bản
  ├── SEARCH-02: Tìm kiếm nâng cao
  ├── SEARCH-03: Lưu bộ lọc tìm kiếm
  └── SEARCH-04: Gợi ý tìm kiếm

Epic 4: Bản đồ tương tác ────────── phụ thuộc: Epic 5 ────────
  ├── MAP-01: Xem bản đồ BĐS
  ├── MAP-02: Marker BĐS
  ├── MAP-03: Tìm kiếm theo bán kính
  └── MAP-04: Bottom sheet chi tiết BĐS

Epic 5: Quản lý Bất động sản ────── phụ thuộc: Epic 1, 7, 8 ─
  ├── BDS-01: Tạo BĐS
  ├── BDS-02: Xem chi tiết BĐS
  ├── BDS-03: Sửa BĐS
  ├── BDS-04: Xóa BĐS
  ├── BDS-05: Duyệt BĐS
  ├── BDS-06: Quản lý BĐS hết hạn
  ├── BDS-07: Đánh dấu nổi bật
  └── BDS-08: Danh sách BĐS của tôi

Epic 6: Quản lý Phòng ───────────── phụ thuộc: Epic 1, 5 ────
  ├── PHONG-01: Tạo phòng
  ├── PHONG-02: Xem chi tiết phòng
  ├── PHONG-03: Sửa phòng
  ├── PHONG-04: Xóa phòng
  ├── PHONG-05: Đổi trạng thái phòng
  ├── PHONG-06: Duyệt đổi trạng thái phòng
  ├── PHONG-07: Xác nhận đặt cọc
  ├── PHONG-08: Quản lý hợp đồng
  └── PHONG-09: Danh sách phòng theo BĐS

Epic 7: Người dùng & Phân quyền ─── phụ thuộc: Epic 1, 8 ────
  ├── USER-01: Danh sách người dùng
  ├── USER-02: Tạo người dùng
  ├── USER-03: Sửa người dùng
  ├── USER-04: Khóa/Mở khóa người dùng
  ├── USER-05: Phân quyền theo vai trò
  ├── USER-06: Gán khu vực quản lý
  └── USER-07: Quản lý vai trò

Epic 8: Danh mục hệ thống (Catalog) ── phụ thuộc: Epic 1 ────
  ├── CAT-01: Quản lý Địa giới hành chính
  ├── CAT-02: Quản lý Loại BĐS
  ├── CAT-03: Quản lý Loại phòng
  ├── CAT-04: Quản lý Nội thất
  ├── CAT-05: Quản lý Tiện ích
  ├── CAT-06: Quản lý Dịch vụ
  └── CAT-07: Quản lý File

Epic 9: Hồ sơ cá nhân ───────────── phụ thuộc: Epic 1 ────────
  ├── PROFILE-01: Xem hồ sơ
  ├── PROFILE-02: Sửa hồ sơ
  ├── PROFILE-03: Đổi avatar
  └── PROFILE-04: Xem thông tin tài khoản

Epic 10: Thông báo ──────────────── phụ thuộc: Epic 1 ────────
  ├── NOTIF-01: Danh sách thông báo
  ├── NOTIF-02: Xem chi tiết thông báo
  ├── NOTIF-03: Đánh dấu đã đọc
  ├── NOTIF-04: Tạo thông báo hệ thống
  ├── NOTIF-05: Tự động gửi thông báo duyệt
  └── NOTIF-06: Xóa thông báo

Epic 11: Chia sẻ ────────────────── phụ thuộc: Epic 5, 6 ────
  ├── SHARE-01: Chia sẻ qua Zalo
  ├── SHARE-02: Chia sẻ qua Facebook
  ├── SHARE-03: Sao chép link
  └── SHARE-04: Chia sẻ hình ảnh

Epic 12: Yêu thích & Lịch sử ────── phụ thuộc: Epic 5, 6 ────
  ├── FAV-01: Yêu thích BĐS
  ├── FAV-02: Yêu thích phòng
  ├── FAV-03: Danh sách yêu thích
  ├── FAV-04: Lịch sử xem BĐS
  └── FAV-05: Xóa lịch sử / yêu thích

Epic 13: Điều hướng & Giao diện ─── phụ thuộc: tất cả epics ─
  ├── NAV-01: Bottom tab bar
  ├── NAV-02: Sidebar điều hướng
  ├── NAV-03: Chuyển đổi màn hình
  ├── NAV-04: Breadcrumb
  ├── NAV-05: Responsive layout
  ├── NAV-06: Loading & Empty state
  └── NAV-07: Error & Network state
```

> **Ký hiệu:** Mũi tên `──>` chỉ luồng điều hướng giữa các màn hình.
> **Dependency:** Epic X phụ thuộc Epic Y = cần Y hoàn thành trước hoặc chạy song song.

---

# Epic 1: Xác thực & Bảo mật

**Mã Epic:** AUTH
**Business Objective:** Đảm bảo chỉ người dùng hợp lệ mới truy cập được hệ thống, bảo vệ thông tin tài khoản.
**Mô tả:** Cho phép người dùng đăng nhập, đăng ký, khôi phục mật khẩu và xác thực qua OTP.

---

## AUTH-01: Đăng nhập

- **Tên:** Đăng nhập hệ thống
- **Role:** Người dùng (Admin, Manager, HouseHolder, Sale)
- **Mô tả:** As a **người dùng**, I want **đăng nhập bằng tên đăng nhập và mật khẩu**, So that **truy cập vào hệ thống theo quyền hạn của tôi**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form đăng nhập có: tên đăng nhập, mật khẩu, checkbox ghi nhớ
- [ ] Validate không để trống các trường
- [ ] Hiển thị lỗi khi sai tên đăng nhập hoặc mật khẩu
- [ ] Hiển thị lỗi khi tài khoản bị khóa
- [ ] Đăng nhập thành công → chuyển đến Dashboard
- [ ] Ghi nhớ đăng nhập (remember me)
- [ ] Hiển thị mật khẩu (eye toggle)
- [ ] Link "Quên mật khẩu?" dẫn đến màn hình quên mật khẩu

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tạo bảng `nguoi_dung` với các trường: id, ten_dang_nhap, mat_khau (hash), trang_thai, ngay_dang_nhap_cuoi |
| **Backend API** | `POST /api/auth/login` - nhận ten_dang_nhap, mat_khau → trả về JWT token + thông tin user |
| **Backend API** | `POST /api/auth/logout` - xóa token |
| **Backend API** | Middleware xác thực JWT, kiểm tra token hết hạn |
| **Frontend UI** | Màn hình login1.html: form đăng nhập với validation |
| **Frontend UI** | Xử lý lưu token vào localStorage/sessionStorage |
| **Frontend UI** | Redirect sau đăng nhập thành công |
| **Frontend UI** | Xử lý trạng thái loading khi gọi API |
| **Validation** | Kiểm tra định dạng tên đăng nhập (không khoảng trắng, ký tự đặc biệt) |
| **Validation** | Kiểm tra độ dài mật khẩu tối thiểu 6 ký tự |
| **Permission** | Gán JWT claims: user_id, role, permissions |
| **Testing** | Test đăng nhập thành công, sai mật khẩu, tài khoản bị khóa |

---

## AUTH-02: Đăng ký tài khoản

- **Tên:** Đăng ký tài khoản mới
- **Role:** Khách hàng, Sale, HouseHolder
- **Mô tả:** As a **người dùng mới**, I want **đăng ký tài khoản với thông tin cá nhân**, So that **có thể sử dụng hệ thống với vai trò phù hợp**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form đăng ký có: tên đăng nhập, mật khẩu, xác nhận mật khẩu, họ tên, email, số điện thoại
- [ ] Validate các trường bắt buộc
- [ ] Validate mật khẩu và xác nhận mật khẩu khớp nhau
- [ ] Kiểm tra tên đăng nhập đã tồn tại
- [ ] Đăng ký thành công → về màn hình đăng nhập với thông báo
- [ ] Tài khoản mặc định ở trạng thái "Đang hoạt động"

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tạo procedure/query kiểm tra tên đăng nhập tồn tại |
| **Backend API** | `POST /api/auth/register` - nhận thông tin → hash mật khẩu → tạo user → trả về thành công |
| **Backend API** | `GET /api/auth/check-username/:username` - kiểm tra tên đăng nhập đã tồn tại |
| **Frontend UI** | Màn hình register1.html: form đăng ký với validation realtime |
| **Frontend UI** | Hiển thị strength meter cho mật khẩu |
| **Frontend UI** | Xử lý loading, success, error states |
| **Validation** | Validate email định dạng hợp lệ |
| **Validation** | Validate số điện thoại (10-11 số, bắt đầu bằng 0) |
| **Validation** | Validate mật khẩu: tối thiểu 6 ký tự, có chữ và số |
| **Testing** | Test đăng ký thành công, trùng username, email sai định dạng |

---

## AUTH-03: Quên mật khẩu

- **Tên:** Quên mật khẩu
- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng quên mật khẩu**, I want **nhập email/số điện thoại để nhận OTP**, So that **có thể đặt lại mật khẩu**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập email hoặc số điện thoại đã đăng ký
- [ ] Validate trường nhập không để trống
- [ ] Kiểm tra email/số điện thoại tồn tại trong hệ thống
- [ ] Hiển thị thông báo lỗi nếu không tìm thấy tài khoản
- [ ] Gửi OTP thành công → chuyển sang màn hình OTP
- [ ] Nút quay lại màn hình đăng nhập

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Query kiểm tra email/SĐT tồn tại |
| **Backend API** | `POST /api/auth/forgot-password` - nhận email/SĐT → tạo OTP → gửi OTP → trả về mã xác thực tạm |
| **Backend API** | Tích hợp dịch vụ gửi email/SMS |
| **Frontend UI** | Màn hình forgot-password.html: form nhập email/SĐT |
| **Frontend UI** | Xử lý chuyển màn hình sau khi gửi OTP thành công |
| **Validation** | Validate email/SĐT theo đúng định dạng |
| **Notification** | Gửi email/SMS chứa mã OTP |
| **Testing** | Test email/SĐT hợp lệ, không tồn tại, lỗi gửi OTP |

---

## AUTH-04: Xác thực OTP

- **Tên:** Xác thực mã OTP
- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng**, I want **nhập mã OTP đã được gửi qua email/SMS**, So that **xác thực danh tính để đặt lại mật khẩu**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập 6 số OTP (có thể split thành 6 ô riêng)
- [ ] Hiển thị email/SĐT đã gửi OTP (dạng ẩn: ***@gmail.com)
- [ ] Tự động focus ô tiếp theo khi nhập
- [ ] Validate mã OTP đủ 6 số
- [ ] Kiểm tra mã OTP còn hiệu lực (thời gian)
- [ ] Kiểm tra mã OTP chính xác
- [ ] Hiển thị lỗi nếu OTP sai
- [ ] Chức năng gửi lại OTP (countdown timer)
- [ ] OTP đúng → chuyển đến màn hình đặt lại mật khẩu

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tạo bảng `otp` (id, identifier (email/SĐT), code, expires_at, used, created_at) |
| **Backend API** | `POST /api/auth/verify-otp` - nhận mã OTP + session_token → xác thực |
| **Backend API** | `POST /api/auth/resend-otp` - gửi lại OTP mới |
| **Backend API** | Tự động xóa OTP hết hạn (cron job) |
| **Frontend UI** | Màn hình otp.html: 6 ô nhập OTP với auto-focus |
| **Frontend UI** | Countdown timer cho nút "Gửi lại" (60s) |
| **Frontend UI** | Hiển thị thông báo lỗi/quá hạn OTP |
| **Validation** | OTP chỉ gồm 6 chữ số |
| **Validation** | Kiểm tra thời gian hiệu lực OTP (5 phút) |
| **Testing** | Test OTP đúng, sai, hết hạn, gửi lại OTP |

---

## AUTH-05: Đặt lại mật khẩu

- **Tên:** Đặt lại mật khẩu mới
- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng đã xác thực OTP**, I want **nhập mật khẩu mới và xác nhận**, So that **có thể đăng nhập với mật khẩu mới**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập mật khẩu mới và xác nhận mật khẩu mới
- [ ] Validate mật khẩu không để trống, tối thiểu 6 ký tự
- [ ] Validate mật khẩu và xác nhận khớp nhau
- [ ] Mật khẩu mới không được trùng mật khẩu cũ
- [ ] Đặt lại thành công → chuyển đến màn hình đăng nhập với thông báo
- [ ] Vô hiệu hóa token OTP sau khi đặt lại thành công

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Cập nhật mật khẩu (hash) cho user |
| **Backend API** | `POST /api/auth/reset-password` - nhận mật khẩu mới + session_token → hash lưu |
| **Frontend UI** | Màn hình reset-password.html: form đặt lại mật khẩu |
| **Frontend UI** | Strength meter cho mật khẩu mới |
| **Frontend UI** | Thông báo thành công và redirect |
| **Validation** | Validate độ mạnh mật khẩu |
| **Validation** | Kiểm tra mật khẩu mới ≠ mật khẩu cũ |
| **Testing** | Test reset thành công, mật khẩu yếu, không khớp |

---

## AUTH-06: Đổi mật khẩu

- **Tên:** Đổi mật khẩu
- **Role:** Người dùng đã đăng nhập (Admin, Manager, HouseHolder, Sale)
- **Mô tả:** As a **người dùng đã đăng nhập**, I want **đổi mật khẩu của tôi khi biết mật khẩu cũ**, So that **bảo vệ tài khoản khi nghi ngờ lộ thông tin**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form nhập: mật khẩu cũ, mật khẩu mới, xác nhận mật khẩu mới
- [ ] Validate không để trống các trường
- [ ] Kiểm tra mật khẩu cũ chính xác
- [ ] Mật khẩu mới không trùng mật khẩu cũ
- [ ] Mật khẩu mới và xác nhận khớp nhau
- [ ] Đổi thành công → thông báo → có thể logout hoặc ở lại
- [ ] Không cho phép đổi nếu tài khoản bị khóa

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/auth/change-password` - nhận mật khẩu cũ + mới → verify + hash lưu |
| **Backend API** | Xác thực JWT, lấy user_id từ token |
| **Frontend UI** | Màn hình change-password.html: form đổi mật khẩu |
| **Frontend UI** | Validate real-time mật khẩu cũ/mới/xác nhận |
| **Frontend UI** | Xử lý thông báo thành công/thất bại |
| **Validation** | Mật khẩu mới tối thiểu 6 ký tự |
| **Validation** | Kiểm tra mật khẩu cũ đúng trước khi cập nhật |
| **Testing** | Test đổi thành công, sai mật khẩu cũ, mật khẩu yếu |

---

# Epic 2: Dashboard & Thống kê

**Mã Epic:** DASH
**Business Objective:** Cung cấp cái nhìn tổng quan về hoạt động kinh doanh BĐS cho người quản lý.
**Mô tả:** Hiển thị các thống kê về BĐS, phòng và doanh thu dưới dạng biểu đồ và số liệu.
**Dependency:** Epic 1 (Xác thực), Epic 5 (Quản lý BĐS), Epic 6 (Quản lý Phòng)

---

## DASH-01: Xem tổng quan Bất động sản

- **Tên:** Dashboard tổng quan BĐS
- **Role:** Admin, Manager, HouseHolder
- **Mô tả:** As a **người quản lý**, I want **xem tổng quan số liệu BĐS trên Dashboard**, So that **nắm được tình hình BĐS đang quản lý**

**Priority:** High

**Acceptance Criteria:**
- [ ] Dashboard hiển thị các thẻ thống kê: Tổng BĐS, Đã duyệt, Chờ duyệt, Hết hạn
- [ ] Biểu đồ tròn phân loại theo trạng thái BĐS
- [ ] Biểu đồ cột BĐS mới theo tháng
- [ ] Danh sách BĐS gần hết hạn (5-10 items)
- [ ] Lọc theo khu vực (đối với Admin, Manager)
- [ ] Refresh dữ liệu định kỳ
- [ ] Xem được BĐS trong khu vực quản lý (Manager)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tạo view/materialized view tổng hợp thống kê BĐS |
| **Backend API** | `GET /api/dashboard/property-summary` - thống kê tổng quan |
| **Backend API** | `GET /api/dashboard/property-by-status` - phân loại theo trạng thái |
| **Backend API** | `GET /api/dashboard/property-by-month` - BĐS mới theo tháng |
| **Backend API** | `GET /api/dashboard/expiring-properties` - BĐS gần hết hạn |
| **Frontend UI** | Màn hình dashboard.html: card thống kê + biểu đồ (Chart.js/Recharts) |
| **Frontend UI** | Component biểu đồ tròn, biểu đồ cột |
| **Frontend UI** | Bảng danh sách BĐS gần hết hạn |
| **Permission** | Manager chỉ xem được BĐS trong khu vực quản lý |
| **Testing** | Test dữ liệu dashboard đúng với quyền |

---

## DASH-02: Xem thống kê phòng

- **Tên:** Dashboard thống kê phòng
- **Role:** Admin, Manager, HouseHolder
- **Mô tả:** As a **người quản lý**, I want **xem thống kê trạng thái phòng**, So that **biết được tỷ lệ lấp đầy và tình trạng phòng**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Biểu đồ tròn phân loại phòng theo trạng thái (đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống)
- [ ] Số liệu tổng số phòng, phòng trống, phòng đã cho thuê
- [ ] Tỷ lệ lấp đầy (occupancy rate)
- [ ] Lọc theo BĐS hoặc khu vực
- [ ] Click vào từng trạng thái → lọc danh sách phòng tương ứng

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/dashboard/room-summary` - thống kê phòng tổng quan |
| **Backend API** | `GET /api/dashboard/room-by-status` - phân loại theo trạng thái |
| **Backend API** | `GET /api/dashboard/occupancy-rate` - tỷ lệ lấp đầy |
| **Frontend UI** | Thẻ thống kê phòng trên dashboard |
| **Frontend UI** | Biểu đồ tròn trạng thái phòng |
| **Frontend UI** | Click filter theo trạng thái |
| **Permission** | Manager chỉ xem được phòng trong khu vực |
| **Testing** | Test dữ liệu phòng chính xác |

---

## DASH-03: Xem doanh thu

- **Tên:** Dashboard doanh thu
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xem thống kê doanh thu từ cho thuê phòng**, So that **đánh giá hiệu quả kinh doanh**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Tổng doanh thu theo tháng/năm
- [ ] Biểu đồ đường doanh thu theo thời gian
- [ ] Top BĐS có doanh thu cao nhất
- [ ] Doanh thu theo khu vực
- [ ] Lọc theo khoảng thời gian

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tạo view tổng hợp doanh thu từ bảng hợp đồng |
| **Backend API** | `GET /api/dashboard/revenue` - doanh thu tổng quan |
| **Backend API** | `GET /api/dashboard/revenue-by-property` - doanh thu theo BĐS |
| **Backend API** | `GET /api/dashboard/revenue-by-area` - doanh thu theo khu vực |
| **Frontend UI** | Component biểu đồ doanh thu |
| **Frontend UI** | Bộ lọc thời gian (date range picker) |
| **Frontend UI** | Top BĐS doanh thu cao (bảng xếp hạng) |
| **Permission** | Chỉ Admin/Super Admin xem được doanh thu |
| **Testing** | Test doanh thu đúng với dữ liệu hợp đồng |

---

# Epic 3: Tìm kiếm BĐS/Phòng

**Mã Epic:** SEARCH
**Business Objective:** Giúp người dùng nhanh chóng tìm được BĐS/phòng phù hợp.
**Mô tả:** Cung cấp các chức năng tìm kiếm cơ bản, nâng cao và gợi ý.
**Dependency:** Epic 5 (Quản lý BĐS), Epic 6 (Quản lý Phòng)

---

## SEARCH-01: Tìm kiếm cơ bản

- **Tên:** Tìm kiếm BĐS/phòng cơ bản
- **Role:** Tất cả (kể cả Khách hàng không cần đăng nhập)
- **Mô tả:** As a **người dùng**, I want **tìm kiếm BĐS/phòng bằng từ khóa**, So that **nhanh chóng tìm được BĐS/phòng mong muốn**

**Priority:** High

**Acceptance Criteria:**
- [ ] Ô tìm kiếm trên header/dashboard
- [ ] Gợi ý kết quả khi gõ (autocomplete)
- [ ] Tìm kiếm theo: tên BĐS, địa chỉ, tên phòng
- [ ] Kết quả hiển thị dạng danh sách có phân trang
- [ ] Highlight từ khóa trong kết quả
- [ ] Debounce input (300ms) tránh gọi API quá nhiều

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tạo full-text search index trên bảng BĐS và Phòng |
| **Backend API** | `GET /api/search?q=keyword` - tìm kiếm cơ bản, phân trang |
| **Backend API** | `GET /api/search/suggest?q=keyword` - gợi ý khi gõ |
| **Frontend UI** | Search bar component với autocomplete dropdown |
| **Frontend UI** | Trang kết quả tìm kiếm |
| **Frontend UI** | Highlight từ khóa, phân trang |
| **Testing** | Test tìm kiếm với nhiều từ khóa, không có kết quả |

---

## SEARCH-02: Tìm kiếm nâng cao

- **Tên:** Tìm kiếm nâng cao với bộ lọc
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **lọc BĐS/phòng theo nhiều tiêu chí**, So that **tìm được BĐS phù hợp với nhu cầu cụ thể**

**Priority:** High

**Acceptance Criteria:**
- [ ] Bộ lọc: loại BĐS, loại phòng, khoảng giá, diện tích, số phòng ngủ
- [ ] Bộ lọc: nội thất, tiện ích, dịch vụ
- [ ] Bộ lọc: khu vực (Tỉnh/Quận/Phường)
- [ ] Bộ lọc: trạng thái phòng (đang trống, sắp trống)
- [ ] Kết hợp nhiều bộ lọc cùng lúc
- [ ] Reset bộ lọc
- [ ] Hiển thị số lượng kết quả tìm thấy

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Tối ưu query với nhiều JOIN và WHERE điều kiện |
| **Backend API** | `GET /api/search/advanced` - search nâng cao với query params |
| **Backend API** | `GET /api/search/filters` - lấy danh sách giá trị cho các bộ lọc |
| **Frontend UI** | Filter panel (có thể là slide-over hoặc modal) |
| **Frontend UI** | Range slider cho giá và diện tích |
| **Frontend UI** | Cascading dropdown cho địa giới HC |
| **Testing** | Test kết hợp nhiều bộ lọc, không có kết quả |

---

## SEARCH-03: Lưu bộ lọc tìm kiếm

- **Tên:** Lưu bộ lọc tìm kiếm yêu thích
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng đã đăng nhập**, I want **lưu bộ lọc tìm kiếm đang dùng**, So that **có thể tìm lại nhanh mà không cần thiết lập lại**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Nút "Lưu bộ lọc" trên kết quả tìm kiếm
- [ ] Đặt tên cho bộ lọc đã lưu
- [ ] Danh sách bộ lọc đã lưu trong trang cá nhân
- [ ] Click vào bộ lọc đã lưu → tự động áp dụng
- [ ] Xóa bộ lọc đã lưu

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `saved_search` (id, user_id, filter_json, name, created_at) |
| **Backend API** | `POST /api/search/saved-filters` - lưu bộ lọc |
| **Backend API** | `GET /api/search/saved-filters` - danh sách đã lưu |
| **Backend API** | `DELETE /api/search/saved-filters/:id` - xóa |
| **Frontend UI** | Dialog lưu bộ lọc, danh sách đã lưu |
| **Testing** | Test lưu, áp dụng, xóa bộ lọc |

---

## SEARCH-04: Gợi ý tìm kiếm thông minh

- **Tên:** Gợi ý tìm kiếm thông minh
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **nhận gợi ý tìm kiếm dựa trên hành vi và xu hướng**, So that **khám phá được BĐS tiềm năng**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Gợi ý BĐS nổi bật (featured)
- [ ] Gợi ý BĐS xem nhiều
- [ ] Gợi ý BĐS mới đăng
- [ ] Gợi ý theo khu vực người dùng hay xem

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/search/trending` - BĐS xu hướng |
| **Backend API** | `GET /api/search/suggestions` - gợi ý cá nhân hóa |
| **Frontend UI** | Suggestions panel dưới search bar |
| **Testing** | Test gợi ý hiển thị đúng dữ liệu |

---

# Epic 4: Bản đồ tương tác

**Mã Epic:** MAP
**Business Objective:** Trực quan hóa BĐS trên bản đồ giúp người dùng dễ dàng khám phá theo vị trí địa lý.
**Mô tả:** Tích hợp Google Maps, hiển thị marker BĐS, tìm kiếm theo bán kính.
**Dependency:** Epic 5 (Quản lý BĐS)

---

## MAP-01: Xem bản đồ BĐS

- **Tên:** Xem bản đồ BĐS
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **xem bản đồ với các marker BĐS**, So that **khám phá BĐS theo vị trí địa lý**

**Priority:** High

**Acceptance Criteria:**
- [ ] Tích hợp Google Maps API
- [ ] Hiển thị tất cả BĐS đã duyệt trên bản đồ
- [ ] Marker hiển thị giá hoặc icon theo loại BĐS
- [ ] Zoom in/out chuột và touch
- [ ] Marker cluster khi zoom xa (nhiều marker gần nhau)
- [ ] Tự động center theo vị trí người dùng (nếu cho phép)
- [ ] Chế độ xem: Map và Satellite

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Đảm bảo bảng BĐS có trường latitude, longitude, indexed |
| **Backend API** | `GET /api/map/properties?sw_lat&sw_lng&ne_lat&ne_lng` - BĐS trong khung bản đồ |
| **Frontend UI** | Màn hình map.html: Google Maps integration |
| **Frontend UI** | Marker components với custom icon |
| **Frontend UI** | Marker clustering (MarkerClusterer) |
| **Frontend UI** | Nút chuyển đổi Map/Satellite |
| **Testing** | Test hiển thị marker đúng vị trí, cluster hoạt động |

---

## MAP-02: Marker và popup thông tin

- **Tên:** Marker chi tiết BĐS
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **click vào marker để xem thông tin tóm tắt BĐS**, So that **biết được thông tin cơ bản trước khi xem chi tiết**

**Priority:** High

**Acceptance Criteria:**
- [ ] Click marker → hiển thị info window/popup
- [ ] Popup hiển thị: tên BĐS, giá, địa chỉ, hình ảnh thumbnail
- [ ] Popup hiển thị trạng thái (nếu còn phòng trống)
- [ ] Nút "Xem chi tiết" trong popup → chuyển đến chi tiết BĐS
- [ ] Marker được đánh dấu active khi click
- [ ] Đóng popup khi click ra ngoài

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/map/property/:id/summary` - thông tin tóm tắt cho popup |
| **Frontend UI** | InfoWindow/ActionSheet component trên bản đồ |
| **Frontend UI** | Xử lý sự kiện click marker và đóng popup |
| **Testing** | Test click marker, popup hiển thị đúng dữ liệu |

---

## MAP-03: Tìm kiếm theo bán kính

- **Tên:** Tìm kiếm BĐS theo bán kính
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **kéo thanh trượt để chọn bán kính tìm kiếm**, So that **tìm BĐS trong phạm vi mong muốn**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Range slider chọn bán kính (1km - 50km)
- [ ] Hiển thị vòng tròn bán kính trên bản đồ
- [ ] Tự động cập nhật marker khi thay đổi bán kính
- [ ] Hiển thị số lượng BĐS tìm thấy trong bán kính
- [ ] Có thể kéo điểm center để thay đổi vị trí trung tâm

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/map/radius?lat&lng&radius_km` - BĐS trong bán kính |
| **Frontend UI** | Range slider component |
| **Frontend UI** | Vẽ vòng tròn bán kính trên Google Maps (Circle) |
| **Frontend UI** | Debounce update khi kéo slider |
| **Testing** | Test tìm kiếm với bán kính khác nhau |

---

## MAP-04: Bottom sheet chi tiết BĐS

- **Tên:** Bottom sheet danh sách BĐS
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **kéo lên bottom sheet hiển thị danh sách BĐS trong khu vực**, So that **có thể xem và so sánh nhiều BĐS cùng lúc**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Bottom sheet kéo từ dưới lên (draggable)
- [ ] Hiển thị danh sách BĐS trong khung bản đồ hiện tại
- [ ] Mỗi item: hình ảnh, tên, giá, địa chỉ, trạng thái phòng
- [ ] Click vào item → focus marker và mở popup
- [ ] Bottom sheet có 2 trạng thái: thu gọn (collapsed) và mở rộng (expanded)
- [ ] Pull-to-refresh danh sách

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Bottom sheet component (react-spring / framer-motion) |
| **Frontend UI** | Danh sách BĐS trong bottom sheet |
| **Frontend UI** | Sync giữa bottom sheet và marker trên bản đồ |
| **Frontend UI** | Pull-to-refresh |
| **Testing** | Test kéo bottom sheet, click item → focus marker |

---

# Epic 5: Quản lý Bất động sản

**Mã Epic:** BDS
**Business Objective:** Quản lý toàn bộ vòng đời BĐS từ tạo mới đến hết hạn.
**Mô tả:** CRUD BĐS, quy trình duyệt, quản lý hết hạn, đánh dấu nổi bật.
**Dependency:** Epic 1 (Xác thực), Epic 7 (Người dùng & Phân quyền), Epic 8 (Danh mục)

---

## BDS-01: Tạo Bất động sản

- **Tên:** Thêm mới BĐS
- **Role:** HouseHolder, Manager, Admin, Super Admin
- **Mô tả:** As a **người có quyền tạo BĐS**, I want **nhập đầy đủ thông tin BĐS bao gồm hình ảnh, nội thất, tiện ích**, So that **đăng tin cho thuê BĐS**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form 2 tab: tab "Thông tin BĐS" và tab "Thông tin phòng"
- [ ] Tab BĐS: tên, mô tả, địa chỉ, loại BĐS, diện tích, giá thuê
- [ ] Tab BĐS: số phòng ngủ, số toilet, số tầng, hướng nhà, năm xây dựng
- [ ] Tab BĐS: mặt tiền, đường vào, giấy tờ pháp lý
- [ ] Tab BĐS: nội thất (group-item UI, thêm nhiều), tiện ích
- [ ] Tab BĐS: chọn tọa độ trên bản đồ (latitude, longitude)
- [ ] Upload tối đa 10 hình ảnh (xem trước, xóa, sắp xếp thứ tự)
- [ ] Validate các trường bắt buộc
- [ ] Tự động lưu nháp (draft) nếu chưa hoàn thành
- [ ] Nút "Lưu nháp" / "Gửi duyệt"
- [ ] Khi tạo bởi HouseHolder/Manager → trạng thái "chờ duyệt"
- [ ] Khi tạo bởi Admin/Super Admin → trạng thái "đã duyệt"

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | INSERT vào bảng `bat_dong_san` + bảng liên quan (hình ảnh, nội thất, tiện ích) |
| **Backend API** | `POST /api/properties` - tạo BĐS mới (multipart/form-data nếu có file) |
| **Backend API** | `POST /api/upload` - upload hình ảnh (tối đa 10) |
| **Backend API** | `DELETE /api/upload/:id` - xóa hình ảnh |
| **Backend API** | `GET /api/catalog/furniture` - danh sách nội thất để chọn |
| **Backend API** | `GET /api/catalog/utilities` - danh sách tiện ích để chọn |
| **Backend API** | `GET /api/catalog/property-types` - loại BĐS |
| **Backend API** | Geocoding: chuyển địa chỉ → tọa độ (Google Geocoding API) |
| **Frontend UI** | Màn hình add-property.html: form 2 tab |
| **Frontend UI** | Google Maps picker cho tọa độ |
| **Frontend UI** | Image upload với preview, drag-and-drop reorder |
| **Frontend UI** | Group-item UI cho nội thất (thêm/xóa từng item) |
| **Frontend UI** | Validation form |
| **Validation** | Validate tên BĐS không để trống, tối đa 255 ký tự |
| **Validation** | Validate diện tích > 0, giá thuê > 0 |
| **Validation** | Validate tọa độ (latitude: -90 to 90, longitude: -180 to 180) |
| **Validation** | Tối đa 10 hình ảnh, định dạng: jpg, png, webp |
| **Permission** | HouseHolder/Manager → trạng thái "chờ duyệt" |
| **Permission** | Admin/Super Admin → trạng thái "đã duyệt" |
| **Testing** | Test tạo BĐS với đầy đủ trường, thiếu trường, upload hình |

---

## BDS-02: Xem chi tiết Bất động sản

- **Tên:** Xem chi tiết BĐS
- **Role:** Tất cả (kể cả không đăng nhập)
- **Mô tả:** As a **người dùng**, I want **xem chi tiết BĐS với đầy đủ thông tin và hình ảnh**, So that **đánh giá BĐS có phù hợp không**

**Priority:** High

**Acceptance Criteria:**
- [ ] Hiển thị: tên, giá, địa chỉ, mô tả, diện tích, loại BĐS
- [ ] Gallery hình ảnh (swipe/carousel, click phóng to)
- [ ] Thông tin chi tiết: số phòng ngủ, toilet, tầng, hướng nhà, năm xây dựng
- [ ] Thông tin: mặt tiền, đường vào, giấy tờ pháp lý
- [ ] Danh sách nội thất (icon + tên)
- [ ] Danh sách tiện ích (icon + tên + khoảng cách)
- [ ] Bản đồ nhỏ hiển thị vị trí BĐS
- [ ] Danh sách phòng trực thuộc (grid)
- [ ] Nút yêu thích, chia sẻ
- [ ] BĐS hiển thị trạng thái theo logic:
    - Chưa duyệt → "Chưa duyệt"
    - Hết hạn → "Hết hạn"
    - Đã duyệt:
        - Có phòng "đang trống" → "Còn trống"
        - Không có phòng "đang trống" nhưng có phòng "sắp trống" → "Sắp có phòng"
        - Còn lại → "Hết phòng"

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Query BĐS + JOIN: loại BĐS, hình ảnh, nội thất, tiện ích, phòng |
| **Backend API** | `GET /api/properties/:id` - chi tiết BĐS |
| **Backend API** | `GET /api/properties/:id/rooms` - danh sách phòng |
| **Backend API** | Tăng lượt xem (nếu có) |
| **Frontend UI** | Màn hình property-detail.html |
| **Frontend UI** | Image gallery/carousel component |
| **Frontend UI** | Mini map component |
| **Frontend UI** | Room grid component |
| **Frontend UI** | Nút yêu thích, chia sẻ |
| **Testing** | Test hiển thị đúng dữ liệu, gallery, bản đồ |

---

## BDS-03: Sửa Bất động sản

- **Tên:** Cập nhật thông tin BĐS
- **Role:** HouseHolder (của mình), Manager (trong KV), Admin, Super Admin
- **Mô tả:** As a **người có quyền sửa**, I want **cập nhật thông tin BĐS**, So that **thông tin luôn chính xác và cập nhật**

**Priority:** High

**Acceptance Criteria:**
- [ ] Mở form sửa với dữ liệu hiện tại
- [ ] Sửa tất cả các trường giống khi tạo
- [ ] Thêm/xóa/sắp xếp lại hình ảnh
- [ ] Nếu sửa bởi HouseHolder/Manager và BĐS đã duyệt → về "chờ duyệt"
- [ ] Nếu sửa bởi Admin/Super Admin → giữ nguyên trạng thái
- [ ] Lưu lịch sử chỉnh sửa

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | UPDATE bảng `bat_dong_san` + xóa/thêm bảng con (hình ảnh, nội thất, tiện ích) |
| **Backend API** | `PUT /api/properties/:id` - cập nhật BĐS |
| **Backend API** | `GET /api/properties/:id/edit` - lấy dữ liệu cho form sửa |
| **Frontend UI** | Form sửa (dùng lại component tạo) |
| **Frontend UI** | Pre-fill dữ liệu hiện tại |
| **Permission** | Kiểm tra quyền sửa: chủ sở hữu hoặc Admin |
| **Testing** | Test sửa thành công, sửa khi không có quyền |

---

## BDS-04: Xóa Bất động sản

- **Tên:** Xóa BĐS
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xóa BĐS không còn sử dụng**, So that **dọn dẹp dữ liệu hệ thống**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Chỉ Admin/Super Admin mới có quyền xóa
- [ ] Hiển thị confirm dialog trước khi xóa
- [ ] Xóa mềm (soft delete) - cập nhật trạng thái "đã xóa"
- [ ] Xóa kéo theo các phòng, hình ảnh, hợp đồng liên quan
- [ ] Thông báo cho chủ BĐS khi bị xóa
- [ ] Không cho xóa BĐS đang có hợp đồng hiệu lực

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Soft delete: UPDATE trạng thái, hoặc hard delete với CASCADE |
| **Backend API** | `DELETE /api/properties/:id` - xóa BĐS |
| **Backend API** | `GET /api/properties/:id/check-delete` - kiểm tra có thể xóa? |
| **Frontend UI** | Confirm dialog + xử lý kết quả |
| **Permission** | Chỉ Admin/Super Admin |
| **Notification** | Gửi thông báo cho chủ BĐS |
| **Testing** | Test xóa BĐS không có HĐ, đang có HĐ hiệu lực |

---

## BDS-05: Duyệt Bất động sản

- **Tên:** Duyệt / Từ chối BĐS
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **duyệt hoặc từ chối BĐS do HouseHolder/Manager tạo**, So that **đảm bảo chất lượng tin đăng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách BĐS chờ duyệt
- [ ] Xem chi tiết BĐS trong luồng duyệt
- [ ] Nút "Duyệt" → trạng thái "đã duyệt"
- [ ] Nút "Từ chối" → hiển thị dialog nhập lý do → trạng thái "bị từ chối"
- [ ] Tự động gửi thông báo cho người tạo
- [ ] Duyệt nhiều BĐS cùng lúc (bulk approve)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Cập nhật trạng thái BĐS, ghi lại người duyệt, thời gian |
| **Backend API** | `PUT /api/properties/:id/approve` - duyệt BĐS |
| **Backend API** | `PUT /api/properties/:id/reject` - từ chối + lý do |
| **Backend API** | `PUT /api/properties/bulk-approve` - duyệt hàng loạt |
| **Backend API** | `GET /api/properties/pending` - danh sách chờ duyệt |
| **Frontend UI** | Tab BĐS chờ duyệt trong my-properties |
| **Frontend UI** | Approve/reject dialog |
| **Frontend UI** | Bulk select + bulk action |
| **Permission** | Chỉ Admin/Super Admin |
| **Notification** | Tự động gửi thông báo kết quả duyệt |
| **Testing** | Test duyệt, từ chối, bulk approve |

---

## BDS-06: Quản lý BĐS hết hạn

- **Tên:** Gia hạn BĐS
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin**, I want **xem và quản lý BĐS sắp hết hạn/hết hạn**, So that **gia hạn kịp thời hoặc gỡ tin**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách BĐS sắp hết hạn (trong 7 ngày)
- [ ] Danh sách BĐS đã hết hạn
- [ ] Nút "Gia hạn" → cập nhật ngày hết hạn mới
- [ ] Tự động chuyển trạng thái "hết hạn" khi đến ngày
- [ ] Thông báo cho chủ BĐS trước khi hết hạn
- [ ] Filter: Tất cả / Sắp hết hạn / Đã hết hạn

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Cron job / scheduler kiểm tra và cập nhật trạng thái hết hạn |
| **Backend API** | `GET /api/properties/expiring` - BĐS sắp hết hạn |
| **Backend API** | `GET /api/properties/expired` - BĐS đã hết hạn |
| **Backend API** | `PUT /api/properties/:id/renew` - gia hạn |
| **Frontend UI** | Tab quản lý hết hạn |
| **Frontend UI** | Nút gia hạn |
| **Notification** | Gửi thông báo nhắc hết hạn |
| **Testing** | Test tự động hết hạn, gia hạn thủ công |

---

## BDS-07: Đánh dấu nổi bật

- **Tên:** Đánh dấu BĐS nổi bật
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **đánh dấu BĐS nổi bật (featured)**, So that **BĐS được ưu tiên hiển thị và gợi ý**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Nút bật/tắt nổi bật trên chi tiết BĐS
- [ ] BĐS nổi bật hiển thị icon/vàng badge
- [ ] Ưu tiên hiển thị BĐS nổi bật trong danh sách
- [ ] BĐS nổi bật xuất hiện trong gợi ý

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Cập nhật trường `featured` trong bảng BĐS |
| **Backend API** | `PUT /api/properties/:id/feature` - toggle featured |
| **Backend API** | `GET /api/properties/featured` - danh sách nổi bật |
| **Frontend UI** | Featured toggle, badge UI |
| **Testing** | Test featured sorting priority |

---

## BDS-08: Danh sách BĐS của tôi

- **Tên:** Quản lý danh sách BĐS cá nhân
- **Role:** HouseHolder, Manager, Admin, Super Admin
- **Mô tả:** As a **người dùng**, I want **xem danh sách BĐS tôi đã tạo/quản lý**, So that **dễ dàng theo dõi và quản lý**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách BĐS dưới dạng grid/card
- [ ] Filter: Tất cả, Đã duyệt, Chờ duyệt, Hết hạn, Nháp
- [ ] Mỗi card hiển thị: hình ảnh, tên, giá, trạng thái, số phòng
- [ ] Nút: Sửa, Xóa, Xem chi tiết
- [ ] Tab: "Của tôi" và "Tất cả" (Admin/Manager)
- [ ] Tìm kiếm trong danh sách
- [ ] Phân trang

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/properties/my-properties` - BĐS của tôi |
| **Backend API** | `GET /api/properties/managed` - BĐS trong KV (Manager) |
| **Backend API** | `GET /api/properties/all` - tất cả (Admin) |
| **Frontend UI** | Màn hình my-properties.html: grid danh sách |
| **Frontend UI** | Filter tabs, search bar |
| **Frontend UI** | Action buttons (sửa, xóa, xem) |
| **Permission** | Lọc theo quyền: HouseHolder chỉ thấy của mình |
| **Testing** | Test danh sách đúng với quyền |

---

# Epic 6: Quản lý Phòng

**Mã Epic:** PHONG
**Business Objective:** Quản lý chi tiết từng phòng trong BĐS, theo dõi trạng thái và khách thuê.
**Mô tả:** CRUD phòng, quản lý trạng thái, quy trình đặt cọc và hợp đồng.
**Dependency:** Epic 1 (Xác thực), Epic 5 (Quản lý BĐS)

---

## PHONG-01: Tạo phòng

- **Tên:** Thêm phòng mới
- **Role:** HouseHolder, Manager, Admin, Super Admin
- **Mô tả:** As a **người quản lý BĐS**, I want **thêm phòng mới vào BĐS**, So that **cập nhật thông tin cho thuê chi tiết**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form tạo phòng trong tab "Thông tin phòng" của add-property
- [ ] Các trường: tên phòng, mô tả, loại phòng, diện tích, giá thuê, giá cọc
- [ ] Chọn nội thất, tiện ích cho phòng
- [ ] Chọn dịch vụ kèm theo (giá, đơn vị, chu kỳ, chỉ số đầu)
- [ ] Upload tối đa 10 hình ảnh
- [ ] Validate các trường bắt buộc
- [ ] Có thể thêm nhiều phòng cùng lúc
- [ ] Mỗi phòng có thể xóa tạm thời (trong form) trước khi lưu

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | INSERT vào bảng `phong` + bảng liên quan (dịch vụ, nội thất, tiện ích) |
| **Backend API** | `POST /api/properties/:propertyId/rooms` - tạo phòng |
| **Backend API** | `GET /api/catalog/room-types` - loại phòng |
| **Backend API** | `GET /api/catalog/services` - dịch vụ |
| **Frontend UI** | Room form trong add-property.html |
| **Frontend UI** | Service dialog: chọn dịch vụ với price/unit/cycle/type/initialIndex |
| **Frontend UI** | Image upload cho từng phòng |
| **Frontend UI** | Add/remove room động |
| **Validation** | Validate giá thuê > 0, diện tích > 0 |
| **Testing** | Test tạo phòng đơn, tạo nhiều phòng cùng lúc |

---

## PHONG-02: Xem chi tiết phòng

- **Tên:** Xem chi tiết phòng
- **Role:** Tất cả (kể cả không đăng nhập)
- **Mô tả:** As a **người dùng**, I want **xem chi tiết phòng trong BĐS**, So that **đánh giá phòng có phù hợp để thuê**

**Priority:** High

**Acceptance Criteria:**
- [ ] Hiển thị: tên phòng, giá thuê, giá cọc, diện tích, loại phòng
- [ ] Gallery hình ảnh phòng
- [ ] Danh sách nội thất, tiện ích
- [ ] Danh sách dịch vụ kèm (giá, đơn vị)
- [ ] Trạng thái phòng hiện tại (đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống)
- [ ] Nút yêu thích, chia sẻ
- [ ] Thông tin khách thuê hiện tại (nếu đã thuê)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/rooms/:id` - chi tiết phòng |
| **Backend API** | `GET /api/rooms/:id/services` - dịch vụ kèm |
| **Frontend UI** | Màn hình room-detail.html |
| **Frontend UI** | Gallery, service list, status badge |
| **Frontend UI** | Customer info section (nếu đã thuê) |
| **Testing** | Test hiển thị đúng dữ liệu phòng |

---

## PHONG-03: Sửa phòng

- **Tên:** Cập nhật thông tin phòng
- **Role:** HouseHolder (của mình), Manager (trong KV), Admin, Super Admin
- **Mô tả:** As a **người quản lý**, I want **sửa thông tin phòng**, So that **thông tin phòng luôn chính xác**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form sửa với dữ liệu hiện tại
- [ ] Sửa tất cả các trường: giá thuê, nội thất, dịch vụ, hình ảnh
- [ ] Khi sửa giá thuê → ghi lại lịch sử giá
- [ ] Thêm/xóa hình ảnh

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/rooms/:id` - cập nhật phòng |
| **Backend API** | `GET /api/rooms/:id/edit` - dữ liệu cho form sửa |
| **Frontend UI** | Form sửa phòng |
| **Frontend UI** | Pre-fill dữ liệu |
| **Permission** | Kiểm tra quyền sở hữu phòng |
| **Testing** | Test sửa thành công, không có quyền |

---

## PHONG-04: Xóa phòng

- **Tên:** Xóa phòng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xóa phòng không còn sử dụng**, So that **dọn dẹp dữ liệu**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Chỉ Admin/Super Admin
- [ ] Confirm dialog
- [ ] Soft delete
- [ ] Không xóa phòng đang có hợp đồng hiệu lực

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `DELETE /api/rooms/:id` |
| **Frontend UI** | Confirm dialog |
| **Permission** | Admin/Super Admin |
| **Testing** | Test xóa phòng, xóa khi có HĐ |

---

## PHONG-05: Đổi trạng thái phòng

- **Tên:** Cập nhật trạng thái phòng
- **Role:** HouseHolder, Manager, Admin, Super Admin, Sale (cần duyệt)
- **Mô tả:** As a **người quản lý phòng**, I want **thay đổi trạng thái phòng**, So that **cập nhật tình trạng cho thuê thực tế**

**Priority:** High

**Acceptance Criteria:**
- [ ] 8 trạng thái: đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống
- [ ] Radio button / dropdown 8 trạng thái (room-detail.html)
- [ ] Admin|SuperAdmin|Manager|HouseHolder đổi trực tiếp (bất kỳ → bất kỳ)
- [ ] Sale đổi X → Y bất kỳ → phòng chuyển sang "chờ duyệt Y", cần duyệt
- [ ] Duyệt (bởi HouseHolder|Manager|Admin|SuperAdmin) → chuyển "chờ duyệt Y" → "Y"
- [ ] Từ chối → chuyển về trạng thái cũ
- [ ] Khi đổi sang "đã cọc" hoặc "đã thuê" → cần nhập thông tin khách
- [ ] Khi đổi sang "đang trống" → xóa thông tin khách hiện tại
- [ ] Ghi lại lịch sử thay đổi trạng thái

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Mở rộng enum trạng thái phòng: thêm `chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống` |
| **Database** | Bảng `lich_su_trang_thai_phong` (id, phong_id, trang_thai_cu, trang_thai_moi, nguoi_thay_doi, thoi_gian) |
| **Database** | Bảng `yeu_cau_doi_trang_thai` (id, phong_id, nguoi_yeu_cau, trang_thai_cu, trang_thai_moi, ly_do, trang_thai_duyet, nguoi_duyet, thoi_gian) |
| **Backend API** | `PUT /api/rooms/:id/status` - đổi trạng thái trực tiếp (Admin|SuperAdmin|Manager|HouseHolder) |
| **Backend API** | `POST /api/rooms/:id/request-status-change` - Sale gửi yêu cầu đổi trạng thái |
| **Backend API** | `GET /api/rooms/:id/status-history` - lịch sử |
| **Backend API** | `GET /api/rooms/:id/request-status` - kiểm tra trạng thái yêu cầu hiện tại |
| **Frontend UI** | Radio button / dropdown 8 trạng thái |
| **Frontend UI** | Customer info form (khi đổi sang đã cọc/đã thuê) |
| **Frontend UI** | Badge màu khác cho trạng thái chờ duyệt |
| **Permission** | Kiểm tra role: Admin|SuperAdmin|Manager|HouseHolder → trực tiếp; Sale → chờ duyệt |
| **Testing** | Test đổi trạng thái trực tiếp, qua duyệt, từ chối, check lịch sử |

---

## PHONG-06: Duyệt đổi trạng thái phòng (Sale)

- **Tên:** Duyệt yêu cầu đổi trạng thái phòng
- **Role:** Admin, SuperAdmin, HouseHolder (chủ phòng), Manager (quản lý phòng)
- **Mô tả:** As a **Admin/SuperAdmin/HouseHolder/Manager**, I want **duyệt hoặc từ chối yêu cầu đổi trạng thái phòng từ Sale**, So that **kiểm soát việc thay đổi trạng thái**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách yêu cầu đổi trạng thái từ Sale
- [ ] Hiển thị: phòng, trạng thái cũ, trạng thái yêu cầu (chờ duyệt Y), người yêu cầu, thời gian
- [ ] Nút "Duyệt" → chuyển từ "chờ duyệt Y" → "Y" (cập nhật thông tin khách nếu có)
- [ ] Nút "Từ chối" → nhập lý do → chuyển về trạng thái cũ
- [ ] Thông báo cho Sale kết quả duyệt
- [ ] HouseHolder chỉ duyệt được yêu cầu cho phòng thuộc BĐS của mình
- [ ] Manager chỉ duyệt được yêu cầu trong khu vực quản lý

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `yeu_cau_doi_trang_thai` (id, phong_id, nguoi_yeu_cau, trang_thai_cu, trang_thai_moi, ly_do, trang_thai_duyet, nguoi_duyet, thoi_gian) |
| **Backend API** | `GET /api/requests/status-changes` - danh sách yêu cầu (có filter theo người duyệt) |
| **Backend API** | `PUT /api/requests/status-changes/:id/approve` - duyệt + cập nhật trạng thái phòng |
| **Backend API** | `PUT /api/requests/status-changes/:id/reject` - từ chối + lý do |
| **Frontend UI** | Danh sách yêu cầu + approve/reject dialog + hiển thị trạng thái cũ→mới |
| **Permission** | Admin|SuperAdmin: tất cả; HouseHolder: phòng BĐS mình; Manager: trong KV |
| **Notification** | Gửi TB cho Sale khi được duyệt/từ chối |
| **Testing** | Test gửi yêu cầu, duyệt thành công, từ chối, kiểm tra quyền duyệt |

---

## PHONG-07: Xác nhận đặt cọc

- **Tên:** Xác nhận đặt cọc phòng
- **Role:** Admin, Manager, HouseHolder, Sale
- **Mô tả:** As a **người quản lý**, I want **xác nhận đặt cọc với thông tin khách hàng đầy đủ**, So that **quản lý được thông tin khách thuê**

**Priority:** High

**Acceptance Criteria:**
- [ ] Khi đổi trạng thái → "đã cọc" → hiển thị form nhập thông tin khách
- [ ] Các trường bắt buộc: tên khách hàng, số điện thoại, hình ảnh khách
- [ ] Validate tên, SĐT
- [ ] Upload hình ảnh khách hàng (có thể chụp trực tiếp)
- [ ] Lưu thông tin khách vào bảng Khách hàng
- [ ] Hiển thị thông tin khách trên chi tiết phòng

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | INSERT/UPDATE bảng `khach_hang` |
| **Backend API** | `POST /api/rooms/:id/deposit` - xác nhận cọc + thông tin khách |
| **Backend API** | `POST /api/customers` - tạo khách hàng |
| **Frontend UI** | Form nhập thông tin khách (room-detail.html) |
| **Frontend UI** | Camera capture hoặc upload từ gallery |
| **Validation** | Validate SĐT: 10-11 số, bắt đầu 0 |
| **Validation** | Validate tên không để trống |
| **Testing** | Test đặt cọc thành công, thiếu thông tin |

---

## PHONG-08: Quản lý hợp đồng

- **Tên:** Quản lý hợp đồng thuê phòng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin**, I want **quản lý hợp đồng thuê phòng**, So that **theo dõi lịch sử cho thuê và thanh toán**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách hợp đồng (đang hiệu lực, đã hết hạn, đã hủy)
- [ ] Tạo hợp đồng mới: chọn phòng, khách hàng, ngày BĐ-KT, giá thuê, cọc
- [ ] Upload file hợp đồng (PDF)
- [ ] Gia hạn hợp đồng
- [ ] Hủy hợp đồng
- [ ] Xem chi tiết hợp đồng

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | CRUD bảng `hop_dong` + file hợp đồng |
| **Backend API** | `GET/POST/PUT/DELETE /api/contracts` - CRUD hợp đồng |
| **Backend API** | `POST /api/contracts/:id/renew` - gia hạn |
| **Backend API** | `PUT /api/contracts/:id/cancel` - hủy |
| **Frontend UI** | Màn hình quản lý hợp đồng |
| **Frontend UI** | Contract form, file upload |
| **Permission** | Admin/Super Admin |
| **Testing** | Test CRUD hợp đồng, gia hạn, hủy |

---

## PHONG-09: Danh sách phòng theo BĐS

- **Tên:** Danh sách phòng theo BĐS
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **xem danh sách phòng của một BĐS dạng grid**, So that **nắm được tổng quan các phòng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Grid hiển thị: hình ảnh, tên phòng, giá, diện tích, trạng thái
- [ ] Badge trạng thái: đang trống (xanh), đã cọc (vàng), đã thuê (đỏ), sắp trống (cam)
- [ ] Lọc theo trạng thái
- [ ] Quick action: sửa, đổi trạng thái (popover/dialog)
- [ ] Click vào phòng → xem chi tiết

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/properties/:id/rooms` |
| **Frontend UI** | Room grid component (property-detail.html) |
| **Frontend UI** | Status badge component |
| **Frontend UI** | Quick-update bottom sheet (edit giá + status + customer) |
| **Testing** | Test danh sách phòng, filter, quick update |

---

# Epic 7: Người dùng & Phân quyền

**Mã Epic:** USER
**Business Objective:** Quản lý người dùng và phân quyền truy cập hệ thống.
**Mô tả:** CRUD người dùng, quản lý vai trò, phân quyền chi tiết và gán khu vực.
**Dependency:** Epic 1 (Xác thực), Epic 8 (Danh mục - Địa giới HC)

---

## USER-01: Danh sách người dùng

- **Tên:** Xem danh sách người dùng
- **Role:** Admin, Super Admin, Manager
- **Mô tả:** As a **Admin/Manager**, I want **xem danh sách người dùng trong hệ thống/khu vực**, So that **quản lý được nhân sự**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách dạng bảng: avatar, họ tên, tên đăng nhập, vai trò, email, SĐT, trạng thái
- [ ] Phân trang
- [ ] Tìm kiếm theo tên, email, SĐT
- [ ] Filter theo vai trò, trạng thái
- [ ] Manager chỉ xem được user trong khu vực quản lý
- [ ] Nút: Thêm mới, Sửa, Khóa/Mở khóa

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/users` - danh sách (phân trang, search, filter) |
| **Backend API** | `GET /api/users/areas` - danh sách user trong khu vực (Manager) |
| **Frontend UI** | Màn hình members.html: bảng danh sách |
| **Frontend UI** | Search bar, filter dropdowns |
| **Frontend UI** | Action buttons (sửa, khóa) |
| **Permission** | Manager: lọc theo UserArea |
| **Testing** | Test hiển thị đúng vai trò, filter hoạt động |

---

## USER-02: Tạo người dùng

- **Tên:** Thêm người dùng mới
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **tạo tài khoản người dùng mới**, So that **cấp quyền truy cập hệ thống**

**Priority:** High

**Acceptance Criteria:**
- [ ] Dialog form tạo user: tên đăng nhập, mật khẩu, họ tên, email, SĐT
- [ ] Chọn vai trò (dropdown)
- [ ] Chọn khu vực quản lý (tỉnh/quận/phường) - nếu là Manager
- [ ] Upload avatar
- [ ] Validate các trường
- [ ] Tạo thành công → tự động gửi thông báo/xác nhận

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `POST /api/users` - tạo user |
| **Backend API** | `POST /api/users/:id/areas` - gán khu vực |
| **Frontend UI** | Dialog tạo user (members.html) |
| **Frontend UI** | Cascading dropdown địa giới HC |
| **Frontend UI** | Avatar upload |
| **Validation** | Validate trùng tên đăng nhập |
| **Permission** | Chỉ Admin/Super Admin |
| **Testing** | Test tạo user với các vai trò khác nhau |

---

## USER-03: Sửa người dùng

- **Tên:** Cập nhật thông tin người dùng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **sửa thông tin người dùng**, So that **thông tin luôn chính xác**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Dialog sửa với dữ liệu hiện tại
- [ ] Sửa: họ tên, email, SĐT, vai trò, khu vực
- [ ] Đổi avatar
- [ ] Không cho sửa tên đăng nhập
- [ ] Admin không thể sửa thông tin Super Admin

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/users/:id` |
| **Backend API** | `PUT /api/users/:id/areas` - cập nhật khu vực |
| **Frontend UI** | Dialog sửa (dùng chung component với tạo) |
| **Permission** | Không cho sửa user có role cao hơn |
| **Testing** | Test sửa thông tin, đổi vai trò |

---

## USER-04: Khóa/Mở khóa người dùng

- **Tên:** Khóa/Mở khóa tài khoản
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **khóa hoặc mở khóa tài khoản người dùng**, So that **kiểm soát truy cập hệ thống**

**Priority:** High

**Acceptance Criteria:**
- [ ] Nút "Khóa" / "Mở khóa" trên mỗi user
- [ ] Confirm dialog
- [ ] Khi khóa → user không thể đăng nhập
- [ ] Khi mở khóa → user đăng nhập lại bình thường
- [ ] Không thể khóa Super Admin
- [ ] Ghi lại lịch sử khóa/mở khóa

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/users/:id/toggle-lock` |
| **Frontend UI** | Lock/unlock button + confirm |
| **Permission** | Không khóa được Super Admin |
| **Testing** | Test khóa → không login được, mở khóa → login được |

---

## USER-05: Phân quyền theo vai trò

- **Tên:** Phân quyền chi tiết cho vai trò
- **Role:** Super Admin
- **Mô tả:** As a **Super Admin**, I want **cấu hình quyền cho từng vai trò**, So that **kiểm soát chức năng mỗi role có thể truy cập**

**Priority:** High

**Acceptance Criteria:**
- [ ] Giao diện 3 tab: Admin, Manager, HouseHolder (permission.html)
- [ ] 12 quyền checkbox: Duyệt BĐS, Duyệt phòng trống, Ghi BĐS, Ghi phòng
- [ ] 12 quyền: Đọc user, Ghi user, Ghi địa giới HC, Ghi nội thất
- [ ] 12 quyền: Ghi tiện ích, Ghi loại phòng, Ghi loại BĐS, Ghi dịch vụ
- [ ] Select all / Deselect all
- [ ] Lưu thay đổi → cập nhật quyền ngay
- [ ] Lưu ý: có phân biệt quyền của Admin và Manager (Admin có thêm quyền duyệt)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `phan_quyen`: role_code + permission_code |
| **Backend API** | `GET /api/permissions/:roleId` - quyền của role |
| **Backend API** | `PUT /api/permissions/:roleId` - cập nhật quyền |
| **Backend API** | `GET /api/permissions/available` - danh sách quyền có sẵn |
| **Frontend UI** | Màn hình permission.html: 3 tab + checkbox grid |
| **Frontend UI** | Select all/deselect all |
| **Frontend UI** | Save changes với xác nhận |
| **Permission** | Chỉ Super Admin |
| **Testing** | Test lưu quyền, kiểm tra truy cập sau khi thay đổi quyền |

---

## USER-06: Gán khu vực quản lý

- **Tên:** Gán khu vực quản lý cho người dùng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **gán tỉnh/quận/huyện/phường cho Manager**, So that **họ chỉ quản lý BĐS trong khu vực được giao**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Trong form tạo/sửa user, phần "Khu vực quản lý"
- [ ] Cascading dropdown: Chọn Tỉnh → Quận/Huyện → Phường/Xã
- [ ] Có thể chọn nhiều khu vực
- [ ] Hiển thị danh sách khu vực đã chọn (dạng tag/chip)
- [ ] Xóa khu vực khỏi danh sách
- [ ] Manager khi đăng nhập chỉ thấy BĐS trong KV được gán

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `user_area`: user_id + area_id |
| **Backend API** | `POST /api/users/:id/areas` - gán khu vực |
| **Backend API** | `DELETE /api/users/:id/areas/:areaId` - xóa |
| **Backend API** | `GET /api/locations` - danh sách địa giới HC |
| **Frontend UI** | Cascading dropdown component |
| **Frontend UI** | Tag/chip hiển thị khu vực đã chọn |
| **Testing** | Test gán KV, Manager chỉ thấy BĐS trong KV |

---

## USER-07: Quản lý vai trò

- **Tên:** Quản lý vai trò người dùng
- **Role:** Super Admin
- **Mô tả:** As a **Super Admin**, I want **thêm/sửa/xóa vai trò**, So that **linh hoạt trong quản lý phân quyền**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Danh sách vai trò (bảng)
- [ ] Thêm vai trò mới: tên, mô tả
- [ ] Sửa vai trò
- [ ] Xóa vai trò (không xóa được role mặc định)
- [ ] Gán quyền cho vai trò (dùng chung UI với USER-05)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | CRUD `GET/POST/PUT/DELETE /api/roles` |
| **Frontend UI** | Dialog CRUD vai trò |
| **Permission** | Super Admin |
| **Testing** | Test CRUD vai trò, xóa role mặc định bị chặn |

---

# Epic 8: Danh mục hệ thống (Catalog)

**Mã Epic:** CAT
**Business Objective:** Quản lý các danh mục dùng chung cho toàn hệ thống.
**Mô tả:** CRUD cho Địa giới hành chính, Loại BĐS, Loại phòng, Nội thất, Tiện ích, Dịch vụ.
**Dependency:** Epic 1 (Xác thực)

---

## CAT-01: Quản lý Địa giới hành chính

- **Tên:** Quản lý địa giới hành chính
- **Role:** Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **Super Admin**, I want **quản lý cây địa giới hành chính (Tỉnh/Quận/Phường)**, So that **cấu trúc dữ liệu vùng miền chính xác**

**Priority:** High

**Acceptance Criteria:**
- [ ] Hiển thị cây 3 cấp: Tỉnh → Quận/Huyện → Phường/Xã
- [ ] Expand/collapse từng node
- [ ] Thêm mới: chọn cấp (Tỉnh/Quận/Phường), nhập tên
- [ ] Sửa: đổi tên, slug
- [ ] Xóa: confirm, không xóa nếu đang được sử dụng
- [ ] Chọn parent khi tạo Quận/Phường
- [ ] Tìm kiếm trong cây địa giới

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `dia_gioi_hanh_chinh`: id, ten, slug, ma, cap, parent_id, path |
| **Backend API** | `GET /api/locations/tree` - cây địa giới |
| **Backend API** | `GET /api/locations/:id/children` - con của node |
| **Backend API** | `POST/PUT/DELETE /api/locations` - CRUD |
| **Frontend UI** | Tree component (catalog.html - tab Địa giới HC) |
| **Frontend UI** | CRUD dialog |
| **Frontend UI** | Search trong tree |
| **Permission** | Super Admin: CRUD, others: R |
| **Testing** | Test CRUD node, xóa node đang được dùng |

---

## CAT-02: Quản lý Loại BĐS

- **Tên:** Quản lý loại Bất động sản
- **Role:** Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **Super Admin**, I want **quản lý danh sách loại BĐS**, So that **phân loại BĐS thống nhất**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách dạng bảng: tên loại, mô tả, trạng thái
- [ ] Thêm: tên, mô tả
- [ ] Sửa: tên, mô tả
- [ ] Xóa (nếu không có BĐS nào dùng)
- [ ] Khóa/Mở khóa

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | CRUD `GET/POST/PUT/DELETE /api/catalog/property-types` |
| **Frontend UI** | Table + dialog CRUD (catalog.html) |
| **Permission** | Super Admin: ghi |
| **Testing** | Test CRUD, xóa loại đang được dùng |

---

## CAT-03: Quản lý Loại phòng

- **Tên:** Quản lý loại phòng
- **Role:** Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **Super Admin**, I want **quản lý danh sách loại phòng**, So that **phân loại phòng thống nhất**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách dạng bảng: tên loại, mô tả, trạng thái
- [ ] CRUD tương tự Loại BĐS

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | CRUD `GET/POST/PUT/DELETE /api/catalog/room-types` |
| **Frontend UI** | Table + dialog (nằm trong sub-tab của catalog.html) |
| **Permission** | Super Admin |
| **Testing** | Test CRUD loại phòng |

---

## CAT-04: Quản lý Nội thất

- **Tên:** Quản lý danh mục nội thất
- **Role:** Super Admin, Admin, Manager, HouseHolder (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý danh sách nội thất với icon**, So that **gắn nội thất cho BĐS/phòng**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách: tên nội thất, mô tả, icon, người tạo, trạng thái
- [ ] Super Admin tạo mặc định
- [ ] Manager/HouseHolder tạo → chỉ sửa/xóa cái của mình
- [ ] Admin sửa/xóa được của Manager/HouseHolder
- [ ] Icon upload/icon picker

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | CRUD `GET/POST/PUT/DELETE /api/catalog/furniture` |
| **Backend API** | Có filter: `?created_by=me` |
| **Frontend UI** | Table + dialog + icon picker |
| **Permission** | Phân quyền theo created_by |
| **Testing** | Test CRUD, kiểm tra quyền xóa theo creator |

---

## CAT-05: Quản lý Tiện ích

- **Tên:** Quản lý danh mục tiện ích
- **Role:** Super Admin, Admin, Manager, HouseHolder (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý danh sách tiện ích với icon và khoảng cách**, So that **gắn tiện ích cho BĐS/phòng**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách: tên, mô tả, icon, khoảng cách (m), người tạo, trạng thái
- [ ] CRUD tương tự Nội thất
- [ ] Có thêm trường khoảng cách (m)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | CRUD `GET/POST/PUT/DELETE /api/catalog/utilities` |
| **Frontend UI** | Table + dialog (giống CAT-04) |
| **Permission** | Giống CAT-04 |
| **Testing** | Test CRUD tiện ích |

---

## CAT-06: Quản lý Dịch vụ

- **Tên:** Quản lý danh mục dịch vụ
- **Role:** Super Admin, Admin, Manager, HouseHolder (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý danh sách dịch vụ kèm giá và đơn vị**, So that **thêm dịch vụ cho phòng cho thuê**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Danh sách: tên, mô tả, giá, đơn vị (tháng/năm/m²), chu kỳ
- [ ] Loại: bắt buộc / tự chọn
- [ ] Chỉ số đầu (cho điện/nước)
- [ ] CRUD theo quyền tương tự Nội thất

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | CRUD `GET/POST/PUT/DELETE /api/catalog/services` |
| **Frontend UI** | Table + dialog (thêm trường price, unit, cycle, type, initialIndex) |
| **Permission** | Theo creator |
| **Testing** | Test CRUD dịch vụ |

---

## CAT-07: Quản lý File

- **Tên:** Quản lý file/ảnh
- **Role:** Manager, HouseHolder, Admin, Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý file ảnh/tài liệu**, So that **đính kèm cho BĐS, phòng hoặc hợp đồng**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Upload file (ảnh: jpg/png/webp, tài liệu: PDF)
- [ ] Xem danh sách file
- [ ] Xóa file
- [ ] Gán entityType (BDS/Phòng/Người dùng/Khách hàng)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `POST /api/upload` - upload (multipart) |
| **Backend API** | `DELETE /api/files/:id` |
| **Backend API** | `GET /api/files?entityType&entityId` |
| **Frontend UI** | Upload component (drag & drop, preview) |
| **Testing** | Test upload, xóa, preview |

---

# Epic 9: Hồ sơ cá nhân

**Mã Epic:** PROFILE
**Business Objective:** Cho phép người dùng quản lý thông tin cá nhân.
**Mô tả:** Xem và chỉnh sửa hồ sơ cá nhân, đổi avatar, xem thông tin tài khoản.
**Dependency:** Epic 1 (Xác thực)

---

## PROFILE-01: Xem hồ sơ

- **Tên:** Xem hồ sơ cá nhân
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem thông tin hồ sơ của tôi**, So that **biết được thông tin tài khoản**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Hiển thị: avatar, họ tên, tên đăng nhập, email, SĐT
- [ ] Hiển thị: vai trò, khu vực quản lý (nếu có)
- [ ] Nút: Sửa hồ sơ, Đổi mật khẩu
- [ ] Nút: Đăng xuất

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/profile` - thông tin hồ sơ |
| **Frontend UI** | Màn hình profile.html |
| **Frontend UI** | Hiển thị thông tin user |
| **Testing** | Test hiển thị đúng thông tin |

---

## PROFILE-02: Sửa hồ sơ

- **Tên:** Cập nhật hồ sơ
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **sửa thông tin hồ sơ của tôi**, So that **thông tin luôn cập nhật**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form sửa: họ tên, email, số điện thoại
- [ ] Không cho sửa tên đăng nhập
- [ ] Validate các trường
- [ ] Lưu thành công → cập nhật giao diện

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/profile` - cập nhật hồ sơ |
| **Frontend UI** | Form sửa hồ sơ (user-info.html) |
| **Validation** | Validate email, SĐT |
| **Testing** | Test sửa thành công, validation |

---

## PROFILE-03: Đổi avatar

- **Tên:** Đổi ảnh đại diện
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **đổi ảnh đại diện**, So that **cá nhân hóa tài khoản**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Click vào avatar → mở dialog upload
- [ ] Upload từ thư viện hoặc chụp ảnh
- [ ] Crop/Resize ảnh
- [ ] Xem trước trước khi lưu
- [ ] Lưu → cập nhật avatar ngay

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/profile/avatar` - upload avatar |
| **Frontend UI** | Avatar upload component (crop, preview) |
| **Testing** | Test upload, crop, cập nhật avatar |

---

## PROFILE-04: Xem thông tin tài khoản

- **Tên:** Thông tin tài khoản
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem thông tin tài khoản chi tiết**, So that **biết được quyền hạn và thông tin đăng nhập**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Màn hình user-info.html: tên tài khoản, mã tài khoản
- [ ] Vai trò và quyền hạn (danh sách quyền)
- [ ] Khu vực quản lý (nếu là Manager)
- [ ] Thông tin đăng nhập: lần đăng nhập cuối, IP (nếu có)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/profile/account-info` |
| **Frontend UI** | Màn hình user-info.html |
| **Testing** | Test hiển thị thông tin |

---

# Epic 10: Thông báo

**Mã Epic:** NOTIF
**Business Objective:** Quản lý và theo dõi các thông báo trong hệ thống.
**Mô tả:** Hiển thị thông báo, đánh dấu đã đọc, tạo thông báo hệ thống, tự động gửi thông báo.
**Dependency:** Epic 1 (Xác thực)

---

## NOTIF-01: Danh sách thông báo

- **Tên:** Danh sách thông báo
- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem danh sách thông báo**, So that **không bỏ lỡ thông tin quan trọng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách thông báo theo thời gian (mới nhất đầu)
- [ ] Mỗi item: icon loại TB, tiêu đề, nội dung tóm tắt, thời gian
- [ ] Badge số lượng chưa đọc trên icon
- [ ] Phân trang hoặc infinite scroll
- [ ] Filter theo loại thông báo
- [ ] Click vào TB → xem chi tiết

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `thong_bao` |
| **Backend API** | `GET /api/notifications` - danh sách (phân trang) |
| **Backend API** | `GET /api/notifications/unread-count` - số chưa đọc |
| **Frontend UI** | Màn hình notifications.html |
| **Frontend UI** | Badge trên tab/bell icon |
| **Testing** | Test danh sách, phân trang, filter |

---

## NOTIF-02: Xem chi tiết thông báo

- **Tên:** Chi tiết thông báo
- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem chi tiết thông báo**, So that **nắm được nội dung đầy đủ**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Hiển thị: tiêu đề, nội dung đầy đủ, thời gian
- [ ] Hiển thị loại thông báo
- [ ] Nếu có entity (BDS/Phòng) → link đến chi tiết entity
- [ ] Tự động đánh dấu đã đọc khi xem

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/notifications/:id` |
| **Frontend UI** | Notification detail screen |
| **Frontend UI** | Deep link đến entity |
| **Testing** | Test xem chi tiết, auto mark read |

---

## NOTIF-03: Đánh dấu đã đọc

- **Tên:** Đánh dấu thông báo đã đọc
- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **đánh dấu thông báo đã đọc hoặc đánh dấu tất cả**, So that **quản lý thông báo hiệu quả**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Đánh dấu 1 TB là đã đọc
- [ ] Đánh dấu tất cả là đã đọc
- [ ] Swipe để mark read (mobile)
- [ ] Badge cập nhật ngay

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `PUT /api/notifications/:id/read` |
| **Backend API** | `PUT /api/notifications/read-all` |
| **Frontend UI** | Swipe action, button "Đánh dấu tất cả" |
| **Testing** | Test mark read, unread count cập nhật |

---

## NOTIF-04: Tạo thông báo hệ thống

- **Tên:** Tạo thông báo hệ thống
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **tạo thông báo hệ thống gửi đến người dùng**, So that **thông báo tin tức, cập nhật**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form tạo: loại (cập nhật hệ thống, tin tức, giảm giá phòng)
- [ ] Tiêu đề, nội dung
- [ ] Chọn người nhận: tất cả / theo vai trò / theo user cụ thể
- [ ] Gửi ngay hoặc hẹn giờ
- [ ] Xem trước thông báo

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `POST /api/notifications/system` - tạo TB hệ thống |
| **Backend API** | `POST /api/notifications/schedule` - hẹn giờ |
| **Frontend UI** | Form tạo thông báo (notifications.html - admin) |
| **Frontend UI** | User/role picker |
| **Permission** | Admin, Super Admin |
| **Testing** | Test tạo TB, gửi đến đúng người nhận |

---

## NOTIF-05: Tự động gửi thông báo duyệt

- **Tên:** Tự động gửi thông báo khi duyệt
- **Role:** Hệ thống
- **Mô tả:** As a **hệ thống**, I want **tự động gửi thông báo khi Admin duyệt BĐS/phòng**, So that **người yêu cầu biết kết quả**

**Priority:** High

**Acceptance Criteria:**
- [ ] Khi duyệt BĐS → TB cho người tạo: "BĐS [tên] đã được duyệt"
- [ ] Khi từ chối BĐS → TB có lý do từ chối
- [ ] Khi duyệt đổi trạng thái phòng → TB cho Sale
- [ ] Khi BĐS sắp hết hạn → TB nhắc nhở

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | Trigger notification service khi approve/reject |
| **Backend API** | Cron job kiểm tra BĐS sắp hết hạn |
| **Database** | Notification queue / direct insert |
| **Testing** | Test tự động gửi TB khi duyệt, từ chối |

---

## NOTIF-06: Xóa thông báo

- **Tên:** Xóa thông báo
- **Role:** Người nhận, Admin
- **Mô tả:** As a **người dùng**, I want **xóa thông báo không cần thiết**, So that **giữ danh sách thông báo gọn gàng**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Xóa 1 thông báo (swipe hoặc menu)
- [ ] Xóa nhiều cùng lúc
- [ ] Xóa tất cả

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `DELETE /api/notifications/:id` |
| **Backend API** | `DELETE /api/notifications/bulk` |
| **Frontend UI** | Delete action, bulk select |
| **Testing** | Test xóa đơn, xóa hàng loạt |

---

# Epic 11: Chia sẻ

**Mã Epic:** SHARE
**Business Objective:** Cho phép chia sẻ thông tin BĐS/phòng qua nhiều kênh.
**Mô tả:** Chia sẻ qua Zalo, Facebook, sao chép link, chia sẻ hình ảnh.
**Dependency:** Epic 5 (Quản lý BĐS), Epic 6 (Quản lý Phòng)

---

## SHARE-01: Chia sẻ qua Zalo

- **Tên:** Chia sẻ BĐS/phòng qua Zalo
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **chia sẻ BĐS/phòng qua Zalo**, So that **gửi cho bạn bè/đồng nghiệp**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Nút chia sẻ Zalo trên chi tiết BĐS/phòng
- [ ] Mở Zalo app/web với nội dung đã soạn sẵn
- [ ] Nội dung: tên BĐS, giá, địa chỉ, link
- [ ] Có thể chọn nội dung chia sẻ: địa chỉ, loại phòng, nội thất, tiện ích, dịch vụ

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/share/:entityType/:entityId` - dữ liệu chia sẻ |
| **Frontend UI** | Zalo sharing integration (Zalo SDK / URL scheme) |
| **Frontend UI** | Checkbox chọn nội dung (sharing.html) |
| **Testing** | Test share Zalo, nội dung đúng |

---

## SHARE-02: Chia sẻ qua Facebook

- **Tên:** Chia sẻ BĐS/phòng qua Facebook
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **chia sẻ BĐS/phòng qua Facebook**, So that **đăng lên timeline/gửi cho bạn**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Nút chia sẻ Facebook
- [ ] Facebook Share dialog với hình ảnh, tiêu đề, mô tả
- [ ] Open Graph tags cho link chia sẻ

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Facebook Share button (FB SDK / share dialog) |
| **Frontend UI** | Open Graph meta tags cho trang chi tiết |
| **Testing** | Test share Facebook, OG tags |

---

## SHARE-03: Sao chép link

- **Tên:** Sao chép link BĐS/phòng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **sao chép link BĐS/phòng**, So that **chia sẻ qua bất kỳ kênh nào**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Nút "Sao chép link"
- [ ] Copy URL vào clipboard
- [ ] Toast thông báo "Đã sao chép"
- [ ] Link dẫn đến trang chi tiết BĐS/phòng

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Copy to clipboard (navigator.clipboard) |
| **Frontend UI** | Toast notification |
| **Testing** | Test copy, paste ra browser |

---

## SHARE-04: Chia sẻ hình ảnh

- **Tên:** Chia sẻ hình ảnh BĐS/phòng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **chia sẻ hình ảnh BĐS/phòng**, So that **gửi ảnh trực tiếp cho người khác**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Nút "Chia sẻ hình ảnh"
- [ ] Chọn ảnh từ gallery của BĐS/phòng
- [ ] Share ảnh qua các app (native share)
- [ ] Có thể share nhiều ảnh cùng lúc

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/share/:entityType/:entityId/images` - danh sách ảnh |
| **Frontend UI** | Image picker + native share API |
| **Testing** | Test share ảnh thành công |

---

# Epic 12: Yêu thích & Lịch sử

**Mã Epic:** FAV
**Business Objective:** Cho phép người dùng lưu BĐS/phòng yêu thích và xem lịch sử.
**Mô tả:** Thêm/xóa yêu thích, danh sách yêu thích, lịch sử xem BĐS.
**Dependency:** Epic 5 (Quản lý BĐS), Epic 6 (Quản lý Phòng)

---

## FAV-01: Yêu thích BĐS

- **Tên:** Thêm BĐS vào yêu thích
- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **thêm BĐS vào danh sách yêu thích**, So that **dễ dàng tìm lại sau**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Icon trái tim trên card/chi tiết BĐS
- [ ] Click → toggle yêu thích
- [ ] Trạng thái active (đã thích) / inactive
- [ ] Animation khi toggle
- [ ] Chỉ cho user đã đăng nhập

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `bat_dong_san_yeu_thich` |
| **Backend API** | `POST /api/favorites/properties/:id/toggle` |
| **Backend API** | `GET /api/favorites/properties/check/:id` - kiểm tra đã thích? |
| **Frontend UI** | Heart icon component |
| **Testing** | Test toggle, hiển thị đúng trạng thái |

---

## FAV-02: Yêu thích phòng

- **Tên:** Thêm phòng vào yêu thích
- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **thêm phòng vào danh sách yêu thích**, So that **dễ dàng tìm lại sau**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Icon trái tim trên card/chi tiết phòng
- [ ] Tương tự FAV-01

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `phong_yeu_thich` |
| **Backend API** | `POST /api/favorites/rooms/:id/toggle` |
| **Frontend UI** | Heart icon (dùng chung component) |
| **Testing** | Test toggle yêu thích phòng |

---

## FAV-03: Danh sách yêu thích

- **Tên:** Xem danh sách yêu thích
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem danh sách BĐS/phòng đã yêu thích**, So that **dễ dàng xem lại**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Tab: BĐS yêu thích / Phòng yêu thích
- [ ] Grid/card hiển thị: hình ảnh, tên, giá, trạng thái
- [ ] Xóa khỏi danh sách yêu thích
- [ ] Click → xem chi tiết

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `GET /api/favorites/properties` |
| **Backend API** | `GET /api/favorites/rooms` |
| **Frontend UI** | Tab UI + card list |
| **Testing** | Test danh sách hiển thị đúng |

---

## FAV-04: Lịch sử xem BĐS

- **Tên:** Lịch sử xem BĐS
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem lịch sử các BĐS tôi đã xem**, So that **dễ dàng tìm lại BĐS đã quan tâm**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Danh sách BĐS đã xem (mới nhất trước)
- [ ] Tối đa 10 BĐS gần nhất
- [ ] Hiển thị: hình ảnh, tên, giá, thời gian xem
- [ ] Click → xem chi tiết

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Database** | Bảng `lich_su_xem_bds` |
| **Backend API** | `POST /api/history/properties/:id` - ghi lịch sử |
| **Backend API** | `GET /api/history/properties` - danh sách (tối đa 10) |
| **Frontend UI** | Lịch sử xem (trong profile hoặc sidebar) |
| **Testing** | Test ghi lịch sử, tối đa 10 item |

---

## FAV-05: Xóa lịch sử / yêu thích

- **Tên:** Xóa lịch sử và yêu thích
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xóa lịch sử xem hoặc yêu thích**, So that **làm sạch danh sách**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Xóa 1 item khỏi lịch sử
- [ ] Xóa tất cả lịch sử
- [ ] Xóa 1 item khỏi yêu thích
- [ ] Confirm dialog khi xóa tất cả

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Backend API** | `DELETE /api/history/properties/:id` |
| **Backend API** | `DELETE /api/history/properties` (xóa tất cả) |
| **Backend API** | `DELETE /api/favorites/properties/:id` |
| **Frontend UI** | Delete action, confirm dialog |
| **Testing** | Test xóa đơn, xóa tất cả |

---

# Epic 13: Điều hướng & Giao diện

**Mã Epic:** NAV
**Business Objective:** Cung cấp trải nghiệm điều hướng mượt mà, nhất quán trên tất cả màn hình.
**Mô tả:** Cấu trúc điều hướng, chuyển đổi màn hình, responsive layout và xử lý trạng thái.
**Dependency:** Tất cả epics

---

## NAV-01: Bottom tab bar

- **Tên:** Thanh điều hướng dưới cùng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **có thanh tab bar dưới cùng với 6 tab chính**, So that **dễ dàng chuyển đổi giữa các chức năng chính**

**Priority:** High

**Acceptance Criteria:**
- [ ] 6 tabs: Trang chủ, Tìm kiếm, Bản đồ, Thông báo, Yêu thích, Cá nhân
- [ ] Icon + label cho mỗi tab
- [ ] Tab active được highlight
- [ ] Badge thông báo chưa đọc trên tab Thông báo
- [ ] Animation khi chuyển tab

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Bottom tab bar component (index.html shell) |
| **Frontend UI** | Tab icon + label + active state |
| **Frontend UI** | Badge component |
| **Frontend UI** | Tab switching logic (iframe hoặc SPA routing) |
| **Testing** | Test chuyển tab, badge hiển thị |

---

## NAV-02: Sidebar điều hướng

- **Tên:** Sidebar menu
- **Role:** Admin, Manager, HouseHolder, Sale (người dùng đã đăng nhập)
- **Mô tả:** As a **người dùng đã đăng nhập**, I want **có sidebar menu chứa các chức năng quản lý**, So that **truy cập nhanh các tính năng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Sidebar: avatar + tên người dùng
- [ ] Menu items: Dashboard, BĐS của tôi, Người dùng, Danh mục, Cài đặt
- [ ] Hiển thị menu theo quyền (VD: Admin thấy "Người dùng", Sale không thấy)
- [ ] Toggle sidebar (mở/đóng)
- [ ] Highlight menu active
- [ ] Nút logout

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Sidebar component (index.html shell) |
| **Frontend UI** | Dynamic menu theo role |
| **Frontend UI** | Toggle animation |
| **Testing** | Test sidebar hiển thị đúng vai trò |

---

## NAV-03: Chuyển đổi màn hình

- **Tên:** Cơ chế chuyển đổi màn hình
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **chuyển đổi mượt mà giữa các màn hình**, So that **trải nghiệm liền mạch**

**Priority:** High

**Acceptance Criteria:**
- [ ] Chuyển đổi giữa các tab chính
- [ ] Mở màn hình con từ danh sách (chi tiết BĐS, chi tiết phòng)
- [ ] Dialog/modal cho form nhỏ
- [ ] Animation: slide, fade, pop
- [ ] Back button hoạt động

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Routing mechanism (React Router / Vue Router hoặc iframe-based) |
| **Frontend UI** | Page transition animations |
| **Frontend UI** | Modal/dialog components |
| **Testing** | Test chuyển trang, back button |

---

## NAV-04: Breadcrumb

- **Tên:** Breadcrumb điều hướng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **thấy breadcrumb hiển thị vị trí hiện tại**, So that **biết đang ở đâu trong hệ thống**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Hiển thị breadcrumb trên đầu trang
- [ ] Các cấp: Trang chủ > BĐS > Chi tiết BĐS
- [ ] Click vào cấp trước → quay lại

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Breadcrumb component |
| **Testing** | Test breadcrumb chính xác với route |

---

## NAV-05: Responsive layout

- **Tên:** Giao diện thích ứng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **giao diện hiển thị tốt trên cả desktop và mobile**, So that **sử dụng được trên mọi thiết bị**

**Priority:** High

**Acceptance Criteria:**
- [ ] Mobile: bottom tab bar + sidebar là drawer
- [ ] Desktop: sidebar cố định + top bar
- [ ] Grid/card layout responsive
- [ ] Touch-friendly buttons và controls
- [ ] Font size và spacing responsive

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Responsive CSS (mobile-first) |
| **Frontend UI** | Breakpoint handling |
| **Frontend UI** | Touch event handling cho mobile |
| **Testing** | Test trên nhiều kích thước màn hình |

---

## NAV-06: Loading & Empty state

- **Tên:** Loading và trạng thái rỗng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **thấy loading indicator khi dữ liệu đang tải và thông báo khi không có dữ liệu**, So that **biết hệ thống đang hoạt động**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Skeleton loading cho danh sách
- [ ] Spinner cho button/nút action
- [ ] Empty state: icon + thông báo + CTA
- [ ] Pull-to-refresh cho danh sách (mobile)

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Skeleton component |
| **Frontend UI** | Spinner component |
| **Frontend UI** | Empty state component |
| **Frontend UI** | Pull-to-refresh (mobile) |
| **Testing** | Test loading, empty state xuất hiện đúng lúc |

---

## NAV-07: Error & Network state

- **Tên:** Xử lý lỗi và mạng
- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **thấy thông báo lỗi thân thiện khi có sự cố mạng hoặc lỗi hệ thống**, So that **biết cách xử lý**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Error state: icon + thông báo lỗi + nút thử lại
- [ ] Toast notification cho lỗi ngắn
- [ ] Offline indicator (khi mất mạng)
- [ ] Auto-retry khi mạng khôi phục
- [ ] Modal cho lỗi nghiêm trọng

**Technical Tasks:**

| Nhóm | Task |
|------|------|
| **Frontend UI** | Error boundary component |
| **Frontend UI** | Toast notification system |
| **Frontend UI** | Network status listener (online/offline) |
| **Frontend UI** | Retry button |
| **Testing** | Test mất mạng, lỗi API, retry |

---

# Ma trận phụ thuộc Epic

| Epic | Phụ thuộc vào | Được phụ thuộc bởi |
|------|---------------|-------------------|
| AUTH (Xác thực) | - | DASH, BDS, PHONG, USER, CAT, PROFILE, NOTIF |
| DASH (Dashboard) | AUTH, BDS, PHONG | - |
| SEARCH (Tìm kiếm) | BDS, PHONG | - |
| MAP (Bản đồ) | BDS | - |
| BDS (Quản lý BĐS) | AUTH, USER, CAT | DASH, SEARCH, MAP, PHONG, SHARE, FAV |
| PHONG (Quản lý Phòng) | AUTH, BDS | DASH, SEARCH, SHARE, FAV |
| USER (Người dùng) | AUTH, CAT | BDS |
| CAT (Danh mục) | AUTH | BDS, USER |
| PROFILE (Hồ sơ) | AUTH | - |
| NOTIF (Thông báo) | AUTH | - |
| SHARE (Chia sẻ) | BDS, PHONG | - |
| FAV (Yêu thích) | BDS, PHONG | - |
| NAV (Điều hướng) | Tất cả | - |

---

# Thứ tự ưu tiên triển khai

| Phase | Epic | Lý do |
|-------|------|-------|
| **Phase 1** (Foundation) | AUTH, CAT, USER | Nền tảng: xác thực, danh mục, người dùng |
| **Phase 2** (Core) | BDS, PHONG, NAV | Nghiệp vụ chính: quản lý BĐS và phòng |
| **Phase 3** (Experience) | SEARCH, MAP, DASH | Trải nghiệm: tìm kiếm, bản đồ, dashboard |
| **Phase 4** (Engagement) | NOTIF, SHARE, FAV, PROFILE | Tương tác: thông báo, chia sẻ, yêu thích |

---

*Tài liệu này được tạo từ phân tích 21 file HTML prototype và các business rules từ Spec.md.*
*Tổng số: 13 Epics, 76 User Stories.*
