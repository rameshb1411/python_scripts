import subprocess
import sys

def install_packages():
    packages = [
        "robotframework",
        "robotframework-requests",
        "robotframework-sshlibrary",
        "robotframework-seleniumlibrary",
        "robotframework-seriallibrary"
    ]
    
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()