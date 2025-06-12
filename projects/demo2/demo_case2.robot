*** Settings ***
Library    Dialogs
Resource    ../resource/prove-step.resource

*** Test Cases ***
Test Demo2 Case1
    [Documentation]    ตัวอย่างการใช้ Run TestCase
    Run TestCase    PATH=D:\\.w\\repositories\\Test\\robotframework101\\projects\\demo2\\10-2025-6-9-16-22-25.csv    ROW_SKIP=2

Example Get Input
    ${user_input}=    Get Value From User    Enter your name:
    Log    ${user_input}