#  IMPORTS
# --------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

# ---------------------
#  OBJECTIVE 1 – CALL DURATION DISTRIBUTION (Histogram)


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
#  OBJ 2 – Comm type counting (Bar plot)
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
#  Objective 4  daily activities(Linegraph)
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

# functin calling Area
# ===============================
df = load_dataset("phone_data.csv")
# print("\n1. Call Duration Histogram")
# call_duration_histogram(df)
# comm_result = communication_type_count(df)
# pie_result = network_usage_pie(df)
daily_activity_line(df)
# ---------------------------------
