import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)
screens = QGuiApplication.screens()
    for screen in screens:

print(str(sys.argv))
