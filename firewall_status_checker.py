import subprocess

def check_firewall_status_windows():
    """
    Check the status of all firewall profiles on Windows and provide detailed logs.

    Returns:
        dict: A dictionary containing the status of each firewall profile.
    """
    try:
        # Run the netsh command to show all firewall profiles
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error executing netsh command: {result.stderr}")
            return None

        # Parse the output to get the status of each profile
        profiles = {}
        current_profile = None

        for line in result.stdout.splitlines():
            if "Profile" in line:
                current_profile = line.split()[0]
                profiles[current_profile] = {"State": "Unknown", "Details": []}
            elif current_profile:
                if "State" in line:
                    state_match = re.search(r"State\s*:\s*(\w+)", line)
                    if state_match:
                        profiles[current_profile]["State"] = state_match.group(1)
                profiles[current_profile]["Details"].append(line.strip())

        # Log details of each profile
        for profile, info in profiles.items():
            print(f"{profile} Profile:")
            for detail in info["Details"]:
                print(f"  {detail}")
            print()

        return profiles

    except Exception as e:
        print(f"Error checking firewall status: {e}")
        return None

if __name__ == "__main__":
    firewall_status = check_firewall_status_windows()
    if firewall_status:
        for profile, info in firewall_status.items():
            print(f"{profile} Profile - State: {info['State']}")