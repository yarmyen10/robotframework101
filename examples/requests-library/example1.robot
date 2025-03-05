*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    Collections
Variables    config.yaml

*** Variables ***
${CHROME_PATH}    C:/Users/iyeno/OneDrive/Documents/chrome-win/chrome.exe

*** Keywords ***
SETYAML
    &{data_login}=    Convert To Dictionary    ${data_login}
    Log    username: ${data_login['username']}

*** Test Cases ***
TESTJSON
    ${response}    GET    https://restful-booker.herokuapp.com/booking/2
    Log    JSON YENZ${response.json()}
    ${firstname}=    Get From Dictionary    ${response.json()}    firstname
    Log    firstname: ${firstname}
    &{booking}=    Convert To Dictionary    ${response.json()}
    Log    firstname: ${booking['firstname']}

TESTYAML
    SETYAML