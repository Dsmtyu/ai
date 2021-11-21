from version.Frog import Frog
from version.brain.organs.Eye import Eye
from version.egg.Zone import Zone

class Organ(Zone):
    def __init__(self,env,*args):
        self.env=env
        if len(args)==1:
            organdesc=args[0]
            super(Organ,self).__init__(organdesc.x,organdesc.y,organdesc.radius)
            self.type=organdesc.type
        elif len(args)==4:
            type,x,y,radius=args
            super(Organ,self).__init__(x,y,radius)
            self.type=type
        self.HUNGRY=0
        self.UP=1
        self.DOWN=2
        self.LEFT=3
        self.RIGHT=4
        self.EAT=5
        self.EYE=6

    def outputActive(self,frog):
        for cell in frog.cells:
            for output in cell.outputs:
                if cell.energy>10 and self.nearby(output):
                    frog.cellGroups[cell.group].fat+=1
                    cell.energy-=6
                    return True
        return False

    def active(self,frog):
        if self.type==self.HUNGRY:
            pass

    def hungry(self,frog):
        for cell in frog.cells:
            if cell.energy>0:
                cell.energy-=1
            if frog.energy<10000 and cell.energy<100:
                for input in cell.inputs:
                    if input.nearby(self):
                        cell.energy+=1

    def up(self,frog):
        if self.outputActive(frog):
            frog.y-=1

    def down(self,frog):
        if self.outputActive(frog):
            frog.y+=1

    def left(self,frog):
        if self.outputActive(frog):
            frog.x-=1

    def right(self,frog):
        if self.outputActive(frog):
            frog.x+=1

    def eat(self,frog):
        x,y=frog.x,frog.y
        if x<0 or x>=self.env.ENV_XSIZE\
        or y<0 or y>=self.env.ENV_YSIZE:#青蛙的横纵坐标是否出界
            self.alive=False#出界时青蛙死亡
            return False

        if self.env.foods[x][y]:
            self.env.foods[x][y]=0
            frog.energy+=1000

    def eye(self,frog):
        frogEye=Eye(self.env)
        frogEye.act(frog,self)