import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L218\gapminder(2007).csv")

print("First 5 rows of data")
print(data.head())

# Data Information
print("Data Information")
print(data.info())

# Check presence of null values
print("Check which data contains null values")
print(data.isnull().any())

labels = ['country', 'life_exp', 'gdp_cap']

# plotting boxplots
for l in labels:
    sns.boxplot(y=data[l], palette='winter')
    plt.show()

sns.boxplot(y='gdp_cap', x='continent', data=data, palette='viridis')
plt.show()

sns.boxplot(y='life_exp', x='continent', data=data, palette='viridis')
plt.show()

# plotting violin plots
sns.violinplot(y='gdp_cap', x='continent',data=data, palette='bright')
plt.show()

sns.violinplot(y='life_exp', x='continent',data=data, palette='bright')
plt.show()

# Plotting Density plot
for l in labels:
    sns.kdeplot(data[l])
    plt.show()

# Plotting histogram
for l in labels:
    plt.hist(data[l])
    plt.xlabel(l)
    plt.show()

# Plotting Displot
for l in labels:
    sns.distplot(data[l])
    plt.show()
    print("Skewness is :", data[l].skew())