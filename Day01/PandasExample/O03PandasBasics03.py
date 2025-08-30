import numpy as np
import pandas as pd

cities = pd.Series(['blr', 'che', 'hyd', 'del', 'mum', 'kol', np.nan])
print(f"Cities :\n{cities}")
res = cities.map({'che': 'hottest'})
print(f"res :\n{res}")


print("-" * 60)
res = cities.map('i love {}'.format, na_action='ignore')
print(f"res :\n{res}")
