import numpy as np
import pandas as pd

data = {
    'name': ['Bill', 'Tom', 'Tim', 'John', 'Alex', 'Venessa', 'Kate'],
    'score': [90, 80, 85, 75, 95, 60, 65],
    'sports': ['wrestling', 'football', 'skiing', 'swimming', 'tennis', 'karate', 'surfing'],
    'sex': ['m', 'm', 'm', 'm', 'm', 'f', 'f']
}

df = pd.DataFrame(data)
print(f"Data Frame :\n{df}")

print("-" * 60)
df = pd.DataFrame(data, columns=['name', 'sports', 'sex', 'score'])
print(f"DataFrame :\n{df}")

print("-" * 60)
print(df.head())

print("-" * 60)
print(df.tail())

print("-" * 60)
df = pd.DataFrame(data, columns=['name', 'sports', 'sex', 'score'],
                  index=['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
print(f"Data Frame :\n{df}")

print("-" * 60)
print(df['sports'])

print("-" * 60)
my_columns = ['name', 'sports']

print(df[my_columns])

print("-" * 60)
print(df.loc[['one']])
print(df.loc[['five']])
print(df.loc[['seven']])

print("-" * 60)
print(df.iloc[0])

print("-" * 60)
print(df.iloc[1, 1])

print("-" * 60)
print(df.iloc[2, 3])

print("-" * 60)
print(df.iloc[0:2, 0:2])

print("-" * 60)
df = pd.DataFrame(data, columns=['name', 'sports', 'sex', 'score'], index = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'])

values = [18, 19, 20, 18, 17, 17, 18]
df['age'] = values

print(f"DataFrame :\n{df}")

print("-" * 60)
# filter the data

df['pass'] = df.score >= 70

print(df)

print("-" * 60)
del df['pass']

print(df)

print("-" * 60)
scores = {'Math': {'A': 85, 'B': 90, 'C': 95}, 'Physics': {'A': 90, 'B': 80, 'C': 75}}

scrs_df = pd.DataFrame(scores)
print(f"Scores :\n{scrs_df}")

print("-" * 60)
print(scrs_df.T)            # T - transpose the table

print("-" * 60)
scrs_df.index.name = "name"
scrs_df.columns.name = 'subjects'

print(scrs_df)

print("-" * 60)
data  = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=['Blr', 'Che', 'Hyd', 'Mum'],
    columns=['one', 'two', 'three', 'four']
)

print(f"data :\n{data}")
