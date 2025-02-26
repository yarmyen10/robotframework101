# (Scalar Variable)
*** Variables ***
${NAME}    Alice
${AGE}     25
${PI}      3.14
${STATUS}  True

*** Test Cases ***
Demo Scalar Variables
    Log    ==== (Scalar Variable) ====
    Log    Name: ${NAME}
    Log    Age: ${AGE}
    Log    PI Value: ${PI}
    Log    Status: ${STATUS}


# (List Variable)
*** Variables ***
@{FRUITS}    Apple    Banana    Orange

*** Test Cases ***
Demo List Variables
    Log    ==== (List Variable) ====
    Log    First fruit: ${FRUITS}[0]
    Log    Second fruit: ${FRUITS}[1]
    Log    First fruit: ${FRUITS}


# (Dictionary Variable)
*** Variables ***
&{USER}    name=John    age=30    city=Bangkok

*** Test Cases ***
Demo Dictionary Variables
    Log    ==== (Dictionary Variable) ====
    Log    Name: ${USER.name}
    Log    Age: ${USER.age}
    Log    City: ${USER.city}


# Custom Keywords
*** Test Cases ***
Demo Custom Keyword
    Say Hello    Alice
    Say Hello    Bob

*** Keywords ***
Say Hello
    [Arguments]    ${name}
    Log    Hello, ${name}!


*** Test Cases ***
Check Adult Status
    Check Age    20
    Check Age    15

*** Keywords ***
Check Age
    [Arguments]    ${age}
    IF    ${age} >= 18
        Log    You are an adult.
    ELSE
        Log    You are a minor.
    END


*** Test Cases ***
Demo Return Keyword
    ${message}    Get Greeting    Alice
    Log    ${message}

*** Keywords ***
Get Greeting
    [Arguments]    ${name}
    ${greeting}    Set Variable    Hello, ${name}!
    RETURN    ${greeting}


*** Settings ***
Variables    variables.json

*** Test Cases ***
Demo Variables from JSON
    Log    Name: ${name}
    Log    Age: ${age}
    Log    First Fruit: ${fruits}[0]
    Log    Username: ${user_json.username}
    FOR    ${i}    IN RANGE    0    ${fruits.__len__()}
        Log    ${fruits}[${i}]
    END
    FOR    ${fruit}  IN    @{fruits}
        Log    ${fruit}
    END