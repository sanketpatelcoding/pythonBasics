import pandas as pd
import numpy as np

# print the first 5 rows to verify it's loaded correctly.
df = pd.read_csv("heart.csv")
print(df.head())


# Get the shape of the DataFrame (number of rows and columns) and print it.
df = pd.read_csv("heart.csv")
print(df.shape)

# Generating summary statistics
df = pd.read_csv("heart.csv")
print(df.describe())


# Convert the Data to a NumPy array and print the shape of the array
heart_array = np.array(df)
print(heart_array.shape)

# access and print the value in the first row  column
heart_array = np.array(df)
print(f'first row and first column {heart_array[0, 0]}')


# : Slice the NumPy array to get the first 3 rows and the first 4 columns
# (age, sex, cp, trestbps), and print the result
heart_array = np.array(df)
print(heart_array[0:3, 0:4])


# mean age
mean_age = df['age'].mean()
print(f'mean_age is :{mean_age}')

# Using NumPy, the maximum cholesterol level (chol column
heart_array = np.array(df)
max_chol = np.max(heart_array[:, 4])
print(f'max_chol is :{max_chol}')

# Filter the DataFrame to show only rows where the target is 0
#  and print the first 5 such rows.
no_disease = df[df['target'] == 0]
print('=====no deseasas follows---------------')
print(f'{no_disease.head()}')
print('=====---------------')

# the sum of the 'thalach'
# column (maximum heart rates) for all patients, and print it.

sum_thalach = np.sum(heart_array[:, 7])
print(f'sum_thalach is: {sum_thalach}')


# Add a new column to the data called 'age_group'
# where values are 'young' if age < 50, else 'old',
# and print the updated dara 's first 5 rows.
df['age_group'] = np.where(df['age'] < 50, 'young', 'old')
print(f'age_group :\n{df.head()}')

# : Sort the DataFrame by 'chol' in descending order and
# print the top 3
sorted_df = df.sort_values(by='chol', ascending=False)
print(f'sorted_df :\n')
print(sorted_df.head(4))

# getting the minimum and maximum values in the  array
min_val = np.min(heart_array)
max_val = np.max(heart_array)
print(f"minim: {min_val}, maxm: {max_val}")


# entire only seconff
print(f'leaving first get next complete array  :\n')
print(heart_array[0::2, :])











