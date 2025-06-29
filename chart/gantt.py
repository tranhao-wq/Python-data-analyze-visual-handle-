import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Example tasks and their start/end dates
tasks = [
    {'name': 'Task 1', 'start': '2023-01-01', 'end': '2023-02-15', 'color': 'tab:red'},
    {'name': 'Task 2', 'start': '2023-02-01', 'end': '2023-03-15', 'color': 'tab:green'},
    {'name': 'Task 3', 'start': '2023-03-01', 'end': '2023-05-01', 'color': 'tab:orange'},
    {'name': 'Task 4', 'start': '2023-04-01', 'end': '2023-06-01', 'color': 'tab:purple'},
    {'name': 'Task 5', 'start': '2023-05-15', 'end': '2023-07-01', 'color': 'tab:blue'},
]

fig, ax = plt.subplots(figsize=(8, 3))

# Convert string dates to datetime
for i, task in enumerate(tasks):
    start = datetime.strptime(task['start'], '%Y-%m-%d')
    end = datetime.strptime(task['end'], '%Y-%m-%d')
    ax.barh(i, (end - start).days, left=start, height=0.5, color=task['color'], label=task['name'])

# Formatting
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task['name'] for task in tasks])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.set_xlabel('Timeline (2023)')
ax.set_title('Gantt Chart Example')
ax.invert_yaxis()
plt.tight_layout()
plt.show() 