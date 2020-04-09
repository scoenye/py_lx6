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
from abc import abstractmethod

from PyQt5 import QtWidgets


class CentralPanel(QtWidgets.QWidget):
	"""
	Common interface for the center panel widgets. This should be an abstract class but Qt uses a custom meta class
	so inheriting from ABC is not possible. Although that can be worked around, that adds a good bit of complications.
	"""
	@abstractmethod
	def keep(self):
		"""
		Indicate if this panel should be kept or discarded when the central widget is replaced.
		:return: True to prevent this panel from being destroyed, False to indicate it should be discarded.
		"""
