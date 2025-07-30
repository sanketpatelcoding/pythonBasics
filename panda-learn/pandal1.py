import pandas as pd
import numpy as np

# array[index]: Access elements at a specific index.

# a=[11,2,3,4,5,6,7,8,9,0]
# b=np.array(a)
# print(b[0])

# array[start:stop:step]: Slice arrays.
# a=[11,2,3,4,5,6,7,8,9,0]
# b=np.array(a)
# c=b[0:5:1]
# # till 5th element
# print(c)

df = pd.read_csv("given.csv")

print(df.head())
# print(df)

# df = df.drop(['Id', 'Species'], axis=1)
# df = df.drop(['Id', 'Species'], axis=1)

# print(df.head())
# print(df.describe())

iris_array = np.array(df)
# # length max
# mxlength=iris_array.max()
# print(mxlength)
# print(iris_array[:,:1].sum())
print(iris_array[0:1,])
print(f'shape {iris_array.shape}')
# print(f'size {iris_array.size}')
print(iris_array[0,])
# # print(iris_array[:5])
#
# sepal_length_mean = iris_array[:, :1].mean()
# print(sepal_length_mean)

