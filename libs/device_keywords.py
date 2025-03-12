from SSHLibrary import SSHLibrary
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configs')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from device_config import DEVICE_CONFIG
from simulator import ModemSimulator, RANSimulator

ssh = SSHLibrary()
ran_simulator = RANSimulator()
modem_simulator = ModemSimulator(ran_simulator)

logging.basicConfig(level=logging.DEBUG)

def setup_device_connection(device_type):
    try:
        if DEVICE_CONFIG["simulation_mode"]:
            logging.debug(f"Setting up connection for {device_type} (mocked)")
            return
        logging.debug(f"Setting up connection for {device_type}")
        ssh.open_connection(DEVICE_CONFIG[device_type]["ip"], port=DEVICE_CONFIG[device_type]["port"])
        ssh.login(DEVICE_CONFIG[device_type]["username"], DEVICE_CONFIG[device_type]["password"])
    except Exception as e:
        logging.error(f"Failed to setup device connection for {device_type}: {e}")

def execute_command(device_type, command, *args):
    try:
        if DEVICE_CONFIG["simulation_mode"]:
            logging.debug(f"Executing command on {device_type} (mocked): {command} with args {args}")
            if command == "check_band_support":
                result = modem_simulator.check_band_support(args[0])
                logging.debug(f"Result for check_band_support: {result}")
                return result
            elif command == "get_signal_strength":
                result = modem_simulator.get_signal_strength(args[0])
                logging.debug(f"Result for get_signal_strength: {result}")
                return result
            elif command == "get_modulation_schemes":
                result = modem_simulator.get_modulation_schemes()
                logging.debug(f"Result for get_modulation_schemes: {result}")
                return result
            elif command == "get_throughput":
                result = modem_simulator.get_throughput()
                logging.debug(f"Result for get_throughput: {result}")
                return result
            elif command == "get_latency":
                result = modem_simulator.get_latency()
                logging.debug(f"Result for get_latency: {result}")
                return result
            elif command == "get_handover_success_rate":
                result = modem_simulator.get_handover_success_rate()
                logging.debug(f"Result for get_handover_success_rate: {result}")
                return result
            elif command == "get_signal_quality":
                result = modem_simulator.get_signal_quality()
                logging.debug(f"Result for get_signal_quality: {result}")
                return result
            elif command == "check_carrier_aggregation_support":
                result = modem_simulator.check_carrier_aggregation_support()
                logging.debug(f"Result for check_carrier_aggregation_support: {result}")
                return result
            elif command == "check_beamforming_support":
                result = modem_simulator.check_beamforming_support()
                logging.debug(f"Result for check_beamforming_support: {result}")
                return result
            elif command == "check_mimo_support":
                result = modem_simulator.check_mimo_support()
                logging.debug(f"Result for check_mimo_support: {result}")
                return result
            elif command == "check_nr_carrier_aggregation_support":
                result = modem_simulator.check_nr_carrier_aggregation_support()
                logging.debug(f"Result for check_nr_carrier_aggregation_support: {result}")
                return result
            elif command == "get_lte_bandwidth":
                result = modem_simulator.get_lte_bandwidth()
                logging.debug(f"Result for get_lte_bandwidth: {result}")
                return result
            elif command == "get_lte_ul_dl_ratio":
                result = modem_simulator.get_lte_ul_dl_ratio()
                logging.debug(f"Result for get_lte_ul_dl_ratio: {result}")
                return result
            elif command == "get_nr_bandwidth":
                result = modem_simulator.get_nr_bandwidth()
                logging.debug(f"Result for get_nr_bandwidth: {result}")
                return result
            elif command == "get_nr_ul_dl_ratio":
                result = modem_simulator.get_nr_ul_dl_ratio()
                logging.debug(f"Result for get_nr_ul_dl_ratio: {result}")
                return result
            elif command == "check_nr_massive_mimo_support":
                result = modem_simulator.check_nr_massive_mimo_support()
                logging.debug(f"Result for check_nr_massive_mimo_support: {result}")
                return result
            elif command == "check_lte_harq_support":
                result = modem_simulator.check_lte_harq_support()
                logging.debug(f"Result for check_lte_harq_support: {result}")
                return result
            elif command == "check_lte_power_control_support":
                result = modem_simulator.check_lte_power_control_support()
                logging.debug(f"Result for check_lte_power_control_support: {result}")
                return result
            elif command == "check_nr_harq_support":
                result = modem_simulator.check_nr_harq_support()
                logging.debug(f"Result for check_nr_harq_support: {result}")
                return result
            elif command == "check_nr_power_control_support":
                result = modem_simulator.check_nr_power_control_support()
                logging.debug(f"Result for check_nr_power_control_support: {result}")
                return result
            elif command == "check_nr_network_slicing_support":
                result = modem_simulator.check_nr_network_slicing_support()
                logging.debug(f"Result for check_nr_network_slicing_support: {result}")
                return result
        logging.debug(f"Executing command on {device_type}: {command} with args {args}")
        result = ssh.execute_command(command)
        logging.debug(f"Result for {command}: {result}")
        return result
    except Exception as e:
        logging.error(f"Failed to execute command on {device_type}: {e}")

def teardown_device_connection(device_type):
    try:
        if DEVICE_CONFIG["simulation_mode"]:
            logging.debug(f"Tearing down connection for {device_type} (mocked)")
            return
        logging.debug(f"Tearing down connection for {device_type}")
        ssh.close_connection()
    except Exception as e:
        logging.error(f"Failed to teardown device connection for {device_type}: {e}")