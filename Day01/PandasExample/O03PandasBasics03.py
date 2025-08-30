import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


cities = pd.Series(['blr', 'che', 'hyd', 'del', 'mum', 'kol', np.nan])
print(f"Cities :\n{cities}")
res = cities.map({'che': 'hottest'})
print(f"res :\n{res}")


print("-" * 60)
res = cities.map('i love {}'.format, na_action='ignore')
print(f"res :\n{res}")

print("-" * 60)
games = pd.read_csv("vgsalesGlobale.csv")
print(games.head())

print("-" * 60)
print(games.dtypes)

print("-" * 60)
print(games.describe())

print("-" * 60)
print(games.Genre.value_counts())

print("-" * 60)
print(games.Genre.nunique())

print("-" * 60)
print(games.Genre.unique())

print("-" * 60)
print(pd.crosstab(games.Genre, games.Year))

print("-" * 60)
print(games.Global_Sales.describe())

print("-" * 60)
print(games.Global_Sales.value_counts())

print("-" * 60)
games.Year.plot(kind='hist')
plt.show()

print("-" * 60)
print(games.Genre.value_counts())
games.Genre.value_counts().plot(kind='bar')
plt.show()




