Chapter 1
===============

การใช้งาน Settings, Test Case, Keywords, และ Variables
---------------

### `*** Settings ***` คืออะไร?  
ใน Robot Framework ส่วน Settings เป็นส่วนที่ใช้กำหนดค่าต่างๆ สำหรับการทำงานของ Test Case และ Test Suite ซึ่งมักจะอยู่ที่ด้านบนของไฟล์ .robot และมีรูปแบบดังนี้:

```robot
*** Settings ***
Documentation   คำอธิบายเกี่ยวกับ Test Suite หรือ Test Case
Library         ชื่อไลบรารีที่ต้องการใช้งาน
Resource        ไฟล์ Resource ที่ต้องนำเข้า
Variables       ไฟล์ตัวแปรที่ต้องนำเข้า
Suite Setup     คำสั่งที่ต้องรันก่อนเริ่ม Test Suite
Suite Teardown  คำสั่งที่ต้องรันหลังจาก Test Suite เสร็จ
Test Setup      คำสั่งที่ต้องรันก่อนเริ่มแต่ละ Test Case
Test Teardown   คำสั่งที่ต้องรันหลังจากแต่ละ Test Case เสร็จ
Force Tags      แท็กที่ต้องใส่กับทุก Test Case ใน Test Suite
Default Tags    แท็กที่ใช้เป็นค่าเริ่มต้นของ Test Case
```


### `*** Test Cases ***` คืออะไร?  
ใน **Robot Framework**, `*** Test Cases ***` คือ **ส่วนที่กำหนดชุดของกรณีทดสอบ** (Test Cases) ซึ่งเป็นหัวใจหลักของการทดสอบอัตโนมัติ  

```robot
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open "google.co.th"
    Open Browser    https://www.google.co.th    Firefox

*** Test Cases ***
Search Google
    Open "google.co.th"
    Input Text    xpath=//*[@id="APjFqb"]    BMafRfS3Kk
    Click Element    xpath=//div[3]/center/input
    [Teardown]    Close Browser
```

### `*** Keywords ***` คืออะไร?  
`*** Keywords ***` คือ ฟังก์ชันหรือคำสั่งที่ทำหน้าที่เป็นขั้นตอนหรือการกระทำที่สามารถนำมาใช้ซ้ำได้ภายในเทสเคส

```robot
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
เปิดหน้า "google.co.th"
    Open Browser    https://www.google.co.th    Firefox

*** Test Cases ***
ค้นหาด้วย Google
    เปิดหน้า "google.co.th"
    Input Text    xpath=//*[@id="APjFqb"]    BMafRfS3Kk
    Click Element    xpath=//div[3]/center/input
    [Teardown]    Close Browser
```

### `*** Variables ***` คืออะไร?  
`*** Variables ***` ใช้เพื่อเก็บค่าและทำให้โค้ดยืดหยุ่นขึ้น เช่น ช่วยในการจัดการข้อมูลที่อาจเปลี่ยนแปลงได้, ทำให้โค้ดมีความสะดวกในการปรับเปลี่ยนค่าเมื่อมีการเปลี่ยนแปลง

```robot
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.google.co.th
${BROWSER}        Firefox
${SEARCH_MESSAGE}    BMafRfS3Kk

*** Keywords ***
เปิดหน้า "google.co.th"
    Open Browser    ${URL}    ${BROWSER} 

*** Test Cases ***
ค้นหาด้วย Google
    เปิดหน้า "google.co.th"
    Input Text    xpath=//*[@id="APjFqb"]    ${SEARCH_MESSAGE}
    Click Element    xpath=//div[3]/center/input
    [Teardown]    Close Browser
```

> สามารถใช้คำสั่ง Test Cases, Keywords ที่เขียนเป็นภาษาไทยได้ แต่ควรระมัดระวังเกี่ยวกับการตั้งชื่อที่อาจจะทำให้การอ่านหรือการใช้งานยากขึ้น
