*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Driver Features
    [Documentation]    Test the features of modem drivers.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    echo Testing modem driver features
    Teardown Device Connection    ${DEVICE}