*** Settings ***
Library    SeleniumLibrary
Library    Dialogs

*** Variables ***
${OPTIONS}    ${EMPTY}

*** Keywords ***
Open MyNetwork Bypass SSL Warning Using Capabilities in Edge
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    Open Browser    https://10.137.16.95:10043/main    browser=edge    options=${options}    desired_capabilities=${capabilities}

Check If URL Is Main
    ${url}=    Get Location
    ${path}=    Evaluate    "${url}".split("?")[0].split("#")[0].split("/")[-1]
    IF    '${path}' == 'main'
        RETURN    ${TRUE}
    ELSE
        RETURN    ${FALSE}
    END