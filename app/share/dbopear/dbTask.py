#coding:utf8
'''
tb_task_completed
tb_task_rewarded

'''
from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor
from twisted.python import log
from firefly.dbentrust import util


def updatePlayerDB(player):
    '''更新角色的数据库任务完成信息'''
    characterId = player.baseInfo.id
    props = {'ifcompleted':player.level.getLevel(),'ifrewarded':player.finance.getCoin()}
    sqlstr = util.forEachUpdateProps('tb_task_completed',props, {'id':characterId})
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


def getTaskInfo(id):
    '''根据ID获取角色的任务完成度
    @param nickname: string 角色的昵称
    '''
    #sql = "select taskId,ifachieved from `tb_task_completed` where characterId ='%d' and ifrewarded = '%d'"%(id,0)

    sql =  "select ifrewarded,ifachieved,taskId from `tb_task_completed`where characterId = '%d' and ifrewarded != '%d'"%(id,1)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def getPersonalTaskInfo(cid,tid):
    '''根据任务ID获取角色的任务完成度
    @param nickname: string 角色的昵称
    '''
    #sql = "select taskId,ifachieved from `tb_task_completed` where characterId ='%d' and ifrewarded = '%d'"%(id,0)
    sql = "select ifrewarded,ifachieved from `tb_task_completed`where characterId = '%d' and taskId = '%d'"%(cid,tid)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result



def setPersonalTaskrInfo(cid,tid,info):
    '''根据任务ID角色设置的任务完成度

    '''
    sql = "update `tb_task_completed` set ifrewarded = '%d' where characterId = '%d' and taskId = '%d'"%(info,cid,tid)
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

def setPersonalTaskaInfo(cid,tid,info):
    '''根据任务ID获取角色的任务完成度
    @param nickname: string 角色的昵称
    '''
    sql = "update `tb_task_completed` set ifachieved = '%d' where characterId = '%d' and taskId = '%d'"%(info,cid,tid)
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


def getDailyTaskInfo(id):
    '''根据ID获取角色的日常任务
    @param nickname: string 角色的昵称
    '''

    sql =  "select ifrewarded,ifachieved,taskId from `tb_dtask`where characterId = '%d' and ifrewarded != '%d'"%(id,1)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def getpointedDailyTaskInfo(cid,tid):
    '''根据任务ID获取角色的日常任务完成度
    @param nickname: string 角色的昵称
    '''

    sql = "select ifrewarded,ifachieved from `tb_dtask`where characterId = '%d' and taskId = '%d'"%(cid,tid)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result



def setDailydTaskrInfo(cid,tid,info):
    '''根据任务ID角色设置的日常任务完成度

    '''
    sql = "update `tb_dtask` set ifrewarded = '%d' where characterId = '%d' and taskId = '%d'"%(info,cid,tid)
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

def setDailyTaskaInfo(cid,tid,info):
    '''根据任务ID获取角色的日常任务完成度
    @param nickname: string 角色的昵称
    '''
    sql = "update `tb_dtask` set ifachieved = '%d' where characterId = '%d' and taskId = '%d'"%(info,cid,tid)
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




def setDailyTaskrInfo(cid,tid,info):
    '''根据任务ID角色设置的任务完成度

    '''
    sql = "update `tb_dtask` set ifrewarded = '%d' where characterId = '%d' and taskId = '%d'"%(info,cid,tid)
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