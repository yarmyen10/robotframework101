*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_OPTIONS}    ${EMPTY}

*** Keywords ***
Open Website Bypass SSL Warning Using Capabilities in Edge
    [Arguments]    ${baseurl}    ${headless}=${False}
    ${BROWSER_OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    IF    ${headless}
        Call Method    ${BROWSER_OPTIONS}    add_argument    -headless
    END
    Call Method    ${BROWSER_OPTIONS}    add_argument    --ignore-certificate-errors
    Call Method    ${BROWSER_OPTIONS}    add_argument    --allow-insecure-localhost
    Call Method    ${BROWSER_OPTIONS}    add_argument    --disable-renderer-backgrounding
    ${capabilities}=    Create Dictionary    acceptInsecureCerts=${True}
    ${status}=    Run Keyword And Return Status    Open Browser   url=${baseurl}    browser=edge    options=${BROWSER_OPTIONS}    desired_capabilities=${capabilities}
    RETURN    ${status}

Open Website Bypass SSL Warning Using Capabilities in Edge2
    [Arguments]    ${baseurl}    ${headless}=${False}
    ${BROWSER_OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    # เพิ่ม arguments
    FOR    ${arg}    IN
        ...    --disable-renderer-backgrounding
        ...    --no-sandbox
        ...    --disable-dev-shm-usage
        ...    --disable-extensions
        ...    --disable-infobars
        ...    --ignore-certificate-errors
        ...    --allow-insecure-localhost
        ...    --insecure
        ...    --disable-gpu
        ...    --guest
        ...    --no-first-run
        ...    --disable-popup-blocking
        ...    --disable-notifications
        ...    --disable-background-networking
        ...    --disable-background-timer-throttling
        ...    --disable-backgrounding-occluded-windows
        ...    --disable-web-security
        ...    --disable-translate
        ...    --disable-application-cache
        ...    --disable-client-side-phishing-detection
        ...    --disable-component-update
        ...    --disable-default-apps
        ...    --disable-desktop-notifications
        ...    --disable-extensions-http-throttling
        ...    --disable-features=TranslateUI
        ...    --disable-ipc-flooding-protection
        ...    --disable-prompt-on-repost
        ...    --disable-sync
        ...    --disable-webgl
        ...    --disable-webgl2-compute-context
        ...    --disable-webgl-image-chromium
        ...    --remote-debugging-port=9222
        ...    --disable-logging
        ...    --log-level=3
        ...    --disable-breakpad
        ...    --disable-crash-reporter
        ...    --disable-domain-reliability
        
        Call Method    ${BROWSER_OPTIONS}    add_argument    ${arg}    
    END
    IF    ${headless}
        Call Method    ${BROWSER_OPTIONS}    add_argument    --headless
    END
    Call Method    ${BROWSER_OPTIONS}    set_capability    acceptInsecureCerts    ${True}
    Create Webdriver    Edge    options=${BROWSER_OPTIONS}
    ${status}=    Run Keyword And Return Status    Go To    ${baseurl}
    RETURN    ${status}

Open Website Bypass SSL Warning Using Capabilities in Firefox
    [Arguments]    ${baseurl}    ${headless}=${False}
    ${BROWSER_OPTIONS}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    FOR    ${arg}    IN
        ...    --disable-renderer-backgrounding
        ...    --no-sandbox
        ...    --disable-dev-shm-usage
        ...    --disable-extensions
        ...    --disable-infobars
        ...    --ignore-certificate-errors
        ...    --allow-insecure-localhost
        ...    --insecure
        ...    --disable-gpu
        ...    --guest
        ...    --no-first-run
        ...    --disable-popup-blocking
        ...    --disable-notifications
        ...    --disable-background-networking
        ...    --disable-background-timer-throttling
        ...    --disable-backgrounding-occluded-windows
        ...    --disable-web-security
        ...    --disable-translate
        ...    --disable-application-cache
        ...    --disable-client-side-phishing-detection
        ...    --disable-component-update
        ...    --disable-default-apps
        ...    --disable-desktop-notifications
        ...    --disable-extensions-http-throttling
        ...    --disable-features=TranslateUI
        ...    --disable-ipc-flooding-protection
        ...    --disable-prompt-on-repost
        ...    --disable-sync
        ...    --disable-webgl
        ...    --disable-webgl2-compute-context
        ...    --disable-webgl-image-chromium
        ...    --disable-logging
        ...    --log-level=3
        ...    --disable-breakpad
        ...    --disable-crash-reporter
        ...    --disable-domain-reliability
        Call Method    ${BROWSER_OPTIONS}    add_argument    ${arg}    
    END
    IF    ${headless}
        Call Method    ${BROWSER_OPTIONS}    add_argument    --headless
    END
    Call Method    ${BROWSER_OPTIONS}    set_capability    acceptInsecureCerts    ${True}
    Create Webdriver    Firefox    options=${BROWSER_OPTIONS}
    ${status}=    Run Keyword And Return Status    Go To    ${baseurl}
    RETURN    ${status}

