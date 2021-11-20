from version.egg.Zone import Zone

class OrganDesc(Zone):
    def __init__(self,type,x,y,radius):
        super(OrganDesc,self).__init__(x,y,radius)
        self.type=type