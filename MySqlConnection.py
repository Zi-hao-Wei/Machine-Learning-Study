import pymysql

class MysqlConnection:
    # A class created for mysql connection
    def __init__(self,config):
    # INIT
        self._db = pymysql.connect(host=config['host'],
                                      port=config['port'],
                                      user=config['user'],
                                      passwd=config['pwd'],
                                      db=config['db'],
                                      charset='utf8')
        self._cursor = self._db.cursor()
    
    def version(self):
        self._cursor.execute("SELECT VERSION()")
        data = self._cursor.fetchone()
        print ("Database version : %s " % data)

    def create(self,name,parameters):
        self._cursor.execute("DROP TABLE IF EXISTS "+ name)
        create_sql="""CREATE TABLE """ + name + " ("
        for parameter in parameters:
            one_parameter_sql=""
            for key in parameter:
                 one_parameter_sql = one_parameter_sql + key + " "
            create_sql = create_sql + one_parameter_sql + ","
        create_sql = create_sql.rstrip()
        create_sql = create_sql.rstrip(",")
        create_sql=create_sql  + " )"
        self.sql_execute(create_sql)

    def insert(self,table,values,time=1):
        insert_sql="INSERT INTO " + table
        keys="("
        value="("
        for it in values:
            keys=keys+it[0]+","
            
            if(isinstance(it[1],str)):
               value=value+"\'"+it[1]+"\'"+"," 
            else:
                value=value+str(it[1])+","

        keys=keys.rstrip(",")+")"
        value=value.rstrip(",")+")"
        insert_sql = insert_sql + " "+ keys + " VALUES " + value 

        for i in range(0,time):
            self.sql_execute(insert_sql)
    
    def select(self,table,columns=[],where=""):
        column_str=""
        if (columns==[]):
            column_str="*"
        else:
            for column in columns:
                column_str=column_str+column+","
            column_str=column_str[:-1]

        if (where==""):
            select_sql="SELECT " + column_str + " FROM " + table
        else:
            select_sql="SELECT " + column_str + " FROM " + table + "" + " WHERE " + where
        
        try:
            self._cursor.execute(select_sql)
            self._db.commit()
            results = self._cursor.fetchall()
            return results
        except:
            self._db.rollback()
            return ()

    def delete(self,table,where):
        delete_sql= "DELETE FROM " + table + " WHERE " + where
        self.sql_execute(delete_sql)

    def sql_execute(self,sql):
        try:
            self._cursor.execute(sql)
            self._db.commit()
        except:
            self._db.rollback()


    def __del__(self):
        self._cursor.close()
        self._db.close()

def main():
    config = {"host": "localhost",
              "port": 3306,
              "user": "root",
              "pwd": "123456",
              "db": "test"}

    mc = MysqlConnection(config)
    db = "IRIS"
    iris_config=[
        ("ID","INT","NOT NULL","AUTO_INCREMENT","PRIMARY KEY"),
        ("CalyxLength","FLOAT"),
        ("CalyxWidth","FLOAT"),
        ("FLowerLength","FLOAT"),
        ("FlowerWidth","FLOAT"),
        ("Type","VARCHAR(255)")
    ]
    mc.version()
    mc.create(db,iris_config)

    key = ["CalyxLength","CalyxWidth","FLowerLength", "FlowerWidth","Type"]
    data1 = [5.1,3.5,1.4,0.2,"Iris-setosa"]
    data2 = [5.1,3.5,1.4,0.2,"Iris-ttl"]
      
    genData = lambda a,b: list(zip(a,b))


    mc.insert(db,genData(key,data2),2)    
    mc.insert(db,genData(key,data1),3)

    columns_needed=["CalyxLength","CalyxWidth"]
    type_needed="type = 'Iris-ttl'"
    type_notneeded = "type = 'Iris-setosa'"
    results=mc.select(db,columns_needed,type_needed)
    print(results)
    mc.delete(db,type_notneeded)

if __name__ == '__main__':
    main()