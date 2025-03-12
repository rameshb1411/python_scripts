*** Settings ***
Library           ../../libs/device_keywords.py
Library           BuiltIn

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test LTE Carrier Aggregation
    [Documentation]    Test the LTE carrier aggregation functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${ca_supported}    Execute Command    ${DEVICE}    check_carrier_aggregation_support
    Should Be True    ${ca_supported}
    Teardown Device Connection    ${DEVICE}

Test LTE MIMO
    [Documentation]    Test the LTE MIMO (Multiple Input Multiple Output) functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${mimo_supported}    Execute Command    ${DEVICE}    check_mimo_support
    Should Be True    ${mimo_supported}
    Teardown Device Connection    ${DEVICE}

Test LTE Bandwidth
    [Documentation]    Test the LTE bandwidth support of the modem.
    Setup Device Connection    ${DEVICE}
    ${lte_bandwidth}    Execute Command    ${DEVICE}    get_lte_bandwidth
    Should Be Equal As Numbers    ${lte_bandwidth}    20
    Teardown Device Connection    ${DEVICE}

Test LTE UL/DL Ratio
    [Documentation]    Test the LTE uplink/downlink ratio of the modem.
    Setup Device Connection    ${DEVICE}
    ${ul_dl_ratio}    Execute Command    ${DEVICE}    get_lte_ul_dl_ratio
    Should Be Equal As Numbers    ${ul_dl_ratio}    4
    Teardown Device Connection    ${DEVICE}

Test LTE HARQ
    [Documentation]    Test the LTE HARQ (Hybrid Automatic Repeat Request) functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${harq_supported}    Execute Command    ${DEVICE}    check_lte_harq_support
    Should Be True    ${harq_supported}
    Teardown Device Connection    ${DEVICE}

Test LTE Power Control
    [Documentation]    Test the LTE power control functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${power_control_supported}    Execute Command    ${DEVICE}    check_lte_power_control_support
    Should Be True    ${power_control_supported}
    Teardown Device Connection    ${DEVICE}