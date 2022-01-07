# OrganDesc.py
# OrganDesc类保存了创造器官Organ的信息
# -----------------------------------------------------------------------------------------------------------------------
from history.version2.egg.Zone import Zone

class OrganDesc(Zone):
    def __init__(self,organType,x,y,radius):
        super(OrganDesc,self).__init__(x,y,radius)
        self.organType=organType