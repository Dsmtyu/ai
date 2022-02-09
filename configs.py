from random import *
from enum import Enum,unique

classpath='C:/Users/admin/Desktop/AI/'

# Speed of test
SHOW_SPEED:int=1
# Steps of one test round
STEPS_PER_ROUND:int=100
DELETE_EGGS:bool=True#每次运行是否先删除保存的蛋
# 屏幕的长和宽
ENV_XSIZE=300
ENV_YSIZE=300
FROG_BRAIN_LENGTH=1000
FOOD_QTY=2000#食物总量
EGG_QTY=20#蛋总量

def nextFloat()->float: return randint(1,100000)/100000

def nextInt(number:int)->int: return randint(1,number)

def percent(number:int)->bool: return nextInt(100)<=number

def vary(number:float)->float:
    if percent(95):return number
    rate=0.1 if percent(20) else 0.05
    return float(number*(1-rate)+nextFloat()*rate*2)

@unique
class Direction(Enum):
    LEFT=1
    RIGHT=2
    UP=3
    DOWN=4