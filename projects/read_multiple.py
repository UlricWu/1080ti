import pandas as pd
import os
if __name__ == '__main__':
    file = [file for file in os.listdir() if '.csv' in file]
    df = []
    for name in file:
        df.append(pd.read_csv(name, header=None))
        # df.append(pd.read_csv(name))
    df = pd.concat(df, ignore_index=True)
    print(df.head())
    print(df.shape)