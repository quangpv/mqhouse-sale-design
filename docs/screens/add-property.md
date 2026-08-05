# Add Property (Thêm BDS) / Add Room (Thêm phòng)

## 1. Screen Overview
- **Screen name**: Thêm BDS / Thêm phòng mới
- **Purpose**: Create new properties and rooms; also serves edit flows for both entities
- **Business context**: Core data-entry interface for listing real estate assets (BĐS) and their constituent rooms. Accessed during initial onboarding and ongoing portfolio management.

## 2. UI Structure
### Layout sections
- **Screen A — Thêm BDS**: Single-page form with 9 collapsible-ish sections stacked vertically, sticky footer
  1. **Basic info**: Tên dự án text input (required, max 255 ký tự), Mã BĐS text input, Loại BĐS dropdown (Căn hộ / Phòng trọ / Tòa nhà)
  2. **Image upload**: Dashed-border upload zone, image previews with remove button, counter `2 / 5`. Tap thumbnail → set ảnh đại diện (mặc định ảnh đầu, badge "Đại diện" + primary ring trên ảnh được chọn)
     - **Logo watermark sub-block**: 40×40 logo upload slot (not counted in 5-image quota), "Áp watermark lên ảnh" toggle (default ON). Each thumbnail shows logo overlay bottom-right when logo set + toggle ON
  3. **Location**: Tỉnh/Thành phố dropdown (có thể chọn), Quận/Huyện dropdown, Địa chỉ text input, GPS button
  4. **Furniture**: Grouped chip selector, add/edit/delete via dialog
  5. **Amenities**: Grouped chip selector, add/edit/delete via dialog
  6. **Services**: 2-column grid cards, add/edit via `service-dialog`
  7. **Description**: Tiêu đề input, Nội dung textarea
  8. **Contact**: Vai trò (readonly), Zalo link, Tên liên hệ, Số điện thoại, Ghi chú
  9. **Room diagram**: 4-column grid of room cards (code, price, bathrooms), "+" add room chip
- Sticky footer: "Xác nhận tạo" button
- **Screen B — Thêm phòng mới**:
  - Parent BDS label (readonly)
  - Mã phòng: multiple codes in batch-add, single in edit mode
  - Trạng thái dropdown: Đang trống / Sắp trống / Đã cọc / Đã cho thuê
  - Loại phòng + Kiểu phòng: linked dropdowns
  - Diện tích (m²), Số phòng vệ sinh
   - Image upload with counter `1 / 20`, tap thumbnail to set ảnh đại diện (mặc định ảnh đầu)
   - **Watermark inherited from parent BDS** (logo preview + note "Kế thừa từ BDS cha" + toggle "Áp watermark lên ảnh phòng", có thể tắt riêng)
   - Giá thuê/tháng
   - Furniture, Amenities, Services (inherited from BDS by default, editable)

- Sticky footer: "Lưu phòng" button

### Components
- `form-input`, `form-dropdown`, `form-textarea`
- `image-upload-zone` with preview grid
- `avatar-badge` (star + "Đại diện" overlay top-left on the selected thumbnail, primary ring) — tap any thumbnail to set as ảnh đại diện, default first image
- `watermark-logo-slot` (upload/remove logo) + `watermark-toggle` (on/off) + `wm-badge` overlay on thumbnails
- `chip-group` (Furniture / Amenities)
- `service-card` (2-column grid)
- `room-card` (4-column diagram grid)
- `add-room-chip`
- `dialog` / `service-dialog`
- `location-picker` (GPS)
- `sticky-footer`

### Important UI patterns
- Batch room code entry (Screen B) — multiple codes separated by newline or delimiter
- Linked dropdowns (Loại phòng → Kiểu phòng cascade)
- Inherited services/amenities from BDS, overridable per room
- Watermark inherited from BDS, overridable per room (toggle off)
- Image counter with max-5 (property) / max-20 (room) enforcement
- Ảnh đại diện: default = first image; removing the avatar image auto-switches to the next one

## 3. Entry Points
- Dashboard "+" FAB
- My Properties "+" header button
- Property Detail room grid "+" chip → navigateTo('them-phong')
- [STORY GAP] No entry point from search/map empty states

## 4. States
- **Loading**: Skeleton for form sections; spinner on "Xác nhận tạo" / "Lưu phòng"
- **Empty**: All fields blank on create; pre-filled on edit
- **Error**: Field-level validation messages; API error toast; image size/type rejection
- **Success**: Navigate to Dashboard / Property Detail with success toast

## 5. Business Rules
### Validation rules
- Mã BĐS / Mã phòng: required, unique
- Loại BĐS: required
- Images: max 5 per property, max 20 per room, jpg/png/webp only, max 10 MB each
- Ảnh đại diện: chọn từ danh sách ảnh đã upload, mặc định ảnh đầu tiên
- Watermark logo: 1 file, png/webp (transparent preferred), max 10 MB, không tính vào quota 5 ảnh; tùy chọn (toggle mặc định ON); phòng kế thừa watermark từ BDS cha
- Tỉnh/Thành phố + Quận/Huyện + Địa chỉ: required
- Tiêu đề + Nội dung mô tả: required
- Số điện thoại: valid phone format
- Giá thuê/tháng: positive number
- Diện tích: positive number

### Permission rules
| Role | Permissions |
|------|------------|
| Sale (R) | Read-only all |
| HouseHolder (CH) | CRUD own properties |
| Manager (QL) | CRUD within managed area |
| Admin (AD) | CRUD all + approve |
| SA | Unrestricted |

### Conditional rendering rules
- **Screen B** `Trạng thái` dropdown: hidden when parent BDS is not yet approved? [ASSUMPTION]
- Customer info fields appear when status = Đã cọc / Đã cho thuê (applies to room status updates, not creation — see property-detail)
- Loại phòng options filtered by Loại BĐS
- Kiểu phòng filtered by Loại phòng selection

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| BDS-01 | Tạo BĐS | — |
| BDS-03 | Sửa BĐS | — |
| PHONG-01 | Tạo phòng | — |
| PHONG-03 | Sửa phòng | — |
| SHARE-04 | Chia sẻ hình ảnh (ảnh chia sẻ mang watermark) | — |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Add Property | Home / Dashboard | Back button / "Xác nhận tạo" success |
| Add Property | Add Room (sub-screen) | "+" room chip → `navigateTo('them-phong')` |
| Add Room | Add Property | Back button (return to parent form) |

## 8. Mapping Notes
- `add-property.html` (895 lines) contains **two sub-screens** toggled via `navigateTo()` — no separate page
- Room image counter, validation, and upload logic shared with property image section
- [DESIGN GAP] No batch-import flow for rooms (only batch code entry)
- [ASSUMPTION] BDS must be saved first before rooms can be added (room diagram acts as post-create step)
- [ASSUMPTION] Edit mode (BDS-03, PHONG-03) reuses the same HTML with pre-populated values — no separate edit screen
