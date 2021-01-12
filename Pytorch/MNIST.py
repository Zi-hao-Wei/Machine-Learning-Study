import torch
import torchvision
from torchvision import datsets
from torchvision import transforms
from torch.autograd import Variable

data_train=datasets.MNIST(root='./data/',transform=transform,train=True,download=True)
data=test=datasets.MNIST(root='./data/',transform=transform,train=False)

data_loader_train=torch.utils.data.DataLoader(dataset=data_train,batch_size=64,shuffle=True)
data_loader_test=torch.utils.data.DataLoader(dataset=data_test,batch_size=64,shuffle=True)

