import numpy
import matplotlib.pyplot as plt
class ConfusionMatrix:
    def __init__(self,confusion_matrix,labels):
        self.matrix=confusion_matrix
        self.labels=labels
    def plot(self,title='Confusion Matrix',color=plt.cm.Blues):
        plt.imshow(self.matrix,cmap=color)
        indices = range(len(self.matrix))
        plt.xticks(indices, self.labels)
        plt.yticks(indices, self.labels)
        plt.colorbar()

        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title(title)

        for first_index in range(len(self.matrix)):    #第几行
            for second_index in range(len(self.matrix[first_index])):    #第几列
                plt.text(first_index, second_index, self.matrix[first_index][second_index])
        plt.show()

def main():
    matrix=[[20,0,0],[ 0,13,2],[ 0,0,10]]
    labels=["Iris-setosa","Iris-versicolor","Iris-virginica"]
    cm=ConfusionMatrix(matrix,labels)
    cm.plot()

if __name__ == '__main__':
    main()