# Env.py
# Env是青蛙生存的模拟环境，使用tkinter作画

from version.utils.EggTool import EggTool
from version.Frog import Frog

from random import randint

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class Env(object):
    def __init__(self,canvas):
        self.SHOW_SPEED=1

        self.STEPS_PER_ROUND=5000

        self.DELETE_EGGS=True

        self.ENV_XSIZE=300
        self.ENV_YSIZE=300

        self.foods=[]

        self.FOOD_QTY=2000
        self.EGG_QTY=80

        self.frogs=[]
        self.eggs=[]

        self.canvas=canvas

        print('Abrabrabra!')
        if self.DELETE_EGGS:
            EggTool().deleteEggs()

        for i in range(self.ENV_XSIZE):
            food=[]
            for j in range(self.ENV_YSIZE):
                food.append(0)
            self.foods.append(food)

    def rebuildFrogAndFood(self):
        self.frogs.clear()
        for i in range(self.ENV_XSIZE):
            for j in range(self.ENV_YSIZE):
                self.foods[i][j]=0
        for i in range(len(self.eggs)):
            for j in range(4):
                self.frogs.append()