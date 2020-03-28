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
