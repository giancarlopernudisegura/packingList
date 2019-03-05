from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.Qt import *
import os
import sys

sexe = None


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        w, h = 400, 300
        self.setGeometry(640, 480, w, h)
        self.setWindowTitle("List Config Editor")

        quitAction = QtWidgets.QAction("&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("Exit the application")
        quitAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(quitAction)

        print(self.getChoice("Sexe:", ("Male", "Female"), 0, 0, 200, 30))

        self.show()

    def closeEvent(self, event):      
        event.ignore()
        self.close_application()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Quit", "Do you really want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
    
    def getChoice(self, label, options, left, top, width, height):
        text = QtWidgets.QLabel(self)
        text.setText(label)
        text.setMargin(left)
        text.setAlignment(Qt.AlignLeft)

        comboBox = QtWidgets.QComboBox(self)
        for opt in options:
            comboBox.addItem(opt)
        comboBox.setGeometry(2 * left + text.width(), top, width, height)

        comboBox.ac

def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    try:
        main()
    except AttributeError:
        print("Closed")
    finally:
        os.system("python generate.py -S %s > list.md" % ('f'))