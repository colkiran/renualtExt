
import numpy as np
import pandas as pd

df1 = pd.DataFrame(
    {"key": ['a', 'b', 'c', 'c', 'd', 'e'],
     "num1": range(6)})

df2 = pd.DataFrame(
    {"key": ['b', 'c', 'e', 'f'],
     "num2": range(4)})

print(f"df1 :\n{df1}")

print("-" * 60)
print(f"df2 :\n{df2}")

print("-" * 60)
# merge the dataframes
print(pd.merge(df1, df2))

print("-" * 60)
print(pd.merge(df1, df2, on="key"))

print("-" * 60)
df3 = pd.DataFrame(
    {"key1" :['a', 'b', 'c', 'c', 'd', 'e'],
     "num1": range(6)})

df4 = pd.DataFrame(
    {"key2": ['b', 'c', 'e', 'f'],
     "num2": range(4)})

print(f"df3 :\n{df3}")
print("-" * 60)
print(f"df4 :\n{df4}")

print("-" * 60)
print(pd.merge(df3, df4, left_on="key1", right_on="key2"))

print("-" * 60)
print(pd.merge(df1, df2, how="outer"))

print("-" * 60)
print(pd.merge(df1, df2, how="right"))

print("-" * 60)
print(pd.merge(df1, df2, how="left"))

print("-" * 60)
print(pd.merge(df1, df2, how="inner"))


print("-" * 60)
# merge on index
df1 = pd.DataFrame(
    {"letter" : ['a', 'a', 'b', 'b', 'a', 'c'],
     "num": range(6)})

df2 = pd.DataFrame(
    {"value": [3, 5, 7]},
     index = ['a', 'b', 'e'])

print(f"df1 :\n{df1}")

print("-" * 60)
print(f"df2 :\n{df2}")

print("-" * 60)
print(pd.merge(df1, df2, left_on="letter", right_index=True))

print("-" * 60)
right = pd.DataFrame(
    [[1, 2], [3, 4], [5, 6]],
    index = ['a', 'c', 'd'],
    columns = ['Tom', 'Tim'])

left = pd.DataFrame(
    [[7, 8], [9, 10], [11, 12], [13, 14]],
    index=['a', 'b', 'e', 'f'],
    columns= ['Sam', 'Kim'])

print(f"right :\n{right}")

print("-" * 60)
print(f"left :\n{left}")

print("-" * 60)
print(pd.merge(right, left,
         right_index=True,
         left_index= True,
         how="outer"))

print("-" * 60)
print(left.join(right))

print("-" * 60)
print(left.join(right, how="outer"))

