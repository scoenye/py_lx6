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

import RPi.GPIO as GPIO


class Button:
	"""
	A single on/off button
	"""

	def __init__(self, pin):
		self._pin = pin

	def on(self):
		"""
		Press the button
		"""
		GPIO.output(self._pin, 1)

	def off(self):
		"""
		Release the button
		"""
		GPIO.output(self._pin, 0)


class ButtonPair:
	"""
	Two buttons working in tandem. Both can be off but only one can be on at any time.
	"""

	def __init__(self, pin1, pin2):
		self._buttons = (Button(pin1), Button(pin2))

	def __getitem__(self, item):
		return self._buttons[item]

	def on(self, button):
		"""
		Turn a button on, The other button will be turned off
		:param button: which button to turn on (0, 1)
		:return:
		"""
		self._buttons[1-button].off()
		self._buttons[button].on()

	def off(self, button):
		"""
		Turn a button off.
		:param button: which button to turn off.
		:return:
		"""
		self._buttons[button].off()
