*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kikka
    Set Password  kikka123
    Set Password Confirmation  kikka123
    Submit Credentials
    Registration Should Succeed

Register With Username That Is Already In Use
    Set Username  kikka
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Registration Should Fail With Message  User with username kikka already exists

Register With Too Short Username And Valid Password
    Set Username  p
    Set Password  psql1234
    Set Password Confirmation  psql1234
    Submit Credentials
    Registration Should Fail With Message  Username has to be at least 3 characters long and contain only letters from a-z

Register With Valid Username And Too Short Password
    Set Username  psql
    Set Password  k
    Set Password Confirmation  k 
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kukkanen
    Set Password  kukkapelto
    Set Password Confirmation  kukkapelto
    Submit Credentials
    Registration Should Fail With Message  Password has to include numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kayttis
    Set Password  kayttis1234
    Set Password Confirmation  kayttis123
    Submit Credentials
    Registration Should Fail With Message  The password confirmation doesn't match the given password

*** Keywords ***
Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password  ${password_confirmation}

Submit Credentials
    Click Button  Register


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page