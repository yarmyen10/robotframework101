*** Settings ***
Library    Collections
Resource    ../../../mynetwork/resource.robot
Variables    requirements.yaml
Variables    results.json

*** Keywords ***
Go To Search CAPEX
    Go To    ${baseurl}${capex['search-path']}

Set Text Search CAPEX
    ${inputList}=    Get From Dictionary    ${searchCapex['ezCase']}    inputList
    FOR    ${input}  IN    @{inputList}
        Log    ${input.type}
        IF    '${input.type}' == 'text'
            Input Text    ${input.locator}    ${input.value}
        END
    END
    Sleep    1s
    Click Button    xpath=//*[@id="print-page"]/div[2]/div/app-search/div[2]/div[2]/div[1]/app-search-criteria/div/div/div/div[1]/button 
    Wait Until Element Is Visible    xpath=//*[@id="print-page"]/div[2]/div/app-search/div[2]/div[2]/div[2]/app-data-table-search/div/app-data-table-budget-planning/div[2]/table    timeout=10s
    Sleep    1s
    ${Text Budget ID}=    Get Text    xpath=//*[@id="print-page"]/div[2]/div/app-search/div[2]/div[2]/div[2]/app-data-table-search/div/app-data-table-budget-planning/div[2]/table/tbody/tr/td[2]/div
    Log    Extracted Text: ${Text Budget ID}
    
    ${checkList}=    Get From Dictionary    ${searchCapex['ezCase']}    checkList
    ${row_xpath}    Set Variable    ${None}
    FOR    ${check}  IN    @{checkList}
        IF    '${Text Budget ID}' == '${check.expected}'
            ${row_xpath}=    Set Variable    xpath=//*[@id="print-page"]/div[2]/div/app-search/div[2]/div[2]/div[2]/app-data-table-search/div/app-data-table-budget-planning/div[2]/table/tbody/tr/td[2]/div
            Exit For Loop
        END
        
    END

    IF    '${row_xpath}' != ${None}
        Click Element    ${row_xpath}
        Sleep    1s
        Validate Search Budget Planning CAPEX
    END
    

    # Run Keyword If    '${check.keyword}' == 'Element Text Should Be'    Element Text Should Be    ${check.locator}    ${check.expected}

Search Budget Planning CAPEX
    Go To Search CAPEX
    Sleep    1s
    Set Text Search CAPEX

Validate Search Budget Planning CAPEX
    ${checkList}=    Get From Dictionary    ${searchCapex['ezCase']}    checkList
    FOR    ${check}  IN    @{checkList}
        IF    '${check.keyword}' == 'Element Text Should Be'
            Log    Element Text Should Be: '${check.locator}'
            Sleep    1s
            Element Text Should Be    ${check.locator}    ${check.expected}
            Exit For Loop
        END
    END
    Pause Execution    จบแล้วจ้า !!!
    Close Browser MyNetwork

*** Test Cases ***
Go To Search Budget Planning CAPEX
    Open MyNetwork Bypass SSL Warning Using Capabilities in Edge
    Maximize Browser Window
    ${Location Main}    Get Location Main?
    ${Result Check}    Check If URL Is Main    ${Location Main}
    Log    Location Main: ${Location Main}
    Log    Result Check: ${Result Check}
    IF    ${Result Check} == ${FALSE}
        Login Bybass MyNetwork
        Sleep    1s
        ${Location Main}    Get Location Main?
        ${Result Check}    Check If URL Is Main    ${Location Main}
        IF    ${Result Check} == ${TRUE}
            Log    OK MAIN
            Sleep    1s
            Search Budget Planning CAPEX
        ELSE
            Close Browser MyNetwork
        END
    END