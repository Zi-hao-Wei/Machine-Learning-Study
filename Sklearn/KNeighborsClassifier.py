from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
# print(iris)
iris_X = iris.data
print(len(iris_X))
iris_y = iris.target
print(iris_y)

X_train,X_test,y_train,y_test=train_test_split(iris_X,iris_y,test_size=0.3)

print(y_train)
print(y_test)

knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
params=knn.get_params()
print(params)
score=knn.score(X_test,y_test)
print(score)

print(knn.predict(X_test))
print(y_test)