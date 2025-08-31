
import numpy as np
import pandas as pd

s = pd.Series(['Sam', np.nan, 'Tim', 'Kim'])
print(f"s :\n{s}")

print("-" * 60)
print(s.isnull())

print("-" * 60)
print(s.notnull())

print("-" * 60)
s[3] = None
print(f"s :\n{s}")

print("-" * 60)
print(s.isnull())

print("-" * 60)
print(s.dropna())

print("-" * 60)
from numpy import nan as NA
df = pd.DataFrame([[1, 2, 3], [4, NA, 5],
                  [NA, NA, NA]])
print(df)

print("-" * 60)
print(df.dropna())

print("-" * 60)
print(df.dropna(how='all'))

print("-" * 60)
df[1] = NA
print(df)

print("-" * 60)
print(df.dropna(axis=1, how='all'))

print("-" * 60)
print(df.dropna(thresh=1))
# print(df)

print("-" * 60)
print(df)

print("-" * 60)
df.fillna(0, inplace=True)
print(df)