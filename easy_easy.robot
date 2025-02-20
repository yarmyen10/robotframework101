*** Settings ***
Documentation     Example using the space separated format. 
# อธิบายถึงการทำงานของไฟล์หรือส่วนต่างๆ โดยทั่วไปแล้วจะอธิบายว่าระบบนี้ทำอะไร
Library           OperatingSystem 
# การนำเข้าไลบรารีที่ใช้ในการทำงาน OperatingSystem เกี่ยวกับระบบปฏิบัติการ เช่น การตรวจสอบหรือทำงานกับไฟล์และไดเรกทอรี


*** Variables ***
${MESSAGE}        Hello, world!

*** Test Cases ***
My Test 
# My Test ชื่อของชุดทดสอบนี้
    [Documentation]    Example test.
    # [Documentation]    Example test. ใช้ในการอธิบายถึงการทดสอบนี้
    Log    ${MESSAGE} ${CURDIR}
    # Log ${MESSAGE}: คำสั่งให้พิมพ์ข้อความจากตัวแปร ${MESSAGE} ซึ่งจะพิมพ์ว่า "Hello, world!"
    My Keyword    ${CURDIR} 
    # My Keyword ${CURDIR}: เรียกใช้คีย์เวิร์ด My Keyword และส่งพารามิเตอร์ ${CURDIR} ซึ่งเป็นตัวแปรที่เก็บเส้นทางของไดเรกทอรีปัจจุบัน

Another Test
# Another Test ชื่อของชุดทดสอบนี้
    Should Be Equal    ${MESSAGE}    Hello, world! 
    # Should Be Equal ${MESSAGE} Hello, world!: ตรวจสอบว่า ${MESSAGE} มีค่าตรงกับ "Hello, world!" หรือไม่ ถ้าไม่ตรงจะล้มเหลว

*** Keywords ***
My Keyword
    [Arguments]    ${path} 
    # [Arguments]: กำหนดพารามิเตอร์ที่คีย์เวิร์ดนี้จะรับ ซึ่งในที่นี้รับพารามิเตอร์ ${path}
    Directory Should Exist    ${path} 
    # Directory Should Exist ${path}: คำสั่งที่ตรวจสอบว่าไดเรกทอรีที่กำหนดใน ${path} มีอยู่จริงหรือไม่ ถ้าไม่ตรงจะล้มเหลว