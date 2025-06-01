*** Settings ***
Library    Dialogs
Resource    ../resource/prove-step.robot


*** Variables ***
${PATH_FILE}    value


*** Test Cases ***
Hard Working
    Run TestCase    PATH=${PATH_FILE}    ROW_SKIP=2