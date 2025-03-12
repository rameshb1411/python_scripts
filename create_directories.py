import os

def create_directories():
    directories = [
        "tests",
        "resources",
        "results",
        "logs",
        "libs",
        "configs"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

if __name__ == "__main__":
    create_directories()