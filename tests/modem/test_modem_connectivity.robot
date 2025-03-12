*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Connectivity
    [Documentation]    Test the connectivity of the modem.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    echo Modem connectivity test successful
    Teardown Device Connection    ${DEVICE}