# คู่มือติดตั้ง (Odoo 15)

## 1) เตรียมไฟล์โมดูล

คัดลอกโฟลเดอร์ `autoinfo_dynamic_view_fields/` ไปไว้ใน addons path ของ Odoo (เช่น `/var/odoo/custom_addons/`)

## 2) อัปเดตรายการแอป (Update Apps List)

เข้า Odoo → Apps → Update Apps List

## 3) ติดตั้งโมดูล

ค้นหา “AutoInfo Dynamic View Fields” แล้วกด Install

## 4) ตั้งค่าระบบ (Settings)

ไปที่ Settings → AutoInfo Dynamic View Fields

- Auto add fields from Form into List/Search: เปิด/ปิดฟังก์ชันหลัก
- Use only active fields (has data): กรองเฉพาะฟิลด์ที่มีข้อมูลจริง เพื่อลดรายการ
- Hide technical/system fields: ซ่อนฟิลด์ระบบ/เทคนิคออกอัตโนมัติ
- Apply reduction to: เลือกให้มีผลกับ Columns / Search / ทั้งคู่
- Max fields to auto add: จำกัดจำนวนฟิลด์ที่ระบบจะเติมเพิ่ม (30/50/80/Custom)
- Allowed modules (comma-separated): ใส่ technical name ของโมดูล เช่น `sale,crm,stock`
- Allowed models (comma-separated): ใส่ชื่อโมเดล เช่น `sale.order,res.partner`

## 5) ตั้งค่าสิทธิ (Access Rights / Groups)

ไปที่ Settings → Users & Companies → Users → เลือกผู้ใช้ → Access Rights

เลือก 1 ในกลุ่มต่อไปนี้

- AutoInfo Dynamic View Fields: Allowed in all modules
- AutoInfo Dynamic View Fields: Allowed only in allowed modules
- AutoInfo Dynamic View Fields: Not allowed

หมายเหตุ:
- ถ้า “ไม่ได้อยู่ในกลุ่ม restricted/none” ระบบจะถือว่าอนุญาต (เหมือน Allowed in all modules)
- ถ้าเลือก “Allowed only in allowed modules” ต้องตั้ง allowlist ใน Settings ด้วย
- ถ้าต้องการให้ “หัวหน้าแผนก” ตั้งค่าการลดรายการ (ซ่อนฟิลด์เทคนิค/จำกัดจำนวน/ขอบเขต) ให้เพิ่มผู้ใช้นั้นเข้า group:
  - AutoInfo Dynamic View Fields: Settings manager

## 6) อัปเกรด/อัปเดตโมดูล (กรณีปรับโค้ดแล้ว)

Apps → ค้นหา “AutoInfo Dynamic View Fields” → Upgrade

หรือใช้คำสั่ง:

```bash
python3 /path/to/odoo-bin -c /etc/odoo.conf -d <db_name> -u autoinfo_dynamic_view_fields --stop-after-init
```

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).
