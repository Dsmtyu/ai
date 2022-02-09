#CellGroup.py
#CellGroup代表了一束相同功能和结构、分布位置相近的脑神经元，目的是为了下蛋时简化串行化海量的神经元,
#只需要在egg里定义一组cellGroup就行了，不需要将海量的一个个的神经元串行化存放到egg里，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
#它的母体，而且每一次测试，一些复杂的条件反射的建立都必须从头开始训练，在项目后期，有可能每个frog生命的一半时间都花在重新建立条件反射的学习过程中。
#-----------------------------------------------------------------------------------------------------------------------
from history.version1.egg.Zone import Zone

class CellGroup(object):
    groupInputZone:Zone=Zone()
    groupOutputZone:Zone=Zone()

    cellInputRadius:float=0.0
    cellOutputRadius:float=0.0

    cellQty:int=0

    inputQtyPerCell:int=0
    outputQtyPerCell:int=0

    def __init__(self):
        pass