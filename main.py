import time
from motor import browseMotor, startMotor, stopMotor, readData
from login import login
from dbhandler import DBHandler

if __name__ == "__main__":
    db = DBHandler('192.168.10.10', '5AHIT', '5ahiT', 'mtk-i40')
    token = login("5AHIT", "5ahiT")

    for i in range (0, 100):
        type = "\"Dpublic\".cosinus"
        data = readData(token, type)
        db.insert_data(data['result'], type, "gruber")
    db.close_connection()

