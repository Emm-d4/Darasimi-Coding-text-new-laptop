import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L219\gapminder(2007).csv")

avg_data = data.groupby(data['continent']).mean(numeric_only=True)

avg_data = avg_data.reset_index()

print(avg_data)

plt.bar(avg_data['continent'], avg_data['life_exp'], color='teal')
plt.xlabel('Continent')
plt.ylabel('Average life Expentancy')
plt.show()