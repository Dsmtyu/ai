from random import *

classpath='C:\\Users\\admin\\Desktop\\AI\\'

# Speed of test
SHOW_SPEED=1
# Steps of one test round
STEPS_PER_ROUND=10
DELETE_EGGS=False#每次运行是否先删除保存的蛋
# 屏幕的长和宽
ENV_XSIZE=300
ENV_YSIZE=300
FROG_BRAIN_LENGTH=1000
FOOD_QTY=5000#食物总量
EGG_QTY=80#蛋总量

def nextFloat(): return randint(1,100000)/100000

def nextInt(number): return randint(1,number)