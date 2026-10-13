import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L211\country_vaccinations.csv")

# display the first 10 row of data
print("First 10rows of data:")
print(df.head(10))
print()

# check the null value
print("Total null value in the data")
print(df.isnull().sum())
print()

# Visualize missing values using a heatmap
subset = df.iloc[:5200, :] # Taking the first 100 rows for better peformance
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

# ddisplay the last 10 rows of data
print("Last 10 rows of data:")
print(df.tail(10))
print()

# remove data with Null/NaN
print("After removing data which contains null value:")
print(df.dropna())
print()

# only removing data if all of the values are NaN
print("after removing data that all values are null")
print(df.dropna(how="all"))
print()

#replace NaN with 0
print("after replacing NaN with 0:")
print(df.fillna(0))
print()

# fill the NA value
print("fill the NA value using interpolate:")
print(df.infer_objects(copy=False))
print()

# get the clean data
print("Clean data after removing null value:")
df_dropped=df.dropna()
print(df_dropped)
print()