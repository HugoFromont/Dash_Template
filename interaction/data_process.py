import pandas as pd

def create_dataset(file):
    df = pd.read_csv("data/{}.csv".format(file), sep = ";")
    return df
