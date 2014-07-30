import spidev
import time

read = 0

spi = spidev.SpiDev()
spi.open(1,0)  # /dev/spidev1.0

#Check the states
def read():
	spi.readbytes(len)
	print len
	
read()