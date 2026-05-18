# คู่มือติดตั้ง (Odoo 15)

## 1) เตรียมไฟล์โมดูล

มี 2 วิธี

### วิธี A: ติดตั้งจาก zip

1. นำไฟล์ `view_auto_field.zip` ไปไว้บนเครื่องเซิร์ฟเวอร์
2. แตกไฟล์ zip จะได้โฟลเดอร์ `view_auto_fields`
3. นำโฟลเดอร์ `view_auto_fields` ไปวางใน addons path ของ Odoo (เช่น `/var/odoo/custom_addons/`)
4. ตรวจสอบว่า `odoo.conf` มี addons_path ชี้ไปยังโฟลเดอร์นั้นแล้ว

### วิธี B: ติดตั้งจากซอร์ส

คัดลอกโฟลเดอร์ `view_auto_fields/` ไปไว้ใน addons path ของ Odoo

## 2) อัปเดตรายการแอป (Update Apps List)

เข้า Odoo → Apps → Update Apps List

## 3) ติดตั้งโมดูล

ค้นหา “Auto View Fields” แล้วกด Install

## 4) ตั้งค่าระบบ (Settings)

ไปที่ Settings → Auto View Fields

- Auto add fields from Form into List/Search: เปิด/ปิดฟังก์ชันหลัก
- Allowed modules (comma-separated): ใส่ technical name ของโมดูล เช่น `sale,crm,stock`
- Allowed models (comma-separated): ใส่ชื่อโมเดล เช่น `sale.order,res.partner`

## 5) ตั้งค่าสิทธิ (Access Rights / Groups)

ไปที่ Settings → Users & Companies → Users → เลือกผู้ใช้ → Access Rights

เลือก 1 ในกลุ่มต่อไปนี้

- Auto View Fields: Allowed in all modules
- Auto View Fields: Allowed only in allowed modules
- Auto View Fields: Not allowed

หมายเหตุ:
- ถ้า “ไม่ได้อยู่ในกลุ่ม restricted/none” ระบบจะถือว่าอนุญาต (เหมือน Allowed in all modules)
- ถ้าเลือก “Allowed only in allowed modules” ต้องตั้ง allowlist ใน Settings ด้วย

## 6) อัปเกรด/อัปเดตโมดูล (กรณีปรับโค้ดแล้ว)

Apps → ค้นหา “Auto View Fields” → Upgrade

หรือใช้คำสั่ง:

```bash
python3 /path/to/odoo-bin -c /etc/odoo.conf -d <db_name> -u view_auto_fields --stop-after-init
```

