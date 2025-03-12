*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Primary Bootloader
    [Documentation]    Test the primary bootloader of the modem.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    modem primary_bootloader
    Teardown Device Connection    ${DEVICE}

Test Modem Secondary Bootloader
    [Documentation]    Test the secondary bootloader of the modem.
    Setup Device Connection    ${DEVICE}
    device_keywords.Execute Command    ${DEVICE}    modem secondary_bootloader
    Teardown Device Connection    ${DEVICE}