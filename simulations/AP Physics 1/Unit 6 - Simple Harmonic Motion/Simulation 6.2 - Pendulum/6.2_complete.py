glowscript VPython

# AP Physics 1 - Unit 6: Simple Harmonic Motion
# Simulation 6.2: The Simple Pendulum
#
# Complete Program

# SCENE & VISUALS
scene.title = "Simple Pendulum Motion"

pivot = vector(0, 5, 0)
pivot_marker = sphere(pos=pivot, radius=0.1, color=color.gray(0.5))
bob = sphere(radius=0.5, color=color.blue, make_trail=True)
rod = cylinder(pos=pivot, radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
bob.m = 1.0
rod.L = 4.0 # Length of the pendulum in meters

# Set the initial angle. Try a small one (e.g., 15) and a large one (e.g., 70)
# to see the effect on the period.
initial_angle_deg = 15
theta = radians(initial_angle_deg)
omega = 0 # Initial angular velocity (released from rest)

# Set initial position based on L and theta
bob.pos = pivot + vector(rod.L * sin(theta), -rod.L * cos(theta), 0)
rod.axis = bob.pos - pivot

# --- THEORETICAL CALCULATIONS ---
# The period using the small angle approximation (T = 2*pi*sqrt(L/g))
# This is only accurate for small angles!
T_small_angle = 2 * pi * sqrt(rod.L / g)

scene.caption = f"Initial Angle: {initial_angle_deg} degrees. Small Angle Approx. Period: {T_small_angle:.2f} s"

# --- GRAPHING SETUP ---
angle_graph = graph(title="Angle vs. Time", xtitle="Time (s)", ytitle="Angle (rad)")
angle_curve = gcurve(color=color.blue, label="Simulation Angle")

# ANIMATION LOOP
while t < 2 * T_small_angle: # Run for roughly two periods
    rate(100)
    
    # Calculate angular acceleration using the full formula (no approximation)
    # alpha = -(g / L) * sin(theta)
    alpha = -(g / rod.L) * sin(theta)
    
    # Update angular velocity and angle using kinematics
    omega = omega + alpha * dt
    theta = theta + omega * dt
    
    # Update the positions of the bob and rod based on the new angle
    bob.pos = pivot + vector(rod.L * sin(theta), -rod.L * cos(theta), 0)
    rod.axis = bob.pos - pivot
    
    # Plot the angle
    angle_curve.plot(t, theta)
    
    t = t + dt

# --- ANALYSIS ---
print("Simulation finished.")
print(f"Theoretical Period (Small Angle Approx): {T_small_angle:.2f} s")

# Find the measured period from the simulation data
peak_times = []
data = angle_curve.data
for i in range(1, len(data) - 1):
    # Find a peak by checking if a point is higher than its neighbors
    if data[i][1] > data[i-1][1] and data[i][1] > data[i+1][1]:
        peak_times.append(data[i][0])

if len(peak_times) >= 2:
    measured_period = peak_times[1] - peak_times[0]
    print(f"Measured Period from Graph: {measured_period:.2f} s")
    error = (abs(measured_period - T_small_angle) / T_small_angle) * 100
    print(f"Difference from small angle approx: {error:.2f}%")
else:
    print("Could not determine measured period from the graph.")

