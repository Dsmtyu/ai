# CellGroup.py
# CellGroup代表了一束相同功能和结构、分布位置相近的脑神经元，目的是为了下蛋时简化串行化海量的神经元,
# 只需要在egg里定义一组cellGroup就行了，不需要将海量的一个个的神经元串行化存放到egg里，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
# 它的母体，而且每一次测试，一些复杂的条件反射的建立都必须从头开始训练，在项目后期，有可能每个frog生命的一半时间都花在重新建立条件反射的学习过程中。
# -----------------------------------------------------------------------------------------------------------------------

from history.version2.egg.Zone import Zone
from configs import *

class CellGroup(object):
    groupInputZone=Zone()
    groupOutputZone=Zone()

    cellInputRadius=0.0
    cellOutputRadius=0.0

    cellQty=0

    inputQtyPerCell=0
    outputQtyPerCell=0

    fat=0
    inherit=0

    def __init__(self):
        pass

    def initByOldCellGroup(self,oldCellGroup):#clone old cellgroup
        self.groupInputZone=Zone()
        self.groupInputZone.initByOldZone(oldZone=oldCellGroup.groupInputZone)
        self.groupOutputZone=Zone()
        self.groupOutputZone.initByOldZone(oldZone=oldCellGroup.groupOutputZone)
        self.cellInputRadius=oldCellGroup.cellInputRadius
        self.cellOutputRadius=oldCellGroup.cellOutputRadius
        self.cellQty=oldCellGroup.cellQty
        self.inputQtyPerCell=oldCellGroup.inputQtyPerCell
        self.outputQtyPerCell=oldCellGroup.outputQtyPerCell
        self.fat=oldCellGroup.fat
        self.inherit=oldCellGroup.inherit

    def initByRandom(self,brainLength,randomCellQtyPerGroup,randomInputQtyPerCell,randomOutputQtyPerCell):
        self.inherit=False
        self.groupInputZone=Zone(x=nextFloat()*brainLength,y=nextFloat()*brainLength,
                                 radius=float(nextFloat()*brainLength*0.01))
        self.groupOutputZone=Zone(x=nextFloat()*brainLength,y=nextFloat()*brainLength,
                                   radius=float(nextFloat()*brainLength*0.01))
        self.cellQty=nextInt(randomCellQtyPerGroup)
        self.cellInputRadius=float(nextFloat()*2+0.001)
        self.cellOutputRadius=float(nextFloat()*2+0.001)
        self.inputQtyPerCell=nextInt(randomInputQtyPerCell)
        self.outputQtyPerCell=nextInt(randomOutputQtyPerCell)