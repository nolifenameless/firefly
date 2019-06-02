#coding:utf8
'''

对物品表（tb_item）的操作
'''
from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor

all_ItemTemplate = {} #所有的物品模板信息
ALL_SETINFO = {}
pointeditem = {}

def getAll_ItemTemplate():
    """获取所有的物品信息
    """
    global all_ItemTemplate
    sql="select * from `tb_item_template`"
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    for _item in result:
        all_ItemTemplate[_item['id']] = _item

def getAllsetInfo():
    '''获取所有的套装信息
    '''
    global ALL_SETINFO
    sql = "SELECT * from tb_equipmentset;"
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    for setinfo in result:
        ALL_SETINFO[setinfo['id']] = setinfo



def getnewItem( characterId,itemId):
    '''
    得到新物品
    '''
    global pointeditem
    sql = "insert into `tb_item`  id ='%d' and  characterId ='%d'"%(itemId, characterId)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    # 执行SQL语句
    cursor.execute(sql)
   # 获取所有记录列表
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def getItem(characterId,itemId):
    """获取指定的物品信息
    """
    global pointeditem
    sql = "select strengthen,stack from `tb_item` where id ='%d' and  characterId ='%d'"%(itemId, characterId)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    # 执行SQL语句
    cursor.execute(sql)
   # 获取所有记录列表
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def setItem(level,characterId,itemId):
    """设定指定的物品信息
    """
    global pointeditem
    sql = "update tb_item set strengthen = %d where id ='%d' and  characterId ='%d'"%(level,itemId, characterId)
    conn = dbpool.connection()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    if count >= 1:
        return True
    else:
        return False

def setStack(level,characterId,itemId):
    """设定指定的物品堆叠
    """
    global pointeditem
    sql = "update tb_item set stack = %d where id ='%d' and  characterId ='%d'"%(level,itemId, characterId)
    conn = dbpool.connection()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    if count >= 1:
        return True
    else:
        return False