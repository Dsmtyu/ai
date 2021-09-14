from version.egg.Zone import Zone
from version.egg.CellGroup import CellGroup

from tkinter import *

class BrainPicture(object):
    def __init__(self,x,y,brainLength,brainDisplayLength):
        self.__brainLength=brainLength
        self.__brainDisplayLength=brainDisplayLength
        self.__colors=['red','orange','yellow','green','blue']
        self.__nextColorID=0

    def drawZone(self,canvas,z):
        rate=self.__brainDisplayLength/self.__brainLength
        x=round(z.x*rate)
        y=round(z.y*rate)
        radius=round(z.radius*rate)
        canvas.create_rectangle(x-radius,y-radius,x+radius,y+radius)

    def drawCircle(self,canvas,z):
        rate=self.__brainDisplayLength/self.__brainLength
        x=round(z.x*rate)
        y=round(z.y*rate)
        canvas.create_oval(x-5,y-5,x+5,y+5)

    def drawLine(self,canvas,z1,z2):
        rate=self.__brainDisplayLength/self.__brainLength
        x1=round(z1.x*rate)
        y1=round(z1.y*rate)
        x2=round(z2.x*rate)
        y2=round(z2.y*rate)
        canvas.create_line(x1,y1,x2,y2)

    def drawText(self,canvas,z,text):
        rate=self.__brainDisplayLength/self.__brainLength
        x=round(z.x*rate)
        y=round(z.y*rate)
        canvas.create_text(x,y,text,font=('宋体',5))

    def __nextColor(self):
        if self.__nextColorID==len(self.__colors):
            self.__nextColorID=0
        ans=self.__colors[self.__nextColorID]
        self.__nextColorID+=1
        return ans

    def __color(self,number):
        if number<=20:
            return 'red'
        elif number<=40:
            return 'orange'
        elif number<=60:
            return 'yellow'
        elif number<=80:
            return 'green'
        else:
            return 'blue'