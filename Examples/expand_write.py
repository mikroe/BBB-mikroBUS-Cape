#!/usr/bin/python


import spidev
import time

spi = spidev.SpiDev()
spi.open(1,0)  # /dev/spidev1.0


#Turns ports on and off in an infinite loop
while True:
	spi.xfer([0,0,0])		#Turns all ports low
	time.sleep(10)
	spi.xfer([1,255,254])	#Turns all ports high
	time.sleep(10)