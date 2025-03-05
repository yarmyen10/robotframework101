*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    Dialogs
# Library    read_yaml.py
Variables    config.yaml

*** Variables ***
${OPTIONS}    ${EMPTY}
# ${YAML_FILE}    config.yaml

*** Keywords ***
Open MyNetwork Bypass SSL Warning Using Capabilities in Edge
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    Open Browser    ${baseurl}    browser=edge    options=${options}    desired_capabilities=${capabilities}

Get Location Main?
    ${url}=    Get Location
    ${path}=    Evaluate    "${url}".split("?")[0].split("#")[0].split("/")[-1]
    RETURN    ${path}

Check If URL Is Main
    [Arguments]    ${path}
    IF    '${path}' == 'main'
        RETURN    ${TRUE}
    ELSE
        RETURN    ${FALSE} 
    END

Login Bybass MyNetwork
    &{data_login}=    Convert To Dictionary    ${data-login}
    Input Text    input-username    ${data_login['username']}
    Input Text    input-password    ${data_login['password']}
    Sleep    1s
    Click Button    btn-login

Close Browser MyNetwork
    Log    Close Browser MyNetwork
    [Teardown]    Close Browser
