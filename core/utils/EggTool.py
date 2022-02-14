#EggTool.py
#EggTool 对保存Egg的文件进行操作
#-----------------------------------------------------------------------------------------------------------------------
from core.egg.Egg import Egg

import pickle,os,logging
from configs import *

CLASSPATH=classpath+'core/'#保存蛋文件的目录路径

class EggTool(object):
    @staticmethod
    def layEggs(env):
        logging.info('Laying eggs!')
        env.frogs.sort(key=lambda frog:frog.energy,reverse=True)
        logging.info('First frog energy=%d, Last frog energy=%d'%(env.frogs[0].energy,env.frogs[len(env.frogs)-1].energy))
        froglist=[]
        for frog in env.frogs:
            froglist.append('%d'%frog.energy)
        logging.info(','.join(froglist))
        try:
            newEggs=[]
            for i in range(EGG_QTY):
                newEggs.append(env.frogs[i].layEgg())
            with open(CLASSPATH+'eggs.ser','wb') as f:
                pickle.dump(newEggs,f)
            env.eggs=newEggs
            logging.info("Saved %d eggs to file '%seggs.ser'"%(len(env.eggs),CLASSPATH))
        except IOError as e:
            logging.error(e)

    @staticmethod
    def loadEggs(env):
        logging.info('Loading eggs!')
        errorfound=False
        try:
            with open(CLASSPATH+'eggs.ser','rb') as f:
                env.eggs=pickle.load(f)
            logging.info("Loaded %d eggs from file %seggs.ser'."%(len(env.eggs),CLASSPATH))
        except Exception as e:
            errorfound=True
        if errorfound:
            logging.info("No eggs files '%s' found, created %d new eggs to do test."%(CLASSPATH,EGG_QTY))
            env.eggs=[]
            for i in range(EGG_QTY):
                env.eggs.append(Egg.createBrandNewEgg())

    @staticmethod
    def deleteEggs():
        logging.info('Deleting eggs!')
        try:
            os.remove(CLASSPATH+'eggs.ser')
            logging.info("Delete exist egg file: '"+CLASSPATH+"eggs.ser'.")
        except FileNotFoundError:
            logging.error("No exist egg file: '"+CLASSPATH+"eggs.ser'.")