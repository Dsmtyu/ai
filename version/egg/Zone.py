# Zone.py
# Zone是一块圆形区域，属性有：圆心坐标，半径
from configs import *

class Zone(object):
    x=0.0
    y=0.0
    radius=0.0

    def __init__(self,*args):
        if len(args)==0:
            pass
        if len(args)==1:
            z=args[0]
            if not isinstance(z,Zone):
                raise TypeError
            self.x=z.x
            self.y=z.y
            self.radius=z.radius
        if len(args)==3:
            x,y,radius=args
            self.x=x
            self.y=y
            self.radius=radius
            if x<0:self.x=0
            if y<0:self.y=0
            if x>=FROG_BRAIN_LENGTH:self.x=FROG_BRAIN_LENGTH
            if y>=FROG_BRAIN_LENGTH:self.y=FROG_BRAIN_LENGTH

    def nearby(self,z):#本体Zone与z这个Zone是否重叠
        distance=self.radius+z.radius
        return True if abs(self.x-z.x)<distance and abs(self.y-z.y)<distance else False

    def roundX(self): return round(self.x)

    def roundY(self): return round(self.y)

    def copyXY(self,fromZone,toZone):#将toZone这个Zone的坐标设为fromZone这个Zone的坐标
        toZone.x=fromZone.x
        toZone.y=fromZone.y