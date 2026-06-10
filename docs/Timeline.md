# Timeline — MQ Sale

> **Bắt đầu:** 01/06/2026
> **Kết thúc:** 27/11/2026 (Go-live + Hypercare)
> **Sprint:** 12 sprints × 2 tuần
> **Demo:** Thứ 6 cuối mỗi sprint

---

## Tổng quan Timeline

```
Tháng 6           Tháng 7           Tháng 8           Tháng 9
├──S1──┼──S2──┼──S3──┼──S4──┼──S5──┼──S6──┼──S7──┼──S8──┼──S9──┤
      DEMO1    DEMO2    DEMO3    DEMO4    DEMO5    DEMO6    DEMO7    DEMO8    DEMO9

Tháng 10                      Tháng 11
┼──S10──┼──S11──┼──S12──┤      ├──Go-live & Hypercare──┤
  DEMO10   DEMO11   DEMO12  14/11 GO-LIVE        27/11 KẾT THÚC
```

---

## Chi tiết từng Sprint

### S1 — Xác thực & Bảo mật

```
T6 01          T6 12
├──────┬──────┤
      DEMO S1
```

**Thời gian:** 01/06 (Mon) → 12/06 (Fri)
**Demo:** 12/06 (Fri)
**Nội dung:** AUTH-01, AUTH-03→06 (Login, Forgot pwd, OTP, Reset, Change pwd)

**Milestone:** ✅ Hệ thống xác thực hoàn chỉnh

---

### S2 — Danh mục & Điều hướng

```
T6 15          T6 26
├──────┬──────┤
      DEMO S2
```

**Thời gian:** 15/06 (Mon) → 26/06 (Fri)
**Demo:** 26/06 (Fri)
**Nội dung:** CAT-01→07 + NAV-01→02

**Milestone:** ✅ Danh mục hệ thống + Khung điều hướng

---

### S3 — Người dùng & Phân quyền

```
T6 29          T6 10/7
├──────┬──────┤
      DEMO S3
```

**Thời gian:** 29/06 (Mon) → 10/07 (Fri)
**Demo:** 10/07 (Fri)
**Nội dung:** USER-01→07

**Milestone:** ✅ Quản lý người dùng + Phân quyền

---

### S4 — BĐS cơ bản + Hồ sơ

```
T6 13/7        T6 24/7
├──────┬──────┤
      DEMO S4
```

**Thời gian:** 13/07 (Mon) → 24/07 (Fri)
**Demo:** 24/07 (Fri)
**Nội dung:** BDS-01→04,08 + PROFILE-01→02

**Milestone:** ✅ CRUD BĐS + Hồ sơ cá nhân

---

### S5 — Duyệt BĐS + Phòng cơ bản

```
T6 27/7        T6 7/8
├──────┬──────┤
      DEMO S5
```

**Thời gian:** 27/07 (Mon) → 07/08 (Fri)
**Demo:** 07/08 (Fri)
**Nội dung:** BDS-05→07 + PHONG-01→02 + PROFILE-03→04

**Milestone:** ✅ Duyệt BĐS + Tạo phòng

---

### S6 — Quản lý phòng + Thông báo

```
T6 10/8        T6 21/8
├──────┬──────┤
      DEMO S6
```

**Thời gian:** 10/08 (Mon) → 21/08 (Fri)
**Demo:** 21/08 (Fri)
**Nội dung:** PHONG-03→06,09 + NOTIF-01→02

**Milestone:** ✅ Quy trình đổi trạng thái phòng

---

### S7 — Cọc, Hợp đồng, Dashboard

```
T6 24/8        T6 4/9
├──────┬──────┤
      DEMO S7
```

**Thời gian:** 24/08 (Mon) → 04/09 (Fri)
**Demo:** 04/09 (Fri)
**Nội dung:** PHONG-07→08 + DASH-01→03 + NOTIF-03→04

**Milestone:** ✅ Dashboard + Quản lý hợp đồng

---

### S8 — Tìm kiếm + Bản đồ

```
T6 7/9         T6 18/9
├──────┬──────┤
      DEMO S8
```

**Thời gian:** 07/09 (Mon) → 18/09 (Fri)
**Demo:** 18/09 (Fri)
**Nội dung:** SEARCH-01→04 + MAP-01→04

**Milestone:** ✅ Tìm kiếm nâng cao + Bản đồ tương tác

---

### S9 — Thông báo, Chia sẻ, Yêu thích, Giao diện

```
T6 21/9        T6 2/10
├──────┬──────┤
      DEMO S9
```

**Thời gian:** 21/09 (Mon) → 02/10 (Fri)
**Demo:** 02/10 (Fri)
**Nội dung:** NOTIF-05→06 + SHARE-01→04 + FAV-01→05 + NAV-03→07

**Milestone:** ✅ Full tính năng — Sẵn sàng test

---

### S10 — Internal Testing

```
T6 5/10        T6 16/10
├──────┬──────┤
      DEMO S10
```

**Thời gian:** 05/10 (Mon) → 16/10 (Fri)
**Demo:** 16/10 (Fri) — Báo cáo kết quả test
**Nhóm test:** 20 người (key users)
**Hoạt động:** Test toàn bộ tính năng, fix bug critical/high, regression

**Milestone:** ✅ Internal test pass

---

### S11 — Company-wide Testing + UAT

```
T6 19/10       T6 30/10
├──────┬──────┤
      DEMO S11
```

**Thời gian:** 19/10 (Mon) → 30/10 (Fri)
**Demo:** 30/10 (Fri) — UAT sign-off
**Nhóm test:** Toàn công ty
**Hoạt động:** UAT, Load test, Security audit, Fix critical bugs

**Milestone:** ✅ UAT approved

---

### S12 — Release preparation + Deploy

```
T6 2/11        T6 13/11
├──────┬──────┤
      DEMO S12
```

**Thời gian:** 02/11 (Mon) → 13/11 (Fri)
**Demo:** 13/11 (Fri) — Release announcement
**Hoạt động:**
- 02/11→06/11: Code freeze, final regression, documentation
- 09/11→11/11: Deploy staging → validation
- 12/11→13/11: Deploy production → monitoring

**Milestone:** ✅ Release ready

---

### Go-live & Hypercare (16/11→27/11)

```
T2 16/11                  T6 27/11
├───────────┬──────────────┤
       GO-LIVE 14/11    KẾT THÚC 27/11
```

| Tuần | Thời gian | Hoạt động |
|------|-----------|-----------|
| 1 | 16/11→20/11 | **Go-live:** Deploy production, monitoring, rollback stand-by, support người dùng |
| 2 | 23/11→27/11 | **Hypercare:** Hotfix, performance tuning, handover, tài liệu vận hành |

**Milestone:** 🚀 **28/11** — Kết thúc dự án

---

## Tổng hợp Demo

| Sprint | Ngày | Nội dung demo |
|--------|------|---------------|
| S1 | 12/06 | Auth flow: Đăng ký → Đăng nhập → Đổi mật khẩu |
| S2 | 26/06 | CRUD danh mục + Điều hướng tab/sidebar |
| S3 | 10/07 | Quản lý user, phân quyền, gán khu vực |
| S4 | 24/07 | Tạo/xem/sửa BĐS + Hồ sơ cá nhân |
| S5 | 07/08 | Duyệt BĐS + Tạo phòng + Avatar |
| S6 | 21/08 | Đổi trạng thái phòng (Sale→Duyệt) + Thông báo |
| S7 | 04/09 | Đặt cọc, Hợp đồng, Dashboard |
| S8 | 18/09 | Tìm kiếm nâng cao + Bản đồ tương tác |
| S9 | 02/10 | Full system demo (tất cả tính năng) |
| S10 | 16/10 | Báo cáo kết quả internal test |
| S11 | 30/10 | UAT sign-off |
| S12 | 13/11 | Release announcement |

---

## Các mốc quan trọng (Milestones)

| Mốc | Thời gian | Mô tả |
|-----|-----------|-------|
| M1 | 12/06 | Auth hoàn chỉnh |
| M2 | 26/06 | Danh mục + Điều hướng |
| M3 | 10/07 | Người dùng + Phân quyền |
| M4 | 24/07 | CRUD BĐS |
| M5 | 07/08 | Duyệt BĐS + Phòng |
| M6 | 21/08 | Quy trình trạng thái phòng |
| M7 | 04/09 | Dashboard + Hợp đồng |
| M8 | 18/09 | Search + Map |
| M9 | 02/10 | Full feature complete |
| M10 | 16/10 | Internal test pass |
| M11 | 30/10 | UAT approved |
| M12 | 13/11 | Release ready |
| **🚀** | **14/11** | **Go-live** |
| **🏁** | **27/11** | **Kết thúc dự án** |

---

## Trạng thái Sprint

```
01/06 ████████████████████████████████ 27/11
      ██ Dev ██ Test ██ Release ██ Hypercare
      
S1  ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S2  ░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S3  ░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S4  ░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S5  ░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S6  ░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S7  ░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S8  ░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S9  ░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░
S10 ░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░
S11 ░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░
S12 ░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░
G-L ░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████
                                  14/11 GO-LIVE   27/11 KẾT THÚC
```

---

## Phụ lục: Lịch các ngày lễ/tắt (dự phòng)

| Ngày | Dịp | Ghi chú |
|------|-----|---------|
| 01/09 | Nghỉ lễ 2/9 | Có thể ảnh hưởng S7 |
| 02/09 | Nghỉ lễ 2/9 | Có thể ảnh hưởng S7 |
| 20/10 | Ngày PNVN | Không nghỉ |
| 20/11 | Ngày NGVN | Không nghỉ |

---

*Timeline được tạo từ Epic.md, phù hợp cho tracking và báo cáo tiến độ.*
