import sys
import numpy as np
sys.path.append("..")
import Tools.MySqlConnection
import DBconfig
import random
import math
class TestTrainDataDivider:
    def __init__(self,config):
        self._config=config
        self._mc=Tools.MySqlConnection.MySqlConnection(self._config.db_config)
    def divide(self,ratio):
        vectorList=self._mc.select(self._config.dbName,self._config.vector)
        labelList=self._mc.select(self._config.dbName,self._config.label)
        
        normedVectorList=self.normalization(np.array(vectorList)).tolist()
        dataSet=[]
        for i in range(0,len(normedVectorList)):
            vector=list(normedVectorList[i])
            label=labelList[i][0]
            dataSet.append((vector,label))


        Test=random.sample(dataSet,math.floor(len(dataSet)*ratio))
        for i in Test:
            if (i in dataSet):
                dataSet.remove(i)
        return(Test,dataSet)

    def normalization(self,dataSet):
        max_arr = dataSet.max(axis=0)
        min_arr = dataSet.min(axis=0)
        ranges = max_arr - min_arr
        norDataSet = np.zeros(dataSet.shape)
        m = dataSet.shape[0]
        norDataSet = dataSet - np.tile(min_arr, (m, 1))
        norDataSet = norDataSet/np.tile(ranges,(m,1))
        return norDataSet


def main():
    config=DBconfig.DBconfig()
    divider=TestTrainDataDivider(config)
    (Test,Train)=divider.divide(0.1)
    print(Test)
    print(Train)
if __name__ == '__main__':
    main()