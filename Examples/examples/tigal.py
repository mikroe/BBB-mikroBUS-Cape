import spidev
import time

spi = spidev.SpiDev()
spi.open(1,0)  # /dev/spidev1.0

matrix = [
		  [0x00, 0x80, 0x80, 0xFE, 0xFE, 0x80, 0x80, 0x00],  # T
		  [0x00, 0x00, 0x00, 0xFE, 0xFE, 0x00, 0x00, 0x00],  # I		  
		  [0x00, 0x4E, 0xCE, 0x8A, 0x82, 0xC6, 0x7C, 0x38],  # G
		  [0x00, 0x3E, 0x7E, 0xC8, 0xC8, 0x7E, 0x3E, 0x00],  # A		  
		  [0x00, 0x02, 0x02, 0x02, 0x02, 0xFE, 0xFE, 0x00],  # L		  
		  [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Space		  
		  [0x00, 0x00, 0x6C, 0xFE, 0x92, 0x92, 0xC6, 0x44],  # 3		  
		  [0x00, 0x00, 0x62, 0xF2, 0x92, 0x9A, 0xCE, 0x46],  # 2		  
		  [0x00, 0x00, 0x00, 0x00, 0xFE, 0xFE, 0x40, 0x00],  # 1
		  [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Space  
]

		  
		  
columns = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08]

# Initialize MAX7219
spi.writebytes([0x09])  # decoding :BCD
spi.writebytes([0x00])

spi.writebytes([0x0A])  # brightness
spi.writebytes([0x03])

spi.writebytes([0x0B])  # scanlimit; 8 LEDs
spi.writebytes([0x07])

spi.writebytes([0x0C])  # power-down mode: 0. normal mode:1
spi.writebytes([0x01])

spi.writebytes([0x0F])  # test display: 1; EOT. display: 0
spi.writebytes([0x00])


for j in range(0, len(matrix)):
	for i in range(0,8):
		spi.xfer([columns[i], matrix[j][i]])
	time.sleep(0.8)

spi.close

