*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Search Google
    Open Browser    https://www.google.co.th    Firefox
    Input Text    xpath=//*[@id="APjFqb"]    คนบ้านเรา
    Click Element    xpath=//div[3]/center/input
    [Teardown]    Close Browser