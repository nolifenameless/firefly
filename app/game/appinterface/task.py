#coding:utf8
'''
Created on

__author__ = 'Administrator'
'''
from app.game.core.PlayersManager import PlayersManager
from app.share.dbopear import dbTask
from app.share.dbopear import dbCharacter
from app.share.dbopear import dbItems
from app.game.core.character.PlayerCharacter import PlayerCharacter
import datetime

def verifytasks(dynamicId,characterId):
    '''检验角色的主线任务信息
    @param userId: int 用户id
    @param characterId: 角色的id
    '''
    player = PlayersManager().getPlayerBydynamicId(dynamicId)
    if dynamicId != player.getDynamicId():
        return {'result':False,'message':""}
    player = PlayersManager().getPlayerByID(characterId)

    taskinfo = dbTask.getTaskInfo(characterId)

    print taskinfo
    tasklist = [101,102,103,104,105,106,107,108,109,110,111]

    #101
    #if player.level.getLevel() < 40:
        #if player.level.getLevel()>=

    length = len(taskinfo)
    taskdata = {}
    for i in range(0,length):
        #101
        if taskinfo[i]['taskId'] == 101:
            if player.level.getLevel() >= taskinfo[i]['ifrewarded']:

                dbTask.setPersonalTaskaInfo(characterId,101,1)
        #102
        if taskinfo[i]['taskId'] == 102:
            pass




    #for i in range(0,length):

    taskdata.update({"tasklist":taskinfo})
    taskdata["taskNums"] = length
    print taskdata
    return taskdata

def Maintaskreward(dynamicId,characterId,taskId):
    '''玩家主要任务奖励发放
    @param userId: int 用户id
    @param characterId: 角色的id
    '''
    player = PlayerCharacter(characterId,dynamicId = dynamicId)
    #player = PlayersManager().getPlayerByID(characterId)
    taskinfo = dbTask.getPersonalTaskInfo(characterId,taskId)
    print taskinfo
    rewardlist = {}
    if taskinfo[0]['ifachieved'] == 1:
        if taskId == 101:
            #升级
            rewardlist.update({"Gold":5*player.formatInfo()['level']})
            print (taskinfo[0]['ifrewarded']+1)
            RewardCleanOut(dynamicId,characterId,rewardlist)
            i = taskinfo[0]['ifrewarded']+1
            resutl = dbTask.setPersonalTaskrInfo(characterId,101,int(i))
            resutl1 = dbTask.setPersonalTaskaInfo(characterId,101,0)
            return {'message':resutl}


        if taskId == 102:
            #过副本
            rewardlist.update({"Coin":10000})
            RewardCleanOut(dynamicId,characterId,rewardlist)
            pass
        if taskId == 103:
            #签到

            pass
        if taskId == 104:
            #商城
            pass
        if taskId == 105:
            #好友
            rewardlist.update({"Coin":10000})
            pass
        if taskId == 106:
            #喇叭
            rewardlist.update({"Coin":10000})
            pass
        if taskId == 107:
            #天梯
            pass
        if taskId == 108:
            #强化
            pass
        if taskId == 109:
            #宠物
            pass
        if taskId == 110:
            #装扮宠物房间
            pass
        if taskId == 111:
            #在告白墙发一次告白
            pass
        if taskId == 112:
            #结婚
            pass
        if taskId == 113:
            #装扮情侣空间
            rewardlist.update({"Gold":10})
            pass
        if taskId == 114:
            #种下爱情树
            rewardlist.update({"Gold":50})
            pass
        if taskId == 115:
            #第一次情侣蜜语
            rewardlist.update({"Coin":50000})
            pass
        if taskId == 116:
            #建立一个王国
            rewardlist.update({"Gold":100})
            pass

def RewardCleanOut(dynamicId,characterId,orders):
    '''奖励发放'''

    player = PlayersManager().getPlayerBydynamicId(dynamicId)
    if dynamicId != player.getDynamicId():
        return {'result':False,'message':""}
    if 'Coin' in orders:
        coinadd = orders['Coin']
        player.finance.addCoin(coinadd)
    if 'Gold' in orders:
        goldadd = orders['Gold']
        player.finance.addGold(goldadd)
        print 1
    if 'stone' in orders:
        stoneadd = orders['stone']
        newstone = dbItems.getItem(characterId,60001)[0]['stack']
        newstone += stoneadd
        result2 =  dbItems.setStack(newstone,characterId,60001)

    #hornadd = orders['horn']
    #gloryadd = orders['glory']

def verifydailytasks(dynamicId,characterId):
    '''日常任务校验'''

    player = PlayersManager().getPlayerBydynamicId(dynamicId)
    if dynamicId != player.getDynamicId():
        return {'result':False,'message':""}
    #player = PlayersManager().getPlayerByID(characterId)
    taskinfo = dbTask.getDailyTaskInfo(characterId)


    length = len(taskinfo)
    taskdata = {}
    for i in range(0,length):
        #登录 30min
        if taskinfo[i]['taskId'] == 100001:
            logintime = dbCharacter.getloginTime(characterId)
            delta = datetime.datetime.now()-logintime[0]
            deltasecond = delta.days*86400+delta.seconds
            if  deltasecond <1801:
                mins = deltasecond/60
                min = int(mins) + 2
                print min
            if min < 4:
                dbTask.setDailyTaskaInfo(characterId,100001,min)
            if min >= 4:
                print 11111
                dbTask.setDailyTaskaInfo(characterId,100001,1)


        #强化
        if taskinfo[i]['taskId'] == 102:
            pass
    taskinfo1 = dbTask.getDailyTaskInfo(characterId)
    taskdata.update({"tasklist":taskinfo1})
    taskdata["taskNums"] = length

    print taskdata
    return taskdata


def dailytaskreward(characterId,dynamicId,dtaskId):
    '''日常任务奖励'''
    player = PlayersManager().getPlayerByID(characterId)
    taskinfo = dbTask.getpointedDailyTaskInfo(characterId,dtaskId)
    print taskinfo
    rewardlist = {}
    if taskinfo[0]['ifachieved'] == 1:
        if dtaskId == 100001:
            #在线30min
            rewardlist.update({"Gold":10})
            rewardlist.update({"Coin":10000})
            RewardCleanOut(dynamicId,characterId,rewardlist)
            resutl = dbTask.setDailyTaskrInfo(characterId,100001,1)
            result = RewardCleanOut(dynamicId,characterId,rewardlist)
            return {'message':resutl}

        if dtaskId == 100010:
            #强化一次装备
            rewardlist.update({"stone":2})
            RewardCleanOut(dynamicId,characterId,rewardlist)
            i = 1
            resutl = dbTask.setDailyTaskrInfo(characterId,100010,int(i))
            result = RewardCleanOut(dynamicId,characterId,rewardlist)
            return {'message':resutl}
        return False

























