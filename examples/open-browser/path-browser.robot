*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CHROME_PATH}    C:/Users/iyeno/OneDrive/Documents/chrome-win/chrome.exe

*** Test Cases ***
Set Chrome Browser Path
    # Create Chrome options object
    ${options}=    Evaluate    selenium.webdriver.chrome.options.Options()    selenium.webdriver
    Set Variable    ${options.binary_location}    ${CHROME_PATH}
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    ---disable-dev-shm-usage
    # Create WebDriver instance
    ${driver}=    Create Webdriver    Chrome    options=${options}
    
    # Go to the desired page
    Go To    https://www.google.com