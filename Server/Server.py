#coding:UTF-8
from socket import *
from Thread.ServerThread import *

HOST = ''
PORT = 20123
BUFSIZ = 128
ADDR = (HOST, PORT)

clientList = []
contentList = []

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)

registeThread = ServerThread(server=udpServer,clientList=clientList,contentList=contentList).start()
