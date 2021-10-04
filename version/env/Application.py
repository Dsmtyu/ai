# Application.py
# Application负责项目的启动，关闭等基础服务

from version.env.Env import Env
from version.env.BrainStructure import BrainStructure

from tkinter import *

class Application(object):
    def __init__(self):
        self.envtk=Tk()
        self.envtk.title('Frog test round: 0, time used: 0s')
        self.envtk.geometry("500x500+0+0")
        self.envcanvas=Canvas(self.envtk,width=300,height=300,bd=0,highlightthickness=0)
        self.envcanvas.place(x=100,y=100)
        self.braintk=Tk()
        self.braintk.title('Brain picture')
        self.braintk.geometry("500x500+600+0")
        self.braincanvas=Canvas(self.braintk,width=800,height=800,bd=0,highlightthickness=0)

        self.envtk.update()
        self.braintk.update()

        self.env=Env(self.envtk,self.envcanvas,self)
        self.brain_structure=BrainStructure(self.braintk,self.braincanvas,self)

    def main(self):
        try:
            self.env.run()
        except TclError:
            pass