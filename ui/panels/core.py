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
from ui.panels.automate import AlignParameterPanel


class ManualControlPanel(QtWidgets.QWidget):
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

		self._buttons[LX6.LX_SPEED].setCheckable(True)
		self._buttons[LX6.LX_DRIVE].setCheckable(True)

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
		button = self._buttons[event]

		if button.isCheckable():
			button.pressed.connect(model.toggle)
		else:
			button.pressed.connect(model.on)
			button.released.connect(model.off)


class ScriptControlPanel(QtWidgets.QWidget):
	"""
	Control scripts launch panel
	"""
	def __init__(self, board):
		super().__init__()
		self.main_layout = QtWidgets.QGridLayout(self)
		self._board = board

		self._buttons = {
			'align': QtWidgets.QPushButton('Align')
		}

		self._assemble_panel()
		self._connect_events()

	def _assemble_panel(self):
		self.main_layout.addWidget(self._buttons['align'], 0, 0, 1, 1)

	def _connect_events(self):
		self._buttons['align'].clicked.connect(self._collect_parameters)

	def _collect_parameters(self):
		# Replace this panel with the parameter panel, but we need to keep ourselves around
		parent_panel = self.parentWidget()
		parent_panel.show_panel(AlignParameterPanel(self._board), True)


class LX6UI(QtWidgets.QMainWindow):
	def __init__(self, board):
		super().__init__()
		self.manual_control_panel = ManualControlPanel()
		self.scripted_control_panel = ScriptControlPanel(board)

		self.setGeometry(100, 100, 460, 320)        # sized to fit a PiTFT screen
		self.setWindowTitle('LX6 controller')
		self.statusBar().showMessage('Ready')
		self.setCentralWidget(self.manual_control_panel)
		self._create_toolbar()

		board.connect_gui(self)

	def _create_toolbar(self):
		toolbar = self.addToolBar('Test')
		manual = toolbar.addAction('Manual')
		manual.triggered.connect(self._select_manual_panel)

		scripted = toolbar.addAction('Scripted')
		scripted.triggered.connect(self._select_scripted_panel)

	def _select_manual_panel(self):
		# Set the manual control panel as the active center panel
		self.show_panel(self.manual_control_panel, True)

	def _select_scripted_panel(self):
		# Set the scripted control panel as the active center panel
		self.show_panel(self.scripted_control_panel, True)

	def show_panel(self, panel, keep):
		"""
		Replace the central widget panel
		:param panel: the panel to install as the new visible control panel
		:param keep: whether or not to keep the current panel around
		:return:
		"""
		if keep:
			self.centralWidget().setParent(None)
		self.setCentralWidget(panel)

	def connect_model(self, event, model):
		"""
		Connect the model event handlers to the user interface
		:param event: the event to connect
		:param model: the model to connect to
		:return:
		"""
		# Delegate to the center panel. All buttons live there.
		self.manual_control_panel.connect_model(event, model)
