import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns. load_dataset("penguins")

type =[df["Culmen Length (mm)"], df["Culmen Depth (mm)"], df["Flipper Length (mm)"],
df["Body Mass (g)"]]
colors = ["g", "y", "b", "r"]
label = ["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body
Mass (g)"]

plt.hist(type, rwidth=0.95, color=colors, label=label)
plt. legend()

#df.hist(figsize=(12,8))
plt. show()