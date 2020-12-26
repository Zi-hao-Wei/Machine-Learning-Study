import sys
import numpy as np
sys.path.append("..")
import Tools.MySqlConnection
import DBconfig
import TestTrainDataDivider

import random
import math

class KNN:
    def __init__(self,K,Train):
        self._K=K
        self._train=Train

    def distance(self,a,b,type="naive"):
        vector1=np.array(a)
        vector2=np.array(b)
        if(type=="naive"):
            return np.sqrt(np.sum(np.square(vector1-vector2)))
        else:
            return np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2))) 

    def process(self,test):
    #test is a vector, we want to predict its label
        distanceList=[]
        for case in self._train:
            distanceList.append((self.distance(test,case[0]),case[1]))
        distanceList=sorted(distanceList,key=lambda x: x[0])

        judgement={}
        typeMAX=0
        typeANS=""

        for case in distanceList[0:self._K]:
            if case[1] in judgement:
                judgement[case[1]]=judgement[case[1]]+1
            else:
                judgement[case[1]]=1
            if(judgement[case[1]]>typeMAX):
                typeMAX=judgement[case[1]]
                typeANS=case[1]

        return typeANS
    def processALL(self,Test,printed=True):
        truth=0
        for testCase in Test:
            ans = self.process(testCase[0])
            label=testCase[1]
            if (printed):
                print((ans,label,ans==label))
            if (ans==label):
                truth=truth+1
        print(truth/len(Test))


def main():
    K=5
    config=DBconfig.DBconfig()
    divider=TestTrainDataDivider.TestTrainDataDivider(config)
    (Test,Train)=divider.divide(0.1)
    knn=KNN(K,Train)
    knn.processALL(Test,False)

if __name__ == '__main__':
    main()