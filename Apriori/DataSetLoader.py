import numpy as np 
import pandas as pd
from MyNLTK import MyNLTK
class DatasetLoader:
    def __init__(self,path):
        self.data=pd.read_csv(path,sep='\t')
        self.nltk=MyNLTK()
        self.data['review_headline']=self.data['review_headline'].apply(self._wordsProcess)
        self.data['review_body']=self.data['review_body'].apply(self._wordsProcess)

        self.data.to_csv('./Processed/microwave.csv')

        print(self.data)
    
    def _wordsProcess(self,sen):
        return self.nltk.process(sen,True,pos=False)



def main():
    dataset=DatasetLoader(r'./data/microwave.tsv')

if __name__=='__main__':
    main()