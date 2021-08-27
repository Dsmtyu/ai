from tkinter import *
import time
CLASSPATH='C:\\Users\\admin\\Desktop\\AI\\'
class Test(object):
    def __init__(self,tk):
        self.tk=tk
        self.canvas=Canvas(self.tk,width=500,height=500,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.imageFile=PhotoImage(file=CLASSPATH+'frog.gif')
        self.image=self.canvas.create_image(100,100,anchor=NW,image=self.imageFile)

    def draw(self):
        self.canvas.move(self.image,10,0)

if __name__ == '__main__':
    tk=Tk()
    tk.title('FrogTest')
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1)
    test=Test(tk)
    while 1:
        test.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.1)