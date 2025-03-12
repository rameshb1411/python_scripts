*** Settings ***
Library           ../libs/device_keywords.py

*** Variables ***
${DEVICE}         network_device

*** Test Cases ***
Test Network Device Connectivity
    [Documentation]    Test the connectivity of the network device.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    ifconfig
    Teardown Device Connection    ${DEVICE}