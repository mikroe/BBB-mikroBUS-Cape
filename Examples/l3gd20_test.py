import l3gd20, time

acc = l3gd20.L3GD20(1, 0x6B)

while(1):
	X = acc.readRawX()
	Y = acc.readRawY()
	Z = acc.readRawZ()
	print('X:' + str(X) + ' Y:' + str(Y) + ' Z:' + str(Z))
	#print(X, Y, Z)
	time.sleep(0.2)