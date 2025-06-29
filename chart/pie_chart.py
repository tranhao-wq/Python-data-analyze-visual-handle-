import matplotlib.pyplot as plt

# Example data: market share distribution
labels = ['Product A', 'Product B', 'Product C', 'Product D']
sizes = [60, 20, 10, 10]
colors = ['#ff6666', '#ffcc66', '#66b3ff', '#999999']
explode = (0.1, 0, 0, 0)  # explode the largest slice

plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140, shadow=True)
plt.title('Pie Chart Example')
plt.tight_layout()
plt.show() 