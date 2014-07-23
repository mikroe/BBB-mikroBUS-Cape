import l3gd20, spidev, time

spi = spidev.SpiDev()
spi.open(1,1)  # /dev/spidev1.1

acc = l3gd20.L3GD20(1, 0x6B)

columns = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
buffer = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

def clearMatrix():
	for i in range(0,8):
		buffer[i] = 0x00
		spi.xfer([columns[i], buffer[i]])

def setPixel(x, y):
	if (x in range(0,8)) and (y in range(0,8)):
		x += 8
		x %= 8
		buffer[y] = buffer[y] | (1 << x)
		for i in range(0,8):
				spi.xfer([columns[i], buffer[i]])

def setSquare(x, y):
	setPixel(x-1, y-1)
	setPixel(x, y-1)
	setPixel(x-1, y)
	setPixel(x, y)

while(1):
	
	X = acc.readRawX()
	Y = acc.readRawY()
	Z = acc.readRawZ()

	# linear mapping, from 0-1023 to 0-15
	x_map = int((float(X)/float(1023))*15)
	y_map = int((float(Y)/float(1023))*15)
	z_map = int((float(Z)/float(1023))*15)
	
	# from 0-15 to -7,7
	if x_map > 7:
		x_map = x_map-15
	if y_map > 7:
		y_map = y_map-15
	if x_map > 7:
		z_map = z_map-15

	# just 180 degree
	if abs(x_map)<4 and abs(y_map)<4:
		buffer = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		setSquare(-y_map+4, x_map+4)

		#print('X:' + str(x_map) + ' Y:' + str(y_map) + ' Z:' + str(z_map))
		time.sleep(0.1)
	
	"""
	for x in range(0, 8):
		for y in range(0, 8):
			clearMatrix()
			setPixel(x, y)
			time.sleep(0.05)
	"""
