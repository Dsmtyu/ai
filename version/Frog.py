# Frog.py
# Frog是青蛙的本体：
# 属性：坐标，能量，蛋，是否存活，是否允许变异，移动时间，青蛙图像

from version.brain.Cell import Cell
from version.brain.IO import Input,Output
from version.egg.Zone import Zone
from version.env.Application import Application

from tkinter import *

from random import randint

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class Frog(object):
    def __init__(self,x,y,egg,canvas):
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

        self.x=x
        self.y=y
        self.xChange=0
        self.yChange=0
        self.egg=egg
        self.energy=1000
        self.canvas=canvas
        self.alive=True
        self.allowVariation=False#是否允许变异
        self.moveCount=0
        self.frogImageFile=PhotoImage(Application().CLASSPATH+'frog.gif')
        self.frogImage=canvas.create_image(self.x,self.y,anchor=NW,image=self.frogImageFile)

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
                    Zone().copyXY(self.randomPosInZone(g.groupInputZone),output)
                    output.radius=g.cellOutputRadius
                    c.outputs.append(output)
                self.cells.append(c)

    def randomPosInZone(self,z):
        return Zone(z.x-z.radius+z.radius*2*nextFloat(),z.y-z.radius+z.radius*2*nextFloat(),0)

    def active(self,env):
        if not self.alive:
            return False
        if self.x<0 or self.x>=env.ENV_XSIZE\
        or self.y<0 or self.y>=env.ENV_YSIZE:
            self.alive=False
            return False

        #移动青蛙
        for cell in self.cells:
            for output in cell.outputs:
                if self.moveUp.nearby(output):self.moveUp(env)
                if self.moveDown.nearby(output):self.moveDown(env)
                if self.moveLeft.nearby(output):self.moveLeft(env)
                if self.moveRight.nearby(output):self.moveRight(env)
                if self.moveRandom.nearby(output):self.moveRandom(env)
        return True

    def checkFoodAndEat(self,env):#如果Frog坐标与Food坐标重合，吃掉它
        eatedFood=False
        if self.x>=0 and self.x<env.ENV_XSIZE\
        and self.y>=0 and self.y<env.ENV_YSIZE:
            if env.foods[self.x][self.y]:
                env.foods[self.x][self.y]=0
                self.energy+=1000
                eatedFood=True
        if eatedFood: #TODO: 奖励措施未完成
            pass

    def moveUp(self,env):
        self.yChange=-1
        if self.y<0 or self.y>=env.ENV_YSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def moveDown(self,env):
        self.yChange=1
        if self.y<0 or self.y>=env.ENV_YSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def moveLeft(self,env):
        self.xChange=-1
        if self.x<0 or self.x>=env.ENV_XSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def moveRight(self,env):
        self.xChange=1
        if self.x<0 or self.x>=env.ENV_XSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def moveRandom(self,env):
        rand=nextInt(4)
        if rand==1:self.moveUp(env)
        if rand==2:self.moveDown(env)
        if rand==3:self.moveLeft(env)
        if rand==4:self.moveRight(env)

    def percet1(self,f):
        if not self.allowVariation:
            return f
        return float(f*(0.99*nextFloat()*0.02))

    def percet5(self,f):
        if not self.allowVariation:
            return f
        return float(f*(0.95*nextFloat()*0.10))

    