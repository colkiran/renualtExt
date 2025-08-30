
import pandas as pd

print("Pandas Series".center(60, "-"))
pds = pd.Series()
print(f'pds :{pds}')
print(type(pds))

print("-" * 60)
ps = pd.Series([1, 2, 3, 4, 5])
print(f"pandas Series :\n{ps}")

print("-" * 60)
ps = pd.Series({'a' : 'Apple', 'b': 'Ball', 'c': 'Cat', 'd': 'Dog'})
print(f"ps :\n{ps}")

print("-" * 60)
ps = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(f"Pandas Series :\n{ps}")

print("-" * 60)
ps1 = pd.Series([1, 2, 3, 4, 5])
ps2 = pd.Series([10, 20, 30, 40, 50], index=['aa', 'bb', 'cc', 'dd', 'ee'])
print(f"Series1 :\n{ps1}")
print(f"Series2 :\n{ps2}")

print("-" * 60)
print(f"Index of Series1 :{ps1.index}")
print(f"Index of Series2 :{ps2.index}")

print("-" * 60)
print(f"values of Series1 :{ps1.values}")
print(f"values of Series2 :{ps2.values}")

print("-" * 60)
print(f"shape of Series1 :{ps1.shape}")
print(f'shape of Series2 :{ps2.shape}')

print("-" * 60)
print(f"datatype of Series1 :{ps1.dtype}")
print(f"datatype of Series2 :{ps2.dtype}")

print("-" * 60)
ps3 = pd.Series()
print(f"check if Series1 is empty :{ps1.empty}")
print(f"check if Series2 is empty :{ps2.empty}")
print(f"check if Series3 is empty :{ps3.empty}")

print("-" * 60)
print(f"count of Series1 :{ps1.count()}")
print(f"counf of Series2 :{ps1.count()}")

print("-" * 60)
print(f"Length of Series1 :{len(ps1)}")
print(F"Length of Series2 :{len(ps2)}")
