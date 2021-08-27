# Application.py
# Application负责项目的启动，关闭等基础服务

from version.env.Env import Env

from tkinter import *
import time

class Application(object):
    def __init__(self):
        self.tk=Tk()
        self.tk.title('Frog test round: 0, time used: 0s')
        self.canvas=Canvas(self.tk,width=520,height=550,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.tk.update()

    def main(self):
        env=Env(self.tk,self.canvas)
        while True:
            env.run()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)