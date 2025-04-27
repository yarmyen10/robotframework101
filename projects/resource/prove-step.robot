*** Settings ***
Library    SeleniumLibrary
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
        ${_XPATH}=    Set Variable    ${ITEM['XPath']}
        ${_CSSSELECTOR}=    Set Variable    ${ITEM['cssSelector']}
        # Log To Console    ${_XPATH}
        ${IS_START_WITH_ENTER}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Enter
        ${IS_START_WITH_CLICK_ON}=    Run Keyword And Return Status    Should Start With    ${_STEP}    Click on
        
        Run Keyword IF    '${_STEP}' == 'Open website'    
        ...    Log To Console    Open Website: ${_DATA}

        # ...    ELSE IF    ${IS_START_WITH_ENTER}    
        # ...    Run Keywords    
        # ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Enter step
        # ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Enter step
        # ...    AND    Input Text    ${_XPATH}    ${_DATA}

        # ...    ELSE IF    ${IS_START_WITH_CLICK_ON}    
        # ...    Run Keywords    
        # ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Click step
        # ...    AND    Click Element    ${_XPATH}

        # ...    ELSE IF    ${IS_START_WITH_SELECT}    
        # ...    Run Keywords    
        # ...        Should Not Be Empty    ${_XPATH}    msg=Missing XPATH for Select step
        # ...    AND    Should Not Be Empty    ${_DATA}    msg=Missing DATA for Select step
        # ...    AND    Select From List By Value    ${_XPATH}    ${_DATA}

        ...    ELSE    
        ...    Log To Console    Default Case: ${_STEP} / ${_DATA}
    END
