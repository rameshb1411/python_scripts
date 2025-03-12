*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         dummy_device

*** Test Cases ***
Test Dummy Device Connectivity
    [Documentation]    Test the connectivity of the dummy device.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    ifconfig
    Teardown Device Connection    ${DEVICE}

Test Dummy Device Driver Features
    [Documentation]    Test the features of dummy device drivers.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    dummy driver1
    device_keywords.Execute Command    ${DEVICE}    dummy driver2
    Teardown Device Connection    ${DEVICE}