# Zone.py
# Zone是一块圆形区域，属性有：圆心坐标，半径

class Zone(object):
    def __init__(self,x=0.0,y=0.0,radius=0.0):
        self.x=x
        self.y=y
        self.radius=radius
        self.brainLength=500
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.x>self.brainLength:
            self.x=self.brainLength
        if self.y>self.brainLength:
            self.y=self.brainLength

    def nearby(self,z):#本体Zone与z这个Zone是否重叠
        distance=self.radius+z.radius
        return True if abs(self.x-z.x)<distance and abs(self.y-z.y)<distance else False

    def roundX(self): return round(self.x)

    def roundY(self): return round(self.y)

    def copyXY(self,fromZone,toZone):#将toZone这个Zone的坐标设为fromZone这个Zone的坐标
        toZone.x=fromZone.x
        toZone.y=fromZone.y