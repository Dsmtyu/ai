#EggTool.py
#EggTool 对保存Egg的文件进行操作
#-----------------------------------------------------------------------------------------------------------------------
from history.version1.egg.Egg import Egg

import pickle,time
import os
from configs import *

CLASSPATH=classpath+'history/version1/'#保存蛋文件的目录路径

class EggTool(object):
    @staticmethod
    def layEggs(env):
        print('[LAY EGG]:Laying eggs!')
        env.frogs.sort(key=lambda frog:frog.energy,reverse=True)
        print('First frog energy=%d, Last frog energy=%d'%(env.frogs[0].energy,env.frogs[len(env.frogs)-1].energy))
        time.sleep(0.5)
        froglist=[]
        for frog in env.frogs:
            froglist.append('%d'%frog.energy)
        print(','.join(froglist))
        time.sleep(0.5)
        try:
            newEggs=[]
            for i in range(EGG_QTY):
                newEggs.append(env.frogs[i].layEgg())
            with open(CLASSPATH+'eggs.ser','wb') as f:
                pickle.dump(newEggs,f)
            env.eggs=newEggs
            print("Saved",len(env.eggs),"eggs to file '"+CLASSPATH+"eggs.ser"+"'")
        except IOError as e:
            print(e)

    @staticmethod
    def loadEggs(env):
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
                env.eggs.append(Egg().createBrandNewEgg)

    @staticmethod
    def deleteEggs():
        print('[DELETE EGG]:Deleting eggs!')
        try:
            os.remove(CLASSPATH+'eggs.ser')
            print("Delete exist egg file: '"+CLASSPATH+"eggs.ser'.")
        except FileNotFoundError:
            print("No exist egg file: '"+CLASSPATH+"eggs.ser'.")