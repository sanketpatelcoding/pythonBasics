
import pandas as pd
import numpy as np


df = pd.read_csv("heart.csv")

#
# Merging and Concatenating:
# pd.concat(): Concatenate DataFrames along a particular axis.
# pd.merge(): Merge DataFrames based on a key.
#
#
#
# Plotting and Visualization:
# df.plot(): Plot DataFrame.
# df.hist(), df.plot.hist(): Plot histograms.
# df.plot.scatter(): Scatter plot.

# Creating another DataFrame for demonstration
df2 = pd.DataFrame({
    'age': [25, 30],
    'cholesterol': [200, 250],
    'target': [1, 0]
})

# Creating another DataFrame for demonstration
df4 = pd.DataFrame({
    'age': [45, 34],
    'cholesterol': [240, 260],
    'target': [1, 0]
})

# Concatenating df and df2 along the rows (axis=0)
concatenated_df = pd.concat([df4, df2], axis=0)
print("Concatenated DataFrame:\n", concatenated_df)

# Creating another DataFrame to merge
df3 = pd.DataFrame({
    'age': [25, 30, 35],
    'target': [1, 0, 1],
    'gender': ['M', 'F', 'M']
})

# Merging df4 and df3 on the 'target' column
merged_df = pd.merge(df4, df3, on='target', how='inner')
print("Merged DataFrame:\n", merged_df)

# 3
# import matplotlib.pyplot as plt(not working)
#
# # Simple line plot of 'age' vs 'target'
# df.plot(x='age', y='target', kind='line')
# plt.title("Age vs Target")
# plt.xlabel("Age")
# plt.ylabel("Target")
# plt.show()


