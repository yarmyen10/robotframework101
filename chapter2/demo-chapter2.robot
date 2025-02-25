*** Test Cases ***
Demo Logging And Sleep
    Log    Hello, this is a log message!
    Sleep  2s
    Log    Test is completed!

Demo Run Keyword If (Old Method)
    ${age}    Set Variable    20
    Run Keyword If    ${age} >= 18    Log    You are an adult!
    Run Keyword If    ${age} < 18    Log    You are a minor!

Demo If Else (Old Method)
    ${score}    Set Variable    85
    ${result}    Set Variable If    ${score} >= 50    Pass    Fail
    Log    Student result: ${result}

Demo If ElseIf Else (New Method)
    ${score}    Set Variable    75
    
    IF    ${score} >= 80
        Log    Grade: A
    ELSE IF    ${score} >= 70
        Log    Grade: B
    ELSE IF    ${score} >= 60
        Log    Grade: C
    ELSE
        Log    Grade: F
    END

Demo Should Be Equal
    ${expected}    Set Variable    Hello
    ${actual}      Set Variable    Hello
    Should Be Equal    ${expected}    ${actual}

Demo Should Be Equal - Ignore Case
    ${expected}    Set Variable    hello
    ${actual}      Set Variable    HELLO
    Should Be Equal    ${expected}    ${actual}    ignore_case=True

Demo Compare Lists (Correct Way)
    @{expected}    Create List    apple    banana    orange
    @{actual}      Create List    apple    banana    orange
    Should Be Equal    ${expected}    ${actual}

Demo For Loop
    FOR    ${i}    IN RANGE    1    6
        Log    This is loop number ${i}
    END

Convert Values To String
    ${str_num}    Convert To String    123
    ${str_bool}   Convert To String    ${True}
    ${str_list}   Convert To String   ['a', 'b', 'c']

    Log To Console    ${str_num}   # Output: 123
    Log To Console    ${str_bool}  # Output: True
    Log To Console    ${str_list}  # Output: ['a', 'b', 'c']