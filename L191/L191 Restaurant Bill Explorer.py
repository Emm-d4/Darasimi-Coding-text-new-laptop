import seaborn as sns 
import matplotlib.pyplot as plt

#--- PART 1: Bar Plot and Count Plot ----
df = sns.load_dataset('tips')
df = df.dropna()

print("First 5 rows")
print(df.head())
print()

print("dataframe info:")
print(df.info())
print()

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.countplot(x='day', hue='sex', data=df)
plt.title('Number of diners per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

# ---- PART 2: Box Plot, Strip Plot and swarm plot ----
sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
plt.title('Every Bill Amount per Day (Strip Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount per Day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

# ---- PART 2: Joint Plot ----
sns.jointplot(x='total_bill', y='tip', data=df)
plt.suptitle('Total Bill vs Tip', y=1.02)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, kind='kde')
plt.suptitle('Total Bill vs KDE Joint plot', y=1.02)
plt.show()