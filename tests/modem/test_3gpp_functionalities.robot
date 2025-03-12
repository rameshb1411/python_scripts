
*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${DEVICE}         modem

*** Test Cases ***
Test Modem Throughput
    [Documentation]    Test the throughput of the modem.
    Setup Device Connection    ${DEVICE}
    ${throughput}    Evaluate    ${device_keywords.Execute Command(${DEVICE}, "get_throughput")}
    Should Be Greater Than    ${throughput}    50
    Teardown Device Connection    ${DEVICE}

Test Modem Latency
    [Documentation]    Test the latency of the modem.
    Setup Device Connection    ${DEVICE}
    ${latency}    Evaluate    ${device_keywords.Execute Command(${DEVICE}, "get_latency")}
    Should Be Less Than    ${latency}    50
    Teardown Device Connection    ${DEVICE}

Test Modem Handover Success Rate
    [Documentation]    Test the handover success rate of the modem.
    Setup Device Connection    ${DEVICE}
    ${handover_success_rate}    Evaluate    ${device_keywords.Execute Command(${DEVICE}, "get_handover_success_rate")}
    Should Be Greater Than    ${handover_success_rate}    95
    Teardown Device Connection    ${DEVICE}

Test Modem Signal Quality
    [Documentation]    Test the signal quality of the modem.
    Setup Device Connection    ${DEVICE}
    ${signal_quality}    Evaluate    ${device_keywords.Execute Command(${DEVICE}, "get_signal_quality")}
    Should Contain    ${signal_quality["SNR"]}    20
    Should Contain    ${signal_quality["BER"]}    0.0001
    Teardown Device Connection    ${DEVICE}
