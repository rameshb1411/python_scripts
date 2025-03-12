*** Settings ***
Library           ../../libs/device_keywords.py
Library           BuiltIn

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Frequency Bands Support
    [Documentation]    Test the frequency bands support of the modem.
    Setup Device Connection    ${DEVICE}
    ${band_supported}    Execute Command