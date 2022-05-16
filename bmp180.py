#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085

#bmp = BMP085.BMP085(busnum=2) # for Beaglebone
bmp = BMP085.BMP085(busnum=1) # for Raspberry pi

print('T = {0:0.2f} *C'.format(bmp.read_temperature()))
print('P = {0:0.2f} Pa'.format(bmp.read_pressure()))
print('C.L. P = {0:0.2f} Pa'.format(bmp.read_sealevel_pressure()))
print('Altitude = {0:0.2f} m'.format(bmp.read_altitude()))
