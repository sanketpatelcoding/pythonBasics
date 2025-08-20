import pandas as pd
import numpy as np


# def printheadtails(headcount, tailcount, df):
#     print(f"first {headcount} rows df")
#     print(df.head(headcount))
#     print(f"last {tailcount} row")
#     print(df.tail(tailcount))

df = pd.read_csv("phone_data.csv")
# head_rows = int(input("Enter number for head"))
# tail_rows = int(input("Enter number for tail"))
# printheadtails(head_rows, tail_rows, df)

print('---------------------------------------------')
# ----------------------------------------------------------
# print("\ndataset info")
# print(df.info())
print('---------------------------------------------')
# print("\ndataset dscription")
# print(df.describe())
print('---------------------------------------------')
# ----------------------unique------------------------------
print(df.head(5))
# print(df.nunique())
# print('-------------- total number of calls-------')
# totalcalls = len(df[df['item'] == 'call'])
# print(f"\nTotal number of calls: {totalcalls}")
# print('-------------- Distinct values in the item column (self)-------------------------------')
# print("unoque values in the item column")
# print(df['item'].unique())
# print('-------------- total number of data incident-')
# totaldata=len(df[df['item']=='data'])
# print(f'{totaldata}  instances used in df')
# print('-------------- total number of sms-')
# totalsmscount=len(df[df['item']=='sms'])
# print(f' is totalsmscount is {totalsmscount}\n')

# Calculate the total duration of all calls combined.
# durationtotal = df[df['item'] == 'call']['duration'].sum()
# print(f' is durationtotal is {durationtotal}')
# # Calculate the total duration of all calls combined.USEING NUMPY
# npdurationtotal=   np.sum(df[df['item'] == 'call']['duration'])
# print(f'USEING NUMPY is npdurationtotal is {npdurationtotal}')
#


# Find the most frequently used mobile network
# without function
# print("\n  unique net")
# print(df['network'].unique())
# print("\nNumber of unique netwrk")
# print(len(df['network'].unique()))
# print("\nFrequency of each netwrk")
# print(df.groupby('network').size())
# with function using firsst groupby
# to group all netwrks and then apply size to find count of each
# idxmax find  index of the maximum value in a panda
# ---------------------------
# def most_frequent_network(df):
#     print(df['network'].unique())
#     freq = df.groupby('network').size()
#     print(freq)
#     print(freq.idxmax())
#
#
# most_frequent_network(df)

# ---------------------
# Calculate the average duration of calls.
print(df['item'].unique())
print(df[df['item'] == 'call']['duration'])
print(df.groupby('duration').size())
print("\nAverage call duration", df[df['item'] == 'call']['duration'].mean())





