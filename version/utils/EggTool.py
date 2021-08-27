# EggTool.py
# EggTool 对保存Egg的文件进行操作

from version.egg.Egg import Egg

import os,json

CLASSPATH='C:\\Users\\admin\\Desktop\\AI\\'

class EggTool(object):
    def layEggs(self,env):
        env.frogs.sort(key=lambda frog:frog.energy)
        print('First frog energy=%d, Last frog energy=%d'%(env.frogs[0].energy,env.frogs[len(env.frogs)-1].energy))
        print('%d,'%frog.energy for frog in env.frogs)
        try:
            newEggs=[]
            for i in range(env.EGG_QTY):
                newEggs.append(env.frogs[i].layEgg())
            with open(CLASSPATH+'eggs.json','w',encoding='utf-8',errors='ignore') as f:
                for newEgg in newEggs:
                    f.write()
            env.eggs=newEggs
            print("Saved",len(env.eggs),"eggs to file '"+CLASSPATH+"eggs.json"+"'")
        except IOError as e:
            print(e)

    def loadEggs(self,env):
        errorfound=False
        try:
            with open(CLASSPATH+'eggs.json','r',encoding='utf-8',errors='ignore') as f:
                env.eggs=f.read()
            print("Loaded",len(env.eggs),"eggs from file '"+CLASSPATH+"eggs.json"+"'.")
        except Exception as e:
            errorfound=True
            print(e)
        if errorfound:
            print("No eggs files '"+CLASSPATH+"' found, created",env.EGG_QTY,"new eggs to do test.")
            env.eggs=[]
            for i in range(env.EGG_QTY):
                env.eggs.append(Egg().createBrandNewEgg())

    def deleteEggs(self):
        print("Delete exist egg file: '"+CLASSPATH+"eggs.json'.")
        os.remove(CLASSPATH+'eggs.json')