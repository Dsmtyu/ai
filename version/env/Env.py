# Env.py
# Env是青蛙生存的模拟环境，使用tkinter作画

from version.utils.EggTool import EggTool
from version.Frog import Frog

from random import randint
import time

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class Env(object):
    def __init__(self,tk,canvas):
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

        self.tk=tk#Tk()
        self.canvas=canvas#Canvas()

        print('Abrabrabra!')
        #if self.DELETE_EGGS:
         #   EggTool().deleteEggs()

        for i in range(self.ENV_XSIZE):
            self.foods.append([])
            for j in range(self.ENV_YSIZE):
                self.foods[i].append(0)

    def rebuildFrogAndFood(self):
        self.frogs.clear()
        for i in range(self.ENV_XSIZE):
            for j in range(self.ENV_YSIZE):
                self.foods[i][j]=0
        for i in range(len(self.eggs)):
            for j in range(4):#一个Egg生出4个Frog
                self.frogs.append(Frog(self.ENV_XSIZE/2-45+nextInt(90),self.ENV_YSIZE/2-45+nextInt(90),self.eggs[i],self.canvas))
        print("Created %d frogs"%(4*len(self.eggs)))
        for i in range(self.FOOD_QTY):
            self.foods[nextInt(self.ENV_XSIZE-3)][nextInt(self.ENV_YSIZE-3)]=1

    def drawFood(self):
        for x in range(self.ENV_XSIZE):
            for y in range(self.ENV_YSIZE):
                if self.foods[x][y]:
                    foodid=self.canvas.create_oval(2,2,2,2,fill='black')
                    self.canvas.move(foodid,x,y)

    def run(self):
        EggTool().loadEggs(self)
        _round=1
        while True:
            t1=time.time()
            self.rebuildFrogAndFood()
            allDead=False
            for i in range(self.STEPS_PER_ROUND):
                if allDead:
                    break
                allDead=True
                for frog in self.frogs:
                    if frog.active(self):
                        allDead=False
                    if frog.alive and frog.moveCount==0 and i>100:
                        frog.alive=False
                if i%self.SHOW_SPEED:
                    continue
                for frog in self.frogs:
                    frog.show()
                self.drawFood()
            EggTool().layEggs(self)
            t2=time.time()
            self.tk.title('Frog test round:',_round,', time used:',(t2-t1),'s')
            _round+=1