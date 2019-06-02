#coding:utf8
'''

'''
from dataloader import registe_madmin,CheckMemDB,MAdminManager,initData
from firefly.server.globalobject import GlobalObject

def doWhenStop():
    """服务器关闭前的处理
    """
    print "##############################"
    print "##########checkAdmins#############"
    print "##############################"
    MAdminManager().checkAdmins()
    
GlobalObject().stophandler = doWhenStop
    

def loadModule():
#     mclient.flush_all()
    registe_madmin()
    initData()
    CheckMemDB(1800)
    
    
    