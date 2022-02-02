# Zone.py
# Zone是一块圆形区域属性有:圆心坐标,半径
# -----------------------------------------------------------------------------------------------------------------------

class Zone(object):
    def __init__(self,x=0.0,y=0.0,radius=0.0):
        self.x=x
        self.y=y
        self.radius=radius

    def initByOldZone(self,oldZone):#clone old Zone
        self.x=oldZone.x
        self.y=oldZone.y
        self.radius=oldZone.radius

    def nearby(self,zone)->bool:#本体Zone与z这个Zone是否重叠
        distance=self.radius+zone.radius
        return True if abs(self.x-zone.x)<distance and abs(self.y-zone.y)<distance else False

    def roundX(self)->int: return round(self.x)#zone的坐标是浮点数类型,不能在索引中使用,用round()将其转为整数类型

    def roundY(self)->int: return round(self.y)

    def copyXY(self,fromZone,toZone):#将toZone这个Zone的坐标设为fromZone这个Zone的坐标
        toZone.x=fromZone.x
        toZone.y=fromZone.y