*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    String

Library    ../lib/read-record.py
Resource    kw.robot

*** Variables ***
@{LIST_OBJECTS}    ${EMPTY}
${OPEN_STATUS}    ${EMPTY}

*** Keywords ***
Run TestCase
    [Arguments]    ${PATH}    ${ROW_SKIP}
    # Log To Console    ${PATH}
    @{LIST_OBJECTS}=    Read CSV File Test Case    ${PATH}    ${ROW_SKIP}
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
        ${IS_START_WITH_WAIT_COMPLETE}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Wait complete    ignore_case=True
        ${IS_START_WITH_WAIT_VISIBLE}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Wait visible    ignore_case=True
        ${IS_START_WITH_WAIT_NOT_VISIBLE}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Wait not visible    ignore_case=True
        ${IS_START_WITH_WAIT_ENABLED}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Wait enabled    ignore_case=True
        ${IS_START_WITH_EXTERNAL_STEP}=    Run Keyword And Return Status    Should Start With    ${_STEP}    External step    ignore_case=True
        Sleep    500ms
        # Wait Until Keyword Succeeds    1min    2s    Execute JavaScript    return document.readyState == 'complete';

        IF    '${_STEP}' == 'Open website Edge'
            ${OPEN_STATUS}=    Open Website Bypass SSL Warning Using Capabilities in Edge2    baseurl=${_DATA}    headless=${False}
            Run Keyword If    not ${OPEN_STATUS}    Fail    ❌ Browser failed to open
            Maximize Browser Window
        
        ELSE IF    '${_STEP}' == 'Open website Firefox'
            ${OPEN_STATUS}=    Open Website Bypass SSL Warning Using Capabilities in Firefox    baseurl=${_DATA}    headless=${False}
            Run Keyword If    not ${OPEN_STATUS}    Fail    ❌ Browser failed to open
            Maximize Browser Window

        ELSE IF    '${_STEP}' == 'Open newtab'
            Run Keywords
            ...    Execute JavaScript    code=window.open("${_DATA}", "_blank")
            ...    AND    Switch Window    index=1
        
        ELSE IF    '${_STEP}' == 'Close website'
            Run Keywords    
            ...    Close Browser

        ELSE IF    ${IS_START_WITH_ENTER}    
            Run Keywords    
            ...    Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Enter step
            ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Enter step
            ...    AND    Input Text    ${_XPATH}    ${_DATA}

        ELSE IF    ${IS_START_WITH_CLICK_ON}    
            Run Keywords    
            ...    Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Click step
            ...    AND    Click Element    ${_XPATH}

        ELSE IF    ${IS_START_WITH_SELECT}    
            Run Keywords    
            ...    Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Select step
            ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Select step
            ...    AND    Select From List By Value    ${_XPATH}    ${_DATA}

        ELSE IF    ${IS_START_WITH_CHOOSE_FILE}    
            Run Keywords    
            ...    Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Choose File step
            ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Choose File step
            ...    AND    Choose File    ${_XPATH}    ${_DATA}

        ELSE IF    ${IS_START_WITH_WAIT_COMPLETE}
            Wait For Page To Be Ready

        ELSE IF    ${IS_START_WITH_WAIT_VISIBLE}
            Wait Until Element Is Visible After Ready    locator=${_XPATH}

        ELSE IF    ${IS_START_WITH_WAIT_NOT_VISIBLE}
            Wait Until Element Is Not Visible After Ready    locator=${_XPATH}
        
        ELSE IF    ${IS_START_WITH_WAIT_ENABLED}
            Wait Until Element Is Enabled After Ready    locator=${_XPATH}

        ELSE IF    ${IS_START_WITH_EXTERNAL_STEP}
            Log To Console    Default Case: ${_STEP} / ${_DATA}
            ${split}=    Split String    ${_DATA}    |
            Log To Console    ${split}    # ควรได้: ['Pause Execution', 'จบแล้วจ้า !!!']
            Run Keyword    @{split}
        ELSE
            Log To Console    Default Case: ${_STEP} / ${_DATA}
        END
    
    END

Wait For Page To Be Ready
    Wait Until Keyword Succeeds    1min    5s    Execute JavaScript    return document.readyState == 'complete';

Wait Until Element Is Visible After Ready
    [Arguments]    ${locator}
    Wait For Page To Be Ready
    Wait Until Element Is Visible    ${locator}    timeout=1min
    # ${TEXT}=    Get Text    locator=${locator}
    # Run Keyword If    '${TEXT}' == ''    Fail    Element is visible but has no text
    # Log    Found text: ${TEXT}

Wait Until Element Is Not Visible After Ready
    [Arguments]    ${locator}
    Wait For Page To Be Ready
    Wait Until Element Is Not Visible    ${locator}    timeout=1min

Wait Until Element Is Enabled After Ready
    [Arguments]    ${locator}
    Wait For Page To Be Ready
    Wait Until Element Is Enabled    ${locator}    timeout=1min