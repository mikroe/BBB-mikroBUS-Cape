import spidev
import time

spi = spidev.SpiDev()
spi.open(1,0)  # /dev/spidev1.0

#Initialise
# Set porta to be output 
spi.writebytes(0,[0x00])

Expander_Set_PullUpsPortB(0,0xFF);     // Set pull-ups to all of the Expander's PORTB pins