# Cell.py
# Cell是神经元，属性有：神经元属于的小组编号，神经元输入区，神经元输出区

class Cell(object):
    def __init__(self):
        self.group=0
        self.energy=0
        self.inputs=[] #神经元输入区
        self.outputs=[] #神经元输出区

    def activate(self):
        for xy in self.inputs:
            pass