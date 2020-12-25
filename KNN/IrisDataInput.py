import sys
sys.path.append("..")
import Tools.MySqlConnection
import KNNconfig
class IrisDataInput:
    def __init__(self,path):
        try:
            self._f=open(path,'r')
        except:
            print("Wrong Path")
    
    def process(self):
        self.processedLines = []
        AllLines = self._f.readlines()
        for oneLine in AllLines[:-1]:
            oneLine=oneLine.rstrip()
            processedStr=oneLine.split(",")
            processedLine=[]
            for pStr in processedStr[:-1]:
                processedLine.append(float(pStr))
            processedLine.append(processedStr[-1])
            self.processedLines.append(processedLine)
        return self.processedLines
    
    def insertToDataBase(self):
        config=KNNconfig.KNNconfig()

        mc = Tools.MySqlConnection.MySqlConnection(config.db_config)
        
        # mc.version()
        mc.create(config.dbName,config.iris_config)
        genData = lambda a,b: list(zip(a,b))

        for line in self.processedLines:            
            mc.insert(config.dbName,genData(config.key,line))

            
    def __del__(self):
        self._f.close()

def main():
    dataProcess=IrisDataInput("iris.data")
    dataProcess.process()
    dataProcess.insertToDataBase()

if __name__ == '__main__':
    main()