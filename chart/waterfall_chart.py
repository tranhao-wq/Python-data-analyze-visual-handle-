import matplotlib.pyplot as plt
import numpy as np

# Example data: profit and loss components
labels = ['Start', 'Sales', 'Returns', 'Expenses', 'Profit']
values = [100, 60, -20, -50, 90]  # The last value is the final total

# Calculate cumulative values for the waterfall
cumulative = np.cumsum([0] + values[:-1])
bar_colors = ['#7ed6df' if v >= 0 else '#ff7979' for v in values[:-1]] + ['#badc58']

plt.figure(figsize=(8, 4))
for i in range(len(values)):
    plt.bar(labels[i], values[i], bottom=cumulative[i], color=bar_colors[i], edgecolor='black')

# Draw connecting lines
for i in range(1, len(values)):
    plt.plot([i-1, i], [cumulative[i], cumulative[i]], color='black')

plt.title('Waterfall Chart Example')
plt.ylabel('Value')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 