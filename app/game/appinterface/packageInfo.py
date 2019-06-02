#coding:utf8
'''


'''
from app.game.core.PlayersManager import PlayersManager
from app.game.core.pack import EquipmentSlot
from app.gate.appinterface import login
import json,datetime
from app.gate.gateservice import localserviceHandle
from app.game.core.character.PlayerCharacter import PlayerCharacter
import random,math
from app.game.component.baseInfo.ItemBaseInfoComponent import ItemBaseInfoComponent
from app.game.component.attribute.ItemAttributeComponent import ItemAttributeComponent
from app.game.component.pack.ItemPackComponent import ItemPackComponet
from app.share.dbopear import dbItems
from app.game.memmode import tbitemadmin
    
def getItemsInEquipSlotNew(dynamicId,characterId):
    '''获取角色的装备栏信息
    @param dynamicId: int 客户端的id
    @param characterId: int 角色的id
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    equipmentList = player.pack.getEquipmentSlotItemList()
    keys_copy = dict(equipmentList)
    equipmentList_copy = []
    for position in range(0,8):
        item = keys_copy.get(position,None)
        if item:
            _item = {}
            _item['id'] = item.baseInfo.id
            _item['strengthen'] = dbItems.getItem(characterId,item.baseInfo.id)[0]['strengthen']
            _item['tempid'] = item.baseInfo.getItemTemplateId()
            #_item['pos'] = position
            #_item['item'] = _item
            #_item['stacks'] = item.pack.getStack
            iteminfo = {'pos':position,'item':_item}
            equipmentList_copy.append(iteminfo)
    #playerInfo = player.formatInfoForWeiXin()
    #data = {}
    #data['equip'] = equipmentList_copy
    #data['attack'] = playerInfo['attack']
    #data['fangyu'] = playerInfo['fangyu']
    #data['blood'] = playerInfo['blood']
    return {'result':True,'message':u'','data':equipmentList_copy}

def getWeaponInEquipSlotNew(dynamicId,characterId):
    '''获取角色的装备武器信息
    @param dynamicId: int 客户端的id
    @param characterId: int 角色的id
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    equipmentList = player.pack.getEquipmentSlotItemList()
    keys_copy = dict(equipmentList)
    position = 0
    item = keys_copy.get(position,None)
    if item:
        _item = {}
        _item['id'] = item.baseInfo.id
        _item['strengthen'] = dbItems.getItem(characterId,item.baseInfo.id)[0]['strengthen']
        _item['tempid'] = item.baseInfo.getItemTemplateId()
        iteminfo = {'item':_item}
    return {'wearing':iteminfo}


def UserItemNew(dynamicId,characterId,tempid):
    '''使用物品
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':"234"}
    data = player.pack.equipEquipmentByItemId(tempid)
    return data

def userweaponreplace(dynamicId,characterId,tempid):
    '''替换武器
    '''
    pos = 0
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':"234"}
    data = player.pack.equipEquipmentByItemIdPos(tempid,pos)
    return data

def userskillreplace(dynamicId,characterId,tempid,pos):
    '''替换技能
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':"234"}
    data = player.pack.equipEquipmentByItemIdPos(tempid,pos)
    return data
    
def GetPackageInfo(dynamicId,characterId):
    '''获取包裹的信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    data = player.pack.getPackageItemList()
    return data

def GetStoneInfo(dynamicId,characterId):
    '''获取强化石的信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    data = player.pack.getStoneNum(characterId)
    return data
    
def GetWeaponInfo(dynamicId,characterId):
    '''获取武器的信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    data = player.pack.getWeaponList(characterId)
    return data

def GetSkillInfo(dynamicId,characterId):
    '''获取包裹技能的信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    data = player.pack.getSkillList()
    return data

def GetFashionInfo(dynamicId,characterId):
    '''获取包裹时装的信息
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    data = player.pack.getFashionList()
    return data

def unloadedEquipment_new(dynamicId, characterId, itemId):
    '''卸下装备
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    data = player.pack.unloaded(itemId)
    return data
    

def qianghua(dynamicId,characterId,itemId):
    '''获取包裹的信息
    '''
    player = PlayerCharacter(characterId,dynamicId = dynamicId)
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    playerinfo = player.formatInfo()
    data = dbItems.getItem(characterId,itemId)
    level = data[0]
    weaponlevel1 = level["strengthen"]
    playerlvl = playerinfo['level']
    if weaponlevel1 > playerlvl * 2:
        result = {'resutl':False,"message":"level limited"}
        return result

    stonedata = dbItems.getItem(characterId,60001)
    stonenums = stonedata[0]
    stonenum = stonenums["stack"]
    Maxqianghualevel = int(int(playerinfo['viplevel']) / 2)

    stonecost = int(weaponlevel1 * 2)
    if (stonenum - stonecost)<0:
        result = {'resutl':False,"message":"no enough stone"}
        return result

    b2 = math.pow(1.07,weaponlevel1)
    need = int(b2*(weaponlevel1*70 + 40))

    money = player.finance.getCoin()
    if money < need :
        result = {'resutl':False,"message":"no enough coin"}
        return result



    levelup = random.randint(1,Maxqianghualevel)
    count = weaponlevel1 + levelup
    data = player.pack.qianghua(itemId,count,characterId)

    result = {'resutl':True,"message":"success","data":levelup}
    if data:
        stonenum = stonenum - stonecost
        dbItems.setStack(stonenum,characterId,60001)
        player.finance.addCoin(-need)

        return result

def GetNewItem(dynamicId,characterId,list):
    '''
    获得物品
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    plist = player.pack.getPackageItemList()['data']['itemlist']
    print list
    print plist
    length = len(list)
    length2 = len(plist)
    print (length,length2)
    print list[1]['itemid']
    print plist[1]['tempid']
    needdel = []
    for i in range(0,length):
        for j in range(0,length2):
            if list[i]['itemid'] == plist[j]['tempid']:
                s = dbItems.getItem(characterId,plist[j]['itemid'])[0]['stack'] + 1
                dbItems.setStack(s,plist[j]['itemid'],characterId)
                needdel.append(i)
                print ('same',i)
                print needdel
    if needdel:
        lendel = len(needdel)
        needdel.reverse()
        for i in range (0,lendel):
            print ('i',i)
            a = needdel[i]
            print ('a',a)
            del list[a]

    print ('needdel',needdel)
    print ('left',list)

    newlength = len(list)
    for i in range (0,newlength):
        data = {'characterId':characterId,
                 'itemTemplateId':list[i]['itemid'],
                 'isBound':0,
                  'accesstime':datetime.datetime.now(),
                  'durability':0,
                  'stack':1,'strengthen':0,
                  'workout':0,'slot_1':0,'slot_2':0,
                  'slot_3':0,'slot_4':0,'exp':0}
        newitemmode = tbitemadmin.new(data)
        itemId = int(newitemmode._name.split(':')[1])
        print itemId



def CostItem(dynamicId,characterId,list):
    '''
    获得物品
    '''
    player = PlayersManager().getPlayerByID(characterId)
    if not player or not player.CheckClient(dynamicId):
        return {'result':False,'message':""}
    plist = player.pack.getPackageItemList()['data']['itemlist']
    length = len(list)
    length2 = len(plist)
    needdel = []
    for i in range(0,length):
        for j in range(0,length2):
            if list[i]['itemid'] == plist[j]['itemid']:
                #s = dbItems.getItem(characterId,plist[j]['itemid'])[0]['stack'] + 1
                dbItems.setStack(list[i]['num'],plist[j]['itemid'],characterId)
                needdel.append(i)
    if needdel:
        lendel = len(needdel)
        needdel.reverse()
        for i in range (0,lendel):
            a = needdel[i]
            del list[a]

    print ('needdel',needdel)
    print ('left',list)

    newlength = len(list)
    for i in range (0,newlength):
        data = {'characterId':characterId,
                 'itemTemplateId':list[i]['itemid'],
                 'isBound':0,
                  'accesstime':datetime.datetime.now(),
                  'durability':0,
                  'stack':1,'strengthen':0,
                  'workout':0,'slot_1':0,'slot_2':0,
                  'slot_3':0,'slot_4':0,'exp':0}
        newitemmode = tbitemadmin.new(data)
        itemId = int(newitemmode._name.split(':')[1])
        print itemId
