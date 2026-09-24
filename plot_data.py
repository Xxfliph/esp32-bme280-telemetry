import matplotlib.pyplot as plt
import csv
from datetime import datetime



time = []
temp = []
press = []
humid = []

with open("data.txt", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        time.append(row[0])
        temp.append(float(row[1]))
        humid.append(float(row[2]))
        press.append(float(row[3]))


time = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") for date in time]


fig, axes = plt.subplots(3, 1)

axes[0].plot(time, temp)
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Temperature")
axes[0].set_title("Temperature vs Time")

axes[1].plot(time, humid)
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Humidity")
axes[1].set_title("Humidity vs Time")

axes[2].plot(time, press)
axes[2].set_xlabel("Time")
axes[2].set_ylabel("Pressure")
axes[2].set_title("Pressure vs Time")

fig.suptitle("BME280 Sensor Data")


plt.tight_layout()
plt.show()

