class DBconfig:
    db_config = {"host": "localhost",
              "port": 3306,
              "user": "root",
              "pwd": "123456",
              "db": "test"}

    dbName = "IRIS"
    
    iris_config=[
        ("ID","INT","NOT NULL","AUTO_INCREMENT","PRIMARY KEY"),
        ("CalyxLength","FLOAT"),
        ("CalyxWidth","FLOAT"),
        ("FLowerLength","FLOAT"),
        ("FlowerWidth","FLOAT"),
        ("Type","VARCHAR(255)")
    ]

    key = ["CalyxLength","CalyxWidth","FLowerLength", "FlowerWidth","Type"]
    vector=["CalyxLength","CalyxWidth","FLowerLength", "FlowerWidth"]
    label=["Type"]