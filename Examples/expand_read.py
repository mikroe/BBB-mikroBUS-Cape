import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)  # /dev/spidev1.0

#Check the states
spi.readbytes(len) = read
print read