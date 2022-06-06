#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP
import sys
import Adafruit_DHT.read_retry as DHT
import time


time.sleep(1)
Device=22
Pin=22

_, temp_dht = Adafruit_DHT.read_retry(Device, Pin)

try:
    bmp = BMP.BMP085()
    temp = temp_dht+ bmp.read_temperature()
except Exception as e:
    temp = temp_dht
    
if temp is not None:
    print('Temperature={0:0.1f}*C '.format(temp))
else:
    print('Fail to read. Try again!')
