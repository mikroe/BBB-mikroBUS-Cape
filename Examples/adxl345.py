import smbus

class ADXL345 :

	_POWER_CTL =   0x2D
	_DATA_FORMAT = 0x31
	_BW_RATE =     0x2C
	_DATAX0 =      0x32
	_DATAX1 =      0x33
	_DATAY0 =      0x34
	_DATAY1 =      0x35
	_DATAZ0 =      0x36
	_DATAZ1 =      0x37
	_FIFO_CTL =    0x38


	def __init__(self, busnum = -1, addr = 0x1D):
		self.bus = smbus.SMBus(busnum)
		self.addr = addr

		# Go into standby mode to configure the device.
		self.bus.write_byte_data(self.addr, self._POWER_CTL, 0x00)         # POWER_CTL reg: standby mode
		id = self.bus.read_byte_data(self.addr, 0x00)
		if id != 0xE5:
			raise Exception()
		else:
			self.bus.write_byte_data(self.addr, self._DATA_FORMAT, 0x08)       # Full resolution, +/-2g, 4mg/LSB, right justified
			self.bus.write_byte_data(self.addr, self._BW_RATE, 0x0A)           # Set 100 Hz data rate
			self.bus.write_byte_data(self.addr, self._FIFO_CTL, 0x80)          # stream mode
			self.bus.write_byte_data(self.addr, self._POWER_CTL, 0x08)         # POWER_CTL reg: measurement mode

	def readRawX(self):
		x1 = self.bus.read_byte_data(self.addr, self._DATAX1)  # Highest byte
		x0 = self.bus.read_byte_data(self.addr, self._DATAX0)  # Lowest byte
		return (x1<<8 | x0) & 0x3FF  # 10bit resolution

	def readRawY(self):
		y1 = self.bus.read_byte_data(self.addr, self._DATAY1)  # Highest byte
		y0 = self.bus.read_byte_data(self.addr, self._DATAY0)  # Lowest byte
		return (y1<<8 | y0) & 0x3FF  # 10bit resolution

	def readRawZ(self):
		z1 = self.bus.read_byte_data(self.addr, self._DATAZ1)  # Highest byte
		z0 = self.bus.read_byte_data(self.addr, self._DATAZ0)  # Lowest byte
		return (z1<<8 | z0) & 0x3FF  # 10bit resolution
