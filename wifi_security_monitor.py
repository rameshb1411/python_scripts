import subprocess
import re
import time
import datetime

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
        return f"Error checking Wi-Fi security: {e}"

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
        intrusions.append(f"Error detecting intrusions: {e}")
    return intrusions

def log_security_status():
    """
    Log the Wi-Fi security status and any detected intrusions.
    """
    wifi_security = check_wifi_security_windows()
    intrusions = detect_intrusions()

    log_entry = f"{datetime.datetime.now()} - Wi-Fi Security: {wifi_security}\n"
    log_entry += "Detected Intrusions:\n"
    for intrusion in intrusions:
        log_entry += f"  {intrusion}\n"
    
    with open("wifi_security_log.txt", "a") as log_file:
        log_file.write(log_entry)
    
    print(log_entry)

def monitor_security(duration_minutes=15):
    """
    Monitor Wi-Fi security and detect intrusions for the specified duration.
    
    Args:
        duration_minutes (int): The duration to monitor in minutes.
    """
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        log_security_status()
        time.sleep(60)

if __name__ == "__main__":
    monitor_security(15)