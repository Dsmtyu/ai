# Frog.py
# Frog是青蛙的本体：
# 属性：坐标，能量，蛋，是否存活，是否允许变异，移动时间，青蛙图像

from version.egg.Zone import Zone
from version.env.Application import Application

from tkinter import *


class Frog(object):
    def __init__(self, x, y, egg, canvas):
        self.brainRadius = 0.0
        self.cells = []
        self.eye = Zone(0, 0, 300)

        self.moveUp = Zone(500, 50, 10)
        self.moveDown = Zone(500, 100, 10)
        self.moveLeft = Zone(500, 150, 10)
        self.moveRight = Zone(500, 200, 10)
        self.moveRandom = Zone(500, 300, 10)

<<<<<<< Updated upstream
        self.x=x
        self.y=y
        self.xChange=0
        self.yChange=0
        self.egg=egg
        self.canvas=canvas
        self.alive=True
        self.moveCount=0
        self.frogImageFile=PhotoImage(Application().CLASSPATH+'frog.gif')
        self.frogImage=canvas.create_image(self.x,self.y,anchor=NW,image=self.frogImageFile)
        
=======
        self.x = x
        self.y = y
        self.egg = egg
        self.canvas = canvas
        self.alive = True
        self.moveCount = 0
        self.frogImageFile = PhotoImage()
>>>>>>> Stashed changes
