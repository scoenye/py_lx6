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
from abc import ABC, abstractmethod
from time import sleep

from features import LX6, AUX


class Script(ABC):
	"""
	Interface for the automated control scripts
	"""
	def __init__(self, board, reporter=None):
		self._board = board
		self._reporter = reporter		# Target for status updates

	@abstractmethod
	def execute(self, **kwargs):
		"""
		Execute the script
		:param kwargs: keyword parameters specific to the script.
		:return:
		"""

	def _feedback(self, update):
		if self._reporter:
			self._reporter.feedback(update)


class DriftAlign(Script):
	"""
	Use the east/west controls and the external camera to align the telescope
	"""
	def execute(self, **kwargs):
		"""
		Execute the alignment script
		:param kwargs: exposure - time in seconds for each leg of the alignment run.
		:return:
		"""
		self._feedback('Paint marker dot')
		self._board.command(AUX.CAM_SHUTTER, 1)
		sleep(10)										# Paint dot

		self._feedback('Going west')
		self._board.command(LX6.LX_WEST, 1)
		sleep(kwargs['exposure'])						# One leg of the V

		self._feedback('Going east')
		self._board.command(LX6.LX_EAST, 1)
		sleep(kwargs['exposure'])						# Other leg of the V

		self._board.command(AUX.CAM_SHUTTER, 0)
		self._feedback('Ready')
