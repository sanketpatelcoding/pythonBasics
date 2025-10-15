import pandas as pd

df = pd.read_csv('phone_data.csv')
df['net_date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df['hour'] = df['net_date'].dt.hour

active = df.groupby('hour').size().sort_values(ascending=False)
active_hour = active.idxmax()
total_hour = active_hour.max()

print(active)
print(active_hour)
print(total_hour)
