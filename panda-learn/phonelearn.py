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

# def information(df):
#     return df.info()


print('---------------------------------------------')
# print("\ndataset dscription")
# print(df.describe())
print('---------------------------------------------')
# ----------------------unique------------------------------
print(df.head(5))
# print(df.nunique())
# print('-------------- total number of calls-------')
# def total_calls(df):
#     return df[df['item'] == 'call'].shape[0]
#
# total = total_calls(df)
# print('Total numbers of calls', total)
# print('****************************************')
#
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
# print(df['item'].unique())
# print(df[df['item'] == 'call']['duration'])
# print(df.groupby('duration').size())
# print("\nAverage call duration", df[df['item'] == 'call']['duration'].mean())


# -------------------------------------------

# Identify the month with the highest number of communications.
# def higest_comm_mnth(df):
#     print(df['month'].unique())
# print(df['month'].unique())(not sure ask)
#     x=df.groupby('month').size()
#     print(x)
#     print(f'hihghest comm mnth {x.idxmax()}')
# higest_comm_mnth(df)

# ============================================
# Calculate the percentage of data usage vs calls vs SMS.(wrong che)

# length = len(df)
# print(length)
# counts = df.groupby('item').size()
# print(f'{counts}')
# percentages = ((counts / length) * 100)
# print(percentages)
# =======================

# print('shape',df.shape)
# print(f'nultiplication :{df.shape[0]*df.shape[1]}')
# print('size',df.size)
# print('len',len(df))
# call_length=len(df[df['item']=='call'])
# sms_length=len(df[df['item']=='sms'])
# data_length=len(df[df['item']=='data'])
#
# print('call length',call_length)
# print('sms length',sms_length)
# print('data length',data_length)

#-----------------------------------------------------
# Find the network with the highest average call duration.# sort_values -> ascending=[False, True]
# def highest_avg_call_duration(df):
#     avg_durations = df[df['item'] == 'call'].groupby('network')['duration'].mean()
#     print("\nAverage call duration per network in second:")
#     print(avg_durations)
#     print('\n')
#     print("Network with highest average call duration:", avg_durations.sort_values(ascending=False).index[0])
#
# highest_avg_call_duration(df)

#---------------------------------------------------------

# Count how many communications occurred on each date.
# commcountsperday = df.groupby('date').size()
# print("Number of communications  date wise")
# print(commcountsperday)

# --------------------------------------------------------------

# Calculate the total duration of communications for each day.(from net)
# definition " to_datetime" is a function primarily found in the Pandas library in Python,
# used for converting various date and time representations into standardized
# Pandas datetime objects.
#
# df['date_only'] = pd.to_datetime(df['date']).dt.date
# total_durations = df.groupby('date_only')['duration'].sum()
# print("Total duration of communication/ day in second")
# print(total_durations)

#
# Create a pivot table showing the count
# of each item type (call, sms, data)
# per network. aggfunc is important
# pivot = pd.pivot_table(df, index='network', columns='item', aggfunc='size', fill_value=0)
# print("\nPivot table count of each item type per network:")
# print(pivot)
# -----------------------------------------------------------------------
# Create a new DataFrame that shows the
# count and total duration of each item type per month. agg is imp
# newdf = df.groupby(['month', 'item']).agg({'item': 'size', 'duration': 'sum'}).rename(columns={'item': 'count'})
# print("\ncount and total duration of each item prer month:")
# print(newdf)

# Calculate the cumulative sum of call durations over time.

print(list(df.columns))
# --------------------------------
print('================')
# Create a summary DataFrame that shows for each network: total calls, total SMS, total duration, and average duration.

