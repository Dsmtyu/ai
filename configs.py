from random import *

classpath='C:\\Users\\admin\\Desktop\\AI\\'

# Speed of test
SHOW_SPEED=1
# Steps of one test round
STEPS_PER_ROUND=100
DELETE_EGGS:bool=False#每次运行是否先删除保存的蛋
# 屏幕的长和宽
ENV_XSIZE=300
ENV_YSIZE=300
FROG_BRAIN_LENGTH=1000
FOOD_QTY=2000#食物总量
EGG_QTY=20#蛋总量

HUNGRY=0
UP=1
DOWN=2
LEFT=3
RIGHT=4
EAT=5

def nextFloat()->float: return randint(1,100000)/100000

def nextInt(number:int)->int: return randint(1,number)

def percent(number:int)->int: return nextInt(100)<=number

def vary(number):
    if percent(95):return number
    rate=0.1 if percent(20) else 0.05
    return float(number*(1-rate)+nextFloat()*rate*2)