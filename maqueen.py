import microbit
import machine
import utime
import neopixel

class Maqueen:
	"""
	Python class for DFRobot Micro:maqueen platform
	https://www.dfrobot.com/product-1783.html
	Author: Krzysztof Sawicki <krzysztof@rssi.pl>
	License: GNU
	"""
	def __init__(self):
		self.rgbleds = neopixel.NeoPixel(microbit.pin15, 4)
		print("MAQUEEN initialized")

	def set_led(self, lednumber, value):
		"""
		Enable or disable the front LEDS
		0 - left LED (P8)
		1 - right LED (P12)
		"""
		if lednumber == 0:
			microbit.pin8.write_digital(value)
		elif lednumber == 1:
			microbit.pin12.write_digital(value)

	def read_distance(self):
		"""
		Reads distance from HC SR04 sensor
		The result is in centimeters
		Divider is taken from Makecode library for micro:maqueen
		"""
		divider = 42
		maxtime = 250 * divider
		microbit.pin2.read_digital()  # just for setting PULL_DOWN on pin2
		microbit.pin1.write_digital(0)
		utime.sleep_us(2)
		microbit.pin1.write_digital(1)
		utime.sleep_us(10)
		microbit.pin1.write_digital(0)

		duration = machine.time_pulse_us(microbit.pin2, 1, maxtime)
		distance = duration/divider
		return distance

	def read_patrol(self, which):
		"""
		Reads patrol sensor
		"""
		if which == 0:  # left
			return microbit.pin13.read_digital()
		elif which == 1:  # right
			return microbit.pin14.read_digital()

	def set_motor(self, motor, value):
		"""
		Controls motor
		motor: 0 - left motor, 1 - right motor
		value: -255 to +255, the sign means direction
		"""
		data = bytearray(3)
		if motor == 0:  # left motor
			data[0] = 0
		else:
			data[0] = 2  # right motor is 2
		if value < 0:  # ccw direction
			data[1] = 1
			value = -1*value
		data[2] = value
		microbit.i2c.write(0x10, data, False)  # 0x10 is i2c address of motor driver

	def motor_stop_all(self):
		self.set_motor(0, 0)
		self.set_motor(1, 0)

