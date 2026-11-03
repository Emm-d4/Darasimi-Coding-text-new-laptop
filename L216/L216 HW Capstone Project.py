#check if there"s null value present
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\Penguins.Data.csv")
#check if there"s null value present
print("Check which data contains null value:")
print(df.isnull().any())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

# Visualize missing values using a heatmap
sns.heatmap(df.isnull())
plt.show()

#fill up numerical null value
#df["Culmen Depth (mm)"] = df.fillna(df["Culmen Depth (mm)"].mean())
df["Culmen Depth (mm)"].fillna(df["Culmen Depth (mm)"].mean())

#fill up categorical null value
#df["Gender"]= df.fillna(df["Gender"].value_counts().index[0])
df["Gender"].fillna(df["Gender"].value_counts().index[0])

#pairplot
sns.pairplot(data=df)
plt.show()

#df["Delta 15 N (o/oo)"] = df.fillna(df["Delta 15 N (o/oo)"].mean())
df["Delta 15 N (o/oo)"].fillna(df["Delta 15 N (o/oo)"].mean())

#heatmap
plt.figure(figsize=(20,10))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="terrain")
plt.show()

#box and whiskers plot
df.plot(kind = "box", subplots=True, layout=(5, 3), figsize=(12,12))
plt.show()

#countplot for gender
sns.countplot(x="Gender", palette="BuGn", data=df)
plt.show()