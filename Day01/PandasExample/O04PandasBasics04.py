
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