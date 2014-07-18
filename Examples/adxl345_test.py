import adxl345, time

acc = adxl345.ADXL345(1, 0x1D)

while(1):
	sx = sy = sz = 0
	avgX = avgY = avgZ = 0
	
	# average accelerometer reading over last 16 samples
	for i in range(0,16):
		sx += acc.readRawX()
		sy += acc.readRawY()
		sz += acc.readRawZ()
		time.sleep(0.01)
	
	# average
	avgX = sx >> 4
	avgY = sy >> 4
	avgZ = sz >> 4
	
	print('X:' + str(avgX) + ' Y:' + str(avgY) + ' Z:' + str(avgZ))
	time.sleep(0.2)
