import json
import random
import math
class TestTrainDataDivider:
    def __init__(self,path):
        with open("SMSSpamData.json", "r", encoding='utf-8') as f:
            self._data=json.load(f)
            # print(self._data)

    def divide(self,ratio):
        
        hamList=self._data["ham"]
        spamList=self._data["spam"]
                
        Test={}
        Test["ham"]=random.sample(hamList,math.floor(len(hamList)*ratio))
        Test["spam"]=random.sample(spamList,math.floor(len(spamList)*ratio))
        
        for i in Test["ham"]:
            if (i in hamList):
                hamList.remove(i)

        for i in Test["spam"]:
            if (i in spamList):
                spamList.remove(i)

        return(Test,hamList,spamList)




def main():
    divider=TestTrainDataDivider("SMSSpamData.json")
    (Test,hamTrain,spamTrain)=divider.divide(0.1)
    print(Test)
    print(hamTrain)
    print(spamTrain)
if __name__ == '__main__':
    main()