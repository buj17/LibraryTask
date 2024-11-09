import sys

from MainWindow import Main
from PyQt6.QtWidgets import QApplication


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
