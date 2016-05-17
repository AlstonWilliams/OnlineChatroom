from socket import *
import threading
from collections import deque

class ServerThread(threading.Thread) :

    BUFSIZE = 1024

    _server = None
    _clientList = []
    _contentList = []

    def __init__(self,server,clientList,contentList):
        threading.Thread.__init__(self)
        self._server = server
        self._clientList = clientList
        self._contentList = deque(contentList)

    def run(self):
        self.receive()

    def receive(self):
        while True:

            (data,addr) = self._server.recvfrom(self.BUFSIZE)
            self._contentList.append(data)

            try:
                if self._clientList.index(addr) :
                    pass
            except ValueError:
                self._clientList.append(addr)

            try:
                for content in self._contentList :
                    try :
                        content = self._contentList.popleft()
                    except IndexError:
                        pass

                    for client in self._clientList :
                        print content
                        self._server.sendto(content,client)
            except RuntimeError:
                # solve queue mutated during iteration
                pass

        self._server.close()