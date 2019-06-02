#coding:utf8
'''


'''
from app.game.gatenodeservice import remoteserviceHandle
import json
from app.game.appinterface import packageInfo

@remoteserviceHandle
def getItemsInEquipSlot_203(dynamicId,request_proto):
    """获取角色的装备栏信息
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    response = packageInfo.getItemsInEquipSlotNew(dynamicId, characterId)
    print response
    return json.dumps(response)

@remoteserviceHandle
def getItemInPackage_204(dynamicId,request_proto):
    """获取角色的包裹信息
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    response = packageInfo.GetPackageInfo(dynamicId, characterId)
    print json.dumps(response)
    return json.dumps(response)

@remoteserviceHandle
def getWeaponInPackage_220(dynamicId,request_proto):
    """获取角色的包裹武器信息
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    response = packageInfo.GetWeaponInfo(dynamicId, characterId)
    print json.dumps(response)
    return json.dumps(response)

@remoteserviceHandle
def getWeaponInPackage_250(dynamicId,request_proto):
    """获取角色的包裹准备强化武器信息
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    response = packageInfo.GetWeaponInfo(dynamicId, characterId)
    response1 = packageInfo.getWeaponInEquipSlotNew(dynamicId, characterId)
    stonenum = packageInfo.GetStoneInfo(dynamicId, characterId)
    print response
    print 1
    response.update(response1)
    response.update(stonenum)
    print json.dumps(response)
    return json.dumps(response)

@remoteserviceHandle
def getSkillInPackage_230(dynamicId,request_proto):
    """获取角色的包裹技能信息
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    response = packageInfo.GetSkillInfo(dynamicId, characterId)
    print json.dumps(response)
    return json.dumps(response)

@remoteserviceHandle
def getSkillInPackage_240(dynamicId,request_proto):
    """获取角色的包裹时装信息
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    response = packageInfo.GetFashionInfo(dynamicId, characterId)
    print json.dumps(response)
    return json.dumps(response)


@remoteserviceHandle
def UserWeaponNew_210(dynamicId,request_proto):
    """使用穿戴物品
    """
    argument = json.loads(request_proto)
    print argument
    characterId = argument.get('characterId')
    tempid = argument.get('itemid')
    response = packageInfo.userweaponreplace(dynamicId,characterId,tempid)
    print json.dumps(response)
    return json.dumps(response)

@remoteserviceHandle
def replaceSkill_209(dynamicId,request_proto):
    """使用穿戴物品
    """
    argument = json.loads(request_proto)
    print argument
    characterId = argument.get('characterId')
    tempid = argument.get('itemid')
    pos = argument.get('pos')
    response = packageInfo.userskillreplace(dynamicId,characterId,tempid,pos)
    print json.dumps(response)
    return json.dumps(response)



@remoteserviceHandle
def unloadedEquipment_215(dynamicId,request_proto):
    """取下装备
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    itemId = argument.get('itemid')
    response = packageInfo.unloadedEquipment_new(dynamicId, characterId, itemId)
    print json.dumps(response)
    return json.dumps(response)

@remoteserviceHandle
def QianghuaEquipment_2000(dynamicId,request_proto):
    """强化装备
    """
    argument = json.loads(request_proto)
    characterId = argument.get('characterId')
    itemId = argument.get('itemid')
    response = packageInfo.qianghua(dynamicId,  characterId,  itemId)
    print json.dumps(response)
    return json.dumps(response)

