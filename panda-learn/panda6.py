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
# age_value = df.at[0, 'age']
# print("The age at index 0 is:", age_value)
print('======================')
#  Accessing a single value using .iat
# age_value_iat = df.iat[1, 0]
# print("The age at index 0 using .iat is:", age_value_iat)
print('======================')
# Checking if values in 'target' column are in [1, 0] using .isin()
# isin_target = df['target'].isin([1, 0])
# print("Rows where 'target' is in [1, 0]:\n", df[isin_target])
print('======================')
# Finding duplicate rows using .duplicated()
# duplicates = df.duplicated()
# print("Duplicate rows:\n", df[duplicates])

print('======================')
# Dropping duplicate rows
# cleaned_df = df.drop_duplicates()
# print("after dropping duplicates:\n", cleaned_df.head())
print('======================')
# Adding a new column 'age_squared' using assign()
# df_with_age_dbl = df.assign(age_dbl=df['age'] * 2)
# print("DataFrame with extra column:\n", df_with_age_dbl.head(2))
# print('======================')
# # Renaming 'cholesterol' column to 'cholesterol_level'
# renamed_df = df.rename(columns={'cholesterol': 'cholesterol_level'})
# print("DataFrame with renamed column:\n", renamed_df.head(2))
print('======================')
#
# newdf = df.isnull()
#
# print(newdf)

print('======================')
# Rename columns
df = df.rename(columns={
    'cp': 'chestpaintype',
    'trestbps': 'restingbp',
    'thal': 'thalassemia'
})
print("\nAfter renaming columns:")
print(df)
# print(df[['age', 'sex', 'chestpaintype', 'restingbp', 'chol', 'thalassemia']].head())
print('======================')
# Sort by age chol  truefalse (ascending)  (descending)
# df_sorted = df.sort_values(by=['age', 'chol'], ascending=[True, False])
# print("\nAfter sort age  chol:")
# print(df_sorted[['age', 'sex', 'chestpaintype', 'restingbp', 'chol']].head())
print('======================')
# notna for hecking for non-missing values
# df_notna = df.notna()
# print("\nNon-missing values notna:")
# print(df_notna)
# print(df_notna[['age', 'sex', 'chestpaintype', 'restingbp', 'chol', 'oldpeak']].head())
print('======================')

# isnull is Checking for missing values
# df_isnull = df.isnull()
# print("\nmissing values isnull")
# print(df_isnull[['age', 'sex', 'chestpaintype', 'restingbp', 'chol', 'oldpeak']].head())
print('======================')
# # Fill missing values
# chol_mean = df['chol'].mean()
# df_filled = df.fillna({'chol': chol_mean, 'oldpeak': 0})
# print("\nAfter filled missing place:")
# print(df_filled[['age', 'sex', 'chestpaintype', 'restingbp', 'chol', 'oldpeak']].head())
print('======================')