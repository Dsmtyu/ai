#IO.py
#IO Input&Output
#Input是细胞输入区,Output是细胞输出区
#-----------------------------------------------------------------------------------------------------------------------
from core.brain.Cell import Cell
from core.egg.Zone import Zone

class Input(Zone):
    def __init__(self,x=0.0,y=0.0,radius=0.0):
        super(Input,self).__init__(x,y,radius)
        self.energy:float=0.0
        self.cell:Cell=Cell()

class Output(Zone):
    def __init__(self,x=0.0,y=0.0,radius=0.0):
        super(Output,self).__init__(x,y,radius)
        self.energy:float=0.0
        self.cell:Cell=Cell()