*** Settings ***
Library    Dialogs
Resource    ../resource/prove-step.resource

*** Variables ***
${PATH_CASE}      default

*** Test Cases ***
Robot Robo-Buddy
    # Log To Console    ${PATH_CASE}
    [Documentation]    Default Script robo-buddy
    Run TestCase    PATH=${PATH_CASE}    ROW_SKIP=2
