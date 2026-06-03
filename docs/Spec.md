# Chuyển đổi số

## 1. Tài khoản & Đăng nhập
- Tôi muốn có màn hình đăng nhập, ai có tài khoản thì vào được, ai chưa có thì đăng ký
- Quên mật khẩu thì lấy lại được qua OTP gửi email, SMS hoặc Zalo
- Đã vào hệ thống rồi thì có thể đổi mật khẩu nếu muốn
- Tài khoản nào vi phạm thì admin có thể khóa lại, khóa rồi không vào được nữa
- Có 5 hạng tài khoản: Super Admin (cao nhất), Admin, Quản lý khu vực, Chủ nhà, Sale
- Đăng ký tài khoản qua form: số điện thoại, tên tài khoản, mật khẩu, họ tên, vai trò mong muốn
- Xác thực số điện thoại bằng Zalo OTP trước khi gửi yêu cầu
- Tài khoản đăng ký tự động ở trạng thái "Chờ duyệt", admin phải duyệt mới kích hoạt

## 2. Bảng tổng quan (Dashboard)
- Vào trang chủ là thấy ngay tổng quan: bao nhiêu BĐS, bao nhiêu phòng, bao nhiêu cái đã duyệt, còn bao nhiêu cái chờ
- Xem được biểu đồ tròn, biểu đồ cột, biết được phòng trống bao nhiêu, đã cho thuê bao nhiêu
- Admin cấp cao xem thêm doanh thu, biết tháng này kiếm được bao nhiêu, BĐS nào đang chạy tốt

## 3. Tìm kiếm BĐS & Phòng
- Có ô tìm kiếm, gõ tên BĐS hoặc địa chỉ là ra ngay
- Lọc được theo: loại BĐS, loại phòng, khoảng giá, diện tích, khu vực (tỉnh/quận/phường), nội thất, tiện ích, phòng còn trống hay sắp trống
- Lưu lại bộ lọc ưa thích để lần sau dùng lại
- Gợi ý BĐS nổi bật, BĐS mới đăng, BĐS xem nhiều

## 4. Bản đồ tương tác
- Xem BĐS trên bản đồ Google Maps, thấy marker từng căn, click vào là hiện thông tin
- Kéo thanh trượt để chọn bán kính tìm kiếm, tự động vẽ vòng tròn trên bản đồ
- Kéo bottom sheet từ dưới lên để xem danh sách BĐS trong khu vực đang nhìn

## 5. Quản lý Bất động sản
- Thêm BĐS mới: nhập tên, địa chỉ, giá, diện tích, số phòng, nội thất, tiện ích, upload ảnh (tối đa 10 tấm), chọn tọa độ trên bản đồ
- Sửa, xóa BĐS (ai tạo thì được sửa, admin sửa được hết)
- BĐS mới tạo cần admin duyệt mới hiện lên
- Admin bấm duyệt hoặc từ chối (kèm lý do), duyệt được nhiều cái cùng lúc
- BĐS có ngày hết hạn, gần hết hạn thì cảnh báo, hết hạn thì tự động ẩn
- Đánh dấu BĐS nổi bật để ưu tiên hiển thị
- Xem danh sách BĐS của mình, lọc theo trạng thái: nháp, chờ duyệt, đã duyệt, hết hạn

## 6. Quản lý Phòng
- Mỗi BĐS có nhiều phòng, thêm phòng kèm: tên, diện tích, giá thuê, giá cọc, loại phòng, nội thất, tiện ích, dịch vụ đi kèm (điện, nước, wifi...), ảnh chụp
- Phòng có 8 trạng thái: đang trống (xanh), đã cọc (vàng), đã thuê (đỏ), sắp trống (cam), chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống
- Admin, SuperAdmin, Manager, HouseHolder đổi trạng thái trực tiếp (bất kỳ → bất kỳ)
- Sale đổi trạng thái → chuyển sang trạng thái chờ duyệt tương ứng, cần được duyệt bởi HouseHolder (chủ phòng), Manager (quản lý phòng), Admin hoặc SuperAdmin
- Khi cho thuê thì nhập tên khách, số điện thoại, chụp ảnh khách
- Xem được hợp đồng thuê, có file PDF đính kèm

## 7. Người dùng & Phân quyền
- Admin xem được danh sách người dùng, thêm người mới, sửa thông tin, khóa/mở khóa
- Phân quyền theo vai trò: duyệt BĐS, duyệt phòng, ghi BĐS, ghi phòng, quản lý user, quản lý danh mục...
- Gán khu vực cho quản lý: chọn tỉnh nào, quận nào, phường nào người đó được quản
- Mỗi người dùng có 1 vai trò, 1 role có nhiều quyền

## 8. Danh mục hệ thống
- Quản lý địa giới hành chính: thêm tỉnh, quận, phường theo cây 3 cấp
- Quản lý loại BĐS, loại phòng: thêm tên loại, mô tả
- Quản lý nội thất (có icon), tiện ích (có icon + khoảng cách), dịch vụ (có giá + đơn vị tính)

## 9. Hồ sơ cá nhân
- Xem và sửa thông tin cá nhân: họ tên, email, số điện thoại
- Đổi ảnh đại diện, đổi mật khẩu
- Xem quyền hạn của mình, khu vực mình được quản lý

## 10. Thông báo
- Có danh sách thông báo, ai gửi, gửi lúc nào, đọc hay chưa đọc
- Admin tạo thông báo hệ thống gửi cho tất cả hoặc theo vai trò
- Khi admin duyệt BĐS hoặc duyệt đổi trạng thái phòng, hệ thống tự động gửi thông báo cho người yêu cầu
- Có badge đỏ trên tab thông báo để biết có bao nhiêu cái chưa đọc

## 11. Chia sẻ
- Chia sẻ BĐS/phòng qua Zalo, Facebook
- Sao chép đường link để gửi qua app khác
- Gửi hình ảnh BĐS/phòng qua các ứng dụng chat

## 12. Yêu thích & Lịch sử
- Bấm trái tim để lưu BĐS hoặc phòng yêu thích
- Xem lại danh sách đã thích
- Tự động lưu lịch sử các BĐS đã xem (tối đa 10 cái gần nhất)
- Xóa yêu thích, xóa lịch sử khi không cần nữa

## 13. Giao diện & Điều hướng
- Có thanh tab bar dưới cùng: Trang chủ, Tìm kiếm, Bản đồ, Thông báo, Yêu thích, Cá nhân
- Có sidebar menu: Dashboard, BĐS của tôi, Người dùng, Danh mục, Cài đặt
- Chạy được trên cả desktop và điện thoại, giao diện tự co giãn
- Có loading khi chờ, có thông báo khi lỗi mạng hoặc khi không có dữ liệu

# Roles
- Sale 
- House holder (Chủ nhà)
- Manager (Quản lý khu vực)
- Admin 
- Super Admin (Root)

# Entities
- Người dùng
- Vai trò
- Phân quyền
- UserArea
- Khách hàng
- Bất động sản
- Phòng
- Hợp đồng
- Loại bất động sản
- Loại phòng
- Nội thất
- Tiện ích
- Dịch vụ
- File
	- Loại: Hình ảnh, Văn bản, Tài liệu
- Địa giới hành chính
- Bất động sản yêu thích
- Phòng yêu thích
- Lịch sử xem bất động sản
- Thông báo
	- Loại: Đã được duyệt bởi admin, cập nhật hệ thống, tin tức, giảm giá phòng, xác thực thành công

# Quan hệ thực thể

## 1. Quan hệ chính (1-N / N-1 / 1-1)

```
 1. Người dùng       n (thuộc vai trò)         -> 1  Vai trò         : Chặn xóa role nếu còn user
 2. Người dùng       1 (quản lý khu vực)        -> n  UserArea        : Xóa user → UserArea mất theo
 3. Người dùng       1 (có avatar)              -> 1  File            : Xóa file → user set avatar null
 4. Vai trò          1 (có quyền)               -> n  Phân quyền      : Xóa role → phân quyền mất theo
 5. UserArea         n (thuộc địa giới)         -> 1  Địa giới HC     : Xóa địa giới → UserArea mất theo
 6. Bất động sản     n (thuộc chủ)              -> 1  Người dùng      : Chặn xóa user nếu còn BĐS
 7. Bất động sản     n (thuộc loại)             -> 1  Loại BĐS        : Chặn xóa loại nếu còn BĐS
 8. Bất động sản     1 (có phòng)               -> n  Phòng           : Xóa BĐS → phòng mất theo
 9. Bất động sản     1 (có lượt yêu thích)      -> n  BĐS yêu thích   : Xóa BĐS → yêu thích mất theo
10. Bất động sản     1 (có lượt xem)            -> n  Lịch sử xem     : Xóa BĐS → lịch sử mất theo
11. Phòng            n (thuộc loại)             -> 1  Loại phòng      : Chặn xóa loại nếu còn phòng
12. Phòng            n (có khách thuê)          -> 1  Khách hàng      : Xóa khách → phòng set khách null
13. Phòng            1 (có hợp đồng)            -> n  Hợp đồng        : Chặn xóa phòng nếu còn HĐ
14. Phòng            1 (có lượt yêu thích)      -> n  Phòng yêu thích : Xóa phòng → yêu thích mất theo
15. Hợp đồng         1 (có file đính kèm)       -> 1  File            : Xóa file → HĐ set file null
16. Khách hàng       1 (có ảnh đại diện)        -> 1  File            : Xóa ảnh → KH set ảnh null
17. File             n (thuộc người upload)      -> 1  Người dùng      : Xóa user → file set null
18. Nội thất         n (thuộc người tạo)        -> 1  Người dùng      : Xóa user → nội thất set null
19. Tiện ích         n (thuộc người tạo)        -> 1  Người dùng      : Xóa user → tiện ích set null
20. Dịch vụ          n (thuộc người tạo)        -> 1  Người dùng      : Xóa user → dịch vụ set null
21. Thông báo (gửi)  n (thuộc người gửi)        -> 1  Người dùng      : Xóa user → TB set người gửi null
22. Thông báo (nhận) n (thuộc người nhận)       -> 1  Người dùng      : Xóa user → TB mất theo
23. BĐS yêu thích    n (thuộc người thích)      -> 1  Người dùng      : Xóa user → yêu thích mất theo
24. Phòng yêu thích  n (thuộc người thích)      -> 1  Người dùng      : Xóa user → yêu thích mất theo
25. Lịch sử xem BĐS  n (thuộc người xem)        -> 1  Người dùng      : Xóa user → lịch sử mất theo
```

> Riêng tự tham chiếu: `Địa giới HC 1 -> n Địa giới HC` – Cây 3 cấp Tỉnh → Quận → Phường (parent_id). Chặn xóa nếu còn con.

## 2. Quan hệ N-N (bảng trung gian)

```
1. Bất động sản 1 ->n bds_noi_that n->1 Nội thất  : BĐS gắn nhiều nội thất. Không thuộc tính bổ sung
2. Bất động sản 1 ->n bds_tien_ich n->1 Tiện ích  : BĐS gắn nhiều tiện ích. Khoảng cách (m)
3. Phòng        1 ->n phong_noi_that n->1 Nội thất : Phòng gắn nhiều nội thất. Không thuộc tính bổ sung
4. Phòng        1 ->n phong_tien_ich n->1 Tiện ích : Phòng gắn nhiều tiện ích. Khoảng cách (m)
5. Phòng        1 ->n phong_dich_vu n->1 Dịch vụ   : Phòng đăng ký dịch vụ. Giá, đơn vị, chu kỳ, loại, chỉ số đầu
```

## 3. Quan hệ đa hình (Polymorphic)

| #  | Bảng       | Cột                      | Mô tả                                                              |
|----|------------|--------------------------|--------------------------------------------------------------------|
| 1  | File       | entityType, entityId     | File thuộc BĐS / Phòng / User / Khách hàng. entityType xác định loại, entityId là ID bản ghi |
| 2  | Thông báo  | entityType, entityId     | Thông báo liên kết đến BĐS hoặc Phòng                              |

## 4. Quan hệ tự tham chiếu

| Bảng                  | Cột       | Mô tả                                                    |
|-----------------------|-----------|----------------------------------------------------------|
| Địa giới hành chính   | parent_id | Cây 3 cấp: Tỉnh (null) → Quận/Huyện → Phường/Xã. Chặn xóa nếu còn con |

# Đặc tả thực thể

## Người dùng
- id, tên đăng nhập, mật khẩu
- họ tên, email, số điện thoại
- mã tài khoản (maTaiKhoan)
- avatar (File)
- vai trò (Vai trò)
- khu vực quản lý (danh sách UserArea)
- trạng thái: [Chờ duyệt, Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Vai trò
- id, tên vai trò, mô tả
- quyền hạn (danh sách Phân quyền)
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Phân quyền
- id, vai trò (Vai trò), mã quyền
- mã quyền: xem_dashboard, xem_bds, them_bds, sua_bds, xoa_bds, duyet_bds, xem_phong, them_phong, sua_phong, xoa_phong, duyet_phong, xem_user, them_user, sua_user, xoa_user, xem_phanquyen, sua_phanquyen, xem_diadiem, them_diadiem, sua_diadiem, xoa_diadiem
- ngày tạo

## UserArea
- id, người dùng (Người dùng), địa giới hành chính (Địa giới hành chính)
- cấp: [Quận/Huyện, Phường/Xã]

## Khách hàng
- id, họ tên, số điện thoại, email
- hình ảnh (File), ghi chú
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Bất động sản
- id, tên BĐS, mô tả, địa chỉ
- tọa độ (latitude, longitude)
- loại BĐS (Loại bất động sản)
- chủ BĐS (Người dùng)
- diện tích (m²), giá thuê (VNĐ/tháng), số phòng ngủ, số toilet, số tầng
- nội thất (danh sách Nội thất), tiện ích (danh sách Tiện ích)
- hướng nhà, năm xây dựng, mặt tiền (m), đường vào (m), giấy tờ pháp lý
- nổi bật (featured - boolean)
- trạng thái: [nháp, chờ duyệt, đã duyệt, bị từ chối, hết hạn]
- hình ảnh (danh sách File)
- ngày tạo, ngày cập nhật, ngày hết hạn

## Phòng
- id, tên phòng, mô tả
- BĐS (Bất động sản)
- loại phòng (Loại phòng)
- diện tích (m²), số phòng vệ sinh, giá thuê (VNĐ/tháng), giá cọc
- nội thất (danh sách Nội thất), tiện ích (danh sách Tiện ích), dịch vụ (danh sách Dịch vụ)
- khách hàng hiện tại (Khách hàng)
- trạng thái: [đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống]
- hình ảnh (danh sách File)
- ngày tạo, ngày cập nhật

## Hợp đồng
- id, phòng (Phòng), khách hàng (Khách hàng)
- ngày bắt đầu, ngày kết thúc
- giá thuê, tiền cọc, chu kỳ thanh toán
- file hợp đồng (File)
- trạng thái: [hiệu lực, đã hết hạn, đã hủy]
- ngày tạo, ngày cập nhật

## Loại bất động sản
- id, tên loại, mô tả
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Loại phòng
- id, tên loại, mô tả
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Nội thất
- id, tên nội thất, mô tả, icon
- người tạo (Người dùng)
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Tiện ích
- id, tên tiện ích, mô tả, icon, khoảng cách (m)
- người tạo (Người dùng)
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Dịch vụ
- id, tên dịch vụ, mô tả
- giá (VNĐ), đơn vị: [tháng, năm, m²], chu kỳ thanh toán
- loại: [bắt buộc, tự chọn]
- chỉ số đầu (cho điện/nước)
- người tạo (Người dùng)
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## File
- id, tên file, đường dẫn, kích thước, định dạng
- loại: [Hình ảnh, Văn bản, Tài liệu]
- entityType: [BDS, Phòng, Người dùng, Khách hàng]
- entityId, người tạo (Người dùng)
- ngày tạo

## Địa giới hành chính
- id, tên, slug, mã
- cấp: [Tỉnh/Thành phố, Quận/Huyện, Phường/Xã]
- cha (parentId), đường dẫn (path)
- trạng thái: [Đang hoạt động, Đã khóa]
- ngày tạo, ngày cập nhật

## Bất động sản yêu thích
- id, người dùng (Người dùng), BĐS (Bất động sản)
- ngày tạo

## Phòng yêu thích
- id, người dùng (Người dùng), phòng (Phòng)
- ngày tạo

## Lịch sử xem bất động sản
- id, người dùng (Người dùng), BĐS (Bất động sản)
- thời gian xem

## Thông báo
- id, tiêu đề, nội dung
- loại: [Đã được duyệt bởi admin, cập nhật hệ thống, tin tức, giảm giá phòng, xác thực thành công]
- trạng thái: [chưa đọc, đã đọc]
- người gửi (Người dùng), người nhận (Người dùng)
- entityType: [BDS, Phòng], entityId
- ngày tạo

# Business Rules:

- Bất động sản
    - Tạo
        - HouseHolder, Manager, Admin, Super Admin có quyền tạo
        - HouseHolder hoặc Manager tạo cần Admin|Super Admin duyệt → trạng thái "chờ duyệt"
        - Admin|Super Admin tạo → trạng thái "đã duyệt" (không cần duyệt lại)
    - Sửa
        - HouseHolder, Manager chỉ sửa được BĐS tạo bởi chính họ
        - Admin, Super Admin sửa được mọi BĐS
        - Nếu sửa bởi HouseHolder|Manager và BĐS đang ở trạng thái "đã duyệt" → chuyển về "chờ duyệt"
        - Nếu sửa bởi Admin|Super Admin → giữ nguyên trạng thái hiện tại
    - Xóa
        - Chỉ Admin, Super Admin có quyền xóa
        - Xóa mềm (soft delete) — cập nhật trạng thái thay vì xóa vật lý
        - Không xóa BĐS nếu còn hợp đồng đang ở trạng thái "hiệu lực"
        - Xóa BĐS → xóa theo phòng, hình ảnh, yêu thích, lịch sử xem
        - Gửi thông báo cho chủ BĐS khi bị xóa
        - Hiển thị confirm dialog trước khi xóa
    - Xem
        - Mọi người đều xem được (kể cả không đăng nhập)
        - Chỉ hiển thị BĐS có trạng thái "đã duyệt" cho người dùng công khai
    - Duyệt
        - Chỉ Admin, Super Admin có quyền duyệt hoặc từ chối
        - Duyệt (approve) → chuyển trạng thái thành "đã duyệt"
        - Từ chối (reject) → nhập lý do từ chối → chuyển trạng thái thành "bị từ chối"
        - Có thể duyệt hoặc từ chối nhiều BĐS cùng lúc (bulk)
        - Tự động gửi thông báo cho người tạo khi duyệt hoặc từ chối
    - Hết hạn
        - BĐS có ngày hết hạn, tự động chuyển trạng thái "hết hạn" khi đến ngày
        - Gần hết hạn (trong 7 ngày) → cảnh báo cho Admin|Super Admin
        - BĐS "hết hạn" tự động ẩn khỏi kết quả tìm kiếm công khai
        - Admin|Super Admin có thể gia hạn → cập nhật ngày hết hạn mới
    - Nổi bật (Featured)
        - Chỉ Admin, Super Admin được đánh dấu BĐS nổi bật
        - BĐS nổi bật ưu tiên hiển thị và xuất hiện trong gợi ý
        - Hiển thị icon/badge trên card BĐS
    - Giới hạn kỹ thuật
        - Tối đa 10 hình ảnh, định dạng: jpg, png, webp
        - Tên BĐS tối đa 255 ký tự, không để trống
        - Diện tích > 0 m², giá thuê > 0 VNĐ/tháng
        - Tọa độ: latitude (-90 đến 90), longitude (-180 đến 180)
        - Có thể lưu nháp (draft) nếu chưa hoàn thành

- Phòng
    - Tạo
        - HouseHolder, Manager, Admin, Super Admin có quyền tạo
        - Có thể thêm nhiều phòng cùng lúc trong một BĐS
    - Sửa
        - HouseHolder, Manager chỉ sửa được phòng tạo bởi chính họ
        - Admin, Super Admin sửa được mọi phòng
        - Khi sửa giá thuê → ghi lại lịch sử giá
    - Sửa — Đổi trạng thái phòng
        - 8 trạng thái: [đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống]
        - Admin|SuperAdmin|Manager|HouseHolder: đổi trực tiếp từ trạng thái hiện tại sang bất kỳ trạng thái nào
        - Sale: đổi từ X → Y bất kỳ (X ≠ Y) → chuyển phòng sang trạng thái "chờ duyệt Y" tương ứng
            - VD: đang trống → đã cọc => chờ duyệt cọc
            - VD: đã thuê → sắp trống => chờ duyệt sắp trống
            - VD: đã cọc → đang trống => chờ duyệt đang trống
        - Khi duyệt (bởi HouseHolder|Manager|Admin|SuperAdmin) → chuyển từ "chờ duyệt Y" sang "Y"
        - Khi từ chối → chuyển về trạng thái cũ
        - Khi đổi sang "đã cọc" hoặc "đã thuê" → bắt buộc nhập thông tin khách:
            - Tên khách hàng (không để trống)
            - Số điện thoại khách hàng (10-11 số, bắt đầu bằng 0)
            - Hình ảnh khách hàng (upload hoặc chụp trực tiếp)
        - Khi đổi sang "đang trống" → xóa thông tin khách hiện tại
        - Ghi lại lịch sử thay đổi trạng thái (trạng thái cũ, trạng thái mới, người thay đổi, thời gian)
    - Xóa
        - Chỉ Admin, Super Admin có quyền xóa
        - Xóa mềm (soft delete)
        - Không xóa phòng nếu còn hợp đồng ở trạng thái "hiệu lực"
    - Xem
        - Mọi người đều xem được (kể cả không đăng nhập)
    - Duyệt đổi trạng thái (Sale)
        - HouseHolder (chủ phòng), Manager (quản lý phòng), Admin, SuperAdmin có quyền duyệt
        - Duyệt → chuyển từ "chờ duyệt Y" sang "Y", cập nhật thông tin khách nếu có
        - Từ chối → nhập lý do từ chối, chuyển về trạng thái cũ
        - Tự động gửi thông báo cho Sale khi duyệt hoặc từ chối
    - Giới hạn kỹ thuật
        - Tối đa 10 hình ảnh/phòng
        - Giá thuê > 0 VNĐ/tháng, diện tích > 0 m²
        - Giá cọc ≥ 0 VNĐ

- Hợp đồng
    - Tạo, Sửa, Xóa
        - Chỉ Admin, Super Admin có quyền
    - Tạo
        - Chọn phòng, khách hàng, ngày bắt đầu, ngày kết thúc
        - Ngày kết thúc phải lớn hơn ngày bắt đầu
        - Upload file hợp đồng (định dạng PDF)
    - Sửa
        - Có thể gia hạn hợp đồng (thay đổi ngày kết thúc hoặc tạo mới)
    - Hủy
        - Hủy hợp đồng → chuyển trạng thái "đã hủy"
    - Xóa
        - Xóa file đính kèm → hợp đồng set file null
    - Xem
        - Admin, Super Admin xem được tất cả
        - HouseHolder xem được hợp đồng của phòng thuộc BĐS mình
    - Trạng thái: [hiệu lực, đã hết hạn, đã hủy]
    - Tự động chuyển "đã hết hạn" khi quá ngày kết thúc

- Người dùng
    - Tạo, Sửa, Xóa
        - Admin, Super Admin có quyền
    - Tạo
        - Chọn vai trò (dropdown)
        - Nếu vai trò là Manager → bắt buộc chọn ít nhất 1 khu vực quản lý
        - Có thể upload avatar
        - Tạo thành công → tự động gửi thông báo cho người dùng mới
    - Sửa
        - Admin|Super Admin sửa được thông tin: họ tên, email, SĐT, vai trò, khu vực
        - Không cho sửa tên đăng nhập
        - Không thể thay đổi vai trò của Super Admin
        - Admin không thể sửa thông tin của Super Admin
    - Xóa
        - Chặn xóa user nếu còn BĐS đang hoạt động
        - Chặn xóa Super Admin
        - Xóa user → UserArea, yêu thích, lịch sử xem mất theo
        - Xóa user → các entity do user tạo (Nội thất, Tiện ích, Dịch vụ, File) set null
        - Xóa user → Thông báo do user gửi set null, TB nhận mất theo
    - Xem
        - Admin, Super Admin, Manager có quyền xem
        - Manager chỉ xem được user trong khu vực quản lý
        - Có phân trang, tìm kiếm, filter theo vai trò và trạng thái
    - Khóa/Mở khóa
        - Admin, Super Admin có quyền khóa hoặc mở khóa
        - Không thể khóa Super Admin
        - Nếu bị khóa → không thể đăng nhập, token hiện tại bị vô hiệu
        - Ghi lại lịch sử khóa/mở khóa
    - Đăng ký (tự đăng ký)
        - Bất kỳ ai có SĐT hợp lệ đều có thể gửi yêu cầu
        - Bắt buộc xác thực SĐT qua Zalo OTP trước khi gửi yêu cầu
        - Yêu cầu đăng ký tự động ở trạng thái "Chờ duyệt"
        - Admin duyệt → chuyển "Đang hoạt động", gửi thông báo cho user
        - Admin từ chối → xóa yêu cầu hoặc chuyển "Bị từ chối", gửi thông báo kèm lý do
        - Tài khoản "Chờ duyệt" không thể đăng nhập
    - Giới hạn kỹ thuật
        - Tên đăng nhập không khoảng trắng, không ký tự đặc biệt, không trùng
        - Mật khẩu tối thiểu 6 ký tự, có chữ và số
        - Email đúng định dạng, SĐT 10-11 số bắt đầu bằng 0

- Vai trò (Role)
    - Tạo, Sửa
        - Chỉ Super Admin có quyền
        - Mỗi role có nhiều quyền (phân quyền)
    - Xóa
        - Chỉ Super Admin có quyền
        - Không xóa được role mặc định (Super Admin, Admin, Manager, HouseHolder, Sale)
        - Chặn xóa role nếu còn user đang gán role đó
        - Xóa role → phân quyền của role mất theo
    - Trạng thái: [Đang hoạt động, Đã khóa]

- Phân quyền
    - Chỉ Super Admin có quyền xem và sửa
    - 20 mã quyền: xem_dashboard, xem_bds, them_bds, sua_bds, xoa_bds, duyet_bds, xem_phong, them_phong, sua_phong, xoa_phong, duyet_phong, xem_user, them_user, sua_user, xoa_user, xem_phanquyen, sua_phanquyen, xem_diadiem, them_diadiem, sua_diadiem, xoa_diadiem
    - Giao diện checkbox grid, có select all/deselect all
    - Thay đổi có hiệu lực ngay sau khi lưu

- Loại phòng, Loại bất động sản
    - Tạo, Sửa, Xóa
        - Chỉ Super Admin có quyền
    - Xóa
        - Chặn xóa nếu còn BĐS (loại BĐS) hoặc còn phòng (loại phòng) đang sử dụng
    - Trạng thái: [Đang hoạt động, Đã khóa]

- Nội thất, Tiện ích, Dịch vụ
    - Tạo
        - Super Admin, Admin, Manager, HouseHolder có quyền tạo
    - Sửa, Xóa
        - Super Admin tạo mặc định, không thể bị xóa bởi thành viên khác
        - Manager, HouseHolder chỉ sửa, xóa được những cái do chính họ tạo
        - Admin sửa, xóa được của chính họ và của Manager, HouseHolder
        - Super Admin sửa, xóa được tất cả
    - Xem
        - Mọi người xem được (công khai)
    - Dịch vụ có thêm: loại [bắt buộc, tự chọn], giá > 0 nếu bắt buộc, đơn vị [tháng, năm, m²], chỉ số đầu (cho điện/nước)
    - Trạng thái: [Đang hoạt động, Đã khóa]

- File
    - Tạo, Sửa, Xóa
        - Manager, HouseHolder, Admin, Super Admin có quyền
    - Xem
        - Công khai (mọi người đều xem được)
    - Upload
        - Định dạng ảnh: jpg, png, webp
        - Định dạng tài liệu: PDF
        - (Đề xuất) Kích thước tối đa 10MB/file
    - entityType: [BDS, Phòng, Người dùng, Khách hàng]
    - Xóa user → file set null

- Địa giới hành chính
    - Tạo, Sửa, Xóa
        - Chỉ Super Admin có quyền
    - Xem
        - Công khai (mọi người xem được)
    - Cây 3 cấp: Tỉnh (parent_id = null) → Quận/Huyện → Phường/Xã
    - Chặn xóa nếu còn node con
    - Chặn xóa nếu đang được sử dụng bởi UserArea hoặc BĐS
    - Trạng thái: [Đang hoạt động, Đã khóa]

- Khách hàng (người thuê)
    - Tạo
        - Được tạo tự động khi đặt cọc phòng (nhập tên, SĐT, hình ảnh)
        - Admin, Super Admin, Manager, HouseHolder có thể tạo trực tiếp
    - Sửa
        - Admin, Super Admin có quyền sửa thông tin
    - Xóa
        - Xóa khách hàng → phòng đang thuê set khách null
    - Trạng thái: [Đang hoạt động, Đã khóa]

- Bất động sản yêu thích, Phòng yêu thích
    - Tạo, Xóa
        - Mọi user đã đăng nhập có thể tạo và xóa
    - Xóa BĐS hoặc Phòng → yêu thích tương ứng mất theo
    - Xóa user → yêu thích của user đó mất theo

- Lịch sử xem bất động sản
    - Tạo
        - Mọi user đã đăng nhập có thể tạo (tự động khi xem chi tiết BĐS)
    - Lưu tối đa 10 BĐS được xem gần nhất (xóa cũ nhất khi đạt giới hạn)
    - Xóa BĐS → lịch sử liên quan mất theo
    - Xóa user → lịch sử của user đó mất theo

- Thông báo
    - Tạo
        - Admin, Super Admin có quyền tạo thông báo hệ thống
        - Có thể gửi đến: tất cả user, theo vai trò, hoặc theo user cụ thể
        - Có thể gửi ngay hoặc hẹn giờ
    - Tự động
        - Khi duyệt BĐS → hệ thống tự động gửi thông báo cho người tạo
        - Khi từ chối BĐS → gửi thông báo kèm lý do từ chối
        - Khi duyệt đổi trạng thái phòng → gửi thông báo cho Sale yêu cầu
        - Khi BĐS sắp hết hạn (7 ngày) → gửi thông báo nhắc nhở
        - Khi BĐS hết hạn → gửi thông báo
    - Nhận
        - Sale nhận thông báo khi admin duyệt thay đổi trạng thái phòng
        - Mọi user nhận thông báo hệ thống từ Admin, Super Admin
    - Xóa
        - Người nhận có thể xóa thông báo của mình
        - Admin có thể xóa thông báo
        - Xóa người nhận → thông báo mất theo
        - Xóa người gửi → thông báo set người gửi null
    - Trạng thái: [chưa đọc, đã đọc]
    - Loại: [Đã được duyệt bởi admin, cập nhật hệ thống, tin tức, giảm giá phòng, xác thực thành công]
    - Có badge đỏ hiển thị số thông báo chưa đọc

- UserArea (Khu vực quản lý)
    - Chỉ Admin, Super Admin có quyền gán khu vực cho Manager
    - Manager bắt buộc phải có ít nhất 1 khu vực
    - Có thể chọn nhiều khu vực (tỉnh/quận/phường)
    - Xóa user → UserArea mất theo
    - Xóa địa giới hành chính → UserArea mất theo

# State Machine & Chuyển trạng thái

## Phòng: [đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống]

- Admin|SuperAdmin|Manager|HouseHolder đổi trực tiếp (không cần duyệt):

    đang trống ←──→ đã cọc ←──→ đã thuê ←──→ sắp trống
         ↑                                      │
         └──────────────────────────────────────┘
    (Cho phép mọi chuyển đổi giữa 4 trạng thái cốt lõi)

- Sale đổi (cần duyệt):

    X ──[yêu cầu]──→ chờ duyệt Y ──[duyệt]──→ Y
                              │
                        [từ chối] → X
    (Với X là trạng thái hiện tại, Y là trạng thái đích)

    VD:
    đang trống ──[yêu cầu đặt cọc]──→ chờ duyệt cọc ──[duyệt]──→ đã cọc
    đã cọc ──[yêu cầu xác nhận thuê]──→ chờ duyệt thuê ──[duyệt]──→ đã thuê
    đã thuê ──[yêu cầu báo trước]──→ chờ duyệt sắp trống ──[duyệt]──→ sắp trống
    đã cọc ──[yêu cầu hủy cọc]──→ chờ duyệt đang trống ──[duyệt]──→ đang trống
    đã thuê ──[yêu cầu trả phòng]──→ chờ duyệt đang trống ──[duyệt]──→ đang trống
    sắp trống ──[yêu cầu trả phòng]──→ chờ duyệt đang trống ──[duyệt]──→ đang trống

    - Mỗi lần đổi trạng thái đều ghi lại lịch sử

## Bất động sản: [nháp, chờ duyệt, đã duyệt, bị từ chối, hết hạn]

    nháp ──[gửi duyệt]──→ chờ duyệt ──[duyệt]──→ đã duyệt

    chờ duyệt ──[từ chối]──→ bị từ chối ──[sửa lại & gửi duyệt]──→ chờ duyệt
    đã duyệt ──[hết hạn]──→ hết hạn ──[gia hạn]──→ đã duyệt
    đã duyệt ──[Admin sửa]──→ giữ nguyên trạng thái
    đã duyệt ──[HouseHolder|Manager sửa]──→ chờ duyệt

## Hợp đồng: [hiệu lực, đã hết hạn, đã hủy]

    hiệu lực ──[hết thời hạn]──→ đã hết hạn
    hiệu lực ──[hủy]──────────→ đã hủy
    đã hết hạn ──[gia hạn]──→ hiệu lực (hoặc tạo hợp đồng mới)

# Hard Constraints (ràng buộc cứng)

    - Không xóa vai trò nếu còn người dùng đang gán vai trò đó
    - Không xóa người dùng nếu còn BĐS do người đó tạo
    - Không xóa loại BĐS nếu còn BĐS đang sử dụng loại đó
    - Không xóa loại phòng nếu còn phòng đang sử dụng loại đó
    - Không xóa phòng nếu còn hợp đồng đang hiệu lực
    - Không xóa BĐS nếu còn hợp đồng đang hiệu lực
    - Không xóa địa giới hành chính nếu còn node con
    - Không xóa địa giới hành chính nếu còn UserArea hoặc BĐS tham chiếu
    - Không thể khóa tài khoản Super Admin
    - Không thể xóa role mặc định của hệ thống
    - Admin không thể sửa thông tin của Super Admin
    - Mật khẩu mới không được trùng với mật khẩu cũ
    - Sale đổi trạng thái phòng bắt buộc phải được duyệt bởi HouseHolder (chủ phòng), Manager (quản lý phòng), Admin hoặc SuperAdmin
    - Manager bắt buộc phải có ít nhất 1 khu vực quản lý
    - Không cho sửa tên đăng nhập sau khi tạo
    - Tài khoản "Chờ duyệt" không thể đăng nhập

# Security Rules

    - Mật khẩu lưu dưới dạng hash (bcrypt), không lưu plaintext
    - Xác thực qua JWT token, kiểm tra token hết hạn mỗi request
    - Chỉ user có trạng thái "Đang hoạt động" mới đăng nhập được
    - OTP có hiệu lực 5 phút, chỉ dùng 1 lần
    - OTP gồm 4 chữ số
    - Khi đặt lại mật khẩu thành công → vô hiệu hóa token OTP
    - (Đề xuất) Giới hạn số lần đăng nhập sai: 5 lần → khóa tạm thời 15 phút
    - (Đề xuất) Giới hạn số lần gửi lại OTP: tối đa 3 lần/giờ
    - Xác thực số điện thoại qua Zalo OTP khi đăng ký

# State (đồng bộ với State Machine ở trên)

Phòng: [đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống]
Bất động sản: [nháp, chờ duyệt, đã duyệt, bị từ chối, hết hạn]
Người dùng: [Chờ duyệt, Đang hoạt động, Đã khóa]
Địa giới hành chính: [Đang hoạt động, đã khóa]
Thông báo: [chưa đọc, đã đọc]
Hợp đồng: [hiệu lực, đã hết hạn, đã hủy]