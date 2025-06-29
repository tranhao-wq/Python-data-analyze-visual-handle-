import matplotlib.pyplot as plt
import numpy as np

# Example data: stock market performance over time
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
values = [100, 110, 105, 120, 115, 130, 125, 140]

plt.figure(figsize=(7, 4))
plt.plot(months, values, marker='o', color='black', linewidth=2)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title('Line Chart Example')
plt.xlabel('Month')
plt.ylabel('Stock Value')
plt.tight_layout()
plt.show() 