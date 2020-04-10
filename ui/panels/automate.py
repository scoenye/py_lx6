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
from PyQt5 import QtWidgets, QtGui

from lx6.automate import DriftAlign
from ui.panels.common import ParameterPanel


class AlignParameterPanel(ParameterPanel):
	"""
	Collect the exposure parameter and launch the alignment run
	"""
	def __init__(self, board):
		super().__init__()
		self.main_layout = QtWidgets.QGridLayout(self)
		self._board = board

		self._widgets = {
			'exp_label': QtWidgets.QLabel('Exposure:'),
			'exposure': QtWidgets.QLineEdit('120'),
			'execute': QtWidgets.QPushButton('Execute'),
			'back': QtWidgets.QPushButton('Back')
		}

		self._widgets['exposure'].setValidator(QtGui.QIntValidator())		# Number only for the exposure values
		self._widgets['exposure'].setMaximumWidth(88)						# ~8 chars @ 11 pts

		self._assemble_panel()
		self._connect_events()

	def _assemble_panel(self):
		self.main_layout.addWidget(self._widgets['exp_label'], 0, 0, 1, 1)
		self.main_layout.addWidget(self._widgets['exposure'], 0, 1, 1, 1)
		self.main_layout.addWidget(self._widgets['back'], 1, 0, 1, 1)
		self.main_layout.addWidget(self._widgets['execute'], 1, 2, 1, 1)

	def _connect_events(self):
		self._widgets['execute'].pressed.connect(self.execute)
		self._widgets['back'].pressed.connect(self.back)

	def execute(self):
		align_script = DriftAlign(self._board, self)
		align_script.execute(exposure=int(self._widgets['exposure'].text()))

	def back(self):
		# Replace this panel with the script control panel,
		parent_panel = self.parentWidget()
		parent_panel.show_panel(None)

	def keep(self):
		"""
		:return: False - this panel can be discarded
		"""
		return False

