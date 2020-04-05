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

import sys

from time import sleep

from PyQt5.QtWidgets import QApplication, QMainWindow

from aux.camera import Camera
from lx6.controller import Controller
from pi.board import BoardV2
from ui.panels import LX6UI


if __name__ == "__main__":
	app = QApplication(sys.argv)
	board = BoardV2()
	board.initialize()
	controller = Controller(board)
	camera = Camera(board)

	form = LX6UI([controller, camera])
	form.connect_automate(board)

	form.show()

	try:
		result = app.exec_()
	finally:
		board.shutdown()

	sys.exit(result)
