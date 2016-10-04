#import libs for use
import time
import math
from bbio import *
import Adafruit_BMP.BMP085 as BMP085
import os
import urllib2
# initialize the sensor and read data 
SPI0.begin()
sensor = BMP085.BMP085() 
def analog_read(channel):
r = SPI0.transfer( [ 1 , ((8 + channel) << 4) , 0] )
#transfer data to adc. 
adc_out = ((r[1]&3) << 8) + r[2]
return adc_out
#indicate if it is day or night 
while True:
if analog_read(0) > 100:
dayandnight = 'day'
else:
dayandnight = 'night'

#read data from sensors.
moist = analog_read(1) 
pressure= sensor.read_pressure()
temp=sensor.read_temperature()
#print data
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()) 
print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature()) 
print "dayandnight = "
print dayandnight 
print "moisture = "
print moist
print " \n"
