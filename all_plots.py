import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('./data/save_the_bees.csv')

# Select 6 states (you can change these)
states = ['Arizona', 'Texas', 'Florida', 'New York', 'Georgia', 'Illinois']
filtered_df = df[df['state'].isin(states)]

fig, ax = plt.subplots(4, 1, figsize=(12, 20))

# 1️⃣ Average Percent Lost (Bar Chart)
avg_lost = filtered_df.groupby('state')['percent_lost'].mean()
ax[0].bar(avg_lost.index, avg_lost.values)
ax[0].set_title("Average Percent Lost (Selected States)")
ax[0].set_ylabel("Percent Lost")
ax[0].tick_params(axis='x', rotation=45)

# 2️⃣ Total Number of Colonies (Bar Chart)
total_colonies = filtered_df.groupby('state')['num_colonies'].sum()
ax[1].bar(total_colonies.index, total_colonies.values)
ax[1].set_title("Total Number of Colonies (Selected States)")
ax[1].set_ylabel("Number of Colonies")
ax[1].tick_params(axis='x', rotation=45)

# 3️⃣ Colony Losses Over Time (Line Plot)
yearly_losses = df.groupby('year')['lost_colonies'].sum()
ax[2].plot(yearly_losses.index, yearly_losses.values, marker='o')
ax[2].set_title("Total Colony Losses Over Time")
ax[2].set_ylabel("Lost Colonies")

# 4️⃣ Percent Lost vs Varroa Mites (Scatter Plot)
ax[3].scatter(df['varroa_mites'], df['percent_lost'])
ax[3].set_title("Percent Lost vs Varroa Mites")
ax[3].set_xlabel("Varroa Mites (%)")
ax[3].set_ylabel("Percent Lost")

plt.tight_layout()
plt.show()
