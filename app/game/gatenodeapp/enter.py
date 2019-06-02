#coding:utf8
'''
Created on 2013-8-14

'''
from app.game.gatenodeservice import remoteserviceHandle
from app.game.core.character.PlayerCharacter import PlayerCharacter
from app.game.core.PlayersManager import PlayersManager
from app.game.core.MatchManager import MatchManager
from app.share.dbopear import dbCharacter
import datetime



@remoteserviceHandle
def enterPlace_601(dynamicId,characterId,player):
    '''进入场景'''
    if not player:
        player = PlayerCharacter(characterId,dynamicId = dynamicId)
    PlayersManager().addPlayer(player)


    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print ('time',now)
    result = dbCharacter.setlogintime(characterId)
    print result

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
                            'sex':playerinfo['sex']}
                    }
    print responsedata


    return True

@remoteserviceHandle
def startmatch_602(dynamicId,characterId):
    '''进入匹配'''
    if 1:
        player = PlayerCharacter(characterId,dynamicId = dynamicId)
    MatchManager().addPlayer(player)
    data = player.arena.getArenaAllInfo()
    matchlist =  player.arena.getall()
    arenadata = {'result':True,'message':'',
                    'data':{'cid':data['id'],
                            'name':data['nickname'],
                            'score':data['score'],
                            }
                    }
    print arenadata
    print matchlist
    return arenadata
