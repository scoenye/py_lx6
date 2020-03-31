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

		self.speed_select = QtWidgets.QPushButton('2x - 8x')
		self.drive_select = QtWidgets.QPushButton('Quartz - Manual')
		self.near = QtWidgets.QPushButton('Near')
		self.far = QtWidgets.QPushButton('Far')
		self.north = QtWidgets.QPushButton('North')
		self.south = QtWidgets.QPushButton('South')
		self.east = QtWidgets.QPushButton('East')
		self.west = QtWidgets.QPushButton('West')

		self._assemble_panel()
		self._connect_signals()

	def _assemble_panel(self):
		self.main_layout.addWidget(self.speed_select, 0, 0, 1, 1)
		self.main_layout.addWidget(self.drive_select, 1, 0, 1, 1)
		self.main_layout.addWidget(self.near, 2, 0, 1, 1)
		self.main_layout.addWidget(self.far, 3, 0, 1, 1)
		self.main_layout.addWidget(self.north, 0, 3, 1, 1)
		self.main_layout.addWidget(self.south, 2, 3, 1, 1)
		self.main_layout.addWidget(self.east, 1, 2, 1, 1)
		self.main_layout.addWidget(self.west, 1, 4, 1, 1)

	def _pressed_near(self):
		print('Near pressed')

	def _released_near(self):
		print('Near released')

	def _connect_signals(self):
		self.near.pressed.connect(self._pressed_near)
		self.near.released.connect(self._released_near)

	def connect_model(self, event, model):
		self.near.clicked.connect(model)
