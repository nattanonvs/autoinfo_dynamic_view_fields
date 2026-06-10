# คู่มือการตั้งค่า (AutoInfo Dynamic View Fields) — Odoo 15

## หน้า Settings

ไปที่

Settings → AutoInfo Dynamic View Fields

## ความหมายของ Settings และค่าที่เก็บในระบบ

ค่าทั้งหมดถูกเก็บใน `ir.config_parameter` โดยใช้ key ดังนี้ (ดู `models/res_config_settings.py`)

### 1) เปิด/ปิดทั้งระบบ

- `view_auto_fields.enabled` (Boolean)
  - เปิด: ระบบจะเติม fields ให้ List/Tree/Search ตาม policy
  - ปิด: ไม่ทำอะไรเลย (เสมือนปิดโมดูลชั่วคราว)

### 2) Allowlist สำหรับโหมด Restricted

- `view_auto_fields.allowed_modules` (Char, comma-separated)
  - ตัวอย่าง: `sale,account,stock`
- `view_auto_fields.allowed_models` (Char, comma-separated)
  - ตัวอย่าง: `sale.order,account.move,res.partner`

แนวทางแนะนำ

- เริ่มจากอนุญาต “เฉพาะโมดูลที่จำเป็น” เพื่อลดความเสี่ยงชนกับ customization ในโมดูลอื่น
- ใช้ `allowed_models` เพื่อเจาะจงหน้าที่ต้องการจริง ๆ

### 3) ลดความลายตา (Field Reduction)

- `view_auto_fields.filter_active_fields` (Boolean)
  - กรองเฉพาะฟิลด์ที่มีข้อมูลจริง (stored field ที่พบค่าไม่เป็น NULL อย่างน้อย 1 แถว)
- `view_auto_fields.active_fields_cache_hours` (Integer)
  - cache ระยะเวลาเป็นชั่วโมง เพื่อลดภาระ query

- `view_auto_fields.hide_technical_fields` (Boolean)
  - ซ่อนฟิลด์เทคนิค/ระบบ เช่น create_uid/write_uid และกลุ่ม field ของ mail/activity

- `view_auto_fields.reduction_scope` (Selection: `both` / `list` / `search`)
  - กำหนดว่าจะให้การลดรายการ field มีผลกับ
    - ทั้ง Columns + Search
    - เฉพาะ Columns
    - เฉพาะ Search

- `view_auto_fields.max_fields_preset` (Selection: `0` / `30` / `50` / `80` / `custom`)
- `view_auto_fields.max_fields_custom` (Integer)
  - จำกัดจำนวน field ที่ระบบเติมเพิ่ม เพื่อลดความรกของ dropdown/advanced search

แนวทางแนะนำ

- เริ่มจาก preset 50 (ค่า default)
- ถ้าผู้ใช้บ่นว่ารายการเยอะ ให้เปิด `filter_active_fields` และ `hide_technical_fields` เพิ่ม

## การตั้งค่าสิทธิ์ (Groups / Access Rights)

Groups ที่มีให้ (ดู `security/view_auto_fields_security.xml`)

- `autoinfo_dynamic_view_fields.group_view_auto_fields_all`
- `autoinfo_dynamic_view_fields.group_view_auto_fields_restricted`
- `autoinfo_dynamic_view_fields.group_view_auto_fields_none`
- `autoinfo_dynamic_view_fields.group_view_auto_fields_settings_manager`

แนวทางใช้งาน

- ให้ผู้ใช้ทั่วไปอยู่ใน All หรือ Restricted
- ให้ผู้ใช้ที่ “ไม่ควรใช้ฟีเจอร์นี้” อยู่ใน None
- ให้เฉพาะผู้ดูแล/หัวหน้าแผนก ที่จะปรับ setting เรื่อง reduction อยู่ใน Settings manager (เพิ่มเติมจากสิทธิ์ admin)

