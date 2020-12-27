import TestTrainDataDivider
import math

class NaiveBayes:
    def __init__(self,hamTrain,spamTrain):
        self._ham=hamTrain
        self._spam=spamTrain
        
        self._hamCount=len(hamTrain)
        self._spamCount=len(spamTrain)
        self._count=self._hamCount+self._spamCount
        
        #先验概率
        self._hamProbability=self._hamCount/self._count
        self._spamProbabilty=self._spamCount/self._count

        self._hamWordsList=sum(self._ham,[])
        self._spamWordsList=sum(self._spam,[])

        self._hamWordsCount=len(self._hamWordsList)
        self._spamWordsCount=len(self._spamWordsList)
        print(self._hamWordsCount)
        print(self._spamWordsCount)


        self._allWordsCount = len(list(set(self._hamWordsList+self._spamWordsList)))
        
        #字典
        self._hamHash=self.wordsHash(self._hamWordsList)
        self._spamHash=self.wordsHash(self._spamWordsList)

        
    def wordsHash(self,wordList):
        wordsHashTable={}
        for i in wordList:
            if(i in wordsHashTable):
                wordsHashTable[i]=wordsHashTable[i]+1
            else:
                wordsHashTable[i]=1
        return wordsHashTable
        
    def probability(self,word):
        # print(self._hamHash)

        hamPro=self._hamHash.get(word,0)+1
        spamPro=self._spamHash.get(word,0)+1

        # print("-----------------")
        # print(hamPro)
        # print(spamPro)

        hamPro=math.log(hamPro/(self._hamWordsCount+self._allWordsCount))
        spamPro=math.log(spamPro/(self._spamWordsCount+self._allWordsCount))
        # print("-----------------")
        # print(hamPro)
        # print(spamPro)
        # print("-----------------")
        # print("-----------------")
        
        return(hamPro,spamPro)
    
    def predict_one(self,test):
        hamPro=math.log(self._hamProbability)
        spamPro=math.log(self._spamProbabilty)
        print("ORIGINAL")
        # print(hamPro)
        # print(spamPro)

        for word in test:
            pro=self.probability(word)
            hamPro=hamPro+pro[0]
            spamPro=spamPro+pro[1]
        
        print(hamPro)
        print(spamPro)
        
        if (hamPro>=spamPro):
            return "ham"
        else:
            return "spam"

def main():
    divider=TestTrainDataDivider.TestTrainDataDivider("SMSSpamData.json")
    (Test,hamTrain,spamTrain)=divider.divide(0.2)
    bayes=NaiveBayes(hamTrain,spamTrain)

    for test in Test["spam"]:
        print(test)
        print(bayes.predict_one(test))
        # break



if __name__ == '__main__':
    main()