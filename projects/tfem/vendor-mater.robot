*** Settings ***
Library    Dialogs
Resource    ../resource/prove-step.resource

*** Test Cases ***
Test Vendor Master
    [Documentation]    Test Vendor Master
    Run TestCase    PATH=D:\\.w\\repositories\\Test\\robotframework101\\projects\\tfem\\vendor-master.csv    ROW_SKIP=2
