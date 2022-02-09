#IO.py
#IO Input&Output
#Input是细胞输入区,Output是细胞输出区
#-----------------------------------------------------------------------------------------------------------------------
from history.version1.brain.Cell import Cell
from history.version1.egg.Zone import Zone

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