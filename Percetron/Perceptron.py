import numpy as np
class Perceptron:
    def __init__(self,input_num,activator):
        self.num=input_num; #dimension
        self.acitvator=activator #激活函数
        self.weights=np.zeros(self.num)
        self.bias=0.0
    def printWeight(self):
        print(self.weights)
    def predict(self,vector):
        return self.acitvator(np.dot(self.weights,np.array(vector)) +self.bias)
    def train(self,input_vec,label,iteration,rate):
        for i in range(iteration): #迭代iteration次
            self.onceIteration(input_vec,label,rate)
    def onceIteration(self,input_vec,label,rate):
        for (vec,vec_label) in zip(input_vec,label):
            output=self.predict(vec)
            delta=vec_label-output
            self.weights=self.weights+delta*rate*np.array(vec)
            self.bias+=delta*rate

def f(x):
    return 1 if x > 0 else 0

def get_training_dataset():
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    p = Perceptron(2, f)
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    return p


if __name__ == '__main__':
    # 训练and感知器
    and_perception = train_and_perceptron()
    # 打印训练获得的权重
    and_perception.printWeight()
    # 测试
    print('1 and 1 = %d' % and_perception.predict([1, 1]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))
