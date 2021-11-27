# Egg.py
# Egg 蛋存在的目的是为了以最小的字节数串行化存储Frog,它是Frog的生成算法描述，而不是Frog本身，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
# 它的母体，而且每一次测试，大部分条件反射的建立都必须从头开始训练，类似于人类，无论人类社会有多聪明，婴儿始终是一张白纸，需要花大量的时间从头学习。
# -----------------------------------------------------------------------------------------------------------------------
from version.egg.CellGroup import CellGroup
from version.egg.OrganDesc import OrganDesc
from version.brain.Organ import Organ
from configs import *

class Egg(object):
    cellGroups=[]
    organDescs=[]

    randomCellGroupQty=30 #随机生成多少个组
    randomCellQtyPerGroup=3 #每个组有多少个脑细胞
    randomInputQtyPerCell=3 #每个脑细胞有多少个输入触突(神经末梢)
    randomOutputQtyPerCell=2 #每个脑细胞有多少个输出触突(树突)

    def __init__(self,*args):
        if len(args)==0:
            pass
        if len(args)==2:
            xEgg,yEgg=args
            if not isinstance(xEgg,Egg) or not isinstance(yEgg,Egg):
                raise TypeError
            cellGroups=[]
            for i in range(len(xEgg.cellGroups)):
                oldCellGroup=xEgg.cellGroups[i]
                newCellGroup=CellGroup(oldCellGroup)
                newCellGroup.inherit=True
                cellGroups.append(newCellGroup)
            yGroup=yEgg.cellGroups[nextInt(len(yEgg.cellGroups))-1]
            cellGroups.append(yGroup)
            for i in range(self.randomCellGroupQty):
                cellGroups.append(CellGroup(FROG_BRAIN_LENGTH,xEgg.randomCellQtyPerGroup,
                                            xEgg.randomInputQtyPerCell,xEgg.randomOutputQtyPerCell))
            self.addOrganDescs()


    def createBrandNewEgg(self):#随即制造一个新的Egg
        egg=Egg()
        for i in range(egg.randomCellGroupQty):
            egg.cellGroups.append(CellGroup(FROG_BRAIN_LENGTH,egg.randomCellQtyPerGroup,
                                            egg.randomInputQtyPerCell,egg.randomOutputQtyPerCell))
        egg.addOrganDescs()
        return egg

    def addOrganDescs(self):
        self.organDescs=[]
        self.organDescs.append(OrganDesc(Organ.HUNGRY,300,100,100))
        self.organDescs.append(OrganDesc(Organ.UP,800,400,60))
        self.organDescs.append(OrganDesc(Organ.DOWN,800,100,60))
        self.organDescs.append(OrganDesc(Organ.LEFT,700,250,60))
        self.organDescs.append(OrganDesc(Organ.RIGHT,900,250,60))
        self.organDescs.append(OrganDesc(Organ.EAT,0,0,0))