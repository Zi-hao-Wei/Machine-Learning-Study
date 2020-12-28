class DBconfig:
    db_config = {"host": "localhost",
              "port": 3306,
              "user": "root",
              "pwd": "123456",
              "db": "test"}
    dbName="nursery"
    dbTrainName="nurseryTrain"
    nursery_config=[
        ("ID","INT","NOT NULL","AUTO_INCREMENT","PRIMARY KEY"),
        ("parents","VARCHAR(255)"),
        ("has_nurs","VARCHAR(255)"),
        ("form","VARCHAR(255)"),
        ("children","VARCHAR(255)"),
        ("housing","VARCHAR(255)"),
        ("finance","VARCHAR(255)"),
        ("social","VARCHAR(255)"),
        ("health","VARCHAR(255)"),
        ("result","VARCHAR(255)")
    ]

    key=["parents","has_nurs","form","children","housing","finance","social","health","result"]
    vector=["parents","has_nurs","form","children","housing","finance","social","health"]
    label=["result"]
    
    vectorString="parents,has_nurs,form,children,housing,finance,social,health,result"