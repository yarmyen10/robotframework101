*** Settings ***
Resource    ../resource/prove-step.resource

*** Test Cases ***
Test Demo1 Case1
    Run TestCase    PATH=D:\\.w\\repositories\\Test\\robotframework101\\projects\\demo1\\10-2025-4-28-14-52-32.csv    ROW_SKIP=2

Test Demo1 Case2
    Run TestCase    PATH=D:\\.w\\repositories\\Test\\robotframework101\\projects\\demo1\\10-2025-5-7-14-34-38.csv    ROW_SKIP=2
