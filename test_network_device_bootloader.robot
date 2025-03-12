*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         network_device

*** Test Cases ***
Test Network Device Primary Bootloader
    [Documentation]    Test the primary bootloader of the network device.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    network primary_bootloader
    Teardown Device Connection    ${DEVICE}

Test Network Device Secondary Bootloader
    [Documentation]    Test the secondary bootloader of the network device.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    network secondary_bootloader
    Teardown Device Connection    ${DEVICE}