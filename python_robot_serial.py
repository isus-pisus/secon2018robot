#!/usr/bin/env python
import serial
from serial import SerialException
import time

FORWARD = 'Move Forward'
REVESRE = 'Move Back'
LEFT = 'Move Left'
RIGHT = 'Move Right'
STOP = 'Stop'

ONE_REVOULTION = 16
STEPS_PER_REVOLUTION = 400

#The that will be used to control the stepper motors
nav_arduino = serial.Serial()  
nav_arduino.port = "COM8" 
# nav_arduino.port = "/dev/ttyACM1"
nav_arduino.baudrate = 9600

#distance -> cm
def number_of_steps(distance):
    return distance / ONE_REVOULTION * STEPS_PER_REVOLUTION 

def get_directions():
    return '111'

def arduino_msg(direction, distance=None):
    if steps is None: 
    	if direction == LEFT or direction == RIGHT:
    		#Add the number of steps it takes to turn 90 degrees
        	return direction + ',' + str(number_of_steps(0))
    	return direction
    return direction + ',' + str(number_of_steps(distance))

def main():
    directions = list(get_directions())
    
    try:   
        nav_arduino.open()
        nav_arduino.flushInput() #flush input buffer, discarding all its contents
        ############
        # Direction to A
        ############
        if directions[0] == '1':
            nav_arduino.write(arduino_msg(FORWARD, 23).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(STOP).encode());
        else:
            nav_arduino.write(arduino_msg(FORWARD, 23).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(STOP).encode());

        ############
        # Direction to B
        ############
        if directions[1] == '1':
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 163).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(STOP).encode());           
        else:
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 163).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(STOP).encode());           

        ############
        # Direction to C
        ############
        if directions[1] == '1':
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 163).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(STOP).encode());           
        else:
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(LEFT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 163).encode());
            nav_arduino.write(arduino_msg(RIGHT).encode());
            nav_arduino.write(arduino_msg(FORWARD, 37).encode());
            nav_arduino.write(arduino_msg(STOP).encode()); 

        
        nav_arduino.flushOutput()#flush output buffer, aborting current output
        nav_arduino.close()
    except SerialException as e:
        print((e))

if __name__ == '__main__':
    main()
