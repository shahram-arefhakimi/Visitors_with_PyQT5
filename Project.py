from Main_Windows_Class import *
import sys
from PyQt5.QtWidgets import QApplication 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())