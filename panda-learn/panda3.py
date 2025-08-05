import pandas as pd
import numpy as np


df = pd.read_csv("heart.csv")
# print(df.head())


# Data Exploration:

# print(df.head(2))
# print(df.tail(2))
# print(df.info())
# df['age'] = df['age'].astype(np.int16)
# print(df.describe())
# print(df.describe(include='all'))

# print(df['age'].head())

# print(df[['age', 'chol']].head())

# print(df.iloc[[1, 2], [1, 2, 3]])


# print(df.loc[[1, 2, 3], ['age']])
#
# print(df.loc[1:25, ["chol", 'age']])

# print(df.query("(age > 50) and (sex == 1)"))
# print(df.query("(age < 50) and (chol >180)"))
# young_patients=np.array(df.query("(age < 50) and (chol >180)"))
# print(young_patients)
# print(young_patients.shape)
# print(young_patients.size)
# wrong one bellow
# print(df.loc[1:30, ["sex", 'col']])
# print(f'oth row\n-{df.loc[0]}')
# print(f'---------correlation------\n {df.corr()}')