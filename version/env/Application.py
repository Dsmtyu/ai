# Application.py
# Application负责项目的启动，关闭等基础服务

from tkinter import *

class Application(object):
    def __init__(self):
        self.CLASSPATH='C:\\Users\\admin\\Desktop\\AI\\'
        self.tk=Tk()
        self.canvas=Canvas(width=520,height=550,bd=0,highlightthickness=0)