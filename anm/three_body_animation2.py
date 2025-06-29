import numpy as np
import os
import time

# Simulation parameters
G = 1
dt = 0.02
steps = 10000

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

# Terminal grid size
W, H = 80, 24
trail_length = 30
trails = [[], [], []]

def compute_accelerations(positions):
    acc = np.zeros_like(positions)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r) + 1e-5
                acc[i] += G * masses[j] * r / dist**3
    return acc

for step in range(steps):
    # Store trails
    for i in range(3):
        trails[i].append(positions[i].copy())
        if len(trails[i]) > trail_length:
            trails[i].pop(0)
    acc = compute_accelerations(positions)
    velocities += acc * dt
    positions += velocities * dt

    # Project to 2D (x, y)
    grid = [[' ' for _ in range(W)] for _ in range(H)]
    for idx, trail in enumerate(trails):
        for tpos in trail[:-1]:
            x, y = int(W/2 + tpos[0]*20), int(H/2 + tpos[1]*10)
            if 0 <= x < W and 0 <= y < H:
                grid[y][x] = '.'
        # Draw current position
        x, y = int(W/2 + trails[idx][-1][0]*20), int(H/2 + trails[idx][-1][1]*10)
        if 0 <= x < W and 0 <= y < H:
            grid[y][x] = str(idx+1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(''.join(row) for row in grid))
    print("Step:", step)
    time.sleep(0.03) 