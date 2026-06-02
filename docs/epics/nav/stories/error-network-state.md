# NAV-07: Error & Network state

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **thấy thông báo lỗi thân thiện khi có sự cố mạng hoặc lỗi hệ thống**, So that **biết cách xử lý**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Error state: icon + thông báo lỗi + nút thử lại
- [ ] Toast notification cho lỗi ngắn
- [ ] Offline indicator (khi mất mạng)
- [ ] Auto-retry khi mạng khôi phục
- [ ] Modal cho lỗi nghiêm trọng

## Technical Tasks

### Frontend
- Error boundary component
- Toast notification system
- Network status listener (online/offline)
- Retry button
