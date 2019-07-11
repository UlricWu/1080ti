import pandas as pd
import numpy as np
import os
class DGP:
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(self.path)
        df = []
        for name in self.files:
            temp = pd.read_csv(self.path + name)
            temp = np.array(temp)
            df.append(temp)
        data = np.array(df[len(df) - 1])
        for item in range(len(df) - 1):
            data = np.vstack((data, df[item]))
        self.data = data
    def validation(self,*args):
        x =args[0]
        y =args[1]
        np.random.seed(127)
        self.n = x.shape[0]
        perm = np.random.permutation(self.n)
        siz = int(self.n*0.7)
        train= perm[:siz]
        test = perm[siz:]
        self.train_x = x[train,:]
        self.train_y = y[train]
        self.test_x = x[test,:]
        self.test_y = y[test]

if __name__ == "__main__":
    path = input("Enter your Path")
    if len(path) == 0: path = os.getcwd()
    df = DGP(path)
     # it depends on your dataset and your things of interest
    #y= df.data[:,7]
    #x= df.data[:,0:7]
    #x = (x - np.mean(x)) / np.std(x)
    #model.validation(x,y)
    print('Load data successfully')