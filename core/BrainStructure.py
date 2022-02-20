#BrainStructure.py
#BrainStructure负责脑图的构建
#-----------------------------------------------------------------------------------------------------------------------

from tkinter import *

from configs import *

from core.egg.Zone import Zone
from core.Frog import Frog

class BrainStructure(object):
    def __init__(self,tk:Tk,canvas:Canvas):
        self.tk:Tk=tk
        self.canvas:Canvas=canvas
        self.colors:list[str]=['red','blue','yellow','green','pink']
        self.rate=FROG_BRAIN_DISPLAY_LENGTH/FROG_BRAIN_LENGTH

    def drawZone(self,zone:Zone,outline:str='black',fill:str=''):
        self.canvas.create_rectangle(round((zone.x-zone.radius)*self.rate),
                                     round((zone.y-zone.radius)*self.rate),
                                     round((zone.x+zone.radius)*self.rate),
                                     round((zone.y+zone.radius)*self.rate),
                                     fill=fill,outline=outline)

    def drawLine(self,fromZone:Zone,toZone:Zone):
        self.canvas.create_line(round(fromZone.x*self.rate),
                                round(fromZone.y*self.rate),
                                round(toZone.x*self.rate),
                                round(toZone.y*self.rate))

    def drawBrain(self,frog:Frog):
        self.canvas.create_rectangle(0,0,FROG_BRAIN_DISPLAY_LENGTH,FROG_BRAIN_DISPLAY_LENGTH,fill='white')
        self.drawZone(frog.eye)
        self.drawZone(frog.moveUpZone)
        self.drawZone(frog.moveDownZone)
        self.drawZone(frog.moveLeftZone)
        self.drawZone(frog.moveRightZone)

        for cellgroup in frog.egg.cellgroups:
            shuffle(self.colors)
            color:str=self.colors[0]
            self.drawLine(fromZone=cellgroup.groupInputZone,toZone=cellgroup.groupOutputZone)
            self.drawZone(cellgroup.groupInputZone,outline=color)
            self.drawZone(cellgroup.groupOutputZone,fill=color)

        self.tk.update()
        self.tk.update_idletasks()