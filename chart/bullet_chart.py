import matplotlib.pyplot as plt

# Example data
performance = 93000   # Actual value
target = 100000       # Target value
ranges = [50000, 90000, 120000]  # Qualitative ranges (bad, satisfactory, good)

fig, ax = plt.subplots(figsize=(7, 2))

# Draw qualitative ranges
ax.barh(0, ranges[2], color='#d4efdf', height=0.5)  # Good (green)
ax.barh(0, ranges[1], color='#f9e79f', height=0.5)  # Satisfactory (yellow)
ax.barh(0, ranges[0], color='#f5b7b1', height=0.5)  # Bad (red)

# Draw performance bar
ax.barh(0, performance, color='#34495e', height=0.2)

# Draw target marker
ax.plot([target, target], [-0.2, 0.2], color='green', linewidth=4)

# Formatting
ax.set_yticks([])
ax.set_xlim(0, ranges[2])
ax.set_xlabel('Last Month Revenue')
ax.set_title('Bullet Chart Example')
ax.set_xticks([50000, 90000, 100000, 120000])
ax.set_xticklabels(['50K', '90K', '100K', '120K'])
plt.tight_layout()
plt.show() 