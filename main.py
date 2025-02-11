from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import resources_rc  # Import the compiled resources
from Custom_Widgets import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)  # Load UI file
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        self.show()

app = QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec())
