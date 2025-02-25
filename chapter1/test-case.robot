*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open "google.co.th"
    Open Browser    https://www.google.co.th    Firefox

*** Test Cases ***
Search Google
    Open "google.co.th"
    Input Text    xpath=//*[@id="APjFqb"]    BMafRfS3Kk
    Click Element    xpath=//div[3]/center/input
    [Teardown]    Close Browser