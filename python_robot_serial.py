#!/usr/bin/env python
import serial
from serial import SerialException
import time
ser = serial.Serial()
ser.port = "/dev/ttyACM1"
ser.baudrate = 9600 #Define bause rate speed, set same on arduino
try:
    
    ser.open()
    ser.flushInput() #flush input buffer, discarding all its contents
    ser.write("Move Forward".encode())
    ser.write("Move Reverse".encode())
    ser.flushOutput()#flush output buffer, aborting current output
    ser.close()

except SerialException as e:
    print(str(e))
