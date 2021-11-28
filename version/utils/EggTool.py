# EggTool.py
# EggTool 对保存Egg的文件进行操作

from version.egg.Egg import Egg

import os,pickle,time
from configs import *

CLASSPATH=classpath#根目录路径

class EggTool(object):
    def layEggs(self,env):
        print('[LAY EGG]:Laying eggs!')
        env.frogs.sort(key=lambda frog:frog.energy,reverse=True)
        print('First frog energy=%d, Last frog energy=%d'%(env.frogs[0].energy,env.frogs[len(env.frogs)-1].energy))
        froglist=[]
        for frog in env.frogs:
            froglist.append('%d'%frog.energy)
        print(','.join(froglist))
        try:
            newEggs=[]
            for i in range(EGG_QTY):
                newEggs.append(Egg(env.frogs[i]))
            with open(CLASSPATH+'eggs.ser','wb') as f:
                pickle.dump(newEggs,f)
            env.eggs=newEggs
            print("Saved",len(env.eggs),"eggs to file '"+CLASSPATH+"eggs.ser"+"'")
        except IOError as e:
            print(e)

    def loadEggs(self,env):
        print('[LOAD EGG]:Loading eggs!')
        errorfound=False
        try:
            with open(CLASSPATH+'eggs.ser','rb') as f:
                env.eggs=pickle.load(f)
            print("Loaded",len(env.eggs),"eggs from file '"+CLASSPATH+"eggs.ser"+"'.")
        except Exception as e:
            errorfound=True
        if errorfound:
            print("No eggs files '"+CLASSPATH+"' found, created",EGG_QTY,"new eggs to do test.")
            env.eggs=[]
            for i in range(EGG_QTY):
                env.eggs.append(Egg().createBrandNewEgg())

    def deleteEggs(self):
        print('[DELETE EGG]:Deleting eggs!')
        try:
            os.remove(CLASSPATH+'eggs.ser')
            print("Delete exist egg file: '"+CLASSPATH+"eggs.ser'.")
        except FileNotFoundError:
            print("No exist egg file: '"+CLASSPATH+"eggs.ser'.")