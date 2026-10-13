import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load penguin dataset
df = sns.load_dataset("penguins")

print("First 10 rows of penguin data:")
print(df.head(10))
print()

print("Last 10 rows of penguin data:")
print(df.tail(10))
print()

print("Total null values in the penguin dataset:")
print(df.isnull().sum())
print()

plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in Penguin Dataset")
plt.show()

print("After removing rows with any null values:")
print(df.dropna())
print()

print("After removing rows where all values are null:")
print(df.dropna(how="all"))
print()

print("After replacing NaN with 0:")
print(df.fillna(0))
print()

sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.title("Penguin Bill Dimensions by Species")
plt.show()