#coding:utf8
'''
Created on 2013-3-18


'''
from app.game.core.PlayersManager import PlayersManager
from app.share.dbopear import dbCharacter
from app.share.dbopear import dbarena

def roleInfo(dynamicId,characterId):
    '''获取角色的状态栏信息
    @param userId: int 用户id
    @param characterId: 角色的id 
    '''
    player = PlayersManager().getPlayerBydynamicId(dynamicId)
    if dynamicId != player.getDynamicId():
        return {'result':False,'message':""}
    playerinfo = player.formatInfo()
    responsedata = {'message':'hasrole',
                    'result': True,
                    'data':{'cid': playerinfo['id'],
                            'name': playerinfo['nickname'],
                            'level':playerinfo['level'],
                            'viplevel':playerinfo['viplevel'],
                            'exp':playerinfo['exp'],
                            # 'maxexp':playerinfo['maxExp'],
                            'coin':playerinfo['coin'],
                            'zuanshi':playerinfo['gold'],
                            'tili':playerinfo['energy'],
                            'sex':playerinfo['sex'],
                            "score":dbarena.getCharacterScoreRank(characterId)['score']}
                    }
    return responsedata

def newname(dynamicId,characterId,newname):
    '''玩家改名
    @param userId: int 用户id
    @param characterId: 角色的id
    '''
    player = PlayersManager().getPlayerBydynamicId(dynamicId)
    if dynamicId != player.getDynamicId():
        return {'result':False,'message':""}
    player.baseInfo.setnickName(newname)
    name = player.baseInfo.getNickName()
    print name
    genxin = dbCharacter.updatePlayerDB(player)
    playerinfo = player.formatInfo()
    responsedata = {'result':True,'message':'',
                    'data':{ 'rolename':playerinfo['nickname']}}
    return responsedata
