import serial
import time

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

while True:
    i = input("command: ")
    ser.write(i.encode())
