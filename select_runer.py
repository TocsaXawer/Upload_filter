import time
from sys import platform
import os
while True:
    if platform == "linux" or platform == "linux2":
        time.sleep(5)
        os.system("python3.9 se_tar.py")
        time.sleep(5)
        os.system("python3.9 checker.py")
    pass
    if platform == "win32":
        time.sleep(5)
        os.system("python se_tar.py")
        time.sleep(5)
        os.system("python checker.py")
    pass