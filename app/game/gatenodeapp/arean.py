#coding:utf8
'''
Created on 2013-7-17

@author: lan (www.9miao.com)
'''
from app.game.gatenodeservice import remoteserviceHandle
from app.game.appinterface import arena
import json

@remoteserviceHandle
def GetEnemyInfo_3700(dynamicId, request_proto):
    '''获取对手天梯信息
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = arena.GetEnemyInfo3700(dynamicId, characterId)
    return json.dumps(data)

@remoteserviceHandle
def ArenaBattle_3704(dynamicId, request_proto):
    '''天梯战斗
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    tocharacterId = argument.get('tid')
    data = arena.ArenaBattle_3704(dynamicId, characterId, tocharacterId)
    response = {}
    response['result'] = data.get('result',False)
    response['message'] = data.get('message','')
    _responsedata = data.get('data')
    if _responsedata:
        battle = _responsedata.get('fight')
        setData = _responsedata.get('setData')
        fightdata = battle.formatFightData()
        response['data'] = fightdata
        fightdata['battleResult'] = battle.battleResult
        fightdata['setData'] = setData
    return json.dumps(response)

@remoteserviceHandle
def GetSelfInfo_3699(dynamicId, request_proto):
    '''获取自己天梯信息
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    data = arena.GetSelfInfo3699(dynamicId, characterId)
    return json.dumps(data)

@remoteserviceHandle
def VerifyResult_3703(dynamicId, request_proto):
    '''天梯结果验证
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    change = argument.get('change')
    result = arena.VerifyResult3703(dynamicId, characterId,change)
    return json.dumps(result)

@remoteserviceHandle
def SignReward_3715(dynamicId, request_proto):
    '''签到奖励
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    result = arena.SignReward3715(dynamicId, characterId)
    return json.dumps(result)

@remoteserviceHandle
def SignReward_3711(dynamicId, request_proto):
    '''签到奖励
    '''
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    result = arena.getReward3711(dynamicId, characterId)
    return json.dumps(result)
