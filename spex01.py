#!usr/bin/env python
import serial
from datetime import datetime
import io

#1
ser=serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

#2
#print(ser.read(size=8))

#3
now = datetime.now()
print(now, ser.read(size=8))

#4
#while ser.isOpen():
#   datastring=ser.read(size=8)
#   print(datetime.utcnow().isoformat(), datastring)

#5
sio=io.TextIOWrapper(io.BufferedRWPair(ser,ser,1), encoding='ascii',newline='\r')
sio._CHUNK_SIZE=1

while ser.isOpen():
    datastring=sio.readline()
    print(datetime.utcnow().isoformat(), datastring)
