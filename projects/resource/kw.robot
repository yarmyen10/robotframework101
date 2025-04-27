*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Website Bypass SSL Warning Using Capabilities in Edge
    [Arguments]    ${baseurl}
    ${OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${OPTIONS}    add_argument    --ignore-certificate-errors
    Call Method    ${OPTIONS}    add_argument    --allow-insecure-localhost
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    Open Browser    ${baseurl}    browser=edge    options=${OPTIONS}    desired_capabilities=${capabilities}