#  IMPORTS
# --------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

# ---------------------
#  OBJE 1 – call duration distribution(Histogram)


# def call_duration_histogram(df):
#     calls = df[df['item'] == 'call']
#     plt.figure(figsize=(8, 5))
#     plt.hist(calls['duration'], bins=30, color='skyblue', edgecolor='black')
#     plt.title('Call duration all')
#     plt.xlabel('duration seconds')
#     plt.ylabel('Number of Calls')
#     # plt.grid(True, alpha=0.3)
#     # plt.tight_layout()
#     plt.show()
#     return {'status': 'histogram_shown'}
# -------------------------------
#  OBJ 2 Comm type counting (Bar plot)
# def communication_type_count(df):
#     counts = df['item'].value_counts()
#     plt.figure(figsize=(6, 4))
#     bars = plt.bar(counts.index, counts.values,
#                    color=['red', 'green', 'pink'])
#     plt.title('cnt  each communication type')
#     plt.xlabel('type')
#     plt.ylabel('count')
    # bellow taken from net
    # for bar in bars:
    #     h = bar.get_height()
    #     plt.text(bar.get_x() + bar.get_width() / 2, h + 0.01 * h,
    #              f'{h}', ha='center', va='bottom')
    # plt.tight_layout()
    # plt.show()
    # return {'avg_duration': avg.to_dict()}
#     ----------------------------------
# def network_usage_pie(df):
#     net_counts = df['network'].value_counts()
#     plt.figure(figsize=(6, 6))
#     wedges, texts, autotexts = plt.pie(
#         net_counts.values,
#         labels=net_counts.index,
#          autopct='%1.1f%%',
#         startangle=90,
#         colors=plt.cm.Set3.colors
#     )
#     plt.title('usage by network')
#     plt.axis('equal')          # circle banava mate
#     plt.tight_layout()
#     plt.show()

# ----------------------------------------
#  Objective 4 daily activities(Linegraph)
# --------------------------------------------------------------
def daily_activity_line(df):
    # convert date (mixeing)to simple datetime(from net)
    df['date_only'] = pd.to_datetime(df['date'], dayfirst=True).dt.date
    daily = df.groupby('date_only').size()
    plt.figure(figsize=(10, 4))
    plt.plot(daily.index, daily.values, marker='o', linestyle='-', color='teal')
    plt.title('Number of Communications per Day')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    return {'daily_counts': daily.to_dict()}


#  obj 5 Duration by Network: Create a bar plot showing average duration by network
def plot_avg_duration_by_network(df):
    calls = df[df['item'] == 'call']
    avg = calls.groupby('network')['duration'].mean()
    plt.figure(figsize=(10, 5))
    plt.bar(avg.index, avg.values, color='green', edgecolor='black')
    plt.title('average call duration by network')
    plt.xlabel('network')
    plt.ylabel('average duration')
    plt.show()

    return {'plot':'average duration by network shown'}

# ----------------------
# sms count by network: generate a bar plot showing sms count for each mobile network
# columns: network, item, network_type
def plot_sms_by_mobile_network(df):
    mobile_sms = df[(df['item'] == 'sms') & (df['network_type'] == 'mobile')]
    sms_count = mobile_sms['network'].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(sms_count.index, sms_count.values, color='orange', edgecolor='black')
    plt.title('sms count by mobile netwrk')
    plt.xlabel('netwrk')
    plt.ylabel('numberof sms')
    plt.show()

    return {'plot': 'sms count by mobile network shown'}

# -------------


# call type distribution: create a pie chart showing the proportion of call durations (short, medium, long)
# columns: duration, item
def plot_call_type_distribution(df):
    calls = df[df['item'] == 'call'].copy()
    # short <1min (60s), medium ke liye 5min, long >5min
    conditions = [
        calls['duration'] < 60,
        (calls['duration'] >= 60) & (calls['duration'] <= 300),
        calls['duration'] > 300
    ]
    choices = ['short', 'medium', 'long']
    calls['type'] = pd.Series(pd.cut(calls['duration'], bins=[0, 60, 300, float('inf')], labels=choices))

    counts = calls['type'].value_counts()

    plt.figure(figsize=(3, 3))
    plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', colors=['lightgreen', 'skyblue', 'pink'])
    plt.title('call type distribution')
    plt.show()

# -----------------
# monthly activity: plot a bar chart showing total communications per month
# columns: month
def plot_monthly_communications(df):
    monthly = df.groupby('month').size()

    plt.figure(figsize=(9, 5))
    plt.bar(monthly.index, monthly.values, color='purple', edgecolor='black')
    plt.title('total communications per month')
    plt.xlabel('month')
    plt.ylabel('number of communications')
    plt.show()
# ================================
# network type usage: generate a count plot showing usage by network type (mobile, data, voicemail)
# columns: network_type
def plot_network_type_usage(df):
    plt.figure(figsize=(5,5))
    sns.countplot(data=df, x='network_type')
    plt.title('usage by network type')
    plt.xlabel('network type')
    plt.ylabel('counts')
    plt.show()
    return {'plot': 'network type count plot shown'}
# ================================
# duration vs date: create a scatter plot of duration against date (with proper date formatting)
# columns: date, duration
def plot_duration_vs_date(df):
    # fix mixed date formats(aa karya vina avatu nathi)
    df['date_clean'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

    plt.figure(figsize=(10, 6))
    plt.scatter(df['date_clean'], df['duration'], alpha=1, color='red')
    plt.title('duration vs date')
    plt.xlabel('date')
    plt.ylabel('duration (seconds)')
    plt.show()
# ===========================================
# network performance:generate a violin plot showing call duration distribution by network
# columns: network, duration, item
def plot_call_duration_violin(df):
    calls = df[df['item'] == 'call']

    plt.figure(figsize=(10, 6))
    sns.violinplot(data=calls, x='network', y='duration')
    plt.title('call duration distribution by network')
    plt.xlabel('network')
    plt.ylabel('duration (seconds)')
    plt.show()
#     -----------------------------------------------------
# communication heatmap: create a heatmap showing communication patterns by date and network
# columns: date, network
def plot_communication_heatmap(df):
    df['date_only'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True).dt.date
    heatmap_data = df.groupby(['date_only', 'network']).size().unstack(fill_value=0)
    # uper nu net ma thi
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlOrRd', linewidths=.5)
    plt.title('communication heatmap')
    plt.xlabel('network')
    plt.ylabel('date')
    plt.tight_layout()
    plt.show()
#     --------------------------------------------
# cumulative duration: plot a line chart showing cumulative call duration over time
# columns: date, duration, item
def plot_cumulative_call_duration(df):
    df['date_time'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)
    calls = df[df['item'] == 'call'][['date_time', 'duration']].sort_values('date_time')
    calls['cumulative'] = calls['duration'].cumsum()
    plt.figure(figsize=(12, 6))
    plt.plot(calls['date_time'], calls['cumulative'], color='darkblue', linewidth=2)
    plt.title('cumulative call duratin')
    plt.xlabel('date')
    plt.ylabel('cumulative duration in secs.')
    plt.show()


# functin calling Area
# ===============================
df = load_dataset("phone_data.csv")
# print("\n1. Call Duration Histogram")
# call_duration_histogram(df)
# comm_result = communication_type_count(df)
# pie_result = network_usage_pie(df)
# daily_activity_line(df)
# plot_avg_duration_by_network(df)
# plot_sms_by_mobile_network(df)
# plot_call_type_distribution(df)
# plot_monthly_communications(df)
# plot_network_type_usage(df)
# plot_duration_vs_date(df)
# plot_call_duration_violin(df)
# plot_communication_heatmap(df)
# plot_cumulative_call_duration(df)
# ---------------------------------
