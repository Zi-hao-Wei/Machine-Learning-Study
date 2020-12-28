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

        (self._keyTree,self._tree)=self.makeTree(self._config.vector,self._train)
        # print(self._keyTree)

    def makeTree(self,keyLeft,subTree):
        if (len(pd.value_counts(subTree[self._config.label[0]])) == 1) or (keyLeft==[]) :
                vCount=pd.value_counts(subTree[self._config.label[0]])
                result = list(vCount.index)[0]
                return (("#",result),result)

        gainRatioList=[]
        for key in keyLeft:
            gainRatioList.append((key,self.gainRatio(key,subTree)))
        
        gainRatioList=sorted(gainRatioList,key=lambda x: x[1],reverse=True)

        usedKey=gainRatioList[0][0]
        
        keyLeftNext=keyLeft.copy()
        keyLeftNext.remove(usedKey)
        newSubTreeTupleList=list(subTree.groupby(usedKey))
        newSubTree={}
        keyTreeTemp={}
        
        for i in newSubTreeTupleList:
            (keyTreeTemp[i[0]],newSubTree[i[0]]) = self.makeTree(keyLeftNext,i[1])
        
        keyTree=(usedKey,keyTreeTemp)
        
        return (keyTree,newSubTree)
        
    def gainRatio(self,key,dataList):
        # 信息增益率
        D=self.infor(dataList)
        #条件熵
        divided=list(dataList.groupby(key))
        D_A=0
        D_Count=len(dataList)

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

    def infor(self,dataList):
        #信息熵
        counting=pd.value_counts(dataList[self._config.label[0]])/len(dataList)
        entropy=np.sum(np.log2(counting)*counting*-1)
        return entropy

    def predict_one(self,Test):
        return self.predictHelper(Test,self._keyTree)
        # print(res)

    def predictHelper(self,Test,DecisionTree):
        keyNow=DecisionTree[0]
        # print(keyNow)
        if (keyNow=="#"):
            return DecisionTree[1]
        else:
            subTree=DecisionTree[1]
            for i in range(0,len(self._config.vector)):
                if (self._config.vector[i]==keyNow):
                    getKeyValue=Test[i]
                    SubTree=subTree[getKeyValue]
                    return self.predictHelper(Test,SubTree)

    def predict(self,Test):
        count=0
        for case in Test:
            test=case[0]
            res=case[1]
            pre=self.predict_one(test)
            if(pre==res):
                count=count+1
        print(count/len(Test))

def main():
    config=DBconfig.DBconfig()
    divider=TestTrainDivider.TestTrainDataDivider(config)
    (Test,Train)=divider.divide(0.1)

    decisionTree=DecisionTreeC4_5(config)
    decisionTree.predict(Test)
    # print(len(Test),len(Train))

if __name__ == '__main__':
    main()