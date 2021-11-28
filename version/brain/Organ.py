from version.egg.Zone import Zone
from version.egg.OrganDesc import OrganDesc
from configs import *

class Organ(Zone):
    type=0

    HUNGRY=0
    UP=1
    DOWN=2
    LEFT=3
    RIGHT=4
    EAT=5

    def __init__(self,env,*args):
        self.env=env
        if len(args)==1:
            organdesc=args[0]
            if not isinstance(organdesc,OrganDesc):
                raise TypeError
            super(Organ,self).__init__(organdesc.x,organdesc.y,organdesc.radius)
            self.type=organdesc.type
        elif len(args)==4:
            type,x,y,radius=args
            super(Organ,self).__init__(x,y,radius)
            self.type=type

    def active(self,frog):
        if self.type==self.HUNGRY:self.hungry(frog)
        if self.type==self.UP:self.up(frog)
        if self.type==self.DOWN:self.down(frog)
        if self.type==self.LEFT:self.left(frog)
        if self.type==self.RIGHT:self.right(frog)
        if self.type==self.EAT:self.eat(frog)

    def outputActive(self,frog):
        for cell in frog.cells:
            for output in cell.outputs:
                if cell.energy>10 and self.nearby(output):
                    frog.cellGroups[cell.group].fat+=1
                    cell.energy-=30
                    return True
        return False

    def checkAlive(self,frog):
        x=frog.x
        y=frog.y
        if x<0 or x>=ENV_XSIZE or y<0 or y>=ENV_YSIZE:
            frog.alive=False
            return None

    def hungry(self,frog):
        for cell in frog.cells:
            if cell.energy>0: cell.energy-=1
            if frog.energy<10000 and cell.energy<100:
                for input in cell.inputs:
                    if self.nearby(input):
                        cell.energy+=2

    def up(self,frog):
        if self.outputActive(frog):
            frog.y+=1
            frog.yChange+=1
            self.checkAlive(frog)

    def down(self,frog):
        if self.outputActive(frog):
            frog.y-=1
            frog.yChange-=1
            self.checkAlive(frog)

    def left(self,frog):
        if self.outputActive(frog):
            frog.x-=1
            frog.xChange-=1
            self.checkAlive(frog)

    def right(self,frog):
        if self.outputActive(frog):
            frog.x+=1
            frog.xChange+=1
            self.checkAlive(frog)

    def eat(self,frog):
        self.checkAlive(frog)
        x=round(frog.x)
        y=round(frog.y)
        if self.env.foods[x][y]:
            self.env.foods[x][y]=0
            frog.energy+=1000