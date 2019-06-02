#coding:utf8
'''

'''
from app.share.dbopear import dbItems
from app.game import util
from app.game.memmode import tb_equipment

BODYTYPE = ['weapon','skill1','skill2','skill3',
            'skill4','head','cloth','wings','decorate']
    
class EquipmentSlot:
    '''角色装备栏'''
    #装备栏中装备位置编号（item的bodytype，装备在身体的部位）
    #0=武器
    #1=技能1
    #2=技能2
    #3=技能3
    #4=技能4
    #5=头部
    #6=衣服
    #7=翅膀
    #8=饰品

    def __init__(self,size = 10):
        '''
        @param size: int 包裹的大小
        '''
        self._items = {}
        
    def putEquipmentInEquipmentSlot(self,parts,equipmentid):
        '''根据数据库获取的信息设置物品
        @param part: str 部位名称
        @param equipment:  Item object 装备实例
        '''
        if parts in BODYTYPE:
            self._items[BODYTYPE.index(parts)] = equipmentid
        
    def updateEquipment(self,partsId,equipmentid):
        '''更换装备
        @param characterId: int 角色的id
        @param partsId: int 角色的部位的id
        @param equipment: Item object 装备
        '''
        self._items[partsId] = equipmentid
        return True
    
    def getItemByPosition(self, position):
        '''根据坐标得到物品
        @param position: int 物品的位置
        '''
        return self._items.get(position)
    
    def updateEquipments(self,characterid):
        """
        更新装备信息
       """
        prop = {}
        for pos,itemid in self._items.items():
            parts = BODYTYPE[pos]
            prop[parts] = itemid
        equipmentsInfo = tb_equipment.getObj(characterid)
        equipmentsInfo.update_multi(prop)
    
    def getAllEquipttributes(self):
        '''得到玩家装备附加属性列表'''
        EXTATTRIBUTE = {}
        for item in [item['itemComponent'] for item in self._items]:
            info = item.getItemAttributes()
            EXTATTRIBUTE = util.addDict(EXTATTRIBUTE, info)
        equipsetattr = self.getEquipmentSetAttr()
        EXTATTRIBUTE = util.addDict(EXTATTRIBUTE, equipsetattr)
        return EXTATTRIBUTE
    
    def getEquipmentSetCont(self):
        '''获取装备中的装备的套装件数
        '''
        itemsetlist = [item['itemComponent'].baseInfo.itemtemplateInfo['suiteId'] \
                        for item in self._items \
                        if item['itemComponent'].baseInfo.itemtemplateInfo['suiteId']]
        nowsets = set(itemsetlist)
        setcontdict = {}
        for setid in nowsets:
            setcount = itemsetlist.count(setid)
            setcontdict[setid] = setcount
        return setcontdict
    
    def getEquipmentSetAttr(self):
        '''获取套装属性加成
        '''
        itemsetlist = [item['itemComponent'].baseInfo.itemtemplateInfo['suiteId'] \
                        for item in self._items \
                        if item['itemComponent'].baseInfo.itemtemplateInfo['suiteId']]
        nowsets = set(itemsetlist)
        info = {}
        for setid in nowsets:
            setinfo = dbItems.ALL_SETINFO[setid]
            setcount = itemsetlist.count(setid)
            allsetattr = eval(setinfo['effect'])
            for key,value in allsetattr.items():
                if key <= setcount:
                    effect = eval(value.get('effect'))
                    info = util.addDict(info, effect)
        return info
    
    def getItemPositionById(self,itemId):
        '''根据物品的id获取物品的位置'''
        for pos,itemid in self._items.items():
            if itemid==itemId:
                return pos
        return -1
    
