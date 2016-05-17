import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from socket import *
from collections import deque

class Chatting(QWidget) :
    _name = None

    serverAddr = ('localhost', 20123)
    client = socket(AF_INET, SOCK_DGRAM)

    def __init__(self,name,):
        super(Chatting, self).__init__()

        self._name = name

        self.setWindowTitle('Chatting(%s)' % self._name)
        self.setFixedWidth(645)
        self.setFixedHeight(445)

        self.center()

        self.messageList = QListWidget()

        send = QWidget()
        horizontalLayoutBottom = QHBoxLayout(send)
        self.contentEdit = QLineEdit()
        horizontalLayoutBottom.addWidget(self.contentEdit)
        self.sendButton = QPushButton('Send')
        self.sendButton.clicked.connect(self.send)
        horizontalLayoutBottom.addWidget(self.sendButton)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.messageList)
        self.mainLayout.addWidget(send)

        self.setLayout(self.mainLayout)

        clientThread = ClientThread(client=self.client,parent=self)
        self.connect(clientThread,clientThread.signal,self.writeToMessageList)
        clientThread.start()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.move((screen.width() - window.width()) / 2 ,(screen.height() - window.height()) / 2)

    def send(self):
        self.client.sendto(self._name.toUtf8() + ' say:' + self.contentEdit.text().toUtf8(),self.serverAddr)
        self.contentEdit.setText('')

    def writeToMessageList(self,message):
        self.messageList.addItem(message)

class ClientThread(QThread) :

    BUFSIZE = 1024

    _client = None

    def __init__(self,client,parent=None):
        QThread.__init__(self, parent)
        self._client = client
        self.signal = SIGNAL("signal")

    def run(self):
        self.receive()

    def receive(self):

        while True:
            data,addr = self._client.recvfrom(self.BUFSIZE)
            self.emit(self.signal,unicode(data,'utf8'))