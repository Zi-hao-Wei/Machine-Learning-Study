import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from LeNet import LeNet
#transform 
transform=transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
    
cifar_train = torchvision.datasets.CIFAR10(root='./data',train=True,download=True,transform=transform)
cifar_test = torchvision.datasets.CIFAR10(root='./data',train=False,transform=transform)

print(cifar_train)

trainloader=torch.utils.data.DataLoader(cifar_train,batch_size=32,shuffle=True)
testloader=torch.utils.data.DataLoader(cifar_test,batch_size=32,shuffle=True)

device=torch.device("cuda:0")
net=LeNet().to(device)

import torch.optim as optim
criterion=nn.CrossEntropyLoss()
optimizer=optim.SGD(net.parameters(),lr=0.001,momentum=0.9)

print("START")
for epoch in range(50):
    loss100=0.0
    for i,data in enumerate(trainloader):
        inputs,labels=data
        inputs,labels=inputs.to(device),labels.to(device)
        outputs=net(inputs)
        loss=criterion(outputs,labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss100+=loss.item()
        if i % 100 == 99:
            print('[Epoch %d, Batch %5d] loss: %.3f' %
                  (epoch + 1, i + 1, loss100 / 100))
            loss100 = 0.0

print("Done Training!")

correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        images, labels = images.to(device), labels.to(device)
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))