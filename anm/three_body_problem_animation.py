import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Gravitational constant (arbitrary units)
G = 1

# Initial positions (x, y, z) and velocities (vx, vy, vz) for 3 bodies
masses = np.array([1, 1, 1])
positions = np.array([
    [0.970, 0, 0],
    [-0.485, 0.841, 0],
    [-0.485, -0.841, 0]
], dtype=float)
velocities = np.array([
    [0, 0.5, 0.3],
    [0, -0.25, -0.4],
    [0, -0.25, 0.1]
], dtype=float)

# Simulation parameters
dt = 0.01
steps = 2000

# Store trajectories for each body
trajectories = [[], [], []]

def compute_accelerations(positions):
    """Compute gravitational accelerations for each body."""
    acc = np.zeros_like(positions)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r) + 1e-5  # Avoid division by zero
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
colors = ['b', 'r', 'y']
lines = [ax.plot([], [], [], color=colors[i], label=f'Star {i+1}')[0] for i in range(3)]
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('x-coordinate')
ax.set_ylabel('y-coordinate')
ax.set_zlabel('z-coordinate')
ax.set_title('Visualization of orbits of stars in a 3-body system')
ax.legend()

def update(num):
    for i in range(3):
        lines[i].set_data(trajectories[i][:num, 0], trajectories[i][:num, 1])
        lines[i].set_3d_properties(trajectories[i][:num, 2])
    return lines

ani = FuncAnimation(fig, update, frames=steps, interval=10, blit=False)
plt.show() 