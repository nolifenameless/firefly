#coding:utf8
'''
Created on 2013-1-8

@author: lan (www.9miao.com)
'''

from app.game.core.PlayersManager import PlayersManager
from app.share.dbopear import dbZhanyi
from app.game.appinterface import packageInfo

def getZhanYiInfo(dynamicId,characterId ,index):
    '''获取角色的战役信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    zhanyiinfo = player.zhanyi.getZhanYiInfo(index)
    return zhanyiinfo

def zhangjieFight(dynamicId,characterId,zhangjieid):
    '''章节战斗
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}

    return False

def getfubenInfo(dynamicId,characterId):
    '''
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    result = dbZhanyi.getfubenInfo(characterId)[0][0]
    return {'record':result}

def setfubenInfo(dynamicId,characterId,argument):
    '''
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    #times = argument.get('times')


    if argument.has_key('process'):
        proc = argument.get('process')
        if proc > dbZhanyi.getfubenInfo(characterId):
            result = dbZhanyi.getfubenInfo(characterId,proc)

    if argument.has_key('coin'):
        coin = argument.get('coin')
        player.finance.addCoin(coin)

    if argument.has_key('exp'):
        exp = argument.get('exp')
        nowtili = player.attribute.getEnergy()
        print nowtili
        if (nowtili + exp) < 0:
            return {'message':'no enough tili'}
        player.level.addExp(exp)

    if argument.has_key('itemlist'):
        itemlist = argument.get('itemlist')
        packageInfo.GetNewItem(dynamicId,characterId,itemlist)



    if argument.has_key('itemcost'):
        itemcost = argument.get('itemcost')







    if argument.has_key('glory'):
        glory = argument.get('glory')

    if argument.has_key('gold'):
        gold = argument.get('gold')
        player.finance.addGold(gold)












    return {'message':True}





