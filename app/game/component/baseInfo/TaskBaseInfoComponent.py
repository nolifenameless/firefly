__author__ = 'Administrator'
#coding:utf8


from app.game.component.baseInfo.BaseInfoComponent import BaseInfoComponent


class TaskBaseInfoComponent(BaseInfoComponent):
    '''任务基础信息组件类'''
    def __init__(self, owner, cid, taskcompleted=0 ,taskrewarded=0,):
        '''
        Constructor
        '''
        BaseInfoComponent.__init__(self, owner, cid, taskcompleted,taskrewarded)
        self._tasktype = tasktype  #任务类型


    #----------------taskcompleted-----------

    def taskcompleted(self,taskcompleted):#从数据库中读取后赋值
        self.taskcompleted = taskcompleted

    def getNickName(self):#获取内存中的值
        return self._taskcompleted

    def setType(self ,tasktype):#
        self._tasktype = tasktype

    def getType(self):
        return self._tasktype

