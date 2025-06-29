import matplotlib.pyplot as plt
import numpy as np

# Example data: ages from a survey
np.random.seed(7)
ages = np.random.normal(30, 10, 200).astype(int)
ages = ages[(ages > 10) & (ages < 60)]  # keep ages between 10 and 60

plt.figure(figsize=(7, 4))
plt.hist(ages, bins=10, color='red', edgecolor='black', alpha=0.8)
plt.title('Histogram Chart Example')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 