"""
	py_lx6
	Raspberry Pi base hand controller for Meade LX-6 telescopes

	Copyright (C) 2020  Sven Coenye

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or any
	later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from abc import ABC, abstractmethod

import RPi.GPIO as GPIO


class Board(ABC):
	"""
	Initialize the Raspberry Pi
	Connect the logical controller functions to the Raspberry Pi header pins
	Shut down the Raspberry Pi on exit
	"""

	LX_pins = []

	@abstractmethod
	def initialize(self):
		"""
		Initialize the Raspberry Pi for use
		:return:
		"""

	@abstractmethod
	def shutdown(self):
		"""
		Release the Raspberry Pi
		:return:
		"""


class BoardV2(Board):
	"""
	LX6 v2 board
	"""

	LX_NEAR = 18
	LX_INFTY = 23
	LX_QRTZ = 24
	LX_SPEED = 25
	LX_NORTH = 12
	LX_SOUTH = 16
	LX_EAST = 20
	LX_WEST = 21

	LX_pins = [LX_NEAR, LX_INFTY, LX_QRTZ, LX_SPEED, LX_NORTH, LX_SOUTH, LX_EAST, LX_WEST]

	def initialize(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		for pin in self.LX_pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 1)  # LX6 contacts are NC: 1 turns signal off

	def shutdown(self):
		GPIO.cleanup()
