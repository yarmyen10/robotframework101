*** Settings ***
Library    Dialogs
Resource    ../resource/prove-step.robot

*** Test Cases ***
Test Demo2 Case1
    [Documentation]    ตัวอย่างการใช้ Run TestCase
    Run TestCase    PATH=D:\\.w\\repositories\\Test\\robotframework101\\projects\\demo2\\dev-tna-2025-6-6-9-54-58.csv    ROW_SKIP=2
