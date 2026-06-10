# คู่มือติดตั้ง (AutoInfo Dynamic View Fields) — Odoo 15

## วัตถุประสงค์

ติดตั้งโมดูล `autoinfo_dynamic_view_fields` เพื่อให้

- List/Tree view สามารถเพิ่ม/ซ่อนคอลัมน์ได้จากฟิลด์ที่อยู่ใน Form view
- Advanced Search มี field ให้เลือกครบตามฟิลด์ใน Form view
- ควบคุมสิทธิ์การใช้งานได้ผ่าน Groups (Access Rights) และ Settings

## ข้อกำหนด

- Odoo 15
- PostgreSQL
- Dependencies ของโมดูล: `base`, `web`

## ขั้นตอนติดตั้ง (ทั่วไป)

1) วางโฟลเดอร์โมดูล `autoinfo_dynamic_view_fields/` ลงใน addons path ของระบบ
2) Restart Odoo service/server
3) เข้า Apps → Update Apps List
4) ค้นหาและกด Install โมดูล `AutoInfo Dynamic View Fields`

## ขั้นตอนติดตั้ง (ตัวอย่างบน Linux — โครงสร้างนิยมใช้)

สมมติคุณวางโมดูลไว้ที่

`/var/odoo/custom15_autoinfo/autoinfo_dynamic_view_fields`

และในไฟล์ `odoo.conf` มี `addons_path` รวมโฟลเดอร์ `/var/odoo/custom15_autoinfo` แล้ว เช่น

`addons_path = /var/odoo/odoo15/odoo/addons,/var/odoo/odoo15/addons,/var/odoo/custom15_autoinfo`

จากนั้น

1) Restart Odoo service
2) เข้า Apps → Update Apps List
3) Install โมดูล `AutoInfo Dynamic View Fields`

## ขั้นตอนหลังติดตั้ง (สำคัญ)

1) ตั้งค่าสิทธิ์การใช้งาน (อย่างน้อย 1 กลุ่ม)

Settings → Users & Companies → Groups

- AutoInfo Dynamic View Fields: Allowed in all modules
- AutoInfo Dynamic View Fields: Allowed only in allowed modules
- AutoInfo Dynamic View Fields: Not allowed

2) ตั้งค่าใน Settings → AutoInfo Dynamic View Fields (ถ้าต้องการ)

- เปิด/ปิดการทำงานทั้งระบบ
- ตั้ง allowlist ของ modules/models (กรณี restricted)
- เปิดตัวเลือก “ลดความลายตา” (active fields / hide technical fields / limit max)

## หมายเหตุการย้ายจากโมดูลเดิม (ถ้ามี)

ถ้าเคยใช้ชื่อโมดูลเก่า `view_auto_fields` มาก่อน แนะนำให้

- ติดตั้ง `autoinfo_dynamic_view_fields` ให้เรียบร้อยก่อน
- จากนั้นค่อย Uninstall โมดูลเดิม (ถ้ายังติดตั้งอยู่)

โมดูลนี้มี `post_init_hook` เพื่อช่วยปิด view เก่าบางตัวที่เคยทำให้เกิดปัญหาในระหว่างการอัปเกรด

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

