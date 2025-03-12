*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Connectivity
    [Documentation]    Test the connectivity of the modem.
    Setup Device Connection    ${DEVICE}
    Execute Command    ${DEVICE}    ifconfig
    Teardown Device Connection    ${DEVICE}

Test Modem Driver Features
    [Documentation]    Test the features of modem drivers.
    Setup Device Connection    ${DEVICE}
    Execute Command    ${DEVICE}    modem driver1
    Execute Command    ${DEVICE}    modem driver2
    Teardown Device Connection    ${DEVICE}