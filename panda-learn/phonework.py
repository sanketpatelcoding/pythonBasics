import pandas as pd
import numpy as np

def load_datasets(path):
    df = pd.read_csv(path)
    return df


df = load_datasets("phone_data.csv")
print(df.head())
