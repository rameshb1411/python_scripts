*** Settings ***
Library           ../../libs/device_keywords.py
Library           BuiltIn

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test 5G Beamforming
    [Documentation]    Test the 5G beamforming functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${beamforming_supported}    Execute Command    ${DEVICE}    check_beamforming_support
    Should Be True    ${beamforming_supported}
    Teardown Device Connection    ${DEVICE}

Test 5G NR Carrier Aggregation
    [Documentation]    Test the 5G NR carrier aggregation functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${nr_ca_supported}    Execute Command    ${DEVICE}    check_nr_carrier_aggregation_support
    Should Be True    ${nr_ca_supported}
    Teardown Device Connection    ${DEVICE}

Test 5G NR Bandwidth
    [Documentation]    Test the 5G NR bandwidth support of the modem.
    Setup Device Connection    ${DEVICE}
    ${nr_bandwidth}    Execute Command    ${DEVICE}    get_nr_bandwidth
    Should Be Equal As Numbers    ${nr_bandwidth}    100
    Teardown Device Connection    ${DEVICE}

Test 5G NR UL/DL Ratio
    [Documentation]    Test the 5G NR uplink/downlink ratio of the modem.
    Setup Device Connection    ${DEVICE}
    ${nr_ul_dl_ratio}    Execute Command    ${DEVICE}    get_nr_ul_dl_ratio
    Should Be Equal As Numbers    ${nr_ul_dl_ratio}    2
    Teardown Device Connection    ${DEVICE}

Test 5G NR Massive MIMO
    [Documentation]    Test the 5G NR massive MIMO functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${nr_massive_mimo_supported}    Execute Command    ${DEVICE}    check_nr_massive_mimo_support
    Should Be True    ${nr_massive_mimo_supported}
    Teardown Device Connection    ${DEVICE}

Test 5G NR HARQ
    [Documentation]    Test the 5G NR HARQ (Hybrid Automatic Repeat Request) functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${nr_harq_supported}    Execute Command    ${DEVICE}    check_nr_harq_support
    Should Be True    ${nr_harq_supported}
    Teardown Device Connection    ${DEVICE}

Test 5G NR Power Control
    [Documentation]    Test the 5G NR power control functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${nr_power_control_supported}    Execute Command    ${DEVICE}    check_nr_power_control_support
    Should Be True    ${nr_power_control_supported}
    Teardown Device Connection    ${DEVICE}

Test 5G NR Network Slicing
    [Documentation]    Test the 5G NR network slicing functionality of the modem.
    Setup Device Connection    ${DEVICE}
    ${network_slicing_supported}    Execute Command    ${DEVICE}    check_nr_network_slicing_support
    Should Be True    ${network_slicing_supported}
    Teardown Device Connection    ${DEVICE}