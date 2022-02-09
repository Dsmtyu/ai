from random import *
from enum import Enum,unique

classpath='C:/Users/admin/Desktop/AI/'

SHOW_SPEED:int=1#调整实验的速度(1~1000),值越小则越慢
STEPS_PER_ROUND:int=100#每轮测试步数,每一步相当于脑思考的一桢,所有青蛙的脑神经元被遍历一次
DELETE_EGGS:bool=False#每次运行是否先删除保存的蛋,如果设为false,将不删除保存的蛋,会接着上次的测试结果续继运行
# 屏幕的长和宽.通常取值100~1000左右
ENV_XSIZE=300
ENV_YSIZE=300
FROG_BRAIN_LENGTH=1000
FOOD_QTY=2000#食物总量
EGG_QTY=20#蛋总量
FROG_PER_EGG=4#每个蛋可以孵出多少个青蛙

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