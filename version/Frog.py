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
        self.canvas=canvas
        self.alive=True
        self.moveCount=0
        self.frogImageFile=PhotoImage()
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

    def randomPosInZone(self,z):
        return Zone(z.x-z.radius+z.radius*2*nextFloat(),z.y-z.radius+z.radius*2*nextFloat(),0)