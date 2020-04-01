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

# Features provided by the controller board. Separate module to avoid circular imports

from enum import Enum,auto


class LX6(Enum):
	LX_NEAR = auto()
	LX_INFTY = auto()
	LX_DRIVE = auto()
	LX_SPEED = auto()
	LX_NORTH = auto()
	LX_SOUTH = auto()
	LX_EAST = auto()
	LX_WEST = auto()