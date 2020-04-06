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

from features import LX6, AUX
from pi.buttons import Button, ButtonPair


class Board(ABC):
	"""
	Initialize the Raspberry Pi
	Connect the logical controller functions to the Raspberry Pi header pins
	Shut down the Raspberry Pi on exit
	"""

	LX_pins = {}
	aux_pins = {}

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

	@abstractmethod
	def command(self, feature, state):
		"""
		External command interface.
		:param feature: which feature to change
		:param state: new status for the feature
		:return:
		"""


class BoardV2(Board):
	"""
	LX6 v2 board
	"""
	LX_pins = {
		LX6.LX_NEAR: 18,
		LX6.LX_INFTY: 23,
		LX6.LX_DRIVE: 24,
		LX6.LX_SPEED: 25,
		LX6.LX_NORTH: 12,
		LX6.LX_SOUTH: 16,
		LX6.LX_EAST: 20,
		LX6.LX_WEST: 21
	}

	aux_pins = {
		AUX.CAM_SHUTTER: 17
	}

	def __init__(self):
		self._east_west = ButtonPair(self.LX_pins[LX6.LX_EAST], self.LX_pins[LX6.LX_WEST])
		self._north_south = ButtonPair(self.LX_pins[LX6.LX_NORTH], self.LX_pins[LX6.LX_SOUTH])
		self._near_far = ButtonPair(self.LX_pins[LX6.LX_NEAR], self.LX_pins[LX6.LX_INFTY])
		self._speed = Button(self.LX_pins[LX6.LX_SPEED])
		self._drive = Button(self.LX_pins[LX6.LX_DRIVE])
		self._shutter = Button(self.aux_pins[AUX.CAM_SHUTTER])

		self._actions = {
			LX6.LX_NEAR: self._near_far[0],
			LX6.LX_INFTY: self._near_far[1],
			LX6.LX_DRIVE: self._drive,
			LX6.LX_SPEED: self._speed,
			LX6.LX_NORTH: self._north_south[0],
			LX6.LX_SOUTH: self._north_south[1],
			LX6.LX_EAST: self._east_west[0],
			LX6.LX_WEST: self._east_west[1],
			AUX.CAM_SHUTTER: self._shutter
		}

	def initialize(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		for pin in self.LX_pins.values():
			GPIO.setup(pin, GPIO.OUT)
			# This to stop the inputs from floating
			GPIO.output(pin, 0)  # Board was modified to use NO instead of the NC used by the LX6

		for pin in self.aux_pins.values():
			GPIO.setup(pin, GPIO.OUT)

	def shutdown(self):
		GPIO.cleanup()

	def command(self, feature, status):
		"""
		External command interface.
		:param feature: which feature to change
		:param status: new status for the feature. 1: on, 0: off
		:return:
		"""
		if status:
			self._actions[feature].on()
		else:
			self._actions[feature].off()

	def connect_gui(self, ui):
		"""
		Connect the control buttons to the interface
		:param ui: user interface instance
		:return:
		"""
		ui.connect_model(LX6.LX_DRIVE, self._drive)
		ui.connect_model(LX6.LX_SPEED, self._speed)
		ui.connect_model(LX6.LX_NEAR, self._near_far[0])
		ui.connect_model(LX6.LX_INFTY, self._near_far[1])
		ui.connect_model(LX6.LX_NORTH, self._north_south[0])
		ui.connect_model(LX6.LX_SOUTH, self._north_south[1])
		ui.connect_model(LX6.LX_EAST, self._east_west[0])
		ui.connect_model(LX6.LX_WEST, self._east_west[1])
		ui.connect_model(AUX.CAM_SHUTTER, self._shutter)
