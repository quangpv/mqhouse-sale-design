# PROFILE-06: Liên hệ và hỗ trợ

- **Role:** Người dùng (tất cả)
- **Mô tả:** As a **người dùng**, I want **xem thông tin hỗ trợ và gửi yêu cầu liên hệ**, So that **được giải đáp thắc mắc khi cần**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Hiển thị thông tin hotline, email, địa chỉ
- [ ] Form gửi yêu cầu: họ tên, email, nội dung
- [ ] Validate form không để trống
- [ ] Gửi thành công → thông báo
- [ ] FAQ: danh sách câu hỏi thường gặp (accordion)

## Technical Tasks

### Backend
- `POST /api/contact` - nhận yêu cầu liên hệ → lưu + thông báo admin

### Frontend
- Màn hình contact.html: thông tin hỗ trợ + form liên hệ
- FAQ accordion component
- Validate form
