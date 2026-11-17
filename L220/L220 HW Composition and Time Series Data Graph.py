import pandas as pd
import matplotlib. pyplot as plt
data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L220")

print("First 5 rows of data:")
print(data.head())

#Data Information
print("Data Information:")
print(data.info())

#Check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

data.groupby('FUELTYPE').size().plot(kind='pie', autopct='%.2f')
plt.show()

plt.pie(data.groupby('FUELTYPE').size(), autopct='%.2f',
labels=['D','E','X','Z'],
labeldistance=1.15, wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' })

plt.show()