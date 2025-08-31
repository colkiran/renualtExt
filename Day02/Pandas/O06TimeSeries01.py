
import numpy as np
import pandas as pd
from datetime import datetime

date = [
    datetime(2020, 1, 5),
    datetime(2020, 1, 10),
    datetime(2020, 1, 15),
    datetime(2020, 1, 20),
    datetime(2020, 1, 25)
]

ts = pd.Series(np.random.randn(5), index = date)
print(ts)

print("-" * 60)
print(ts.index)

print("-" * 60)
print(pd.to_datetime("01/01/2020"))

dates = pd.to_datetime(
    [datetime(2020, 7, 5),
     '6th july, 2020',
     "2020-jul-7",
     "20200708"])

print(dates)

print("-" * 60)
print(dates.to_period("D"))
print(dates[0])

print("-" * 60)
print(dates - dates[0])

print("-" * 60)
# Creating a time series
print(pd.date_range("2020-08-13", "2020-09-01"))

print("-" * 60)
print(pd.date_range("2020-07-15", periods=10))

print("-" * 60)
print(pd.date_range("2020-07-15", periods=10, freq="h"))

print("-" * 60)
print(pd.date_range("2020-10", periods=10, freq="ME"))

print("-" * 60)
stamp = ts.index[1]
print(stamp)

print("-" * 60)
print(f"ts :{ts}")

print("-" * 60)
print(ts[stamp])

print("-" * 60)
print(ts["25.1.2020"])

print("-" * 60)
long_ts = pd.Series(
    np.random.randn(1000),
    index=pd.date_range("1/1/2020",
                        periods=1000))

print(f"long_ts :\n{long_ts}")

print("-" * 60)
print(long_ts.head())

print("-" * 60)
print(long_ts[datetime(2022, 9, 20):])

print("-" * 60)
# important methods
print(ts.truncate(after="1/15/2020"))

print("-" * 60)
print(pd.date_range("1/1/2020", periods=100, freq="W-SUN"))

print("-" * 60)
long_df = pd.DataFrame(np.random.randn(100, 4),
                    index=date,
                    columns=list("ABCD"))
print(long_df)
