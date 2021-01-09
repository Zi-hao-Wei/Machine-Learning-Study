import sklearn
from sklearn.datasets.samples_generator import make_classification
from sklearn.datasets import make_blobs
from matplotlib import pyplot
#Classification Problem
X,y = make_classification(n_samples=6,n_features=5,n_informative=2,n_redundant=2,n_classes=2,n_clusters_per_class=2,scale=1.0,random_state=20)
print(X)
print(y)
print(zip(X,y))
#Claster Problem
data,label=sklearn.datasets.make_blobs(n_samples=100, n_features=2, centers=3,cluster_std=1.0, center_box=(-10.0, 10.0), shuffle=True, random_state=None)
print(data)
print(label)
pyplot.scatter(data[:,0],data[:,1],c=label)
pyplot.show()