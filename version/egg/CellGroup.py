# CellGroup.py
# CellGroup代表了一束相同功能和结构、分布位置相近的脑神经元，目的是为了下蛋时简化串行化海量的神经元,
# 只需要在egg里定义一组cellGroup就行了，不需要将海量的一个个的神经元串行化存放到egg里，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
# 它的母体，而且每一次测试，一些复杂的条件反射的建立都必须从头开始训练，在项目后期，有可能每个frog生命的一半时间都花在重新建立条件反射的学习过程中。

from version.egg.Zone import Zone
from random import *

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class CellGroup(object):
    groupInputZone=Zone()
    groupOutputZone=Zone()

    cellInputRadius=0.0
    cellOutputRadius=0.0

    cellQty=0

    inputQtyPerCell=0
    outputQtyPerCell=0

    fat=0
    inherit=False

    def __init__(self,*args):
        if len(args)==0:
            pass
        if len(args)==1:
            cellGroup=args[0]
            if not isinstance(cellGroup,CellGroup):
                raise TypeError
            self.groupInputZone=cellGroup.groupInputZone
            self.groupOutputZone=cellGroup.groupOutputZone
            self.cellInputRadius=cellGroup.cellInputRadius
            self.cellOutputRadius=cellGroup.cellOutputRadius
            self.cellQty=cellGroup.cellQty
            self.inputQtyPerCell=cellGroup.inputQtyPerCell
            self.outputQtyPerCell=cellGroup.outputQtyPerCell
            self.fat=cellGroup.fat
            self.inherit=cellGroup.inherit
        if len(args)==4:
            brainLength,randomCellQtyPerGroup,randomInputQtyPerCell,randomOutputQtyPerCell=args
            self.inherit=False
            self.groupInputZone=Zone(nextFloat()*brainLength,nextFloat()*brainLength,
                                     float(nextFloat()*brainLength*0.01))
            self.groupOutputZone=Zone(nextFloat()*brainLength,nextFloat()*brainLength,
                                     float(nextFloat()*brainLength*0.01))
            self.cellQty=nextInt(randomCellQtyPerGroup)
            self.cellInputRadius=float(nextFloat()*2+0.001)
            self.cellOutputRadius=float(nextFloat()*2+0.001)
            self.inputQtyPerCell=nextInt(randomInputQtyPerCell)
            self.outputQtyPerCell=nextInt(randomOutputQtyPerCell)