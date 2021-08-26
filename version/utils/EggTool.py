# EggTool.py
# EggTool 对保存Egg的文件进行操作

from version.env.Application import Application
from version.egg.Egg import Egg

import os

class EggTool(object):
    def layEggs(self,env):
        env.frogs.sort(key=lambda frog:frog.energy)
        print('First frog energy=%d, Last frog energy=%d'%(env.frogs[0].energy,env.frogs[len(env.frogs)-1].energy))
        for frog in env.frogs:
            print('%d,'%frog)
        try:
            newEggs=[]
            for i in range(env.EGG_QTY):
                newEggs.append(env.frogs[i].layEgg())
            with open(Application().CLASSPATH+'egg.ser','w',encoding='utf-8',errors='ignore') as f:
                f.write(newEggs)
            env.eggs=newEggs
            print("Saved "+len(env.eggs)+" eggs to file '"+Application().CLASSPATH+"eggs.ser"+"'")
        except IOError as e:
            print(e)

    def loadEggs(self,env):
        errorfound=False
        try:
            with open(Application().CLASSPATH+'egg.ser','r',encoding='utf-8',errors='ignore') as f:
                env.eggs=f.read()
            print("Loaded "+len(env.eggs)+" eggs from file '"+Application().CLASSPATH+"eggs.ser"+"'.")
        except Exception as e:
            errorfound=True
        if errorfound:
            print("No eggs files '"+Application().CLASSPATH+"' found, created "+env.EGG_QTY+" new eggs to do test.")
            env.eggs=[]
            for _ in range(env.EGG_QTY):
                env.eggs.append(Egg().createBrandNewEgg())

    def deleteEggs(self):
        print("Delete exist egg file: '"+Application().CLASSPATH+"eggs.ser'.")
        os.remove(Application().CLASSPATH+'eggs.ser')