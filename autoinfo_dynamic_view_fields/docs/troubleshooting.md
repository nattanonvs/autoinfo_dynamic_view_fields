# Troubleshooting (AutoInfo Dynamic View Fields) — Odoo 15

## 1) ติดตั้ง/อัปเกรดแล้วเกิด RPC_ERROR (Traceback อ้างถึงโมดูลนี้)

แนวทางแก้

- เปิดดู traceback เต็ม ๆ ใน log (แนะนำตั้ง `--log-handler :INFO` หรือสูงกว่า)
- ตรวจว่าใช้ Odoo 15 และโมดูลอยู่ใน addons_path จริง

## 2) รายการ field เยอะเกินไป / dropdown คอลัมน์รก

แนวทางแก้ (แนะนำตามลำดับ)

1) เปิด `Hide technical/system fields`
2) เปิด `Use only active fields (has data)`
3) ตั้ง `Max fields to auto add` เป็น 30/50 และเลือก scope ให้เหมาะ (Columns/Search/Both)

## 3) ระบบช้าเมื่อเปิด list view (โดยเฉพาะโมเดลใหญ่)

สาเหตุที่เป็นไปได้

- เปิด `Use only active fields (has data)` และระบบต้องตรวจ field ที่มีข้อมูลจริง (มี cache แต่รอบแรกจะใช้เวลา)

แนวทางแก้

- เพิ่ม `Active fields cache (hours)` ให้มากขึ้น (เช่น 24/72)
- ปรับ policy เป็น Restricted และจำกัด allowlist เฉพาะโมดูลที่ต้องใช้จริง

## 4) ช่องค้นหาในเมนูคอลัมน์ไม่ขึ้น

ตรวจสอบ

- เปิดหน้า list view แล้วกด Ctrl+Shift+I (DevTools) ดู Console และ Network ว่า JS asset โหลดครบหรือไม่
- กด Ctrl+F5 เพื่อ refresh แบบไม่ใช้ cache

หมายเหตุ

ไฟล์ JS อยู่ที่ `static/src/js/optional_columns_search.js` และถูกโหลดผ่าน `web.assets_backend` ใน manifest

## 5) ต้องการ “ปิดชั่วคราว” โดยไม่ถอนการติดตั้ง

ทำได้โดย

Settings → AutoInfo Dynamic View Fields → ปิด `Auto add fields from Form into List/Search`

## 6) อัปเกรดแล้วติดข้อความ cron lock

อาการตัวอย่าง

- “Odoo is currently processing a scheduled action. Module operations are not possible...”

แนวทางแก้ (ฝั่ง server)

- หยุดงาน cron ชั่วคราว (เช่นรันแบบ `--max-cron-threads=0` เพื่ออัปเกรด) แล้วค่อย upgrade

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

