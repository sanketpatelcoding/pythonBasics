import pandas as pd
df = pd.read_csv("heart.csv")
# ---------yet to be done
# sort_values()
# reset_index()
# set_index
# notna()
# isnul
# filna
# groupby()
# transform
# filter
print("Original DataFrame:\n", df.head())
print('======================')
# 1. Accessing a single value using .at
age_value = df.at[0, 'age']
print("The age at index 0 is:", age_value)
print('======================')
#  Accessing a single value using .iat
age_value_iat = df.iat[1, 0]
print("The age at index 0 using .iat is:", age_value_iat)
print('======================')
# Checking if values in 'target' column are in [1, 0] using .isin()
isin_target = df['target'].isin([1, 0])
print("Rows where 'target' is in [1, 0]:\n", df[isin_target])
print('======================')
# Finding duplicate rows using .duplicated()
duplicates = df.duplicated()
print("Duplicate rows:\n", df[duplicates])

print('======================')
# Dropping duplicate rows
cleaned_df = df.drop_duplicates()
print("after dropping duplicates:\n", cleaned_df.head())
print('======================')
# Adding a new column 'age_squared' using assign()
df_with_age_dbl = df.assign(age_dbl=df['age'] * 2)
print("DataFrame with extra column:\n", df_with_age_dbl.head(2))
print('======================')
# Renaming 'cholesterol' column to 'cholesterol_level'
renamed_df = df.rename(columns={'cholesterol': 'cholesterol_level'})
print("DataFrame with renamed column:\n", renamed_df.head(2))
print('======================')