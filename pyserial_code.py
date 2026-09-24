import serial
from datetime import datetime

ser = serial.Serial("COM3", 115200)

with open("data.txt", "a") as file:
    while True:
        data = ser.readline().decode().strip()
        sepdata = data.split(",")
        temp = sepdata[0]
        humid = sepdata[1]
        pres = sepdata[2]

        timestamp = datetime.now()
        print(temp)
        print(humid)
        print(pres)
        file.write(f"{timestamp},{data}\n")

