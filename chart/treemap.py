import matplotlib.pyplot as plt
import squarify

# Example data: file system usage (in MB)
labels = ['System', 'Users', 'Apps', 'Temp', 'Logs', 'Backups', 'Other']
sizes = [500, 300, 200, 100, 80, 60, 40]
colors = ['#ffcc99', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0', '#ffb3e6', '#c2f0c2']

plt.figure(figsize=(7, 4))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, pad=True, text_kwargs={'fontsize':10})
plt.title('Treemap Example: File System Usage')
plt.axis('off')
plt.tight_layout()
plt.show() 