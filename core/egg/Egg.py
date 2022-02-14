#Egg.py
#Egg 蛋存在的目的是为了以最小的字节数串行化存储Frog,它是Frog的生成算法描述，而不是Frog本身，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
#它的母体，而且每一次测试，大部分条件反射的建立都必须从头开始训练，类似于人类，无论人类社会有多聪明，婴儿始终是一张白纸，需要花大量的时间从头学习。
#-----------------------------------------------------------------------------------------------------------------------
from core.egg.CellGroup import CellGroup
from core.egg.Zone import Zone
from configs import *

class Egg(object):
    def __init__(self,CELL_GROUP_QTY=30,brainRadius=1000,cellgroups=None):
        if cellgroups is None:cellgroups=[]
        self.CELL_GROUP_QTY:int=CELL_GROUP_QTY
        self.brainRadius:float=brainRadius
        self.cellgroups:list[CellGroup]=cellgroups

    @staticmethod
    def createBrandNewEgg():#随机制造一个新的Egg
        egg=Egg()
        for i in range(egg.CELL_GROUP_QTY):
            cellGroup=CellGroup()
            cellGroup.groupInputZone=Zone(x=nextFloat()*egg.brainRadius,y=nextFloat()*egg.brainRadius,
                                          radius=float(nextFloat()*egg.brainRadius*0.01))
            cellGroup.groupOutputZone=Zone(x=nextFloat()*egg.brainRadius,y=nextFloat()*egg.brainRadius,
                                          radius=float(nextFloat()*egg.brainRadius*0.01))
            cellGroup.cellQty=nextInt(10)
            cellGroup.cellInputRadius=float(nextFloat()*0.001)
            cellGroup.cellOutputRadius=float(nextFloat()*0.001)
            cellGroup.inputQtyPerCell=nextInt(10)
            cellGroup.outputQtyPerCell=nextInt(5)
            egg.cellgroups.append(cellGroup)
        return egg