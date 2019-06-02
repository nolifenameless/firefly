#coding:utf8

import time

from socket import AF_INET,SOCK_STREAM,socket
from thread import start_new
import struct,json
HOST='127.0.0.1'
PORT=11009
BUFSIZE=1024
ADDR=(HOST , PORT)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)

def sendData(sendstr,commandId):
    """78,37,38,48,9,0"""
    HEAD_0 = chr(0)
    HEAD_1 = chr(0)
    HEAD_2 = chr(0)
    HEAD_3 = chr(0)
    ProtoVersion = chr(0)
    ServerVersion = 0
    sendstr = sendstr
    data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,\
                       HEAD_3,ProtoVersion,ServerVersion,\
                       len(sendstr)+4,commandId)
    senddata = data+sendstr
    return senddata

def resolveRecvdata(data):
    head = struct.unpack('!sssss3I',data[:17])
    lenght = head[6]
    data = data[17:17+lenght]
    return data


def login():
    client.sendall(sendData(json.dumps({"username":"test101","password":111111}),101))

def cre8role():
    client.sendall(sendData(json.dumps({"sex":1,"nickname":u"波波波","userId":3}),102))

def rolelogin():
    client.sendall(sendData(json.dumps({"userId":7,"characterId":1000008}),103))

def rolelogin1():
    client.sendall(sendData(json.dumps({"userId":7,"characterId":1000008}),105))

def rolelogin2():
    client.sendall(sendData(json.dumps({"userId":7,"characterId":1000008}),105))


def entertianti():
    client.sendall(sendData(json.dumps({"characterId":1000008}),3699))

def match():
    client.sendall(sendData(json.dumps({"characterId":1000008}),3700))

def sign1():
    client.sendall(sendData(json.dumps({"characterId":1000008,"kind":3}),3715))

def sign():
    client.sendall(sendData(json.dumps({"characterId":1000008,"kind":3}),3711))

def changescore():
    client.sendall(sendData(json.dumps({"characterId":1000008,"change":60}),3703))

def getdressed():
    client.sendall(sendData(json.dumps({"characterId":1000008,"itemid":10002}),209))

def takeoff():
    client.sendall(sendData(json.dumps({"characterId":1000008,"itemid":20001}),215))

def getequipment():
    client.sendall(sendData(json.dumps({"characterId":1000008}),203))

def getpack():
    client.sendall(sendData(json.dumps({"characterId":1000008,"itemid":10001}),2000))

def newname():
    client.sendall(sendData(json.dumps({"characterId":1000008,"newname":"哇咔咔逗比"}),106))

def newname1():
    client.sendall(sendData(json.dumps({"characterId":1000008,"newname":"王大锤"}),106))

def taskinfomain():
    client.sendall(sendData(json.dumps({"characterId":1000008}),3334))

def taskinfomain1():
    client.sendall(sendData(json.dumps({"characterId":1000008,"taskId":100010}),403))

def test3334():
    client.sendall(sendData(json.dumps({"characterId":1000008,"itemlist":({'itemid':1003},{'itemid':1004})}),3334))


login()
#cre8role()
rolelogin()
rolelogin1()
getequipment()
#getpack()
test3334()
#newname()
#rolelogin1()
#taskinfomain()
#taskinfomain1()
#rolelogin1()
#sign1()
#sign()
#rolelogin1()
#entertianti()
#match()
#changescore()
#getequipment()
#getpack()
#getdressed()
#takeoff()
#getequipment()
#getpack()

while True:
    pass

