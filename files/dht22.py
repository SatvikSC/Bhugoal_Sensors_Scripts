#!/usr/bin/python

import sys
import Adafruit_DHT
import os

#PIN='P9_12' # for Beaglebone
PIN=4 # for Raspberry pi

while True:
	hum, tempC = Adafruit_DHT.read_retry(22, PIN)
	tempF = tempC * 9/5.0 + 32
	if hum is not None and tempC is not None:
	    print('TC={0:0.1f}*C TF={1:0.1f}F H={2:0.1f}%'.format(tempC,tempF,hum))
	else:
	    print('Fail to read. Try again!')
	    sys.exit(1)
