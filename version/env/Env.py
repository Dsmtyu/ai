# Env.py
# Env是青蛙生存的模拟环境，使用tkinter作画

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

        print('Abrabrabra!')