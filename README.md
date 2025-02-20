Robotframework101 Step-By-Step
===============
Set Environment & Install
---------------
ติดตั้ง python https://www.python.org/downloads/

#### Set Virtual Environment:
```powershell 
python -m venv ${myenv} #ตั้งชื่ออะไรก็ได้
```
> เป็นคำสั่งที่ใช้สร้าง Virtual Environment (สภาพแวดล้อมเสมือน) ใน Python ซึ่งช่วยให้เราสามารถแยกแพ็กเกจและไลบรารีของแต่ละโปรเจกต์ออกจากกันได้

#### Activate:
```powershell 
myenv/Scripts/activate 
```
> เป็นสคริปต์ที่ใช้ เปิดใช้งาน Virtual Environment ที่สร้างขึ้นด้วย python -m venv บน Windows
>> ถ้าใช้ PowerShell แล้ว `Activate` ไม่ได้ ทำ Bypass ```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass``` ถ้ายังไม่ได้ `สวดมนต์ 😒` ไม่ก็ไปที Terminal อื่น

#### Install Requirements:
สร้าง ` requirements.txt ` สำหรับลง Lib ที่เกี่ยวกับ Robot Framework

```txt
invoke >= 0.20 # รันคำสั่งเชลล์ใน Python
rellu >= 0.6 # จัดการ release และ changelog สำหรับ Robot Framework
docutils >= 0.14 # ประมวลผลเอกสาร reStructuredText
robotframework >= 3.1.1 # เฟรมเวิร์กสำหรับการทดสอบอัตโนมัติ
robotframework-seleniumlibrary >= 3.3.1 # ใช้ Selenium ทดสอบเว็บใน Robot Framework
```

```powershell
pip install -r requirements.txt
```
> ใช้สำหรับติดตั้งแพ็กเกจ Python ทั้งหมดที่ระบุในไฟล์ `requirements.txt`
>> ตรวจสอบว่ามี pip ไหม `pip --version`

#### ลองทดสอบคำสั่ง Robot 
> อย่าลืม [Activate:](#activate) project ก่อน

```powershell
robot --version
```


---------------

