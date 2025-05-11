*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_OPTIONS}    ${EMPTY}

*** Keywords ***
Open Website Bypass SSL Warning Using Capabilities in Edge
    [Arguments]    ${baseurl}
    ${BROWSER_OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${BROWSER_OPTIONS}    add_argument    --ignore-certificate-errors
    Call Method    ${BROWSER_OPTIONS}    add_argument    --allow-insecure-localhost
    Call Method    ${BROWSER_OPTIONS}    add_argument    --disable-renderer-backgrounding
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    ${status}=    Run Keyword And Return Status    Open Browser   url=${baseurl}    browser=edge    options=${BROWSER_OPTIONS}    desired_capabilities=${capabilities}
    RETURN    ${status}

Open Website Bypass SSL Warning Using Capabilities in Edge2
    [Arguments]    ${baseurl}
    ${BROWSER_OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${BROWSER_OPTIONS}    add_argument    --disable-renderer-backgrounding
    Call Method    ${BROWSER_OPTIONS}    add_argument    --no-sandbox
    Call Method    ${BROWSER_OPTIONS}    add_argument    --disable-dev-shm-usage
    Call Method    ${BROWSER_OPTIONS}    add_argument    --ignore-certificate-errors
    Call Method    ${BROWSER_OPTIONS}    add_argument    --allow-insecure-localhost
    Call Method    ${BROWSER_OPTIONS}    add_argument    --insecure
    Call Method    ${BROWSER_OPTIONS}    set_capability    acceptInsecureCerts    ${True}
    ${status}=    Run Keyword And Return Status    Open Browser    url=${baseurl}    browser=edge    options=${BROWSER_OPTIONS}
    RETURN    ${status}

Open Website Bypass SSL Warning Using Capabilities in Firefox
    [Arguments]    ${baseurl}
    ${BROWSER_OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    Call Method    ${BROWSER_OPTIONS}    add_argument    -headless
    ${status}=    Run Keyword And Return Status    Open Browser   url=${baseurl}    browser=firefox    options=${BROWSER_OPTIONS}
    RETURN    ${status}

