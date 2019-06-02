#coding:utf8
'''
Created on 2012-2-27

@author: sean_lan
'''
from app.gate.appinterface import login
import json
from app.gate.gateservice import localserviceHandle

@localserviceHandle
def loginToServer_101(key,dynamicId,request_proto):

    argument = json.loads(request_proto)
    dynamicId = dynamicId
    username = argument.get('username')
    password = argument.get('password')
    data = login.loginToServer(dynamicId, username, password)
    response = {}
    _data = data.get('data')
    response['result']=data.get('result',False)
    responsedata = {}
    response['data'] = responsedata
    if _data:
        responsedata['userId'] = _data.get('userId',0)
        responsedata['hasRole'] = _data.get('hasRole',False)
        responsedata['characterId'] = _data.get('defaultId',False)
        responsedata['serverNum'] = 6637
        responsedata['serverId'] = u"测试服"
        responsedata['serverState'] = u"爆满"
    print json.dumps(response)
    return json.dumps(response)

@localserviceHandle
def activeNewPlayer_102(key,dynamicId,request_proto):
    '''创建角色
    '''
    argument = json.loads(request_proto)
    userId = argument.get('userId')
    nickName = argument.get('nickname')
    sex = int(argument.get('sex'))
    #profession = int(argument.get('profession'))
    data  = login.activeNewPlayer(dynamicId, userId, nickName, sex)
    return json.dumps(data)

def SerializePartialEnterScene(result,response):
    '''序列化进入场景的返回消息
    '''
    return json.dumps(result)

@localserviceHandle
def roleLogin_103(key,dynamicId, request_proto):
    '''角色登陆'''
    argument = json.loads(request_proto)
    print argument
    userId = argument.get('userId')
    characterId = argument.get('characterId')
    data = login.rolecheck(dynamicId, userId, characterId)
    data1 = login.roleLogin(dynamicId,characterId)
    if not data.get('result'):
        return json.dumps(data)
    placeId = data1['data'].get('placeId',1000)
    response = {}

    dd = login.enterScene(dynamicId, characterId, placeId, True)
    if not dd:
        return
    dd.addCallback(SerializePartialEnterScene,response)
    return json.dumps(data)


@localserviceHandle
def roleinfo_104(key,dynamicId, request_proto):
    '''角色信息'''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = login.roleLogin(dynamicId,characterId)
    if not data.get('result'):
        return json.dumps(data)
    placeId = data['data'].get('placeId',1000)
    response = {}

    dd = login.enterScene(dynamicId, characterId, placeId, True)
    if not dd:
        return
    dd.addCallback(SerializePartialEnterScene,response)
    return dd

@localserviceHandle
def roleinfo_114(key,dynamicId, request_proto):
    '''角色信息'''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = login.roleLogin(dynamicId,characterId)
    if not data.get('result'):
        return json.dumps(data)
    placeId = data['data'].get('placeId',1000)
    response = {}
    #dd = roleinfo
    #return dd

