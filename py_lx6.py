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


class LX6UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 460, 320)        # sized to fit a PiTFT screen
        self.setWindowTitle('PyNSD')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LX6UI()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
