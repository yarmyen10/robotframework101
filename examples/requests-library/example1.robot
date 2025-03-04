*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    Collections

*** Variables ***
${CHROME_PATH}    C:/Users/iyeno/OneDrive/Documents/chrome-win/chrome.exe

*** Test Cases ***
TESTJSON
    ${response}    GET    https://restful-booker.herokuapp.com/booking/2
    Log    JSON YENZ${response.json()}
    ${firstname}=    Get From Dictionary    ${response.json()}    firstname
    Log    firstname: ${firstname}
    &{booking}=    Convert To Dictionary    ${response.json()}
    Log    firstname: ${booking['firstname']}