*** Settings ***
Library    Dialogs
Resource    ../resource/prove-step.robot

*** Test Cases ***
Test Demo2 Case1
    [Documentation]    ตัวอย่างการใช้ Run TestCase
    Run TestCase    PATH=E:\\robotframework101\\projects\\demo2\\uitestingplayground-2025-5-13-13-30-11.csv    ROW_SKIP=2
