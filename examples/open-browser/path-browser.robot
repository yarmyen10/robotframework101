# *** Settings ***
# Library    SeleniumLibrary
# Library    Collections

# *** Variables ***
# ${CHROME_PATH}    C:/Users/iyeno/OneDrive/Documents/chrome-win/chrome.exe

# *** Test Cases ***
# Set Chrome Browser Path
#     ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
#     Set To Dictionary    ${options}    binary_location    ${CHROME_PATH}
#     Open Browser    https://www.google.com    browser=chrome    options=${options}
#     Sleep    5s
#     Close Browser