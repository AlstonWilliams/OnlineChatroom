#coding:UTF-8
import sys
from PyQt4 import QtCore,QtGui,uic
from socket import *
from View.Chatting import *
import locale

qtCreatorFile = "LoginView.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LoginView(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.center()

        #1. add callback method from button
        self.startButton.clicked.connect(self.registe)

    '''
        Send your name to server
    '''
    def registe(self):
        #2. Notice: data type returned by method named 'text' is QString which default encoding is not utf-8
        #3. redirect to Chatting window
        # set Chatting window to a member of this class,otherwise Chatting window doesn't appear
        self.chatting = Chatting(name=self.nameInput.text())
        self.chatting.show()
        self.hide()

    # center the window
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,(screen.height() - size.height())/2)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = LoginView()
    window.show()
    app.exec_()

