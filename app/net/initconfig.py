#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from firefly.server.globalobject import GlobalObject
from firefly.netconnect.datapack import DataPackProtoc

def doConnectionMade(conn):
    str3 = '<cross-domain-policy><allow-access-from domain=\"*\" to-ports=\"*\"/></cross-domain-policy>'
    GlobalObject().netfactory.pushObject(11009,str3,[conn.transport.sessionno])

def callWhenConnLost(conn):
    dynamicId = conn.transport.sessionno
    GlobalObject().remote['gate'].callRemote("netconnlost",dynamicId)

GlobalObject().netfactory.doConnectionLost = callWhenConnLost
GlobalObject().netfactory.doConnectionMade = doConnectionMade
dataprotocl = DataPackProtoc(0,0,0,0,0,0)
GlobalObject().netfactory.setDataProtocl(dataprotocl)



def loadModule():
    import netapp
    import gatenodeapp