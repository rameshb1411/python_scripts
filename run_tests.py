import subprocess
import sys
import os
from datetime import datetime
import logging

logging.basicConfig(filename='test_run.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_variables = {
    'MODEM_IP': os.getenv('MODEM_IP', '192.168.1.1'),
    'MODEM_PORT': os.getenv('MODEM_PORT', '22'),
    'MODEM_USERNAME': os.getenv('MODEM_USERNAME', 'admin'),
    'MODEM_PASSWORD': os.getenv('MODEM_PASSWORD', 'secret'),
    'NETWORK_DEVICE_IP': os.getenv('NETWORK_DEVICE_IP', '192.168.1.2'),
    'NETWORK_DEVICE_PORT': os.getenv('NETWORK_DEVICE_PORT', '22'),
    'NETWORK_DEVICE_USERNAME': os.getenv('NETWORK_DEVICE_USERNAME', 'admin'),
    'NETWORK_DEVICE_PASSWORD': os.getenv('NETWORK_DEVICE_PASSWORD', 'secret'),
    'DUMMY_DEVICE_IP': os.getenv('DUMMY_DEVICE_IP', '192.168.1.3'),
    'DUMMY_DEVICE_PORT': os.getenv('DUMMY_DEVICE_PORT', '22'),
    'DUMMY_DEVICE_USERNAME': os.getenv('DUMMY_DEVICE_USERNAME', 'admin'),
    'DUMMY_DEVICE_PASSWORD': os.getenv('DUMMY_DEVICE_PASSWORD', 'secret'),
    'SIMULATION_MODE': os.getenv('SIMULATION_MODE', 'true')
}

for var, value in env_variables.items():
    os.environ[var] = value

def get_env_variable(var_name, default_value=None):
    value = os.environ.get(var_name, default_value)
    if value is None:
        logging.warning(f"Environment variable {var_name} not set. Using default value: {default_value}")
    return value

def is_package_installed(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'show', package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_packages():
    packages = [
        "robotframework",
        "robotframework-requests",
        "robotframework-sshlibrary",
        "robotframework-seleniumlibrary",
        "robotframework-seriallibrary"
    ]
    
    for package in packages:
        if not is_package_installed(package):
            logging.info(f"Installing package: {package}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError as e:
                logging.error(f"Error installing package {package}: {e}")
        else:
            logging.info(f"Package already installed: {package}")

def create_directories():
    directories = [
        "tests",
        "tests/modem",
        "tests/network_device",
        "tests/dummy_device",
        "resources",
        "results",
        "logs",
        "libs",
        "configs"
    ]
    
    for directory in directories:
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Created directory: {directory}")
            else:
                logging.info(f"Directory already exists: {directory}")
        except OSError as e:
            logging.error(f"Error creating directory {directory}: {e}")

def create_config():
    modem_ip = get_env_variable('MODEM_IP', '127.0.0.1')
    modem_port = int(get_env_variable('MODEM_PORT', 22))
    modem_username = get_env_variable('MODEM_USERNAME', 'admin')
    modem_password = get_env_variable('MODEM_PASSWORD', 'admin')

    network_device_ip = get_env_variable('NETWORK_DEVICE_IP', '127.0.0.1')
    network_device_port = int(get_env_variable('NETWORK_DEVICE_PORT', 22))
    network_device_username = get_env_variable('NETWORK_DEVICE_USERNAME', 'admin')
    network_device_password = get_env_variable('NETWORK_DEVICE_PASSWORD', 'admin')

    dummy_device_ip = get_env_variable('DUMMY_DEVICE_IP', 'dummy_ip')
    dummy_device_port = int(get_env_variable('DUMMY_DEVICE_PORT', 22))
    dummy_device_username = get_env_variable('DUMMY_DEVICE_USERNAME', 'dummy_user')
    dummy_device_password = get_env_variable('DUMMY_DEVICE_PASSWORD', 'dummy_pass')
    
    simulation_mode = get_env_variable('SIMULATION_MODE', 'true').lower() == 'true'

    config_content = f"""
DEVICE_CONFIG = {{
    "modem": {{
        "ip": "{modem_ip}",
        "port": {modem_port},
        "username": "{modem_username}",
        "password": "{modem_password}"
    }},
    "network_device": {{
        "ip": "{network_device_ip}",
        "port": {network_device_port},
        "username": "{network_device_username}",
        "password": "{network_device_password}"
    }},
    "dummy_device": {{
        "ip": "{dummy_device_ip}",
        "port": {dummy_device_port},
        "username": "{dummy_device_username}",
        "password": "{dummy_device_password}"
    }},
    "simulation_mode": {simulation_mode}
}}
"""
    config_path = os.path.join("configs", "device_config.py")
    
    try:
        with open(config_path, "w") as config_file:
            config_file.write(config_content)
            logging.info(f"Created config file: {config_path}")
        logging.info(f"Config created with modem IP: {modem_ip}, network device IP: {network_device_ip}, dummy device IP: {dummy_device_ip}")
    except IOError as e:
        logging.error(f"Error creating config file {config_path}: {e}")

def create_test_files():
    modem_tests = {
        "test_modem_connectivity.robot": "Test Modem Connectivity",
        "test_modem_reboot.robot": "Test Modem Reboot",
        "test_modem_firmware_version.robot": "Test Modem Firmware Version",
        "test_modem_network_configuration.robot": "Test Modem Network Configuration",
        "test_modem_speed.robot": "Test Modem Speed",
        "test_modem_port_status.robot": "Test Modem Port Status",
        "test_modem_factory_reset.robot": "Test Modem Factory Reset",
        "test_modem_wifi_configuration.robot": "Test Modem Wi-Fi Configuration",
        "test_modem_security_settings.robot": "Test Modem Security Settings",
        "test_modem_signal_strength.robot": "Test Modem Signal Strength",
        "test_modem_system_logs.robot": "Test Modem System Logs",
        "test_modem_configuration_backup.robot": "Test Modem Configuration Backup",
        "test_modem_configuration_restore.robot": "Test Modem Configuration Restore",
        "test_modem_software_update.robot": "Test Modem Software Update",
        "test_modem_timer_functionality.robot": "Test Modem Timer Functionality",
        "test_modem_bootloader.robot": "Test Modem Bootloader",
        "test_modem_driver_features.robot": "Test Modem Driver Features",
        "test_modem_rf.robot": "Test Modem RF Functionalities"
    }
    
    network_device_tests = {
        "test_network_device_connectivity.robot": "Test Network Device Connectivity",
        "test_network_device_reboot.robot": "Test Network Device Reboot",
        "test_network_device_firmware_version.robot": "Test Network Device Firmware Version",
        "test_network_device_network_configuration.robot": "Test Network Device Network Configuration",
        "test_network_device_speed.robot": "Test Network Device Speed",
        "test_network_device_port_status.robot": "Test Network Device Port Status",
        "test_network_device_factory_reset.robot": "Test Network Device Factory Reset",
        "test_network_device_wifi_configuration.robot": "Test Network Device Wi-Fi Configuration",
        "test_network_device_security_settings.robot": "Test Network Device Security Settings",
        "test_network_device_signal_strength.robot": "Test Network Device Signal Strength",
        "test_network_device_system_logs.robot": "Test Network Device System Logs",
        "test_network_device_configuration_backup.robot": "Test Network Device Configuration Backup",
        "test_network_device_configuration_restore.robot": "Test Network Device Configuration Restore",
        "test_network_device_software_update.robot": "Test Network Device Software Update",
        "test_network_device_timer_functionality.robot": "Test Network Device Timer Functionality",
        "test_network_device_bootloader.robot": "Test Network Device Bootloader",
        "test_network_device_driver_features.robot": "Test Network Device Driver Features"
    }
    
    dummy_device_tests = {
        "test_dummy_device_connectivity.robot": "Test Dummy Device Connectivity",
        "test_dummy_device_reboot.robot": "Test Dummy Device Reboot",
        "test_dummy_device_firmware_version.robot": "Test Dummy Device Firmware Version",
        "test_dummy_device_network_configuration.robot": "Test Dummy Device Network Configuration",
        "test_dummy_device_speed.robot": "Test Dummy Device Speed",
        "test_dummy_device_port_status.robot": "Test Dummy Device Port Status",
        "test_dummy_device_factory_reset.robot": "Test Dummy Device Factory Reset",
        "test_dummy_device_wifi_configuration.robot": "Test Dummy Device Wi-Fi Configuration",
        "test_dummy_device_security_settings.robot": "Test Dummy Device Security Settings",
        "test_dummy_device_signal_strength.robot": "Test Dummy Device Signal Strength",
        "test_dummy_device_system_logs.robot": "Test Dummy Device System Logs",
        "test_dummy_device_configuration_backup.robot": "Test Dummy Device Configuration Backup",
        "test_dummy_device_configuration_restore.robot": "Test Dummy Device Configuration Restore",
        "test_dummy_device_software_update.robot": "Test Dummy Device Software Update",
        "test_dummy_device_timer_functionality.robot": "Test Dummy Device Timer Functionality",
        "test_dummy_device_bootloader.robot": "Test Dummy Device Bootloader",
        "test_dummy_device_driver_features.robot": "Test Dummy Device Driver Features"
    }
    
    def write_test_files(test_cases, path):
        for file_name, test_case in test_cases.items():
            content = f"""
*** Settings ***
Library           ../../libs/device_keywords.py

*** Variables ***
${{DEVICE}}         {path.split('/')[-1]}

*** Test Cases ***
{test_case}
    [Documentation]    {test_case}.
    Setup Device Connection    ${{DEVICE}}
    Execute Command    ${{DEVICE}}    echo {test_case} successful
    Teardown Device Connection    ${{DEVICE}}
"""
            test_path = os.path.join("tests", path, file_name)
            try:
                with open(test_path, "w") as test_file:
                    test_file.write(content)
                    logging.info(f"Created test file: {test_path}")
            except IOError as e:
                logging.error(f"Error creating test file {test_path}: {e}")

    write_test_files(modem_tests, "modem")
    write_test_files(network_device_tests, "network_device")
    write_test_files(dummy_device_tests, "dummy_device")

def create_libs():
    libs_content = """
from SSHLibrary import SSHLibrary
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configs')))
from device_config import DEVICE_CONFIG
from simulator import ModemSimulator, RANSimulator

ssh = SSHLibrary()
ran_simulator = RANSimulator()
modem_simulator = ModemSimulator(ran_simulator)

def setup_device_connection(device_type):
    try:
        if DEVICE_CONFIG["simulation_mode"]:
            print(f"Setting up connection for {device_type} (mocked)")
            return
        print(f"Setting up connection for {device_type}")
        ssh.open_connection(DEVICE_CONFIG[device_type]["ip"], port=DEVICE_CONFIG[device_type]["port"])
        ssh.login(DEVICE_CONFIG[device_type]["username"], DEVICE_CONFIG[device_type]["password"])
    except Exception as e:
        print(f"Failed to setup device connection for {device_type}: {e}")

def execute_command(device_type, command, *args):
    try:
        if DEVICE_CONFIG["simulation_mode"]:
            print(f"Executing command on {device_type} (mocked): {command}")
            if command == "check_band_support":
                return modem_simulator.check_band_support(args[0])
            elif command == "get_signal_strength":
                return modem_simulator.get_signal_strength(args[0])
            elif command == "get_modulation_schemes":
                return modem_simulator.get_modulation_schemes()
        print(f"Executing command on {device_type}: {command}")
        return ssh.execute_command(command)
    except Exception as e:
        print(f"Failed to execute command on {device_type}: {e}")

def teardown_device_connection(device_type):
    try:
        if DEVICE_CONFIG["simulation_mode"]:
            print(f"Tearing down connection for {device_type} (mocked)")
            return
        print(f"Tearing down connection for {device_type}")
        ssh.close_connection()
    except Exception as e:
        print(f"Failed to teardown device connection for {device_type}: {e}")
"""
    
    libs_path = os.path.join("libs", "device_keywords.py")
    
    try:
        with open(libs_path, "w") as libs_file:
            libs_file.write(libs_content)
            logging.info(f"Created library file: {libs_path}")
    except IOError as e:
        logging.error(f"Error creating library file {libs_path}: {e}")

def run_tests():
    logging.info("Running tests...")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join([os.path.abspath("configs"), os.path.abspath("libs"), os.path.abspath('.'), env.get("PYTHONPATH", "")])
    logging.info(f"PYTHONPATH is set to: {env['PYTHONPATH']}")
    try:
        subprocess.run(["robot", "--outputdir", "results", "tests"], check=True, env=env)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running tests: {e}")

if __name__ == "__main__":
    logging.info(f"Script started at: {datetime.now()}")
    try:
        install_packages()
        create_directories()
        create_config()
        create_test_files()
        create_libs()
        run_tests()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    logging.info(f"Script finished at: {datetime.now()}")