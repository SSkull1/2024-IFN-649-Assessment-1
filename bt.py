import serial
import time
import string


#reading and writing data from and to arduino serially
#rfcomm0_> this could be different
ser = serial.Serial("/dev/rfcomm0",9600,timeout=1)
ser.reset_input_buffer()
ser.write(str.encode('Start\r\n'))

while True:
	#if ser.in_waiting>0:
		rawserial = ser.readline()
		print("Test again")
		cookedserial=rawserial.decode('utf-8').strip('\r\n')
		print(cookedserial)
	
