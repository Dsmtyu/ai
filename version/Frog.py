# Frog.py
# Frog是青蛙的本体：
# 属性：坐标，能量，蛋，是否存活，是否允许变异，移动时间，青蛙图像

from version.brain.Cell import Cell
from version.brain.IO import Input,Output
from version.brain.Organ import Organ
from version.egg.Zone import Zone
from configs import *

CLASSPATH=classpath#根目录路径

from tkinter import *

class Frog(object):
    cells=[]#frog的神经元
    cellGroups=[]
    organs=[]#frog的器官
    # 视觉细胞在脑中的区域，暂时先随便取，以后考虑使用
    eye=Zone(0,0,300)
    # 运动细胞在脑中的区域，暂时先随便取，以后考虑使用
    moveUp=Zone(500,50,10)
    moveDown=Zone(500,100,10)
    moveLeft=Zone(500,150,10)
    moveRight=Zone(500,200,10)
    moveRandom=Zone(500,300,10)

    x=0  #青蛙的x坐标
    y=0  #青蛙的y坐标
    xChange=0  #青蛙水平方向的移动
    yChange=0  #青蛙垂直方向的移动
    change=1
    energy=10000  #青蛙的能量，能量耗尽时青蛙死亡
    egg=None

    alive=True  #是否活着
    moveCount=0  #移动计数

    def __init__(self,x,y,egg,env,tk,canvas):
        self.x=x
        self.y=y

        self.tk=tk
        self.canvas=canvas  #tkinter画布
        self.frogImageDir=CLASSPATH+'frog.gif'  #青蛙图像路径
        self.frogImageFile=PhotoImage(file=self.frogImageDir)  #青蛙图像文件
        self.frogImage=canvas.create_image(self.x,self.y,anchor=NW,image=self.frogImageFile)  #显示在canvas上的图像

        if egg.cellGroups is None:
            raise RuntimeError("Illegal egg cellgroups argument!")

        for k in range(len(egg.cellGroups)):
            g=egg.cellGroups[k]
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

        if egg.organDescs is not None:
            for organdesc in egg.organDescs:
                self.organs.append(Organ(env,organdesc))

    def randomPosInZone(self,z):#在Zone区域中的随机点，即坐标在Zone内，半径为0的一个Zone
        return Zone(z.x-z.radius+z.radius*2*nextFloat(),z.y-z.radius+z.radius*2*nextFloat(),0)

    def active(self):#青蛙是否存活
        self.energy-=20
        if not self.alive:#青蛙已死亡，返回False
            return False
        if self.x<0 or self.x>=ENV_XSIZE\
        or self.y<0 or self.y>=ENV_YSIZE\
        or self.energy<0:#青蛙的横纵坐标是否出界;青蛙的能量是否<0
            self.alive=False#出界时青蛙死亡
            return False

        for organ in self.organs:
            organ.active(self)
        return self.alive

    def show(self,canvas):
        if not self.alive:
            return None
        canvas.move(self.frogImage,self.xChange,self.yChange)#对Frog进行移动
        self.xChange=0
        self.yChange=0