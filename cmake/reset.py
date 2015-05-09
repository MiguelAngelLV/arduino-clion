#!/usr/bin/env python
import serial, sys
from time import sleep

print ("Reset arduino in ");
print (sys.argv[1]);
print("\n");

serialPort = sys.argv[1]
ser = serial.Serial(
    port=serialPort,
    baudrate=1200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()
ser.close() # always close port
sleep(2)
