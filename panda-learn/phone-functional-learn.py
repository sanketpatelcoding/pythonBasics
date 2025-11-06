import pandas as pd
import numpy as np


# loadnig csv from path
# index,date,duration,item,month,network,network_type
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


#  header 5
def show_head(df, n=5):
    return {'head': df.head(n)}


# Return data types and non-null counts
def dataset_info(df):
    return {
        # 'dtypes': df.dtypes,
        'non_null_counts': df.count()
    }


#   summary stats for numerical column
def numerical_summary(df):
    return {'describe': df.describe()}
# count of unique values per column
def unique_value_counts(df):
    return {'unique_counts': df.nunique()}

# # index,date,duration,item,month,network,network_type
#  total calls and total call duration
def call_analysis(df):
    calls = df[df['item'] == 'call']
    return {
        # 'total_calls': len(df),
        'total_calls': int(len(calls)),
        'total_call_duration': float(calls['duration'].sum())
    }

#  total number of SMS
# index,date,duration,item,month,network,network_type
def sms_count(df):
    sms = df[df['item'] == 'sms']
    return {'total_sms': int(len(sms))}

#  most frequently used mobile network
# index,date,duration,item,month,network,network_type
def most_frequent_network(df):
    mobile = df[df['network_type'] == 'mobile']
    network_counts = mobile['network'].value_counts()
    most_used = network_counts.idxmax()
    count = network_counts.max()
    return {
        'most_frequent_network': str(most_used),
        'count': int(count)
    }

#  Return average duration of calls
# index,date,duration,item,month,network,network_type
def average_call_duration(df):
    calls = df[df['item'] == 'call']
    avg = calls['duration'].mean()
    return {'average_call_duration': round(float(avg), 2)}
# =================================================================
# index,date,duration,item,month,network,network_type
# identify the month with the highest number of communications
def busiest_month(df):
    month_counts = df.groupby('month').size()
    busiest = month_counts.idxmax()
    count = month_counts.max()
    return {
        'busiest_month': str(busiest),
        'total_communications': int(count)
    }
# index,date,duration,item,month,network,network_type
# group the data by 'network' and calculate the total duration for each network
def total_duration_by_network(df):
    duration = df.groupby('network')['duration'].sum()
    return {'total_duration_per_network': duration.to_dict()}
# index,date,duration,item,month,network,network_type
# calculate the percentage of data usage vs calls vs SMS
def usage_percentage(df):
    total = len(df)
    counts = df.groupby('item').size()
    percentages = (counts / total * 100).round(2)
    return {
        'call_percentage': float(percentages.get('call', 0)),
        'sms_percentage': float(percentages.get('sms', 0)),
        'data_percentage': float(percentages.get('data', 0))
    }

# # -----BAKI CHe-----------------------------
# index,date,duration,item,month,network,network_type
# create a new column 'call_type' that categorizes calls as 'short' (<1 min), 'medium' (1-5 min), or 'long' (>5 min)
# def add_call_type_column(df):
# -----BAKI CHe-----------------------------


# index,date,duration,item,month,network,network_type
# calculate the average call duration for each network provider
def avg_call_duration_by_network(df):
    calls = df[df['item'] == 'call']
    avg = calls.groupby('network')['duration'].mean().round(2)
    return {'avg_call_duration_per_network': avg.to_dict()}
# index,date,duration,item,month,network,network_type
# find the network with the highest average call duration
def network_with_highest_avg_call_duration(df):
    calls = df[df['item'] == 'call']
    avg = calls.groupby('network')['duration'].mean()
    best_network = avg.idxmax()
    best_avg = round(avg.max(), 2)
    return {
        'network': str(best_network),
        'highest_avg_duration': float(best_avg)
    }
# index,date,duration,item,month,network,network_type
# count how many communications occurred on each date
def communications_per_date(df):
    df['date_only'] = pd.to_datetime(df['date']).dt.date
    counts = df.groupby('date_only').size()
    return {'communications_per_date': counts.to_dict()}
# ----------segment3---------



# --------------------------------------------------------
# function calls down
# ---------------------------------------------------------
df = load_dataset("phone_data.csv")
# print(show_head(df)['head'])
# print(dataset_info(df)['dtypes'])
# print(numerical_summary(df)['describe'])
# print(unique_value_counts(df)['unique_counts'])
# print(call_analysis(df))
# print(sms_count(df))
# print(most_frequent_network(df))
# print(average_call_duration(df))
# ====segment2
# print(busiest_month(df))
# print(total_duration_by_network(df))
# print(usage_percentage(df))
# print(avg_call_duration_by_network(df))
# print(network_with_highest_avg_call_duration(df))
# print(communications_per_date(df))
# ------segment3=========



