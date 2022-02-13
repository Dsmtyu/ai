# Frog.py
# Frog是青蛙的本体：
# 属性:坐标,能量,蛋,是否存活,是否允许变异,移动时间,青蛙图像

from history.version1.brain.Cell import Cell
from history.version1.brain.IO import Input,Output
from history.version1.egg.Egg import Egg
from history.version1.egg.Zone import Zone
from history.version1.egg.CellGroup import CellGroup
from configs import *

CLASSPATH=classpath#根目录路径

from tkinter import *

class Frog(object):
    brainRadius: float=0.0
    cells:list[Cell]=[]
    #视觉细胞在脑中的区域，暂时先随便取，以后考虑使用
    eye:Zone=Zone(0,0,300)
    #运动细胞在脑中的区域，暂时先随便取，以后考虑使用
    moveUpZone:Zone=Zone(500,50,10)
    moveDownZone:Zone=Zone(500,100,10)
    moveLeftZone:Zone=Zone(500,150,10)
    moveRightZone:Zone=Zone(500,200,10)
    moveRandomZone:Zone=Zone(500,300,10)

    x:float=0#青蛙的x坐标
    y:float=0#青蛙的y坐标

    change:int=1#青蛙一次移动的最小步长

    energy:int=10000  #青蛙的能量，能量耗尽时青蛙死亡

    alive:bool=True  #是否活着
    allowVariation:bool=False  #是否允许变异
    moveCount:int=0  #移动计数


    def __init__(self,x:float,y:float,egg:Egg,tk:Tk,canvas:Canvas):
        self.x=x
        self.y=y

        self.egg:Egg=egg#蛋

        self.tk=tk
        self.canvas=canvas#tkinter画布

        self.frogImageDir=CLASSPATH+'frog.gif'  #青蛙图像路径
        self.frogImageFile=PhotoImage(file=self.frogImageDir)  #青蛙图像文件

        if egg.cellgroups is None:
            raise RuntimeError("Illegal egg cellgroups argument!")
        self.brainRadius=egg.brainRadius

        for k in range(len(egg.cellgroups)):
            cellGroup=egg.cellgroups[k]
            for i in range(cellGroup.cellQty):
                c:Cell=Cell()
                c.inputs=[]
                c.outputs=[]
                for j in range(cellGroup.inputQtyPerCell):
                    input:Input=Input()
                    input.cell=c
                    Zone().copyXY(self.randomPosInZone(cellGroup.groupInputZone),input)
                    input.radius=cellGroup.cellInputRadius
                    c.inputs.append(input)
                for j in range(cellGroup.outputQtyPerCell):
                    output:Output=Output()
                    output.cell=c
                    Zone().copyXY(self.randomPosInZone(cellGroup.groupOutputZone),output)
                    output.radius=cellGroup.cellOutputRadius
                    c.outputs.append(output)
                self.cells.append(c)

    def randomPosInZone(self,zone:Zone)->Zone:#在Zone区域中的随机点，即坐标在Zone内，半径为0的一个Zone
        return Zone(zone.x-zone.radius+zone.radius*2*nextFloat(),zone.y-zone.radius+zone.radius*2*nextFloat(),0)

    def checkalive(self)->bool:
        if self.x<0 or self.x>=ENV_XSIZE\
        or self.y<0 or self.y>=ENV_YSIZE:#青蛙的横纵坐标是否出界
            self.alive=False#出界时青蛙死亡
            return False
        return True

    def active(self,env)->bool:#青蛙是否存活
        if not self.alive:#青蛙已死亡，返回False
            return False
        if not self.checkalive():
            return False

        #移动青蛙
        for cell in self.cells:
            for output in cell.outputs:
                if self.moveLeftZone.nearby(output):self.movefrog(env=env,number=1)
                if self.moveRightZone.nearby(output):self.movefrog(env=env,number=2)
                if self.moveUpZone.nearby(output):self.movefrog(env=env,number=3)
                if self.moveDownZone.nearby(output):self.movefrog(env=env,number=4)
                if self.moveRandomZone.nearby(output):
                    number=nextInt(4)
                    self.movefrog(env=env,number=number)
        return True

    def checkFoodAndEat(self,env):#如果Frog坐标与Food坐标重合，吃掉它
        eatedFood:bool=False#是否吃掉食物
        if self.x>=0 and self.x<ENV_XSIZE\
        and self.y>=0 and self.y<ENV_YSIZE:
            if env.foods[round(self.x)][round(self.y)] is True:
                env.foods[round(self.x)][round(self.y)]=False
                self.energy+=1000#吃到食物青蛙能量增加1000
                eatedFood=True
        if eatedFood: #TODO: 奖励措施未完成
            pass

    def movefrog(self,env,number):
        if Direction(number)==Direction.LEFT:
            self.x-=self.change
        if Direction(number)==Direction.RIGHT:
            self.x+=self.change
        if Direction(number)==Direction.UP:
            self.y+=self.change
        if Direction(number)==Direction.DOWN:
            self.y-=self.change
        if not self.checkalive():
            return None
        self.checkFoodAndEat(env=env)

    def percent1(self,f:float)->float:#变异1%
        return f if not self.allowVariation else float(f*(0.99+nextFloat()*0.02))

    def percent5(self,f:float)->float:#变异5%
        return f if not self.allowVariation else float(f*(0.95+nextFloat()*0.10))

    def layEgg(self):
        self.allowVariation=percent(25)#变异率先控制在25%
        #如果不允许变异，下的蛋就等于原来的蛋
        newEgg=Egg()
        newEgg.brainRadius=self.percent5(self.egg.brainRadius)
        newEgg.cellgroups=[]
        for i in range(len(self.egg.cellgroups)):
            cellGroup=CellGroup()
            oldCellGroup:CellGroup=self.egg.cellgroups[i]
            cellGroup.groupInputZone=Zone(x=self.percent5(oldCellGroup.groupInputZone.x),
                                          y=self.percent5(oldCellGroup.groupInputZone.y),
                                          radius=self.percent5(oldCellGroup.groupInputZone.radius))
            cellGroup.groupOutputZone=Zone(x=self.percent5(oldCellGroup.groupInputZone.x),
                                           y=self.percent5(oldCellGroup.groupInputZone.y),
                                          radius=self.percent5(oldCellGroup.groupInputZone.radius))
            cellGroup.cellQty=round(self.percent5(oldCellGroup.cellQty))
            cellGroup.cellInputRadius=self.percent1(oldCellGroup.cellInputRadius)
            cellGroup.cellOutputRadius=self.percent1(oldCellGroup.cellOutputRadius)
            cellGroup.inputQtyPerCell=round(self.percent5(oldCellGroup.inputQtyPerCell))
            cellGroup.outputQtyPerCell=round(self.percent5(oldCellGroup.outputQtyPerCell))
            newEgg.cellgroups.append(cellGroup)
        return newEgg

    def show(self,canvas:Canvas):
        if not self.alive:
            return None
        canvas.create_image(self.x,self.y,anchor=NW,image=self.frogImageFile)