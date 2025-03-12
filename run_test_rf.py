import os

def run_robot_tests():
    os.system("robot tests/modem/test_common_functionalities.robot")
    os.system("robot tests/modem/test_lte_functionalities.robot")
    os.system("robot tests/modem/test_5g_functionalities.robot")

if __name__ == "__main__":
    run_robot_tests()