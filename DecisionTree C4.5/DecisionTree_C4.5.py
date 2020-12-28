import sys
import numpy as np
import pandas as pd
sys.path.append("..")
import Tools.MySqlConnection
import TestTrainDivider
import DBconfig
class DecisionTreeC4_5:
    def __init__(self,config):
        self._config=config
        self._mc=Tools.MySqlConnection.MySqlConnection(self._config.db_config)
        readSql="SELECT "+self._config.vectorString+" FROM " + config.dbTrainName


        
        self._train=pd.read_sql(readSql,self._mc.returnDB())
        print(self.gainRatio("parents",self._train))



    def makeTree(self,vectorLeft,subTree):
        
        gainRatioList=[]
        # for key in vectorLeft:
        #     self.gainRation()


    def gainRatio(self,key,vectorList):
        # 信息增益率
        D=self.infor(vectorList)
        #条件熵
        divided=list(vectorList.groupby(key))
        D_A=0
        D_Count=len(vectorList)

        #特征熵
        h=0
        for inforA in divided:
            D_Di=len(inforA[1])/D_Count
            D_A=D_A + D_Di*self.infor(inforA[1])
            h=h - np.log2(D_Di)*D_Di 
        
        #信息增益
        g = D - D_A
        
        r = g/h
        return r




    def infor(self,vectorList):
        #信息熵
        counting=pd.value_counts(vectorList[self._config.label[0]])/len(vectorList)
        entropy=np.sum(np.log2(counting)*counting*-1)
        return entropy

def main():
    config=DBconfig.DBconfig()
    divider=TestTrainDivider.TestTrainDataDivider(config)
    (Test,Train)=divider.divide(0.1)

    decisionTree=DecisionTreeC4_5(config)
    
    # print(len(Test),len(Train))

if __name__ == '__main__':
    main()