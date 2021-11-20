from version.Frog import Frog
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

    def active(self,frog):
        if self.type==self.HUNGRY:
            pass