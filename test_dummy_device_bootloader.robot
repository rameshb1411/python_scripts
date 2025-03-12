*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         dummy_device

*** Test Cases ***
Test Dummy Device Primary Bootloader
    [Documentation]    Test the primary bootloader of the dummy device.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    dummy primary_bootloader
    Teardown Device Connection    ${DEVICE}

Test Dummy Device Secondary Bootloader
    [Documentation]    Test the secondary bootloader of the dummy device.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    dummy secondary_bootloader
    Teardown Device Connection    ${DEVICE}