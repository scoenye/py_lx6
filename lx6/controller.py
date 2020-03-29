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
from pi.buttons import Button, ButtonPair


class Controller:
	"""
	LX6 hand controller
	"""
	def __init__(self, board):
		"""
		:param board: Board through which the controller is connected to the Raspberry Pi
		"""
		self._board = board

		self._east_west = ButtonPair()
		self._north_south = ButtonPair()
		self._near_far = ButtonPair()
		self._speed = Button()
		self._drive = Button()

