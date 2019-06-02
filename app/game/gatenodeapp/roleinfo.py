#coding:utf8
'''

'''
from app.game.gatenodeservice import remoteserviceHandle
from app.game.appinterface import roleinfo
import json
    
@remoteserviceHandle
def RoleInfo_105(dynamicId,request_proto):
    '''获取角色的状态栏信息
    '''
    argument = json.loads(request_proto)
    print (1,argument)
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






