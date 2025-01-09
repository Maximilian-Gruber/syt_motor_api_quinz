import time
from motor import browseMotor, startMotor, stopMotor
from login import login

if __name__ == "__main__":
    token = login("5AHIT", "5ahiT")
    print(browseMotor(token))
    startMotor(token)
    time.sleep(5)
    stopMotor(token)
