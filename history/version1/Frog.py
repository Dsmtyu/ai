# Frog.py
# Frog是青蛙的本体：
# 属性：坐标，能量，蛋，是否存活，是否允许变异，移动时间，青蛙图像

from history.version1.brain.Cell import Cell
from history.version1.brain.IO import Input,Output
from history.version1.egg.Egg import Egg
from history.version1.egg.Zone import Zone
from history.version1.egg.CellGroup import CellGroup

CLASSPATH='C:\\Users\\jack\\Desktop\\AI\\'#根目录路径

from tkinter import *

from random import randint

import time

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class Frog(object):
    def __init__(self,x,y,egg,tk,canvas,frogid):
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
        self.frogid=frogid#frog编号
        self.egg=egg#蛋
        self.energy=1000#青蛙的能量，能量耗尽时青蛙死亡
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
                    Zone().copyXY(self.randomPosInZone(g.groupInputZone),output)
                    output.radius=g.cellOutputRadius
                    c.outputs.append(output)
                self.cells.append(c)

    def randomPosInZone(self,z):#在Zone区域中的随机点，即坐标在Zone内，半径为0的一个Zone
        return Zone(z.x-z.radius+z.radius*2*nextFloat(),z.y-z.radius+z.radius*2*nextFloat(),0)

    def active(self,env):#青蛙是否存活
        if not self.alive:#青蛙已死亡，返回False
            return False
        if self.x<0 or self.x>=env.ENV_XSIZE\
        or self.y<0 or self.y>=env.ENV_YSIZE:#青蛙的横纵坐标是否出界
            self.alive=False#出界时青蛙死亡
            return False

        #移动青蛙
        for cell in self.cells:
            for output in cell.outputs:
                if self.moveUp.nearby(output):self._moveUp(env)
                if self.moveDown.nearby(output):self._moveDown(env)
                if self.moveLeft.nearby(output):self._moveLeft(env)
                if self.moveRight.nearby(output):self._moveRight(env)
                if self.moveRandom.nearby(output):self._moveRandom(env)
        return True

    def checkFoodAndEat(self,env):#如果Frog坐标与Food坐标重合，吃掉它
        eatedFood=False#是否吃掉食物
        if self.x>=0 and self.x<env.ENV_XSIZE\
        and self.y>=0 and self.y<env.ENV_YSIZE:
            if env.foods[round(self.x)][round(self.y)]==1:
                env.foods[round(self.x)][round(self.y)]=-1
                self.energy+=1000#吃到食物青蛙能量增加1000
                eatedFood=True
                #print('[EAT]:Frog %d ate food!'%self.frogid)
        if eatedFood: #TODO: 奖励措施未完成
            pass

    def _moveUp(self,env):
        #print("[MOVE]:Frog %d move up!"%self.frogid)
        self.yChange-=self.change
        self.y-=self.change
        if self.y<0 or self.y>=env.ENV_YSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def _moveDown(self,env):
        #print("[MOVE]:Frog %d move down!"%self.frogid)
        self.yChange+=self.change
        self.y+=self.change
        if self.y<0 or self.y>=env.ENV_YSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def _moveLeft(self,env):
        #print("[MOVE]:Frog %d move left!"%self.frogid)
        self.xChange-=self.change
        self.x-=self.change
        if self.x<0 or self.x>=env.ENV_XSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def _moveRight(self,env):
        #print("[MOVE]:Frog %d move right!"%self.frogid)
        self.xChange+=self.change
        self.x+=self.change
        if self.x<0 or self.x>=env.ENV_XSIZE:
            self.alive=False
            return None
        self.checkFoodAndEat(env)

    def _moveRandom(self,env):
        #print("[MOVE]:Frog %d move random!"%self.frogid)
        rand=nextInt(4)
        if rand==1:self._moveUp(env)
        if rand==2:self._moveDown(env)
        if rand==3:self._moveLeft(env)
        if rand==4:self._moveRight(env)

    def percet1(self,f):#1%的变异率
        if not self.allowVariation:
            return f
        return float(f*(0.99+nextFloat()*0.02))

    def percet5(self,f):#5%的变异率
        if not self.allowVariation:
            return f
        return float(f*(0.95+nextFloat()*0.10))

    def layEgg(self):
        self.allowVariation=False if nextInt(100)>25 else True#变异率先控制在25%
        #如果不允许变异，下的蛋就等于原来的蛋
        newEgg=Egg()
        newEgg.brainRadius=self.percet5(self.egg.brainRadius)
        newEgg.cellgroups=[]
        for i in range(len(self.egg.cellgroups)):
            cellGroup=CellGroup()
            oldGp=self.egg.cellgroups[i]
            cellGroup.groupInputZone=Zone(self.percet5(oldGp.groupInputZone.x),self.percet5(oldGp.groupInputZone.y),
                                          self.percet5(oldGp.groupInputZone.radius))
            cellGroup.groupOutputZone=Zone(self.percet5(oldGp.groupInputZone.x),self.percet5(oldGp.groupInputZone.y),
                                          self.percet5(oldGp.groupInputZone.radius))
            cellGroup.cellQty=round(self.percet5(oldGp.cellQty))
            cellGroup.cellInputRadius=self.percet1(oldGp.cellInputRadius)
            cellGroup.cellOutputRadius=self.percet1(oldGp.cellOutputRadius)
            cellGroup.inputQtyPerCell=round(self.percet5(oldGp.inputQtyPerCell))
            cellGroup.outputQtyPerCell=round(self.percet5(oldGp.outputQtyPerCell))
            newEgg.cellgroups.append(cellGroup)
        return newEgg

    def show(self,canvas):
        if not self.alive:
            return None
        canvas.move(self.frogImage,self.xChange,self.yChange)#对Frog进行移动
        self.xChange=0
        self.yChange=0