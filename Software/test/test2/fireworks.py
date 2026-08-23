# Python simulation of a fireworks burst (2D cross-section)
# - Simulates shell ascent, burst at apex, and ejection of N "stars"
# - Stars experience gravity and quadratic air drag (F = 0.5 * rho * Cd * A * v^2)
# - Integrates with simple RK4-like explicit method (semi-implicit Euler for stability)
# - Produces two plots: trajectories of many stars, and a snapshot of positions at a chosen time.
# Notes: matplotlib is used (no seaborn), each chart is a separate plot. No explicit colors/styles set.
import math, numpy as np
import matplotlib.pyplot as plt

# Physical constants and parameters
g = 9.81                      # m/s^2
rho = 1.225                   # kg/m^3 (air density at sea level)
Cd = 0.47                     # drag coefficient (sphere approx)
r_star = 0.008                # m (star radius ~8 mm)
A = math.pi * r_star**2       # cross-sectional area
m_star = 0.003                # kg (approx mass of a star)
N = 300                       # number of stars to simulate
u = 50.0                      # m/s radial ejection speed
burst_height = 120.0          # m (shell burst altitude)
shell_horizontal_offset = 0.0 # m, viewer directly under burst (for plotting convenience)

# Integration parameters
dt = 0.01                     # time step (s)
t_max = 6.0                   # simulate for 6 s after burst
steps = int(t_max / dt) + 1

# Generate random ejection angles uniformly on the circle (2D cross-section)
angles = np.random.uniform(0, 2*math.pi, size=N)
vel0 = np.column_stack((u * np.cos(angles), u * np.sin(angles)))  # initial velocities

# Initial positions: all at burst point (shell apex)
positions = np.zeros((N, 2))
positions[:, 0] = shell_horizontal_offset
positions[:, 1] = burst_height

# Preallocate arrays to store trajectories for plotting
trajectories_x = np.zeros((N, steps))
trajectories_y = np.zeros((N, steps))
trajectories_x[:, 0] = positions[:, 0]
trajectories_y[:, 0] = positions[:, 1]

# Velocities
vel = vel0.copy()

# Time integration loop (semi-implicit Euler for simplicity and stability)
for i in range(1, steps):
    speeds = np.linalg.norm(vel, axis=1)
    # Drag magnitude: 0.5 * rho * Cd * A * v^2
    drag_mag = 0.5 * rho * Cd * A * speeds**2
    # Avoid division by zero: when speed is zero, drag direction is zero
    drag_dir = np.zeros_like(vel)
    nonzero = speeds > 1e-8
    drag_dir[nonzero] = - (vel[nonzero].T / speeds[nonzero]).T  # unit vector opposite velocity
    # Acceleration from drag and gravity
    acc = (drag_dir * (drag_mag.reshape(-1,1) / m_star))
    acc[:,1] -= g  # gravity downwards
    
    # Semi-implicit Euler update
    vel += acc * dt
    positions += vel * dt
    
    # Store
    trajectories_x[:, i] = positions[:, 0]
    trajectories_y[:, i] = positions[:, 1]

# Plot 1: trajectories (x vs y)
plt.figure(figsize=(8,6))
for j in range(min(N, 200)):   # plot up to 200 trajectories for clarity
    plt.plot(trajectories_x[j,:], trajectories_y[j,:])
plt.xlabel('Horizontal distance (m)')
plt.ylabel('Altitude (m)')
plt.title('Trajectories of firework "stars" after burst (2D cross-section)')
plt.ylim(0, burst_height + 20)
plt.xlim(-burst_height, burst_height)
plt.axhline(0, linewidth=0.8)  # ground
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Plot 2: snapshot of star positions at t = 1.0 s after burst
snapshot_t = 1.0
idx = int(snapshot_t / dt)
plt.figure(figsize=(6,6))
plt.scatter(trajectories_x[:, idx], trajectories_y[:, idx], s=8)
plt.xlabel('Horizontal distance (m)')
plt.ylabel('Altitude (m)')
plt.title(f'Snapshot at t = {snapshot_t:.2f} s after burst (N={N})')
plt.ylim(0, burst_height + 20)
plt.xlim(-burst_height, burst_height)
plt.axhline(0, linewidth=0.8)  # ground
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Summary outputs for the user
max_altitudes = trajectories_y.max(axis=1)
mean_fall_time = np.mean([np.argmax(trajectories_y[j,:] <= 0) * dt if np.any(trajectories_y[j,:] <= 0) else np.nan for j in range(N)])
print(f"Simulated {N} stars, burst height = {burst_height} m, ejection speed = {u} m/s")
print(f"Mean time-to-ground for stars that hit ground within simulation: {mean_fall_time:.2f} s (NaN means didn't hit within {t_max}s)")
print("You can change parameters (N, u, burst_height, r_star, m_star, Cd) and rerun to explore effects.")
