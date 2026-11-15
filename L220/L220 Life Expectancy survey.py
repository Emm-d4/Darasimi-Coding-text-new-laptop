import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L220\gapminder(2007).csv")

print("First 5 rows of data:")
print(data.head())

#Data Information
print("Data Information")
print(data.info())

#Check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

data.groupby('continent').size().plot(kind ='pie', autopct='%.2f')
plt.show()

plt.pie(data.groupby('continent').size(), autopct='%.2f',
        labels=['Africa','America','Aisa','Europe','Oceania'],
        labeldistance=1.15, wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white'})
plt.show()