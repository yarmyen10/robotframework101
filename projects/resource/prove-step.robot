*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    ../lib/read-record.py
Resource    kw.robot

*** Variables ***
@{LIST_OBJECTS}    ${EMPTY}
${OPTIONS}    ${EMPTY}

*** Test Cases ***
Switch TestCase
    ${PATH}=    Set Variable    C:\\Users\\Phong\\Downloads\\automationtesting-2025-4-27-18-48-34.csv
    # Log To Console    ${PATH}
    @{LIST_OBJECTS}=    Read CSV File Test Case    ${PATH}    2
    # Log To Console    ${LIST_OBJECTS}
    FOR    ${ITEM}    IN    @{LIST_OBJECTS}
        ${_STEP}=    Set Variable    ${ITEM['Step']}
        ${_DATA}=    Set Variable    ${ITEM['Data']}
        ${_XPATH}=    Set Variable    ${ITEM['XPath']}
        ${_CSSSELECTOR}=    Set Variable    ${ITEM['cssSelector']}
        # Log To Console    ${_XPATH}
        ${IS_START_WITH_ENTER}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Enter    ignore_case=True
        ${IS_START_WITH_CLICK_ON}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Click on    ignore_case=True
        ${IS_START_WITH_SELECT}=    Run Keyword And Return Status    Should Start With    ${_STEP}    select    ignore_case=True
        ${IS_START_WITH_CHOOSE_FILE}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Choose File    ignore_case=True
        Sleep    1s
        IF    '${_STEP}' == 'Open website'
        ...    Open Website Bypass SSL Warning Using Capabilities in Edge    ${_DATA}

        ...    ELSE IF    ${IS_START_WITH_ENTER}    
        ...    Run Keywords    
        ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Enter step
        ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Enter step
        ...    AND    Input Text    ${_XPATH}    ${_DATA}

        ...    ELSE IF    ${IS_START_WITH_CLICK_ON}    
        ...    Run Keywords    
        ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Click step
        ...    AND    Click Element    ${_XPATH}

        ...    ELSE IF    ${IS_START_WITH_SELECT}    
        ...    Run Keywords    
        ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Select step
        ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Select step
        ...    AND    Select From List By Value    ${_XPATH}    ${_DATA}

        ...    ELSE IF    ${IS_START_WITH_CHOOSE_FILE}    
        ...    Run Keywords    
        ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Choose File step
        ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Choose File step
        ...    AND    Choose File    ${_XPATH}    ${_DATA}

        ...    ELSE    
        ...    Log To Console    Default Case: ${_STEP} / ${_DATA}
    END

