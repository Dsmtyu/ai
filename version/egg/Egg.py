# Egg.py
# Egg 蛋存在的目的是为了以最小的字节数串行化存储Frog,它是Frog的生成算法描述，而不是Frog本身，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
# 它的母体，而且每一次测试，大部分条件反射的建立都必须从头开始训练，类似于人类，无论人类社会有多聪明，婴儿始终是一张白纸，需要花大量的时间从头学习。
# -----------------------------------------------------------------------------------------------------------------------
from version.egg.CellGroup import CellGroup
from version.egg.Zone import Zone
from random import randint

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class Egg(object):
    def __init__(self):
        self.CELL_GROUP_QTY=30
        self.brainRadius=1000
        self.cellgroups=[]

    def createBrandNewEgg(self):
        egg=Egg()
        for i in range(self.CELL_GROUP_QTY):
            cellGroup=CellGroup()
            cellGroup.groupInputZone=Zone(nextFloat()*egg.brainRadius,nextFloat()*egg.brainRadius,
                                          float(nextFloat()*egg.brainRadius*0.01))
            cellGroup.groupOutputZone=Zone(nextFloat()*egg.brainRadius,nextFloat()*egg.brainRadius,
                                          float(nextFloat()*egg.brainRadius*0.01))
            cellGroup.cellQty=nextInt(10)
            cellGroup.cellInputRadius=float(nextFloat()*0.001)
            cellGroup.cellOutputRadius=float(nextFloat()*0.001)
            cellGroup.inputQtyPerCell=nextInt(10)
            cellGroup.outputQtyPerCell=nextInt(5)
            egg.cellgroups.append(cellGroup)
        return egg