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
    def __init__(self,x,y,egg,tk:Tk,canvas:Canvas):
        self.brainRadius=0.0
        self.cells=[]
        #视觉细胞在脑中的区域，暂时先随便取，以后考虑使用
        self.eye=Zone(0,0,300)
        #运动细胞在脑中的区域，暂时先随便取，以后考虑使用
        self.moveUp=Zone(500,50,10)
        self.moveDown=Zone(500,100,10)
        self.moveLeft=Zone(500,150,10)
        self.moveRight=Zone(500,200,10)
        self.moveRandom=Zone(500,300,10)

        self.x=x#青蛙的x坐标
        self.y=y#青蛙的y坐标
        self.xChange=0#青蛙水平方向的移动
        self.yChange=0#青蛙垂直方向的移动
        self.change=1
        self.egg=egg#蛋
        self.energy=10000#青蛙的能量，能量耗尽时青蛙死亡
        self.tk=tk
        self.canvas=canvas#tkinter画布
        self.alive=True#是否活着
        self.allowVariation=False#是否允许变异
        self.moveCount=0#移动计数
        self.frogImageDir=CLASSPATH+'frog.gif'#青蛙图像路径
        self.frogImageFile=PhotoImage(file=self.frogImageDir)#青蛙图像文件
        self.frogImage=canvas.create_image(self.x,self.y,anchor=NW,image=self.frogImageFile)#显示在canvas上的图像

        if egg.cellgroups is None:
            raise RuntimeError("Illegal egg cellgroups argument!")
        self.brainRadius=egg.brainRadius

        for k in range(len(egg.cellgroups)):
            g=egg.cellgroups[k]
            for i in range(g.cellQty):
                c=Cell()
                c.inputs=[]
                for j in range(g.inputQtyPerCell):
                    input=Input()
                    input.cell=c
                    Zone().copyXY(self.randomPosInZone(g.groupInputZone),input)
                    input.radius=g.cellInputRadius
                    c.inputs.append(input)
                c.outputs=[]
                for j in range(g.outputQtyPerCell):
                    output=Output()
                    output.cell=c
                    Zone().copyXY(self.randomPosInZone(g.groupOutputZone),output)
                    output.radius=g.cellOutputRadius
                    c.outputs.append(output)
                self.cells.append(c)

    def randomPosInZone(self,zone:Zone):#在Zone区域中的随机点，即坐标在Zone内，半径为0的一个Zone
        return Zone(zone.x-zone.radius+zone.radius*2*nextFloat(),zone.y-zone.radius+zone.radius*2*nextFloat(),0)

    def checkalive(self):
        if self.x<0 or self.x>=ENV_XSIZE\
        or self.y<0 or self.y>=ENV_YSIZE:#青蛙的横纵坐标是否出界
            self.alive=False#出界时青蛙死亡
            return False
        return True

    def active(self,env):#青蛙是否存活
        if not self.alive:#青蛙已死亡，返回False
            return False
        if not self.checkalive():
            return False

        #移动青蛙
        for cell in self.cells:
            for output in cell.outputs:
                if self.moveLeft.nearby(output):self.movefrog(env=env,number=1)
                if self.moveRight.nearby(output):self.movefrog(env=env,number=2)
                if self.moveUp.nearby(output):self.movefrog(env=env,number=3)
                if self.moveDown.nearby(output):self.movefrog(env=env,number=4)
                if self.moveRandom.nearby(output):
                    number=nextInt(4)
                    self.movefrog(env=env,number=number)
        return True

    def checkFoodAndEat(self,env):#如果Frog坐标与Food坐标重合，吃掉它
        eatedFood:bool=False#是否吃掉食物
        if self.x>=0 and self.x<ENV_XSIZE\
        and self.y>=0 and self.y<ENV_YSIZE:
            if env.foods[round(self.x)][round(self.y)]==1:
                env.foods[round(self.x)][round(self.y)]=-1
                self.energy+=1000#吃到食物青蛙能量增加1000
                eatedFood=True
        if eatedFood: #TODO: 奖励措施未完成
            pass

    def movefrog(self,env,number):
        if Direction(number)==Direction.LEFT:
            self.xChange-=self.change
            self.x-=self.change
        if Direction(number)==Direction.RIGHT:
            self.xChange+=self.change
            self.x+=self.change
        if Direction(number)==Direction.UP:
            self.yChange+=self.change
            self.y+=self.change
        if Direction(number)==Direction.DOWN:
            self.yChange-=self.change
            self.y-=self.change
        if not self.checkalive():
            return None
        self.checkFoodAndEat(env=env)

    def percent1(self,f:float):#变异1%
        if not self.allowVariation:
            return f
        return float(f*(0.99+nextFloat()*0.02))

    def percent5(self,f:float):#变异5%
        if not self.allowVariation:
            return f
        return float(f*(0.95+nextFloat()*0.10))

    def layEgg(self):
        self.allowVariation=percent(25)#变异率先控制在25%
        #如果不允许变异，下的蛋就等于原来的蛋
        newEgg=Egg()
        newEgg.brainRadius=self.percent5(self.egg.brainRadius)
        newEgg.cellgroups=[]
        for i in range(len(self.egg.cellgroups)):
            cellGroup=CellGroup()
            oldGp=self.egg.cellgroups[i]
            cellGroup.groupInputZone=Zone(x=self.percent5(oldGp.groupInputZone.x),y=self.percent5(oldGp.groupInputZone.y),
                                          radius=self.percent5(oldGp.groupInputZone.radius))
            cellGroup.groupOutputZone=Zone(x=self.percent5(oldGp.groupInputZone.x),y=self.percent5(oldGp.groupInputZone.y),
                                          radius=self.percent5(oldGp.groupInputZone.radius))
            cellGroup.cellQty=round(self.percent5(oldGp.cellQty))
            cellGroup.cellInputRadius=self.percent1(oldGp.cellInputRadius)
            cellGroup.cellOutputRadius=self.percent1(oldGp.cellOutputRadius)
            cellGroup.inputQtyPerCell=round(self.percent5(oldGp.inputQtyPerCell))
            cellGroup.outputQtyPerCell=round(self.percent5(oldGp.outputQtyPerCell))
            newEgg.cellgroups.append(cellGroup)
        return newEgg

    def show(self):
        if not self.alive:
            self.frogImageDir=CLASSPATH+'nothing.gif'
            self.frogImageFile=PhotoImage(file=self.frogImageDir)
            self.canvas.itemconfig(self.frogImage,image=self.frogImageFile)
            return None
        self.canvas.move(self.frogImage,self.xChange,self.yChange)#对Frog进行移动
        self.xChange=0
        self.yChange=0