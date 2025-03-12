*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Frequency Bands Support
    [Documentation]    Test the frequency bands support of the modem.
    Setup Device Connection    ${DEVICE}
    ${band_supported}    Evaluate    ${device_keywords.Execute Command(${DEVICE}, "check_band_support", "1800MHz")} == True
    Should Be True    ${band_supported}
    Teardown Device Connection    ${DEVICE}