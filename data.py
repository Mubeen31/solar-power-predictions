import serial
import csv
from datetime import datetime

# copy the port from your Arduino editor
PORT = 'COM3'
ser = serial.Serial(PORT, 9600)

while True:
    message = ser.readline()
    data = message.strip().decode()
    split_string = data.split(',')  # split string
    voltage = float(split_string[0])  # convert first part of string into float
    current = float(split_string[1])  # convert tenth part of string into float
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("sensors_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, voltage, current])
        print(dt_string, voltage, current)
