# Application.py
# Application负责项目的启动，关闭等基础服务

from history.version1_1.env.Env import Env

from tkinter import *

class Application(object):
    def __init__(self):
        self.tk=Tk()
        self.tk.title('Frog test round: 0, time used: 0s')
        self.tk.geometry("520x550")
        self.canvas=Canvas(self.tk,width=300,height=300,bd=0,highlightthickness=0)
        self.canvas.place(x=100,y=100)
        self.tk.update()

    def main(self):
        env=Env(self.tk,self.canvas)
        try:
            env.run()
        except Exception:
            pass