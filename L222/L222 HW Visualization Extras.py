import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L222\FuelConsumption.csv")

print("first 5 row of data")
print(data.head())
print()

# Check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

grouped_df = data.groupby('FUELTYPE').mean(numeric_only=True)
grouped_df = grouped_df.reset_index()

plots = sns.barplot(x=grouped_df['FUELTYPE'], y=grouped_df['FUELCONSUMPTION_COMB'], color='teal')
plt.show()

plots = sns.barplot(x=grouped_df['FUELTYPE'], y=grouped_df['FUELCONSUMPTION_COMB'], color='teal')
plt.show()

#Annontating Bar Plot
for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                  (bar.get_x() + bar.get_width() / 2,
                   bar.get_height()), ha='center', va='center',
                    size=12, xytext=(0, 8),
                      textcoords='offset points')

plt.xlabel("FUELTYPE", size=14)

#Setting the label for y-axis
plt.ylabel("FUELCONSUMPTION_COMB", size=14)

# Setting the title for the graph
plt.title("This is an annotated barplot")

plt.show()