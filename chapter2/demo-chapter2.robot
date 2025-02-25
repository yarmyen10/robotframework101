*** Test Cases ***
Demo Logging And Sleep
    Log    Hello, this is a log message!
    Sleep  2s
    Log    Test is completed!

Demo Run Keyword If
    ${age}    Set Variable    20
    Run Keyword If    ${age} >= 18    Log    You are an adult!
    Run Keyword If    ${age} < 18    Log    You are a minor!

Demo Should Be Equal
    ${expected}    Set Variable    Hello
    ${actual}      Set Variable    Hello
    Should Be Equal    ${expected}    ${actual}

Demo For Loop
    FOR    ${i}    IN RANGE    1    6
        Log    This is loop number ${i}
    END