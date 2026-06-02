# NOTIF-05: Tự động gửi thông báo

- **Role:** Hệ thống
- **Mô tả:** As a **hệ thống**, I want **tự động gửi thông báo khi Admin duyệt BĐS/phòng**, So that **người yêu cầu biết kết quả**

**Priority:** High

**Acceptance Criteria:
- [ ] Khi duyệt BĐS → TB cho người tạo: "BĐS [tên] đã được duyệt"
- [ ] Khi từ chối BĐS → TB có lý do từ chối
- [ ] Khi duyệt đổi trạng thái phòng → TB cho Sale
- [ ] Khi BĐS sắp hết hạn → TB nhắc nhở

## Technical Tasks

### Backend
- Trigger notification service khi approve/reject
- Cron job kiểm tra BĐS sắp hết hạn
- Notification queue / direct insert
