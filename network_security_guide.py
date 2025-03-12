import hashlib
import os
import base64
from cryptography.fernet import Fernet
import socket
import subprocess
import re


# Password Hashing
def hash_password(password):
    """
    Hash a password using SHA-256.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


# File Encryption
def generate_key():
    """
    Generate a key for encryption.
    
    Returns:
        bytes: The generated key.
    """
    return Fernet.generate_key()


def encrypt_file(file_path, key):
    """
    Encrypt a file using the given key.
    
    Args:
        file_path (str): The path to the file to encrypt.
        key (bytes): The encryption key.
    """
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted)


def decrypt_file(file_path, key):
    """
    Decrypt a file using the given key.
    
    Args:
        file_path (str): The path to the file to decrypt.
        key (bytes): The encryption key.
    """
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(file_path, 'wb') as file:
        file.write(decrypted)


# Basic Network Security Check
def check_open_ports(host, ports):
    """
    Check for open ports on a given host.
    
    Args:
        host (str): The host to check.
        ports (list): The list of ports to check.
    
    Returns:
        list: The list of open ports.
    """
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
    """
    Check if the firewall is enabled and configured correctly on Windows.
    
    Returns:
        bool: True if the firewall is enabled, False otherwise.
    """
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True)
        return 'State ON' in result.stdout
    except Exception as e:
        print(f"Error checking firewall status: {e}")
        return False


# Wi-Fi Security Check for Windows
def check_wifi_security_windows():
    """
    Check the security of the connected Wi-Fi network on Windows.
    
    Returns:
        str: The security type of the Wi-Fi network.
    """
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
    """
    Detect potential intrusions based on unusual network activity.
    
    Returns:
        list: The list of detected intrusions.
    """
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


# Enable Firewall (if Disabled)
def enable_firewall_windows():
    """
    Enable the firewall on Windows if it is disabled.
    """
    try:
        subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'on'], check=True)
        print("Firewall enabled successfully.")
    except Exception as e:
        print(f"Error enabling firewall: {e}")


if __name__ == "__main__":
    # Example usage of password hashing
    password = "my_secure_password"
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")

    # Example usage of file encryption
    key = generate_key()
    print(f"Encryption Key: {key.decode()}")

    file_path = "test.txt"
    with open(file_path, 'w') as file:
        file.write("This is a test file.")
    
    encrypt_file(file_path, key)
    print(f"File '{file_path}' encrypted.")

    decrypt_file(file_path, key)
    print(f"File '{file_path}' decrypted.")

    # Example usage of network security check
    host = "127.0.0.1"
    ports = [22, 80, 443]
    open_ports = check_open_ports(host, ports)
    print(f"Open Ports on {host}: {open_ports}")

    # Check firewall status on Windows
    firewall_status = check_firewall_status_windows()
    print(f"Firewall Status: {'Enabled' if firewall_status else 'Disabled'}")

    if not firewall_status:
        enable_firewall_windows()

    # Check Wi-Fi security on Windows
    wifi_security = check_wifi_security_windows()
    print(f"Wi-Fi Security: {wifi_security}")

    # Detect intrusions
    intrusions = detect_intrusions()
    print(f"Detected Intrusions: {intrusions}")