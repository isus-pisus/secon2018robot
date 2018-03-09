import time, os
import numpy as np
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = 10
ser.port = '/dev/ttyACM0'

destination_A = np.array([
    [
        ['FORWARD', 1000],
        ['RIGHT', 700],
        ['STOP', 0],
        ['LEFT', 500],
        ['STOP', 0]
    ],
    [
        ['FORWARD', 5000],
        ['LEFT', 700],
        ['STOP', 0],
        ['RIGHT', 500],
        ['STOP', 0]

    ]
])

destination_B = np.array([
    [
        ['FORWARD', 5000],
        ['RIGHT', 700],
        ['STOP', 0],
        ['LEFT', 500],
        ['STOP', 0]
    ],
    [
        ['FORWARD', 5000],
        ['LEFT', 700],
        ['STOP', 0],
        ['RIGHT', 500],
        ['STOP', 0]

    ]
])

def number_of_steps(distance):
    return distance / ONE_REVOLUTION * STEPS_PER_REVOLUTION

def arduino_msg(x):
    ser.write((x[0]+","+str(x[1])).encode())
    # ser.write((x[0], x[1]).encode())

def get_direction():
    return [0, 1, 1]


def join_arrays(x):
    final_command = np.concatenate((destination_A[x[0]], destination_B[x[0]]), out=None)
    return final_command

cmd = iter(join_arrays(get_direction()))

if __name__ == '__main__':
    ser.open()
    command = next(cmd)
    print(command)
    arduino_msg(command)

    # print('sent')
    while 1:
        ser.flushInput()
        is_finished = ser.read().decode('utf-8')
        print('getting ', is_finished)
        if is_finished == '1':
            command = next(cmd)
            print(command)
            arduino_msg(command)
        ser.flushOutput()
    ser.close()
