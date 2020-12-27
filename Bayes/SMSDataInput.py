import json
import re
class SMSDataInput:
    def __init__(self,path):
        try:
            self._f=open(path,'r', errors='ignore')
        except:
            print("Wrong Path")
    
    def process(self):
        lines=self._f.readlines()
        self._ham=[]
        self._spam=[]

        for line in lines:
            line=re.sub(r"[^a-zA-Z]"," ",line.lower())
            original_words=re.split(r"\W+",line)
            
            smsType=original_words[0]
            words=list(filter(self.filter_fun ,original_words[1:]))
            if (smsType=="ham"):
                self._ham.append(words)
            else:
                self._spam.append(words)

    def dump(self,path):
        data={}
        data["ham"]=self._ham
        data["spam"]=self._ham
        with open(path, "w", encoding='utf-8') as f:
            json.dump(data,f,indent=4)

    def filter_fun(self,x):
        return (len(x)>=3)    
    
    def __del__(self):
        self._f.close()

def main():
    dataProcess=SMSDataInput("SMSSpamCollection")
    dataProcess.process()
    dataProcess.dump("SMSSpamData.json")


if __name__ == '__main__':
    main()