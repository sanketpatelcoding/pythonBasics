import pandas as pd
import matplotlib.pyplot as plt


# Communication Type Count: Generate a bar plot
# showing the count of each communication type (call, sms, data)


# df = pd.read_csv("phone_data.csv")
# counts = df.groupby('item').size()
# plt.bar(counts.index, counts.values, color=['red', 'green', 'blue'])
# plt.xlabel('Communication Type')
# plt.ylabel('Count')
# plt.title('Count of Each Communication Type')
# plt.show()

# -------------------------------------------------
# Network Usage: Create a pie chart showing the proportion of
# usage by each network
# df = pd.read_csv("phone_data.csv")
# counts = df.groupby('network').size()
#
# plt.pie(counts.values, labels=counts.index, colors=['red', 'green', 'blue', 'yellow', 'pink', 'maroon', 'brown', 'grey', 'teal'])
# plt.title('Proportion of use by network')
# plt.show()
# ------------------------------------------------------------------
# Daily Activity: Plot a line chart showing the number of communications
# per day
# here to_datetime(df['date']).dt.date to grab date without time
df = pd.read_csv("phone_data.csv")
df['date_only'] = pd.to_datetime(df['date']).dt.date
counts = df.groupby('date_only').size()

plt.plot(counts.index, counts.values, color='#2196F3')
plt.xlabel('Date')
plt.ylabel('Number of Communications')
plt.title('Daily Communication Activity')
plt.xticks(rotation=45)
plt.show()