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


class CenterPanel(QtWidgets.QWidget):
	"""
	Controller UI main panel
	"""
	def __init__(self):
		super().__init__()
		self.main_layout = QtWidgets.QGridLayout(self)

		self._buttons = {
			'speed': QtWidgets.QPushButton('2x - 8x'),
			'drive': QtWidgets.QPushButton('Quartz - Manual'),
			'near': QtWidgets.QPushButton('Near'),
			'far': QtWidgets.QPushButton('Far'),
			'north': QtWidgets.QPushButton('North'),
			'south': QtWidgets.QPushButton('South'),
			'east': QtWidgets.QPushButton('East'),
			'west': QtWidgets.QPushButton('West')
		}

		self._assemble_panel()

	def _assemble_panel(self):
		self.main_layout.addWidget(self._buttons['speed'], 0, 0, 1, 1)
		self.main_layout.addWidget(self._buttons['drive'], 1, 0, 1, 1)
		self.main_layout.addWidget(self._buttons['near'], 2, 0, 1, 1)
		self.main_layout.addWidget(self._buttons['far'], 3, 0, 1, 1)
		self.main_layout.addWidget(self._buttons['north'], 0, 3, 1, 1)
		self.main_layout.addWidget(self._buttons['south'], 2, 3, 1, 1)
		self.main_layout.addWidget(self._buttons['east'], 1, 2, 1, 1)
		self.main_layout.addWidget(self._buttons['west'], 1, 4, 1, 1)

	def connect_model(self, event, model):
		self._buttons[event].pressed.connect(model.on)
		self._buttons[event].released.connect(model.off)
