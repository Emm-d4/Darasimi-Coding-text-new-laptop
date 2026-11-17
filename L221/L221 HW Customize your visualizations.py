import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L221\FuelConsumption.csv")

print("first 5 rows of data")
print(data.head())

# Data Information
print("Data Information")
print(data.info())

# check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

# Countplot for feature FUELCONSUMPTION
# Setting diffrent themes
sns.set_style('white')
sns.countplot(x=data['FUELCONSUMPTION'])
plt.show()

sns.set_style('dark')
sns.countplot(x=data['FUELCONSUMPTION'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['FUELCONSUMPTION'])
plt.show()

sns.set_style('darkgrid')
sns.countplot(x=data['FUELCONSUMPTION'])
plt.show()

sns.set_style('ticks')
sns.countplot(x=data['FUELCONSUMPTION'])
plt.show()

# Despining
sns.set_style("white")
sns.countplot(x=data['FUELCONSUMPTION'])
sns.despine()
plt.show()

# Trying diffrent palettes
sns.set_style('whitegrid')
sns.countplot(x=data['FUELCONSUMPTION'], palette='winter')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['FUELCONSUMPTION'], color='Purple')
plt.show()

# Scaling figures
sns.set_style('whitegrid')
sns.set_context("paper")
sns.countplot(x=data['FUELCONSUMPTION'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("notebook")
sns.countplot(x=data['FUELCONSUMPTION'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("talk")
sns.countplot(x=data['FUELCONSUMPTION'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['FUELCONSUMPTION'], color='Purple')
plt.xticks(rotation=45)
plt.show()

# Scaling font size of figure
sns.set_style('whitegrid')
sns.set_context("poster", font_scale=0.8)
sns.countplot(x=data['FUELCONSUMPTION'], color='Purple')
plt.xticks(rotation=45)
plt.show()