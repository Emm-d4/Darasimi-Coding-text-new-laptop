import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L213\Countries Data.csv")

# display the first 5 rows
print("First 5 rows of data:")
print(df.head(5))
print()

# population in 1967
print("Data in the year 1967")
y_67 = df.loc[df["year"] == 1967]
print(y_67.head())
print()

# population in 2007
print("Data in the year 2007")
y_07 = df.loc[df["year"] == 2007]
print(y_07.head())
print()

# merge on country
print("Merge Data in the year 1967 and 2007")
d_merge = y_67.merge(y_07, on="country")
print(d_merge.head())
print()

# drop year columns
print("Merged Data after dropping 'year' column")
d_merge = d_merge.drop(["year_x", "year_y"], axis=1)
print(d_merge.head())
print()

# compute population growth
print("Population growth from 1967 to 2007")
d_merge["population_growth"] = d_merge["population_y"] - d_merge["population_x"]
print(d_merge.head())
print()

#  Seaborn plot
plt.figure(figsize=(12, 6))
sns.barplot(
    data=d_merge,
    x="country",
    y="population_growth",
    palette="viridis"
)

plt.xticks(rotation=90)
plt.title("Population Growth (1967–2007)")
plt.xlabel("Country")
plt.ylabel("Population Growth")
plt.tight_layout()
plt.show()