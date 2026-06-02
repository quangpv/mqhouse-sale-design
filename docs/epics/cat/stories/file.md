# CAT-07: Quản lý File

- **Tên:** Quản lý file/ảnh
- **Role:** Manager, HouseHolder, Admin, Super Admin (ghi), tất cả (xem)
- **Mô tả:** As a **người dùng**, I want **quản lý file ảnh/tài liệu**, So that **đính kèm cho BĐS, phòng hoặc hợp đồng**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Upload file (ảnh: jpg/png/webp, tài liệu: PDF)
- [ ] Xem danh sách file
- [ ] Xóa file
- [ ] Gán entityType (BDS/Phòng/Người dùng/Khách hàng)

## Technical Tasks

### Backend
- `POST /api/upload` - upload (multipart)
- `DELETE /api/files/:id`
- `GET /api/files?entityType&entityId`

### Frontend
- Upload component (drag & drop, preview)
