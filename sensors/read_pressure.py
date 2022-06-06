#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085
import time


time.sleep(1)
bmp = BMP085.BMP085()

print('P = {0:0.2f} Pa'.format(bmp.read_pressure()))
print('C.L. P = {0:0.2f} Pa'.format(bmp.read_sealevel_pressure()))
