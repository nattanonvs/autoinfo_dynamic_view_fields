# AutoInfo Dynamic View Fields (Odoo 15)

โมดูลนี้ช่วยให้ List/Tree view สามารถ “เพิ่มคอลัมน์ได้” ตามฟิลด์ที่อยู่ใน Form view และทำให้ Search (Advanced Search) มี field ให้เลือกครบตามฟิลด์ใน Form view โดยอัตโนมัติ

## คุณสมบัติ

- Tree/List: เพิ่มคอลัมน์จาก Form view เป็น `optional="hide"` (ผู้ใช้เลือกเพิ่มเองได้จากตัวเลือกคอลัมน์)
- Search: เพิ่ม `<field/>` ลง search view เพื่อให้เลือกใช้ใน Advanced Search
- เปิด/ปิดได้ระดับระบบ (Settings)
- ควบคุมสิทธิได้ผ่าน Access Rights (Groups) 3 ระดับ
  - Allowed in all modules
  - Allowed only in allowed modules
  - Not allowed
- รองรับการซ่อนฟิลด์ที่แสดงอยู่เดิมใน Tree/List (คอลัมน์เดิมจะถูกตั้งให้ toggle ได้ด้วย `optional="show"`)
- ตัวเลือก “ลดความลายตา”:
  - กรองเฉพาะฟิลด์ที่มีข้อมูลจริง (active fields) พร้อม cache
  - ซ่อนฟิลด์ระบบ/เทคนิคอัตโนมัติ (เช่น mail/activity/audit)
  - จำกัดจำนวนฟิลด์ที่ระบบเติมเพิ่ม (30/50/80/Custom)
  - เลือกให้มีผลกับ Columns / Search / ทั้งคู่

## เอกสาร

- คู่มือติดตั้ง: INSTALL.md

## คู่มือใช้งาน (สรุป)

1) เปิดใช้งาน: Settings → AutoInfo Dynamic View Fields  
2) ในหน้า List/Tree: กดไอคอน “คอลัมน์” แล้วเลือกเพิ่ม/ซ่อนคอลัมน์ที่ต้องการ  
3) ในหน้า Search: ใช้ Advanced Search จะเห็น field เพิ่มเติมตาม Form view  
4) หากรายการยาวเกินไป ให้ตั้งค่า:
   - Use only active fields (has data)
   - Hide technical/system fields
   - Apply reduction to (Columns/Search/Both)
   - Max fields to auto add (30/50/80/Custom)

## รายการงานที่ทำ (สรุปทั้งหมด)

- ทำให้ทุก List/Tree สามารถเพิ่มคอลัมน์ได้จากฟิลด์ที่อยู่ใน Form view โดยอัตโนมัติ
- ทำให้ Search (Advanced Search) มี field ให้เลือกตามฟิลด์ใน Form view โดยอัตโนมัติ
- ทำให้คอลัมน์เดิมที่มีอยู่ใน List/Tree สามารถซ่อน/แสดงได้อิสระ (optional show)
- เพิ่ม Settings เพื่อเปิด/ปิดการทำงาน และกำหนด allowlist (modules/models) สำหรับโหมด restricted
- เพิ่ม Access Rights Groups เพื่อควบคุมสิทธิการใช้งานฟีเจอร์ (all/restricted/none)
- แก้ปัญหา icon ใน Settings sidebar โดยกำหนด data-key และมี icon.png ใน static/description
- แก้ปัญหาอัปเกรด/legacy views โดย:
  - ปิดการใช้งาน view เก่าที่อ้างอิงฟิลด์ที่ถูกลบ (cleanup views)
  - เพิ่ม compatibility field บน res.users เพื่อกัน error ตอน rebuild access rights view
- เพิ่มการกรองฟิลด์ “active fields” (ฟิลด์ที่มีข้อมูลจริง) และทำ cache ตามชั่วโมงที่ตั้งค่า
- เพิ่มตัวเลือกซ่อนฟิลด์เทคนิค/ระบบ และจำกัดจำนวนฟิลด์ที่เติมเพิ่ม พร้อมกำหนดขอบเขต (Columns/Search/Both)
- อัปเดตโครงสร้าง repo ให้เป็นโมดูลเดียว (โฟลเดอร์โมดูลเป็น root ของ addon)

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).
