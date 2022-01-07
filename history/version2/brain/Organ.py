# Organ.py
# 器官,分为输入器官和输出器官两大类,它们在蛋里定义,数量,位置,大小可以随机变异进化,但目前在蛋里用硬编码写死,不允许器官进化
# 一个眼睛都没搞定,要进化出100个眼睛来会吓死人
# -----------------------------------------------------------------------------------------------------------------------
from history.version2.egg.Zone import Zone
from configs import *

class Organ(Zone):
    def __init__(self,organType,x,y,radius):
        super(Organ,self).__init__(x,y,radius)
        self.organType=organType

    def initByOrganDesc(self,organDesc):
        super(Organ,self).__init__(organDesc.x,organDesc.y,organDesc.radius)
        self.organType=organDesc.organType

    def active(self,frog):
        if self.organType==HUNGRY:pass
        if self.organType==UP:pass
        if self.organType==DOWN:pass
        if self.organType==LEFT:pass
        if self.organType==RIGHT:pass
        if self.organType==EAT:pass

    def outputActive(self,frog):
        for cell in frog.cells:
            for output in cell.outputs:
                if cell.energy>10 and self.nearby(output):
                    frog.cellGroups[cell.group].fat+=1
                    cell.energy-=10
                    return True
        return False