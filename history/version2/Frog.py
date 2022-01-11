# Frog.py
# Frog是青蛙的本体：
# 属性:坐标,能量,蛋,是否存活,是否允许变异,移动时间,青蛙图像

from history.version2.brain.Cell import Cell
from history.version2.brain.IO import Input,Output
from history.version2.brain.Organ import Organ
from history.version2.egg.Egg import Egg
from history.version2.egg.Zone import Zone
from history.version2.egg.CellGroup import CellGroup
from configs import *

CLASSPATH=classpath#根目录路径

from tkinter import *

class Frog(object):
    def __init__(self,x,y,egg,tk,canvas):
        self.cells=[]
        self.cellgroups=[]
        self.organs=[]
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

        for k in range(len(egg.cellgroups)):
            g=egg.cellgroups[k]
            cellGroup=CellGroup()
            cellGroup.initByOldCellGroup(g)
            self.cellgroups.append(cellGroup)
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

        if egg.organdescs is not None:
            for organdesc in egg.organdescs:
                organ=Organ()
                organ.initByOrganDesc(organdesc)
                self.organs.append(organ)

    def randomPosInZone(self,z):#在Zone区域中的随机点，即坐标在Zone内，半径为0的一个Zone
        return Zone(z.x-z.radius+z.radius*2*nextFloat(),z.y-z.radius+z.radius*2*nextFloat(),0)

    def checkalive(self):
        if self.x<0 or self.x>=ENV_XSIZE\
        or self.y<0 or self.y>=ENV_YSIZE:#青蛙的横纵坐标是否出界
            self.alive=False#出界时青蛙死亡
            return False
        return True

    def active(self,env):#青蛙是否存活
        self.energy-=20
        if not self.alive:#青蛙已死亡，返回False
            return False
        if not self.checkalive():
            return False

        for organ in self.organs:
            organ.active(self,env)
        return True if self.checkalive() else False

    def show(self):
        if not self.alive:
            self.frogImageDir=CLASSPATH+'nothing.gif'
            self.frogImageFile=PhotoImage(file=self.frogImageDir)
            self.canvas.itemconfig(self.frogImage,image=self.frogImageFile)
            return None
        self.canvas.move(self.frogImage,self.xChange,self.yChange)#对Frog进行移动
        self.xChange=0
        self.yChange=0