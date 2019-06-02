#coding:utf8
'''
Created on 2013-1-8
战役相关数据库操作
@author:
'''
from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor


ALL_ZHANYI_INFO = {}#所有的战役的信息
ALL_ZHANGJIE_INFO = {}#所有章节的信息
ALL_ZHANGJIE_GROP = {}#战役与章节关系

def getAllZhanYiInfo():
    '''获取所有战役的信息
    '''
    global ALL_ZHANYI_INFO
    sql = "SELECT * FROM tb_zhanyi"
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    for zhanyi in result:
        ALL_ZHANYI_INFO[zhanyi['id']] = zhanyi
        
        
def getAllZhangJieInfo():
    '''获取章节的信息
    '''
    global ALL_ZHANGJIE_INFO,ALL_ZHANGJIE_GROP
    sql = "SELECT * FROM tb_zhangjie"
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    for zhangjie in result:
        ALL_ZHANGJIE_INFO[zhangjie['id']] = zhangjie
        if not ALL_ZHANGJIE_GROP.get(zhangjie['yid']):
            ALL_ZHANGJIE_GROP[zhangjie['yid']] = []
        ALL_ZHANGJIE_GROP[zhangjie['yid']].append(zhangjie['id'])
            




def getfubenInfo(cid):
    '''根据任务ID获取角色的日常任务完成度
    @param nickname: string 角色的昵称
    '''

    sql = "select zhanyi from `tb_zhanyi_record`where characterId = '%d' "%(cid)
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result



def setfubenInfo(cid,info):
    '''根据任务ID角色设置的日常任务完成度

    '''
    sql = "update `tb_zhanyi_record` set zhanyi = '%d' where characterId = '%d'"%(info,cid)
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