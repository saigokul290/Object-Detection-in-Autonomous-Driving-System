import serial
import time

ser = serial.Serial(
   'COM11',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

def Send(msg):
    ser.write(str.encode(msg))
