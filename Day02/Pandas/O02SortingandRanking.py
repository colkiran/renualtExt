
import numpy as np
import pandas as pd

s = pd.Series(range(5), index = ['e', 'd', 'a', 'b', 'c'])

print(f"Series :\n{s}")

print("-" * 60)
# sort the data by index
print(s.sort_index())

print("-" * 60)
df = pd.DataFrame(
    np.arange(12).reshape(3, 4),
    index = ['two', 'one', 'three'],
    columns=['d', 'a', 'b', 'c']
)

print(f"Dataframe :\n{df}")

print("-" * 60)
# sort it by index

print(df.sort_index())

print("-" * 60)
print(df.sort_index(axis=1))

print("-" * 60)
print(df.sort_index(axis=1, ascending=False))

print("-" * 60)
data = pd.read_csv("C:/Training/PycharmProjects/renualtExt/Day01/PandasExample/vgsalesGlobale.csv")

print(data.head())

print("-" * 60)
# sort it by name
print(data['Name'].sort_values(ascending=False))

print("-" * 60)
# sort the dataframe with names column
print(data.sort_values('Name'))

print("-" * 60)
print(data.sort_values('Year'))

print("-" * 60)
print(data.sort_values(['Year', 'Name']))

