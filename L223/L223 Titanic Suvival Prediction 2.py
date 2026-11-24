import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L223\Titanic Dataset.csv")

#Display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# Mean Value of age
mean_age = np.mean(df["Age"])
print(f"Mean of passengers is = {mean_age}")
print()

# Mean Value of Fare
mean_fare = np.mean(df["Fare"])
print(f"Mean Fare is = {mean_fare}")