import os

def list_directory_contents(path):
    try:
        for root, dirs, files in os.walk(path):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
    except Exception as e:
        print(f"An error occurred: {e}")

list_directory_contents("C:\\Users\\Ramesh1\\PycharmProjects\\PythonProject2\\.venv\\ramesh\\robotfrmawork")