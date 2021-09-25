# Env.py
# Env是青蛙生存的模拟环境，使用tkinter作画

from history.version1.utils.EggTool import EggTool
from history.version1.Frog import Frog

from random import randint
import time

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)

class Env(object):
    def __init__(self,tk,canvas,brain_structure):
        #Speed of test
        self.SHOW_SPEED=1
        #Steps of one test round
        self.STEPS_PER_ROUND=5

        self.DELETE_EGGS=False #每次运行是否先删除保存的蛋
        #屏幕的长和宽
        self.ENV_XSIZE=300
        self.ENV_YSIZE=300

        self.foods=[] #foods

        self.FOOD_QTY=5000 #as name
        self.EGG_QTY=80 #as name

        self.frogs=[] #Frog
        self.eggs=[] #Egg

        self.tk=tk#Tk()
        self.canvas=canvas#Canvas()
        self.brain_structure=brain_structure

        print('Abrabrabra!')
        if self.DELETE_EGGS:
            EggTool().deleteEggs()

        for i in range(self.ENV_XSIZE):
            self.foods.append([])
            for j in range(self.ENV_YSIZE):
                self.foods[i].append(0)

    def rebuildFrogAndFood(self):
        #先把背景画成白色
        self.canvas.create_rectangle(0,0,self.canvas.winfo_width(),self.canvas.winfo_height(),fill='white')
        self.frogs.clear()#清空Frogs
        frogid=0
        for i in range(self.ENV_XSIZE):
            for j in range(self.ENV_YSIZE):
                self.foods[i][j]=0#清空食物
        for i in range(len(self.eggs)):
            for j in range(4):#一个Egg生出4个Frog
                self.frogs.append(Frog(self.ENV_XSIZE/2+nextInt(90),self.ENV_YSIZE/2+nextInt(90),self.eggs[i],
                                       self.tk,self.canvas,frogid))
                frogid+=1
        print("Created %d frogs"%(4*len(self.eggs)))
        for i in range(self.FOOD_QTY):
            self.foods[nextInt(self.ENV_XSIZE-3)][nextInt(self.ENV_YSIZE-3)]=1

    def drawFood(self,canvas):#画食物
        for x in range(self.ENV_XSIZE):
            for y in range(self.ENV_YSIZE):
                if self.foods[x][y]==1:
                    canvas.create_oval(x,y,x+2,y+2,outline='black',fill='black')
                elif self.foods[x][y]==-1:
                    canvas.create_oval(x,y,x+2,y+2,outline='white',fill='white')

    def run(self):#运行
        EggTool().loadEggs(self)#导入或新建一批Egg
        _round=1#运行次数
        while True:
            t1=time.time()#开始时间
            self.rebuildFrogAndFood()
            allDead=False#青蛙是否全部死亡
            for i in range(self.STEPS_PER_ROUND):
                self.drawFood(self.canvas)#画食物
                if allDead:#全部死亡就可以提前结束
                    break
                allDead=True
                for frog in self.frogs:
                    if frog.active(self):
                        allDead=False
                    if frog.alive and frog.moveCount==0 and i>100:#不移动的”懒惰青蛙“死亡
                        frog.alive=False
                if i%self.SHOW_SPEED:#画青蛙会拖慢速度
                    continue
                for frog in self.frogs:#画青蛙
                    if frog.alive:
                        frog.show(self.canvas)#青蛙移动
                self.tk.update_idletasks()
                self.tk.update()
            EggTool().layEggs(self)#保存蛋
            self.brain_structure.drawBrain(self.frogs[0])
            t2=time.time()#结束时间
            self.tk.title('Frog test round: %d , time used: %.4f s'%(_round,t2-t1))
            _round+=1