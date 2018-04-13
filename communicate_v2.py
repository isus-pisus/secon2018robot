import numpy as np
import serial, time
from lcd import lcd
from ir_decoder import get_ir_code

ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = None
ser.port = '/dev/ttyACM0'

""" Destination array is in the format
    destination_array = np.array([
        [
            all commands for the left side of the field ie. a '0'
        ],
        [
            all commands for the right side of the field ie. a '1'
        ]
    ])
"""

destination_A = np.array([
    [
        ['LEFT', 70],
        ['STOP', 0],
        ['FORWARD', 1000],
        ['STOP', 0],
        # ['DOSTUFF', 0],
        ['BACK', 1000],
        ['STOP', 0],
        ['RIGHT', 700],
        ['STOP', 0]
    ],
    [
        ['RIGHT', 700],
        ['STOP', 0],
        ['FORWARD', 1000],
        ['STOP', 0],
        # ['DOSTUFF', 0],
        ['BACK', 1000],
        ['STOP', 0],
        ['LEFT', 700],
        ['STOP', 0]
    ]
])

destination_B = np.array([
    [
        ['FORWARD', 50],
        ['STOP', 0],
        ['LEFT', 700],
        ['STOP', 0],
        ['FORWARD', 750],
        ['STOP', 0],
        ['BACK', 750],
        ['STOP', 0],
        ['RIGHT', 500],
        ['STOP', 0]

    ],
    [
        ['FORWARD', 500],
        ['STOP', 0],
        ['RIGHT', 700],
        ['STOP', 0],
        ['FORWARD', 750],
        ['STOP', 0],
        ['BACK', 750],
        ['STOP', 0],
        ['LEFT', 500],
        ['STOP', 0]
    ]
])

destination_C = np.array([
    [
        ['FORWARD', 10],
        ['STOP', 0],
        # ['PICKUP', 700],
        ['FORWARD', 2000],
        ['STOP', 0],
        # ['TURNFLAG', 0],
        ['BACK', 2000],
        ['LEFT', 0],
        ['LEFT', 0],
        ['STOP', 0],
        ['FORWARD', 10000],
        ['STOP', 0],
        ['RIGHT', 0],
        ['STOP', 0],
        ['FORWARD', 700],
        ['STOP', 0],

    ],
    [
        ['FORWARD', 100],
        ['STOP', 0],
        # ['PICKUP', 700],
        ['FORWARD', 2000],
        ['STOP', 0],
        # ['TURNFLAG', 0],
        ['BACK', 2000],
        ['LEFT', 0],
        ['LEFT', 0],
        ['STOP', 0],
        ['FORWARD', 10000],
        ['STOP', 0],
        ['LEFT', 0],
        ['STOP', 0],
        ['FORWARD', 700],
        ['STOP', 0],
    ]
])


def arduino_msg(x):
    ser.write((x[0]+","+str(x[1])).encode())


def get_direction():
    return [0, 1, 0]


def join_arrays(x):
    final_command = np.concatenate(
        (destination_A[x[0]], destination_B[x[1]], destination_C[x[2]]))
    return final_command


def check_for_valid_ir_signal():
    while get_ir_code() == [1, 1, 1, 1, 1, 1, 1, 1]:
        get_ir_code()

if __name__ == '__main__':
    check_for_valid_ir_signal()
    final_destination = get_ir_code()

    lcd.write_string(u'Destination')
    lcd.cursor_pos = (1, 0)
    lcd.write_string("".join(str(e) for e in final_destination))

    final_array_with_commands = join_arrays(final_destination[5:])
    cmd = iter(final_array_with_commands)

    ser.open()
    command = next(cmd)
    arduino_msg(command)

    while 1:
        ser.flushInput()
        is_finished = ser.read().decode('utf-8')
        if is_finished == '1':
            print('Done!')
            try:
                command = next(cmd)
            except StopIteration:
                print('All done')
                break
            else:
                print(command)
                arduino_msg(command)
        ser.flushOutput()
    ser.close()
