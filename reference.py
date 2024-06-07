import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from mainGui import Ui_mainGUIfile
class mainFile(QWidget):
    def __init__(self):
        super(mainFile,self).__init__()
        print("Main File")
        self.mainUI =Ui_mainGUIfile()
        self.mainUI.setupUi(self)

        self.mainUI.movie = QtGui.QMovie("../../../../../hp/speak.gif")
        self.mainUI.label.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

        self.mainUI.pushButton_2.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile() 
    ui.show()
    sys.exit(app.exec_())       