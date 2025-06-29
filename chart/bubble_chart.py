import matplotlib.pyplot as plt
import numpy as np

# Example data: social media engagement metrics
np.random.seed(1)
x = np.random.rand(10) * 100  # e.g., number of posts
y = np.random.rand(10) * 100  # e.g., number of likes
sizes = np.random.rand(10) * 800 + 100  # e.g., engagement (bubble size)

plt.figure(figsize=(6, 6))
plt.scatter(x, y, s=sizes, alpha=0.5, color='skyblue', edgecolors='black')
plt.xlabel('Number of Posts')
plt.ylabel('Number of Likes')
plt.title('Bubble Chart Example')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 