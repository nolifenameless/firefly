__author__ = 'Administrator'
#coding:utf8
'''
Created on 2014-6-25

@author: cx
'''
from app.game.gatenodeservice import remoteserviceHandle
from app.game.appinterface import roleinfo
import json

@remoteserviceHandle
def fuben_605(dynamicId,request_proto):
    '''获取角色的副本进度信息
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = roleinfo.roleInfo(dynamicId,characterId)
    print data
    return json.dumps(data)

@remoteserviceHandle
def newname_106(dynamicId,request_proto):
    '''玩家改名
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    newname = argument.get('newname')
    data = roleinfo.newname(dynamicId,characterId,newname)
    return json.dumps(data)






