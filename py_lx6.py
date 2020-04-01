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

from PyQt5.QtWidgets import QApplication, QMainWindow

from aux.camera import Camera
from lx6.controller import Controller
from pi.board import BoardV2
from ui import panels


class LX6UI(QMainWindow):
	def __init__(self, hardware):
		super().__init__()
		self.center_panel = panels.CenterPanel()

		self.setGeometry(100, 100, 460, 320)        # sized to fit a PiTFT screen
		self.setWindowTitle('LX6 controller')
		self.statusBar().showMessage('Ready')
		self.setCentralWidget(self.center_panel)

		for part in hardware:
			part.connect_gui(self)

	def connect_model(self, event, model):
		"""
		Connect the model event handlers to the user interface
		:param event: the event to connect
		:param model: the model to connect to
		:return:
		"""
		# Delegate to the center panel. All buttons live there.
		self.center_panel.connect_model(event, model)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	board = BoardV2()
	board.initialize()
	controller = Controller(board)
	camera = Camera(board)

	form = LX6UI([controller, camera])

	form.show()

	try:
		result = app.exec_()
	finally:
		board.shutdown()

	sys.exit(result)
