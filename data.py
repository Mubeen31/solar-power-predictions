import serial
import csv
from datetime import datetime
import time

# copy the port from your Arduino editor
PORT = 'COM4'
ser = serial.Serial(PORT, 9600)

while True:
    message = ser.readline()
    data = message.strip().decode()
    split_string = data.split(',')  # split string
    voltage = split_string[0]  # convert first part of string into float
    current = split_string[1]  # convert second part of string into float
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("sensors_data.csv", "a", newline = '\n') as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, voltage, current])
        print(dt_string, voltage, current)
