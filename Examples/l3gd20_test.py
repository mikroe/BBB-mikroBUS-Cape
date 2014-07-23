#!/usr/bin/python

import l3gd20, time

# ===========================================================
# Example for the Gyro click
# After the installation of py-spidev and all the python tools
# This example will just print the X Y Z calues of the Gyro click
#
# NOTE: This progam has an endless loop.
# ===========================================================


acc = l3gd20.L3GD20(1, 0x6B)

while(1):
	X = acc.readRawX()
	Y = acc.readRawY()
	Z = acc.readRawZ()
	print('X:' + str(X) + ' Y:' + str(Y) + ' Z:' + str(Z))
	#print(X, Y, Z)
	time.sleep(0.25)
