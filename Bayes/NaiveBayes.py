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
        hamPro=self._hamHash.get(word,0)+1
        spamPro=self._spamHash.get(word,0)+1 


        hamPro=math.log(hamPro/(self._hamWordsCount+self._allWordsCount))
        spamPro=math.log(spamPro/(self._spamWordsCount+self._allWordsCount))
        
        return(hamPro,spamPro)
    
    def predict_one(self,test):
        hamPro=math.log(self._hamProbability)
        spamPro=math.log(self._spamProbabilty)

        for word in test:
            pro=self.probability(word)
            hamPro=hamPro+pro[0]
            spamPro=spamPro+pro[1]
        
        if (hamPro>=spamPro):
            return "ham"
        else:
            return "spam"

    def predict(self,Test):
        hamPredict=0
        spamPredict=0
        for test in Test["ham"]:
            if(self.predict_one(test)=="ham"):
                hamPredict=hamPredict+1
        for test in Test["spam"]:
            if (self.predict_one(test)=="spam"):
                spamPredict=spamPredict+1
            
        print("Ham",hamPredict/len(Test["ham"]))
        print("Spam",spamPredict/len(Test["spam"]))

def main():
    divider=TestTrainDataDivider.TestTrainDataDivider("SMSSpamData.json")
    (Test,hamTrain,spamTrain)=divider.divide(0.2)
    bayes=NaiveBayes(hamTrain,spamTrain)
    bayes.predict(Test)

if __name__ == '__main__':
    main()