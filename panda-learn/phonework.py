import pandas as pd
import numpy as np

def load_datasets(path):
    # df = pd.read_csv(path)
    # return df
    try:
        if path.lower().endswith(('.xlsx', 'xls')):
            df = pd.read_excel(path)

        else:
            df = pd.read_csv(path, dtype=str)

    except Exception as e:
        raise RuntimeError(e)

    df.columns = [col.strip() for col in df.columns]

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce', infer_datetime_format=True)
    else:
        raise KeyError('date column not found')

    if 'duration' in df.columns:
        df['duration'] = pd.to_numeric(df['duration'].str.replace(',', '.', regex=False), errors='coerce')
    else:
        df['duration'] = np.nan

    for col in ['item', 'network', 'month', 'network_type']:
        if col in df.columns:
            df[col] = df[col].fillna('unknown').astype(str)
        else:
            if col == 'month' and 'date' in df.columns:
                df['month'] = df['date'].dt.to_period('M').astype(str).fillna('unknown')
            else:
                df[col] = 'unknown'

    return df


def basic_inspection(df):
    inspection = {
        'head': df.head(),
        'tail': df.tail(),
        'info': df.info(),
        'dtypes': df.dtypes,
        'non_null_counts': df.count(),
        'describe': df.describe()
    }

    return inspection

df = load_datasets("phone_data.csv")
# print(df.head())
inspection = basic_inspection(df)
print(inspection['head'])
print(inspection['info'])
print(inspection['describe'])
