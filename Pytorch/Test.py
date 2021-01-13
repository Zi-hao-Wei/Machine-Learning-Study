from __future__ import print_function
import torch
x=torch.empty(5,3)
print(x)

X=torch.rand(5,3)
print(X)

x=torch.zeros(5,3,dtype=torch.long)
print(x)

x=torch.tensor([5.5,3])
print(x)

x=torch.randn(1)
print(x.item())
