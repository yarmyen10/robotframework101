*** Settings ***
Library    ../lib/read-record.py

*** Variables ***
@{LIST_OBJECTS}

*** Test Cases ***
Switch Case TestCase
    ${PATH}=    Set Variable    C:\\Users\\iyeno\\Downloads\\uitestingplayground-2025-4-25-23-38-29.csv
    # Log To Console    ${PATH}
    @{LIST_OBJECTS}=    Read CSV File Test Case    ${PATH}    2
    # Log To Console    ${LIST_OBJECTS}
    FOR    ${ITEM}    IN    @{LIST_OBJECTS}
        ${_STEP}=    Set Variable    ${ITEM['Step']}
        ${_DATA}=    Set Variable    ${ITEM['Data']}
        Log To Console    ${_STEP}
        ${IS_START_WITH_ENTER}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Enter
        Run Keyword If    '${_STEP}' == 'Open website'    Log To Console    Open Website: ${_DATA}
        ...    ELSE IF    ${IS_START_WITH_ENTER}    Log To Console    Enter Test: ${_DATA}
        ...    ELSE    Log To Console    Default Case: ${_DATA}
    END
