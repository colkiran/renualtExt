
import numpy as np
import pandas as pd

data = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=[list("aabb"), [1, 2]*2],
    columns= [['num', 'num', 'comp', 'comp'], ['math', 'stat']*2])

print(data)

print("-" * 60)
data.index.names = ['class', 'exam']
data.columns.names = ['field', 'subject']

print(data)

print("-" * 60)
print(data.stack(future_stack = True))

print("-" * 60)
print(data.unstack())

print("-" * 60)
print(data.stack(0, future_stack=True))

print("-" * 60)
print(data.stack('field', future_stack=True))

print("-" * 60)
# pivoting

stock = pd.DataFrame(
    {"fruit": ['apple', 'plum', 'grape'] * 2,
     "color": ['purple', 'yellow'] * 3,
     "piece": [3,4,5,6,1,2]})

print(stock)

print("-" * 60)
print(stock.pivot(index="fruit", columns="color", values="piece"))

print("-" * 60)
stock['value'] = np.random.randn(len(stock))

print(stock)

print("-" * 60)
res = stock.pivot(index="fruit", columns="color")
print(res)

print("-" * 60)
print(res["value"])

print("-" * 60)
data = pd.DataFrame(
    {"subject" : ['math', 'stat', 'bio'],
     "Sam": [50, 60, 70],
     "Kim": [80, 70, 90],
     "Tom": [60, 80, 85]})

print(f"data :\n{data}")

print("-" * 60)
res = pd.melt(data, ['subject'])
print(res)

print("-" * 60)
data = res.pivot(index="subject", columns="variable", values="value")
print(data)

print("-" * 60)
print(data.reset_index())
