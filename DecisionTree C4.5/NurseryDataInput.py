import sys
sys.path.append("..")
import Tools.MySqlConnection
import DBconfig

class NurseryDataInput:
    def __init__(self,path):
        try:
            self._f=open(path,'r')
        except:
            print("Wrong Path")
    
    def process(self):

        AllLines= self._f.readlines()
        self._Lines=[]
        for oneLine in AllLines[:-1]:
            oneLine=oneLine.rstrip()
            processedStr=oneLine.split(",")
            self._Lines.append(processedStr)
    
    def insertToDataBase(self):
        config=DBconfig.DBconfig()

        mc = Tools.MySqlConnection.MySqlConnection(config.db_config)
        
        # mc.version()
        mc.create(config.dbName,config.nursery_config)
        genData = lambda a,b: list(zip(a,b))

        for line in self._Lines:            
            mc.insert(config.dbName,genData(config.key,line))

            
    def __del__(self):
        self._f.close()

def main():
    dataProcess=NurseryDataInput("nursery.data")
    dataProcess.process()
    dataProcess.insertToDataBase()

if __name__ == '__main__':
    main()