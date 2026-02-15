import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("./data/gas_electricity_rent_expenses.csv")
fig, ax = plt.subplots(figsize=( 10,6))

cat_df = df['Category'].unique()
markers=['o','^','x','D','x']


for i,bills in enumerate(cat_df):
    data = df[df['Category'] == bills]
    ax.plot(data['Month'], data['Amount_USD'],marker = markers[i],label=bills)

ax.set_title('Rent Expenses')
ax.set_xlabel('Month of the Year')
ax.set_ylabel("Amount_USD")
ax.legend()        
plt.show()
