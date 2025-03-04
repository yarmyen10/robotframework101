*** Settings ***
Resource    ../../../mynetwork/resource.robot

*** Test Cases ***
Go To Search Budget Planning CAPEX
    Open MyNetwork Bypass SSL Warning Using Capabilities in Edge
    ${resultCheck}    Check If URL Is Main
    Log    ${resultCheck}

