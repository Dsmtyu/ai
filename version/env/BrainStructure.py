import random

class BrainStructure(object):
    def __init__(self,tk,canvas,app):
        self.tk=tk
        self.canvas=canvas
        self.app=app
        self.colors=['red','orange','yellow','green','blue']

    def drawZone(self,z,outline='black',fill='white'):
        self.canvas.create_rectangle(
            round(z.x-z.radius/2),round(z.y-z.radius/2),round(z.x+z.radius/2),round(z.y+z.radius/2),
            outline=outline,fill=fill
        )

    def drawBrain(self,frog):
        self.canvas.create_rectangle(0,0,800,800,outline='black',fill='white')
        self.drawZone(frog.eye,outline='red')

        self.drawZone(frog.moveUp,outline='gray')
        self.drawZone(frog.moveDown,outline='gray')
        self.drawZone(frog.moveLeft,outline='gray')
        self.drawZone(frog.moveRight,outline='gray')

        for cellgroup in frog.egg.cellgroups:
            random.shuffle(self.colors)
            color=self.colors[1]
            self.canvas.create_line(
                round(cellgroup.groupInputZone.x),round(cellgroup.groupInputZone.y),
                round(cellgroup.groupOutputZone.x),round(cellgroup.groupOutputZone.y),
                fill=color
            )
            self.drawZone(cellgroup.groupInputZone,outline=color)
            self.drawZone(cellgroup.groupOutputZone,fill=color)

        for cell in frog.cells:
            pass

        self.tk.update_idletasks()
        self.tk.update()