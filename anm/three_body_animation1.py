import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Gravitational constant (arbitrary units)
G = 1

# Elon Musk version: more dramatic initial conditions
masses = np.array([1.5, 1, 0.8])
positions = np.array([
    [1.2, 0, 0],
    [-0.6, 1.1, 0],
    [-0.6, -1.1, 0]
], dtype=float)
velocities = np.array([
    [0, 0.7, 0.5],
    [0, -0.35, -0.6],
    [0, -0.35, 0.2]
], dtype=float)

# Simulation parameters
dt = 0.008
steps = 2500

# Store trajectories for each body
trajectories = [[], [], []]

# Colors for a more 'Elon Musk' (SpaceX) style
colors = ['#00ffff', '#ff0080', '#ffd700']  # cyan, magenta, gold

# Compute accelerations
def compute_accelerations(positions):
    acc = np.zeros_like(positions)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r) + 1e-5
                acc[i] += G * masses[j] * r / dist**3
    return acc

# Simulate motion
for _ in range(steps):
    for i in range(3):
        trajectories[i].append(positions[i].copy())
    acc = compute_accelerations(positions)
    velocities += acc * dt
    positions += velocities * dt

trajectories = [np.array(traj) for traj in trajectories]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lines = [ax.plot([], [], [], color=colors[i], label=f'Star {i+1}', linewidth=2)[0] for i in range(3)]
points = [ax.plot([], [], [], marker='o', color=colors[i], markersize=8)[0] for i in range(3)]
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('x-coordinate')
ax.set_ylabel('y-coordinate')
ax.set_zlabel('z-coordinate')
ax.set_title('Elon Musk Style 3-Body Problem Animation')
ax.legend()

trail_length = 200  # Number of points to show in the trail

def update(num):
    for i in range(3):
        start = max(0, num - trail_length)
        lines[i].set_data(trajectories[i][start:num, 0], trajectories[i][start:num, 1])
        lines[i].set_3d_properties(trajectories[i][start:num, 2])
        points[i].set_data(trajectories[i][num-1:num, 0], trajectories[i][num-1:num, 1])
        points[i].set_3d_properties(trajectories[i][num-1:num, 2])
    return lines + points

ani = FuncAnimation(fig, update, frames=steps, interval=10, blit=False)
plt.show() 