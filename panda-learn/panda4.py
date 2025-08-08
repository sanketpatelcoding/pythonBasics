import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from todo_data import todo_data
# todo_data coming from py file todo_data

# Create DataFrame from todo_data
todo_dataframe = pd.DataFrame(todo_data)

# print(todo_dataframe)


print("Displaying three columns (id, todo, completed):")
print(todo_dataframe[['id','userId', 'todo', 'completed']])
print(todo_dataframe[['id','userId', 'todo']])
print(todo_dataframe[['id','userId', 'completed']])
# -----------------------------------------
print("Displaying==========")
print(todo_dataframe.info())
print("Displaying==========")

# -----------------------------------------
# DataFrame()
data = {'Name': ['Aman', 'Ankit', 'Vaibhav'],
        'Age': [25, 30, 35]
        }
df = pd.DataFrame(data)
print(df[['Age','Name']])
