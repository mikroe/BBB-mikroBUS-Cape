import smbus

class L3GD20 :

	_CTRL_REG1 = 0x20
	_CTRL_REG2 = 0x21
	_CTRL_REG3 = 0x22
	_CTRL_REG4 = 0x23
	_CTRL_REG5 = 0x24
	_OUT_X_L = 0x28
	_OUT_X_H = 0x29
	_OUT_Y_L = 0x2A
	_OUT_Y_H = 0x2B
	_OUT_Z_L = 0x2C
	_OUT_Z_H = 0x2D


	def __init__(self, busnum = -1, addr = 0x6B):
		self.bus = smbus.SMBus(busnum)
		self.addr = addr

		self.bus.write_byte_data(self.addr, self._CTRL_REG1, 0x0F)     # Power Up
		self.bus.write_byte_data(self.addr, self._CTRL_REG4, 0x00)     # dps: 250

	def readRawX(self):
		x1 = self.bus.read_byte_data(self.addr, self._OUT_X_H)  # Highest byte
		x0 = self.bus.read_byte_data(self.addr, self._OUT_X_L)  # Lowest byte
		return x1<<8 | x0  # 16bit resolution

	def readRawY(self):
		y1 = self.bus.read_byte_data(self.addr, self._OUT_Y_H)  # Highest byte
		y0 = self.bus.read_byte_data(self.addr, self._OUT_Y_L)  # Lowest byte
		return y1<<8 | y0  # 16bit resolution

	def readRawZ(self):
		z1 = self.bus.read_byte_data(self.addr, self._OUT_Z_H)  # Highest byte
		z0 = self.bus.read_byte_data(self.addr, self._OUT_Z_L)  # Lowest byte
		return z1<<8 | z0  # 16bit resolution
