# Egg.py
# Egg 蛋存在的目的是为了以最小的字节数串行化存储Frog,它是Frog的生成算法描述，而不是Frog本身，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
# 它的母体，而且每一次测试，大部分条件反射的建立都必须从头开始训练，类似于人类，无论人类社会有多聪明，婴儿始终是一张白纸，需要花大量的时间从头学习。
# -----------------------------------------------------------------------------------------------------------------------
from history.version2.egg.CellGroup import CellGroup
from history.version2.egg.Zone import Zone
from history.version2.egg.OrganDesc import OrganDesc
from configs import *

class Egg(object):
    randomCellGroupQty=30#随机生成多少个组
    randomCellQtyPerGroup=3#每个组有多少个脑细胞
    randomInputQtyPerCell=3#每个脑细胞有多少个输入触突
    randomOutputQtyPerCell=2#每个脑细胞有多少个输出触突

    cellgroups=[]
    organdescs=[]

    def __init__(self):
        pass#default constructor

    def initByXY(self,x,y):
        #模拟XY染色体,不能做简单加法,会撑暴内存的,现在每次只随机加一个Y的Cellgroup进来,这也不太好,因为基因会越加越多,只好用用进废退原则来加大淘汰率
        if not isinstance(x,Egg) or not isinstance(y,Egg):
            raise TypeError
        self.cellgroups=[]
        for i in range(len(x.cellgroups)):
            oldCellGroup:CellGroup=x.cellgroups[i]
            cellGroup=CellGroup()
            cellGroup.initByOldCellGroup(oldCellGroup=oldCellGroup)
            cellGroup.inherit=True
            self.cellgroups.append(cellGroup)
        randomY=y.cellgroups[nextInt(len(y.cellgroups))-1]
        cellGroup=CellGroup()
        cellGroup.initByOldCellGroup(oldCellGroup=randomY)
        self.cellgroups.append(cellGroup)
        for i in range(self.randomCellGroupQty):
            cellGroup=CellGroup()
            cellGroup.initByRandom(brainLength=FROG_BRAIN_LENGTH,
                                   randomCellQtyPerGroup=x.randomCellQtyPerGroup,
                                   randomInputQtyPerCell=x.randomInputQtyPerCell,
                                   randomOutputQtyPerCell=x.randomOutputQtyPerCell)
            self.cellgroups.append(cellGroup)
        self.addOrganDescs()

    #create egg from frog
    def initByFrog(self,frog):#青蛙下蛋,蛋的基因生成遵循用进废退,随机变异两个原则
        for i in range(len(frog.cellgroups)):
            if frog.cellgroups[i].fat<=0:
                if not frog.cellgroups[i].inherit:continue#从未激活过的神经元,并且就是本轮随机生成的,丢弃之
                if percent(5):continue#继承下来的神经元,但是本轮并没用到,扔掉又可惜,可以小概率丢掉
            oldCellGroup=CellGroup()
            cellGroup=CellGroup()
            cellGroup.groupInputZone=Zone(vary(oldCellGroup.groupInputZone.x),vary(oldCellGroup.groupInputZone.y),
                                          vary(oldCellGroup.groupInputZone.radius))
            cellGroup.groupOutputZone=Zone(vary(oldCellGroup.groupOutputZone.x),vary(oldCellGroup.groupOutputZone.y),
                                           vary(oldCellGroup.groupOutputZone.radius))
            cellGroup.cellQty=round(vary(oldCellGroup.cellQty))
            cellGroup.cellInputRadius=vary(oldCellGroup.cellInputRadius)
            cellGroup.cellOutputRadius=vary(oldCellGroup.cellOutputRadius)
            cellGroup.inputQtyPerCell=round(oldCellGroup.inputQtyPerCell)
            cellGroup.outputQtyPerCell=round(oldCellGroup.outputQtyPerCell)
            cellGroup.inherit=True
            self.cellgroups.append(cellGroup)
        self.addOrganDescs()

    #create a brand new Egg
    @staticmethod
    def createBrandNewEgg():#无中生有,随机制造一个新的Egg
        egg=Egg()
        for i in range(egg.randomCellGroupQty):
            cellGroup=CellGroup()
            cellGroup.initByRandom(brainLength=FROG_BRAIN_LENGTH,
                                   randomCellQtyPerGroup=egg.randomCellQtyPerGroup,
                                   randomInputQtyPerCell=egg.randomInputQtyPerCell,
                                   randomOutputQtyPerCell=egg.randomOutputQtyPerCell)
            egg.cellgroups.append(cellGroup)
        egg.addOrganDescs()
        return egg

    def addOrganDescs(self):
        self.organdescs=[]
        self.organdescs.append(OrganDesc(HUNGRY,300,100,100))
        self.organdescs.append(OrganDesc(UP,800,400,60))
        self.organdescs.append(OrganDesc(DOWN,800,100,60))
        self.organdescs.append(OrganDesc(LEFT,700,250,60))
        self.organdescs.append(OrganDesc(RIGHT,900,250,60))
        self.organdescs.append(OrganDesc(EAT,0,0,0))