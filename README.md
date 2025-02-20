Robotframework101
=================================================================
ติดตั้ง python https://www.python.org/downloads/

```cmd 
python -m venv ${myenv} <- ตั้งชื่ออะไรก็ได้
```
> เป็นคำสั่งที่ใช้สร้าง Virtual Environment (สภาพแวดล้อมเสมือน) ใน Python ซึ่งช่วยให้เราสามารถแยกแพ็กเกจและไลบรารีของแต่ละโปรเจกต์ออกจากกันได้

```cmd 
myenv/Scripts/activate 
```
> เป็นสคริปต์ที่ใช้ เปิดใช้งาน Virtual Environment ที่สร้างขึ้นด้วย python -m venv บน Windows
>> ถ้าใช้ PowerShell แล้ว `Activate` ไม่ได้ ทำ Bypass ```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```