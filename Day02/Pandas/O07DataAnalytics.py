
import pandas as pd

# load the data
df = pd.read_csv("forbes_2022_billionaires.csv")
print(df.head())

print("-" * 60)
print(df.shape)

print("-" * 60)
print(df.columns)

print("-" * 60)
# Data Preprocessing
df = df.loc[:,["rank", "personName", "age", "finalWorth", "category", "gender", "country"]]
print(df.head())

print("-" * 60)
print(df.dtypes)

print("-" * 60)
df.dropna(inplace=True)
print(df.shape)

print("-" * 60)
# count of males and females
print(df['gender'].value_counts())

print("-" * 60)
print(df['country'].value_counts())

print("-" * 60)
print(df['country'].unique())

print("-" * 60)
print(df[df['country'] == 'Turkey'].gender.value_counts())

print("-" * 60)
import seaborn as sns
import matplotlib.pyplot as plt

df_gender = df.groupby(["gender"])
sns.set_theme()
sns.set(rc = {"figure.dpi":300})
import warnings
warnings.filterwarnings("ignore")

# df_gender.size().plot(kind="bar")
# plt.show()

print("-" * 60)
# top 10 richest in the world

# sns.barplot(y = df["personName"][:10], x=df["finalWorth"][:10])
# plt.show()

print("-" * 60)
# country that has the highest no of billionaries
df_cntry = df.groupby("country")
df_cntry_count = pd.DataFrame(df_cntry.size().sort_values(ascending=False), columns=["country_name"])

print(df_cntry_count.head())

# sns.barplot(x = df_cntry_count["country_name"][:10],  y = df_cntry_count.index[:10])
# plt.show()

print("-" * 60)
# top 10 richest people in india
df_india = df[df['country'] == "India"]

print(df_india.head(10))
