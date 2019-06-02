#coding:utf8
'''

'''
from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor
from twisted.python import log
from firefly.dbentrust import util


def updatePlayerDB(player):
    '''更新角色的数据库信息'''
    characterId = player.baseInfo.id
    props = {'level':player.level.getLevel(),'coin':player.finance.getCoin(),'gold':player.finance.getGold(),
             'exp':player.level.getExp(),'nickname':player.baseInfo.getNickName()}
    sqlstr = util.forEachUpdateProps('tb_character',props, {'id':characterId})
    conn = dbpool.connection()
    cursor = conn.cursor()
    count = cursor.execute(sqlstr)
    conn.commit()
    cursor.close()
    conn.close()
    if count >= 1:
        return True
    else:
        log.err(sqlstr)
        return False
    
def getCharacterIdByNickName(nickname):
    '''根据昵称获取角色的id
    @param nickname: string 角色的昵称
    '''
    sql = "select id from `tb_character` where nickname ='%s'"%nickname
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def getloginTime(cid):
    '''获取登录时间
    @param nickname: string 角色的昵称
    '''
    sql = "select logintime from `tb_character` where id='%s'"%cid
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def setlogintime(id):
    '''设置登录时间
    @param loginsign
    '''
    sql = "update `tb_character` set logintime = now()  where id ='%d'"%(id)
    conn = dbpool.connection()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    if count >= 1:
        return True
    else:
        log.err(sql)
        return False

def getNickNameByCharacterId(id):
    '''根据ID获取角色的nickname
    @param nickname: string 角色的昵称
    '''
    sql = "select nickname from `tb_character` where id ='%d'"%id
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
    
def getALlCharacterBaseInfo():
    """获取所有的角色的基础信息
    """
    sql = "SELECT `id`,`level`,`profession`,`nickname` FROM tb_character;";
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def getCharacterBaseInfoById(id):
    """获取指定角色的基础信息
    """
    sql = "SELECT `level`,`profession`,`nickname` FROM tb_character where id ='%d'"%id
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
    

def getlastsignByCharacterId(id):
    '''根据ID获取角色最后签到
    @param loginsign
    '''
    sql = "select lastsignday,signtimes from `tb_character` where id ='%d'"%id
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def sign1(id,day):
    '''签到
    @param loginsign
    '''
    sql = "update `tb_character` set lastsignday = '%d'  where id ='%d'"%(day,id)
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def signtimes(id,times):
    '''签到
    @param loginsign
    '''
    sql = "update `tb_character` set signtimes = '%d'  where id ='%d'"%(times,id)
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def setget(id,nums):
    '''领奖
    @param loginsign
    '''
    sql = "update `tb_character` set reward = '%d'  where id ='%d'"%(nums,id)
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def getreward(id):
    '''根据ID获取角色领取签到
    @param loginsign
    '''
    sql = "select reward from `tb_character` where id ='%d'"%id
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result