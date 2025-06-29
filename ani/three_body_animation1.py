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
trail_length = 200  # Increased for longer, more dramatic trails

# Store trajectories as (position, velocity) pairs
trajectories = [[], [], []]

def compute_accelerations(positions):
    acc = np.zeros_like(positions)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = positions[j] - positions[i]
                acc[i] += G * masses[j] * r / (np.linalg.norm(r)**3 + 1e-5)
    return acc

# Simulate motion
for _ in range(steps):
    for i in range(3):
        trajectories[i].append((positions[i].copy(), velocities[i].copy()))
    acc = compute_accelerations(positions)
    velocities += acc * dt
    positions += velocities * dt

# Convert trajectories to arrays for easier slicing
trajectories = [np.array(traj) for traj in trajectories]

# Plotting setup
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
colors = ['#00FFFF', '#FF00FF', '#FFFF00']  # Cyan, Magenta, Yellow for a futuristic look

# Set space-like background
ax.w_xaxis.set_pane_color((0, 0, 0, 1))
ax.w_yaxis.set_pane_color((0, 0, 0, 1))
ax.w_zaxis.set_pane_color((0, 0, 0, 1))

# Add stars for depth
stars = np.random.uniform(-2, 2, (1000, 3))
ax.scatter(stars[:, 0], stars[:, 1], stars[:, 2], c='white', s=1, alpha=0.3)

# Initialize artists for trails, points, and velocity vectors
trail_artists = [None, None, None]
point_artists = [None, None, None]
quiver_artists = [None, None, None]

# Set axis limits and labels with futuristic styling
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X', fontsize=12, color='white')
ax.set_ylabel('Y', fontsize=12, color='white')
ax.set_zlabel('Z', fontsize=12, color='white')
ax.set_title('Super Elon Musk 3-Body Simulation', fontsize=14, pad=20, color='white')

# Time display with enhanced visibility
time_text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=14, color='white')

def update(num):
    for i in range(3):
        # Glowing trails with fading effect
        start = max(0, num - trail_length)
        if start < num:
            trail = trajectories[i][start:num]
            x = trail[:, 0, 0]
            y = trail[:, 0, 1]
            z = trail[:, 0, 2]
            ages = np.arange(len(x))
            alphas = (len(x) - ages) / float(len(x))
            if trail_artists[i] is not None:
                trail_artists[i].remove()
            trail_artists[i] = ax.scatter(x, y, z, c=[colors[i]]*len(x), alpha=alphas, s=2)
        
        # Current position and velocity vector
        if num > 0:
            pos, vel = trajectories[i][num-1]
            if point_artists[i] is not None:
                point_artists[i].remove()
            point_artists[i] = ax.scatter([pos[0]], [pos[1]], [pos[2]], c=colors[i], s=50)
            if quiver_artists[i] is not None:
                quiver_artists[i].remove()
            quiver_artists[i] = ax.quiver(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2], 
                                         color=colors[i], length=0.2, normalize=True)
    
    # Update time display
    time_text.set_text(f'Time: {num*dt:.2f} units')
    
    # Rotate camera for dynamic view
    ax.view_init(elev=30, azim=45 + num * 0.05)
    
    return trail_artists + point_artists + quiver_artists + [time_text]

# Create animation
ani = FuncAnimation(fig, update, frames=steps, interval=20, blit=False)

# Adjust layout
plt.tight_layout()
plt.show()