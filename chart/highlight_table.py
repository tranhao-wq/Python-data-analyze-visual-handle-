import numpy as np
import matplotlib.pyplot as plt

# Example data: survey responses or scores
np.random.seed(0)
data = np.random.randint(1, 10, (5, 7))

fig, ax = plt.subplots(figsize=(7, 3))
cax = ax.matshow(data, cmap='coolwarm')

# Add text annotations
for (i, j), val in np.ndenumerate(data):
    ax.text(j, i, f'{val}', va='center', ha='center', color='black' if val < 7 else 'white', fontsize=10)

# Set axis labels
ax.set_xticks(range(data.shape[1]))
ax.set_yticks(range(data.shape[0]))
ax.set_xticklabels([f'Q{j+1}' for j in range(data.shape[1])])
ax.set_yticklabels([f'Resp {i+1}' for i in range(data.shape[0])])
plt.title('Highlight Table Example')
fig.colorbar(cax, label='Value')
plt.tight_layout()
plt.show() 