import sys
import numpy as np
sys.path.append("..")
import Tools.MySqlConnection
import DBconfig
import random
import math
import pandas as pd

class TestTrainDataDivider:
    def __init__(self,config):
        self._config=config
        self._mc=Tools.MySqlConnection.MySqlConnection(self._config.db_config)
    def divide(self,ratio):
        vectorList=self._mc.select(self._config.dbName,self._config.vector)
        labelList=self._mc.select(self._config.dbName,self._config.label)
        
        dataSet=[]
        self._train=[]
        for i in range(0,len(vectorList)):
            vector=list(vectorList[i])
            label=labelList[i][0]
            dataSet.append((vector,label))
            self._train.append(vector+[label])


        Test=random.sample(dataSet,math.floor(len(dataSet)*ratio))
        for i in Test:
            if (i in dataSet):
                dataSet.remove(i)
        return(Test,dataSet)

    def trainInsert(self):
        self._mc.create(self._config.dbTrainName,self._config.nursery_config)
        genData = lambda a,b: list(zip(a,b))
        # print()
        for line in self._train:            
            # print(line)
            self._mc.insert(self._config.dbTrainName,genData(self._config.key,line))
            
def main():
    config=DBconfig.DBconfig()
    divider=TestTrainDataDivider(config)
    (Test,Train)=divider.divide(0.1)
    divider.trainInsert()
    # print(len(Test),len(Train))

if __name__ == '__main__':
    main()