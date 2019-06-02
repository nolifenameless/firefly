#coding:utf8
'''
Created on 2012-7-1
竞技场操作
@author: Administrator
'''
from app.game.core.PlayersManager import PlayersManager
from app.share.dbopear import dbCharacter
from app.share.dbopear import dbarena
import random
import datetime,math
from app.share.dbopear import dbItems
from app.game.core.character.PlayerCharacter import PlayerCharacter


def GetSelfInfo3699(dynamicId,characterId):
    '''获取自己天梯信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':u""}
    selfinfo = dbCharacter.getCharacterBaseInfoById(characterId)
    selfarenainfo = dbarena.getCharacterScoreRank(characterId)
    selfinfo.update(selfarenainfo)
    print selfinfo
    return selfinfo

def GetEnemyInfo3700(dynamicId,characterId):
    '''获取对手天梯信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':u""}
    data = player.arena.getArenaAllInfo()
    nums = 0
    for k in data['dsList']:
        nums += 1
    randnum = random.randint(0,nums-1)
    topid =(data["dsList"][randnum]['characterId'])
    enemyinfo = dbCharacter.getCharacterBaseInfoById(topid)
    enemyinfo.update(data["dsList"][randnum])
    print enemyinfo
    return enemyinfo

def VerifyResult3703(dynamicId,characterId,change):
    '''天梯分校验
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':u""}
    selfscore = dbarena.getCharacterScoreRank(characterId)
    oriscore = selfscore['score']
    if abs(change)>=50:
        print {'result':False,'message':u"illegal score request"}
        return {'result':False,'message':u"illegal score request"}
    elif abs(change)<50:
        result = dbarena.updateCharacterArenaScore(characterId,change,oriscore)
        print result
        return result

def ArenaBattle_3704(dynamicId,characterId,tocharacterId):
    '''竞技场战斗
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    result = player.arena.doFight(tocharacterId)
    return result

def TiantiBattle_3701(dynamicId,characterId,tocharacterId,battleresult):
    '''天梯战斗结果处理
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    result = player.arena.doFight(tocharacterId)
    return result
    
def SignReward3715(dynamicId,characterId):
    '''签到
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':u""}
    delta = datetime.datetime.now()
    data = dbCharacter.getlastsignByCharacterId(characterId)
    lastsign = data["lastsignday"]
    times = data["signtimes"]
    if lastsign < delta.day :
        times += 1
        addcoin = player.finance.addCoin(10000)
        newstone = dbItems.getItem(characterId,60001)[0]['stack']
        nums =  newstone + 5
        result = dbItems.setStack(nums,characterId,60001)
        dbCharacter.sign1(characterId,delta.day)
        dbCharacter.signtimes(characterId,times)
        print {"message":result,'data':{"signtimes":times}}
        return {"message":result,'data':{"signtimes":times}}
    return {"message":'got','data':{"signtimes":times}}

def getReward3711(dynamicId,characterId):
    '''签到奖励
    '''
    player = PlayerCharacter(characterId,dynamicId = dynamicId)
    #player.updatePlayerDBInfo
    dat = dbCharacter.getreward(characterId)
    data = dat[0]
    i1 = int(data / 1000)
    i2 = int((data - i1 * 1000)/100)
    i3 = int((data - i2 * 100 - i1 * 1000)/10)
    i4 = int(data - i2 * 100 - i1 * 1000 - i3 * 10)
    signtimes = dbCharacter.getlastsignByCharacterId(characterId)['signtimes']
    result11 = False
    result2 = False
    result3 = False
    result4 = False


    if i1 == 1 and signtimes>2:
        addcoin = player.finance.addCoin(50000)
        addgold = player.finance.addGold(10)
        player.updatePlayerDBInfo()
        print(addcoin,addgold)
        newstone = dbItems.getItem(characterId,60001)[0]['stack']
        nums =  newstone + 5
        result11 = dbItems.setStack(nums,characterId,60001)
        i1 += 1

    if  i2 == 1  and signtimes>6:
        i2 += 1
        player.finance.addCoin(80000)
        player.finance.addGold(30)
        newstone = dbItems.getItem(characterId,60001)[0]['stack']
        newstone += 20
        result2 =  dbItems.setStack(newstone,characterId,60001)
    if  i3 == 1  and signtimes>14:
        i3 += 1
        player.finance.addCoin(200000)
        player.finance.addGold(60)
        newstone = dbItems.getItem(characterId,60001)[0]['stack']
        newstone += 80
        result3 = dbItems.setStack(newstone,characterId,60001)

    if  i4 == 1  and signtimes> 24:
        i4 += 1
        player.finance.addCoin(300000)
        player.finance.addGold(100)
        newstone = dbItems.getItem(characterId,60001)[0]['stack']
        newstone += 150
        result4 = dbItems.setStack(newstone,characterId,60001)

    newdata = i1*1000 + i2*100 + i3*10 + i4
    genxin = dbCharacter.updatePlayerDB(player)
    result1 = dbCharacter.setget(characterId,newdata)
    print {"message":{'3':result11,'7':result2,'15':result3,'25':result4}}
    return {"message":{'3':result11,'7':result2,'15':result3,'25':result4}}






