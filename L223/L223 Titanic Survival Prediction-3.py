import pandas as pd
import numpy as np
import statistics as stats

df = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L223\Titanic Dataset.csv")

# display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# Median Value of age 
median_age = np.median(df["Age"])
print(f"Median Age of Passengeers is = {median_age}")
print()

# Mode value of age
mode_age  = stats.mode(df["Age"])
print(f"Mode value of Age = {mode_age}")
print()