import matplotlib.pyplot as plt

# Example data: sales across different regions
regions = ['North', 'South', 'East', 'West', 'Central']
sales = [120, 90, 150, 110, 95]
colors = ['#ffbe76', '#ff7979', '#badc58', '#7ed6df', '#f6e58d']

plt.figure(figsize=(7, 4))
plt.bar(regions, sales, color=colors, edgecolor='black')
plt.title('Bar Chart Example')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 