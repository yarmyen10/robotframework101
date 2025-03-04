*** Settings ***
Library    SeleniumLibrary
Library    Dialogs

*** Variables ***
${OPTIONS}    ${EMPTY}

*** Test Cases ***
Bypass SSL Warning Using Capabilities in Chrome
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    Open Browser    https://expired.badssl.com    browser=chrome    options=${options}    desired_capabilities=${capabilities}
    Sleep    5s
    Close Browser

Bypass SSL Warning Using Capabilities in Edge
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    Open Browser    https://expired.badssl.com    browser=edge    options=${options}    desired_capabilities=${capabilities}
    Sleep    5s
    Close Browser

Test Pause Execution
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    Open Browser    https://expired.badssl.com    browser=edge    options=${options}    desired_capabilities=${capabilities}
    Pause Execution    กรุณากรอกข้อมูลใน popup แล้วกด OK
    Sleep    5s
    Close Browser
