import matplotlib.pyplot as plt
# import numpy as np

import pandas as pd

fig, ax = plt.subplots(4,1, figsize=(6,20), sharex=True)
plt.xlabel('Subjects')
ax[0].bar(df['Exam'],df['Alice'], label="Alice's Scores", color='lightgreen')
ax[0].set_title("Alice's Performance")
ax[0].set_ylabel("Scores")

ax[1].bar(df['Exam'],df['Bob'], label="Bob's Scores", color='blue')
ax[1].set_title("Bob's Performance")
ax[1].set_ylabel("Scores")

ax[2].bar(df['Exam'],df['Charlie'], label="Charlie's Scores", color='red')
ax[2].set_title("Charlie's Performance")
ax[2].set_ylabel("Scores")

ax[3].bar(df['Exam'],df['Diana'], label="Diana's Scores", color='orange')
ax[3].set_title("Diana's Performance")
ax[3].set_ylabel("Scores")

ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[3].legend()

plt.show()
