#coding:utf8
'''
Created on

@author: cx
'''
from app.game.gatenodeservice import remoteserviceHandle
from app.game.appinterface import task

import json

@remoteserviceHandle
def VerifyTask_400(dynamicId,request_proto):
    '''主线任务完成校验
   '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = task.verifytasks(dynamicId, characterId)
    return json.dumps(data)

@remoteserviceHandle
def VerifyTask_401(dynamicId,request_proto):
    '''主线任务奖励校验
   '''
    print request_proto
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    taskId = argument.get('taskId')
    print type(characterId)
    print type(taskId)
    data = task.Maintaskreward(dynamicId, characterId,taskId)
    return json.dumps(data)

@remoteserviceHandle
def VerifyTask_402(dynamicId,request_proto):
    '''日常任务完成校验
   '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = task.verifydailytasks(dynamicId, characterId)
    print (402,data)
    return json.dumps(data)

@remoteserviceHandle
def VerifyTask_403(dynamicId,request_proto):
    '''日常任务完成校验
   '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    taskId = argument.get('taskId')
    data = task.dailytaskreward( characterId,dynamicId,taskId)
    print (403,data)
    return json.dumps(data)