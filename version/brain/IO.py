# IO.py
# IO Input&Output
# 这两个类继承了Zone，也就是说它们都是一块区域；
# Input是细胞输入区，Output是细胞输出区

from version.brain.Cell import Cell
from version.egg.Zone import Zone

class Input(Zone):
    def __init__(self,x=0.0,y=0.0,radius=0.0):
        super(Input,self).__init__(x,y,radius)
        self.energy=0.0
        self.cell=Cell()

class Output(Zone):
    def __init__(self,x=0.0,y=0.0,radius=0.0):
        super(Output,self).__init__(x,y,radius)
        self.energy=0.0
        self.cell=Cell()