#!/usr/bin/env python3
import serial
import time
import string

if __name__ == '__main__':
    ser = serial.Serial('/dev/rfcomm0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        ser.write(str.encode('LED_ON\r\n'))
        time.sleep(5)
        ser.write(str.encode('LED_OFF\r\n'))
        time.sleep(5)
