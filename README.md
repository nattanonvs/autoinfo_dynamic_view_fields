# Auto View Fields (Odoo 15)

โมดูลนี้ช่วยให้ List/Tree view สามารถ “เพิ่มคอลัมน์ได้” ตามฟิลด์ที่อยู่ใน Form view และทำให้ Search (Advanced Search) มี field ให้เลือกครบตามฟิลด์ใน Form view โดยอัตโนมัติ

## คุณสมบัติ

- Tree/List: เพิ่มคอลัมน์จาก Form view เป็น `optional="hide"` (ผู้ใช้เลือกเพิ่มเองได้จากตัวเลือกคอลัมน์)
- Search: เพิ่ม `<field/>` ลง search view เพื่อให้เลือกใช้ใน Advanced Search
- เปิด/ปิดได้ระดับระบบ (Settings)
- ควบคุมสิทธิได้ผ่าน Access Rights (Groups) 3 ระดับ
  - Allowed in all modules
  - Allowed only in allowed modules
  - Not allowed

## โครงสร้างไฟล์

- โมดูล: `view_auto_fields/`
- ไฟล์ zip สำหรับติดตั้ง: `C:\odoo\NEW APP CUSTOM BY ARM\view_auto_fields_15.0.zip`

## เอกสาร

- คู่มือติดตั้ง: INSTALL.md
