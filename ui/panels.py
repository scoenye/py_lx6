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
from PyQt5 import QtWidgets

from features import LX6, AUX


class CenterPanel(QtWidgets.QWidget):
	"""
	Controller UI main panel
	"""
	def __init__(self):
		super().__init__()
		self.main_layout = QtWidgets.QGridLayout(self)

		self._buttons = {
			LX6.LX_SPEED: QtWidgets.QPushButton('2x - 8x'),
			LX6.LX_DRIVE: QtWidgets.QPushButton('Quartz - Manual'),
			LX6.LX_NEAR: QtWidgets.QPushButton('Near'),
			LX6.LX_INFTY: QtWidgets.QPushButton('Far'),
			LX6.LX_NORTH: QtWidgets.QPushButton('North'),
			LX6.LX_SOUTH: QtWidgets.QPushButton('South'),
			LX6.LX_EAST: QtWidgets.QPushButton('East'),
			LX6.LX_WEST: QtWidgets.QPushButton('West'),
			AUX.CAM_SHUTTER: QtWidgets.QPushButton('Click!')
		}

		self._assemble_panel()

	def _assemble_panel(self):
		self.main_layout.addWidget(self._buttons[LX6.LX_SPEED], 0, 0, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_DRIVE], 1, 0, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_NEAR], 2, 0, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_INFTY], 3, 0, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_NORTH], 0, 3, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_SOUTH], 2, 3, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_EAST], 1, 2, 1, 1)
		self.main_layout.addWidget(self._buttons[LX6.LX_WEST], 1, 4, 1, 1)
		self.main_layout.addWidget(self._buttons[AUX.CAM_SHUTTER], 3, 4, 1, 1)

	def connect_model(self, event, model):
		self._buttons[event].pressed.connect(model.on)
		self._buttons[event].released.connect(model.off)
