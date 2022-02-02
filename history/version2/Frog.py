# Frog.py
# Frog是青蛙的本体：
# 属性:坐标,能量,蛋,是否存活,是否允许变异,移动时间,青蛙图像
# Frog=brain+organ,but now let's only focus on brain,organs are too hard
# 青蛙由脑细胞和器官组成,目前脑细胞可以变异,进化,遗传,由电脑自动生成神经网络,但是器官在蛋里硬编码,不许进化,将来可以考虑器官的进化
# -----------------------------------------------------------------------------------------------------------------------

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
    def __init__(self,x,y,egg,tk:Tk,canvas:Canvas):
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

        self.x=x#frog在env中的x坐标
        self.y=y#frog在env中的y坐标
        self.xChange=0#青蛙水平方向的移动
        self.yChange=0#青蛙垂直方向的移动
        self.change=1
        self.egg=egg#蛋
        self.energy=10000#青蛙的能量,能量为0则死掉
        self.tk=tk
        self.canvas=canvas#tkinter画布
        self.alive=True#是否活着,设为false表示青蛙死掉了,将不参与任何计算和显示,以节省时间
        self.allowVariation=False#是否允许变异
        self.moveCount=0#移动计数
        self.frogImageDir=CLASSPATH+'frog.gif'#青蛙图像路径
        self.frogImageFile=PhotoImage(file=self.frogImageDir)#青蛙图像文件
        self.frogImage=canvas.create_image(self.x,self.y,anchor=NW,image=self.frogImageFile)#显示在canvas上的图像

        if egg.cellgroups is None:
            raise RuntimeError("Illegal egg cellgroups argument!")

        for k in range(len(egg.cellgroups)):
            oldCellGroup:CellGroup=egg.cellgroups[k]
            cellGroup=CellGroup()
            cellGroup.initByOldCellGroup(oldCellGroup)
            self.cellgroups.append(cellGroup)
            for i in range(oldCellGroup.cellQty):
                c=Cell()
                c.inputs=[]
                for j in range(oldCellGroup.inputQtyPerCell):
                    input=Input()
                    input.cell=c
                    Zone().copyXY(fromZone=self.randomPosInZone(zone=oldCellGroup.groupInputZone),toZone=input)
                    input.radius=oldCellGroup.cellInputRadius
                    c.inputs.append(input)
                c.outputs=[]
                for j in range(oldCellGroup.outputQtyPerCell):
                    output=Output()
                    output.cell=c
                    Zone().copyXY(fromZone=self.randomPosInZone(zone=oldCellGroup.groupOutputZone),toZone=output)
                    output.radius=oldCellGroup.cellOutputRadius
                    c.outputs.append(output)
                self.cells.append(c)

        if egg.organdescs is not None:
            for organdesc in egg.organdescs:
                organ=Organ()
                organ.initByOrganDesc(organdesc)
                self.organs.append(organ)

    def randomPosInZone(self,zone):#在Zone区域中的随机点，即坐标在Zone内，半径为0的一个Zone
        return Zone(zone.x-zone.radius+zone.radius*2*nextFloat(),zone.y-zone.radius+zone.radius*2*nextFloat(),0)

    def checkalive(self):
        if self.x<0 or self.x>=ENV_XSIZE\
        or self.y<0 or self.y>=ENV_YSIZE\
        or self.energy<0:#青蛙的横纵坐标是否出界,青蛙的能量是否耗尽
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