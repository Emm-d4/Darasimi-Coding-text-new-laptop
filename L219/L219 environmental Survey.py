import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L219\FuelConsumption.csv")

print("First 5 rows of data:")
print(data.head())

# Data Information
print("Data Information")
print(data.info())

# Check presence of null values
print("Check which data contains null values")
print(data.isnull().any())

df_grouped = data.groupby('VEHICLECLASS').mean(numeric_only=True)

print(df_grouped.head())

# numerical x
x= np.arange(0, len(df_grouped.index))

# plot bars
plt.bar(x, df_grouped['FUELCONSUMPTION_CITY'], bottom=df_grouped['FUELCONSUMPTION_HWY'], color = '#1D2F6F')
plt.show()

plt.bar(x, df_grouped['FUELCONSUMPTION_HWY'], color = '#8390fa')
plt.show()

plt.bar(x, df_grouped['FUELCONSUMPTION_COMB'], bottom=df_grouped['FUELCONSUMPTION_COMB'], color = '#6EAF46')

plt.ylabel('Fuel Consumption')
plt.xticks(x, df_grouped.index, rotation=90)
plt.legend(['City', 'Highway','Combined'])
plt.title('Average Fuel Consumption for Diffrent Vehicle Type')
plt.show()