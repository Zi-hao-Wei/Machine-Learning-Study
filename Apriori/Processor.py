from efficient_apriori import apriori 
import numpy as np 
import pandas as pd 
import json
import pickle
class featureExtration:
    def __init__(self,path):
        self.data=pd.read_csv(path)
        # print(self.data)
        self.filename='./Result/rules.txt'

    def strToList(self,x):
        l=x[1:-1]
        l=l.replace('\'','').split(',')
        return l
    def stringDataProcess(self,x):
        x=x.values.tolist()
        x=list(map(self.strToList,x))
        return x
  
    def findFeature(self):
        reviewHeadline=self.stringDataProcess(self.data['review_body'])        
        # print(reviewHeadline)

        # # print(reviewHeadline.values.tolist())
        itemsets,rules=apriori(reviewHeadline,min_support=0.02,min_confidence=0.5,max_length=10)
        # print(itemsets)
        # print(rules)
        # f=open(self.filename,'w')  
        # pickle.dump(rules,f,0)
        # with open(filename,'w') as file_obj:
        #     for i in itemsets:
        #         tmp=itemsets[i]
        #         print(tmp)
        #         tmp = json.dumps({str(k): tmp[k] for k in tmp})
        #         json.dump(str(itemsets),file_obj)
        #         break

    # def test(self):
        # rules=pickle.load(self.filename)
        with open(self.filename,'w') as f:
            for rule in rules:
                l=list(rule.lhs)
                r=list(rule.rhs)
                if (" microwave" in l) or (" microwave" in r):
                    f.write(','.join(l)+" -> "+','.join(r)+'\n')
                    print(rule)
                    # f.write(rule.lhs)
                    # f.write(rule.rhs)
            

        # filename='./Result/rules.json'
        # with open(filename,'w') as file_obj:
            
        #     # rules = json.dumps({str(k): rules[k] for k in rules})
        #     json.dump(str(rules),file_obj)

        # for s in itemsets:
            # print(itemsets[s])

def main():
    test=featureExtration(r'./Processed/microwave.csv')
    # test.test()
    test.findFeature()
if __name__=="__main__":
    main()