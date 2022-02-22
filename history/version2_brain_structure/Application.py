#Application.py
#Application负责项目的启动,关闭等基础服务
#-----------------------------------------------------------------------------------------------------------------------
from history.version2_brain_structure.Env import Env
from history.version2_brain_structure.BrainStructure import BrainStructure
from configs import *

from tkinter import *
import logging;logging.basicConfig(level=logging.INFO)

class Application(object):
    def __init__(self):
        self.tk:Tk=Tk()
        self.tk.title('Frog test round 0')
        self.tk.geometry("1000x500")

        self.envcanvas:Canvas=Canvas(self.tk,width=300,height=300,bd=0,highlightthickness=0)
        self.envcanvas.pack()
        self.envcanvas.place(x=100,y=100)

        self.braincanvas:Canvas=Canvas(self.tk,width=FROG_BRAIN_DISPLAY_LENGTH,height=FROG_BRAIN_DISPLAY_LENGTH,
                                       bd=0,highlightthickness=0)
        self.braincanvas.pack()
        self.braincanvas.place(x=500,y=0)

        self.tk.update()

    def main(self):
        brain_structure=BrainStructure(self.tk,self.braincanvas)
        env:Env=Env(self.tk,self.envcanvas,brain_structure)
        try:
            env.run()
            self.tk.destroy()
        except TclError:
            pass