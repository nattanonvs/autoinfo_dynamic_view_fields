# Timeline & Change Log (AutoInfo Dynamic View Fields) — Odoo 15

## สรุปแนวทางพัฒนา

โมดูลนี้พัฒนาเพื่อ “ทำให้ list/search เลือก field ได้ครบตาม form” แบบใช้ได้ทั้งระบบ (global) แต่มี governance controls เพื่อคุมผลกระทบ

- เปิด/ปิดระดับระบบ (Settings)
- ควบคุมระดับผู้ใช้ (Groups)
- จำกัดขอบเขต (allowlist modules/models)
- ลดความรกของรายการ field (active fields / hide technical / max fields / scope)

## Change Log

### 15.0.1.5.0

- ปรับ metadata และมาตรฐานโมดูล (author/maintainer/license/summary/category)
- เพิ่มโครงสร้าง `controllers/` ให้ครบตามมาตรฐาน
- ปรับมาตรฐาน path ตัวอย่างสำหรับ server Linux: `/var/odoo/custom15_autoinfo/autoinfo_dynamic_view_fields`
- เตรียมเอกสารชุด `docs/` ให้ครบตาม Phase 3–6

### 15.0.1.5.1

- ปรับตัวอย่าง path ในเอกสารจาก Windows ให้เป็นโครงสร้างนิยมใช้บน Linux (`/var/odoo/custom15_autoinfo`)

### 15.0.1.4.x (ช่วงก่อนหน้า)

- Patch `BaseModel.load_views` เพื่อเติม fields ให้ List/Tree/Search แบบ runtime ครอบคลุมทุกโมเดล
- ทำให้คอลัมน์เดิมใน list view ซ่อน/แสดงได้อิสระ (`optional="show"`) และคอลัมน์ที่เติมใหม่เป็นค่าเริ่มต้นซ่อน (`optional="hide"`)
- เพิ่ม Groups 3 ระดับ (all / restricted / none) + กลุ่ม settings manager
- เพิ่ม Settings: allowlist modules/models
- เพิ่มระบบลดความรก:
  - active fields detection + cache
  - hide technical/system fields
  - จำกัดจำนวน field (30/50/80/custom) + เลือก scope (columns/search/both)
- เพิ่ม search bar ใน dropdown เลือกคอลัมน์ (web client)
- เพิ่ม `post_init_hook` เพื่อปิด legacy views ที่เคยทำให้เกิด error ตอน rebuild user groups view
- เพิ่ม compatibility field บน `res.users` เพื่อกัน error จาก legacy view ที่อ้างฟิลด์เดิม

## ข้อจำกัด (Known Limitations)

- โมดูลนี้ patch เมทอดระดับแกนของ Odoo (global) จึงมีโอกาสชนกับโมดูลอื่นที่ patch จุดเดียวกัน
- การกรอง active fields ต้องอาศัยการสแกนข้อมูลจริงของตาราง (มี cache ลดภาระแล้ว)

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

