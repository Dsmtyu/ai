# Cell.py
# Cell是细胞，属性有：细胞属于的小组编号，细胞输入区，细胞输出区

class Cell(object):
    def __init__(self):
        self.group=0
        self.inputs=[] #细胞输入区
        self.outputs=[] #细胞输出区

    def activate(self):
        for xy in self.inputs:
            pass