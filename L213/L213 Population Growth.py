import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L213\Countries Data.csv")

# display the first 5 rowsof df
print("First 5 rows of data:")
print(df.head(5))
print()

# display population in the year 1967
print("Data in the year 1967")
y_67 = df.loc[df["year"] == 1967]
print(y_67.head())
print()

# display population in the year 2007
print("Data in the year 2007")
y_07 = df.loc[df["year"] == 2007]
print(y_07.head())
print()

# merge data in the year 1967 and 2007
print("Merge Data in the year 1967 and 2007")
d_merge = y_67.merge(y_07, left_on="country", right_on="country")
print(d_merge.head())
print()
 
# drop "year" column on the merge data
print("Merged Data after dropping 'year' column")
print(d_merge.drop(["year_x", "year_y"], axis=1))
print()

#create new column for the diffrence between population_y and population_x
print("Population growth from 1967 to 2007")
d_merge["population_growth"] = d_merge["population_y"] - d_merge["population_x"]
print(d_merge.head())
print()

# merge data shape
print("Data shape")
print(d_merge.shape, type(d_merge))
print()

# sort values to get 10 countries with the biggest population growth
print("10 countries with the biggest population growth")
d_merge = d_merge.sort_values("population_growth", ascending=False)
print(d_merge.head(10))
print()

# reset index
print("Resetting index")
d_merge = d_merge.reset_index()
print(d_merge.head(10))
print()

# drop index column
print("drop index column")
d_merge = d_merge.drop(["index"], axis=1)
print(d_merge.shape)
print()

# top 10 countries with the highest population between 1967 and 2007
print("10 countries with the highest population growth")
print(d_merge.head(10))

# plot the data
names = ["India", "China", "Indonesia", "Pakistan", "United States", "Brazil", "Nigeria", "Bangledesh", "Mexico", "Philippines"]
f_10_country = d_merge.head(10)
pop_grow = (f_10_country["population_growth"] / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)
plt.xlabel("country")
plt.ylabel("population Growth (Millions)")
plt.title("Top 10 countries with the the biggest population Growth from 1967 to 2007")
plt.xticks(rotation=45)
plt.show()