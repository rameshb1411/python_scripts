import hashlib
import os
import base64
from cryptography.fernet import Fernet
import socket
import subprocess
import re

# Password Hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# File Encryption
def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(file_path, 'wb') as file:
        file.write(decrypted)

# Basic Network Security Check
def check_open_ports(host, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

# Firewall Configuration Check for Windows
def check_firewall_status_windows():
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error executing netsh command: {result.stderr}")
            return None
        profiles = {}
        current_profile = None
        for line in result.stdout.splitlines():
            if "Profile" in line:
                current_profile = line.split()[0]
                profiles[current_profile] = {"State": "Unknown", "Details": []}
            elif current_profile:
                profiles[current_profile]["Details"].append(line.strip())
                if "State" in line:
                    state_match = re.search(r"State\s*:\s*(\w+)", line)
                    if state_match:
                        profiles[current_profile]["State"] = state_match.group(1)
        for profile, info in profiles.items():
            print(f"{profile} Profile:")
            for detail in info["Details"]:
                print(f"  {detail}")
            print()
        return profiles
    except Exception as e:
        print(f"Error checking firewall status: {e}")
        return None

# Wi-Fi Security Check for Windows
def check_wifi_security_windows():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        security_match = re.search(r'Authentication\s*:\s*(.*)', result.stdout)
        if security_match:
            return security_match.group(1).strip()
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error checking Wi-Fi security: {e}")
        return "Error"

# Intrusion Detection (Basic)
def detect_intrusions():
    intrusions = []
    try:
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
        connections = result.stdout.split('\n')
        for connection in connections:
            if "ESTABLISHED" in connection and not re.search(r'127.0.0.1|::1', connection):
                intrusions.append(connection)
    except Exception as e:
        print(f"Error detecting intrusions: {e}")
    return intrusions

# Enable Firewall (if Disabled) using PowerShell
def enable_firewall_windows():
    try:
        result = subprocess.run(['powershell', '-Command', 'Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Firewall enabled successfully.")
        else:
            print(f"Error enabling firewall: {result.stderr}")
    except Exception as e:
        print(f"Error enabling firewall: {e}")

if __name__ == "__main__":
    password = "my_secure_password"
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")

    key = generate_key()
    print(f"Encryption Key: {key.decode()}")

    file_path = "test.txt"
    with open(file_path, 'w') as file:
        file.write("This is a test file.")
    
    encrypt_file(file_path, key)
    print(f"File '{file_path}' encrypted.")

    decrypt_file(file_path, key)
    print(f"File '{file_path}' decrypted.")

    host = "127.0.0.1"
    ports = [22, 80, 443]
    open_ports = check_open_ports(host, ports)
    print(f"Open Ports on {host}: {open_ports}")

    firewall_status = check_firewall_status_windows()
    if firewall_status:
        for profile, info in firewall_status.items():
            print(f"{profile} Profile - State: {info['State']}")

    wifi_security = check_wifi_security_windows()
    print(f"Wi-Fi Security: {wifi_security}")

    intrusions = detect_intrusions()
    print(f"Detected Intrusions: {intrusions}")