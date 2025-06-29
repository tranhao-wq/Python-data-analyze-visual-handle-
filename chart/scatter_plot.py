import matplotlib.pyplot as plt
import numpy as np

# Example data: relationship between two variables
np.random.seed(2)
x = np.random.rand(20) * 10
y = 2 * x + np.random.randn(20) * 2

plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='dodgerblue', edgecolor='black', s=60)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Scatter Plot Example')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 