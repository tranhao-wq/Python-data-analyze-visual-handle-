import matplotlib.pyplot as plt
import numpy as np

# Example data: exam scores for three classes
np.random.seed(42)
class1 = np.random.normal(75, 10, 30)
class2 = np.random.normal(80, 7, 30)
class3 = np.random.normal(70, 12, 30)

data = [class1, class2, class3]
labels = ['Class A', 'Class B', 'Class C']
colors = ['#ffe066', '#66d9e8', '#fab1a0']

plt.figure(figsize=(7, 4))
box = plt.boxplot(data, patch_artist=True, labels=labels)

# Color the boxes
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Box & Whisker Plot Example')
plt.ylabel('Exam Scores')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 