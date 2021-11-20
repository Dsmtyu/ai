from version.egg.Zone import Zone

class Eye(object):
    def __init__(self,env):
        self.env=env

    def hasFood(self,x,y):
        return x>=0 and y>=0 and x<self.env.ENV_XSIZE and y<self.env.ENV_YSIZE and self.env.foods[x][y]

    def act(self,frog,organ):
        qRadius=organ.radius*0.25
        q3Radius=organ.radius*0.75
        seeUp=Zone(organ.x,organ.y+q3Radius,qRadius)
        seeDown=Zone(organ.x,organ.y-q3Radius,qRadius)
        seeLeft=Zone(organ.x-q3Radius,organ.y,qRadius)
        seeRight=Zone(organ.x+q3Radius,organ.y,qRadius)

        seeFood=False
        foodUp=False
        foodDown=False
        foodLeft=False
        foodRight=False

        seeDistance=10

        for i in range(1,seeDistance):
            if self.hasFood(frog.x,frog.y+i):
                seeFood=True
                foodUp=True
                break
        for i in range(1,seeDistance):
            if self.hasFood(frog.x,frog.y-i):
                seeFood=True
                foodDown=True
                break
        for i in range(1,seeDistance):
            if self.hasFood(frog.x-i,frog.y):
                seeFood=True
                foodLeft=True
                break
        for i in range(1,seeDistance):
            if self.hasFood(frog.x+i,frog.y):
                seeFood=True
                foodRight=True
                break

        if seeFood:
            for cell in frog.cells:
                if cell.energy<100:
                    for input in cell.inputs:
                        if input.nearby(organ):
                            if foodUp and input.nearby(seeUp):
                                input.cell.energy+=30
                            if foodDown and input.nearby(seeDown):
                                input.cell.energy+=30
                            if foodLeft and input.nearby(seeLeft):
                                input.cell.energy+=30
                            if foodRight and input.nearby(seeRight):
                                input.cell.energy+=30