
data = [10, 20, None, 30, 40, None, 50, 60, None, 70, 80]
print(f"data :{data}")

# filter the data and extract the data
fltData = [x for x in data if x != 'None']
print(f"Filtered Data :{fltData}")

print("*" * 60)
import pandas as pd
s = pd.Series([10, 20, None, 30, 40, None, 50, 60, None, 70, 80])
print(s.isna())
print('-' * 60)
fltSrs = s.dropna()
print(fltSrs)


