glowscript VPython

# AP Physics 1 - Unit 6: Simple Harmonic Motion
# Simulation 6.1: Mass on a Spring
#
# Complete Program

# SCENE & VISUALS
scene.title = "Simple Harmonic Motion: Mass-Spring System"

wall = box(pos=vector(-10, 0, 0), size=vector(0.2, 4, 4), color=color.gray(0.7))
floor = box(pos=vector(0, -1.1, 0), size=vector(20, 0.2, 4), color=color.gray(0.7))
block = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.green)
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.5, coils=20, thickness=0.1, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

block.m = 2.0 # Mass (kg)
spring.k = 10 # Spring constant (N/m)

# The position where the net force on the block is zero.
spring.equilibrium_pos = vector(-4, 0, 0)
eq_marker = cylinder(pos=spring.equilibrium_pos + vector(0,-1,0), axis=vector(0,-0.5,0), radius=0.1, color=color.white)

# Set the initial position of the block (amplitude of oscillation) and release from rest.
initial_pos = vector(4, 0, 0)
block.pos = initial_pos
block.velocity = vector(0, 0, 0)

# --- THEORETICAL CALCULATIONS ---
# Calculate the theoretical period of oscillation
T_theory = 2 * pi * sqrt(block.m / spring.k)
# Calculate the theoretical angular frequency
omega_theory = sqrt(spring.k / block.m)

scene.caption = f"The plot shows the block's position vs. time. The motion should be sinusoidal.\nTheoretical Period T = 2*pi*sqrt(m/k) = {T_theory:.2f} s"

# --- GRAPHING SETUP ---
pos_graph = graph(title="Position vs. Time", xtitle="Time (s)", ytitle="Position (m)")
pos_curve = gcurve(color=color.green, label="x-position")
# Also plot the analytical solution to compare: x(t) = A*cos(omega*t)
A = initial_pos.x - spring.equilibrium_pos.x # Amplitude
analytical_curve = gcurve(color=color.black, label="A*cos(omega*t)", linestyle='dotted')

# ANIMATION LOOP
while t < (2 * T_theory): # Run for two full periods
    rate(100)
    
    # Calculate the displacement vector from equilibrium
    x_vec = block.pos - spring.equilibrium_pos
    
    # Calculate the spring force using Hooke's Law (F = -kx)
    F_spring = -spring.k * x_vec
    
    # Calculate acceleration from Newton's 2nd Law (a = F/m)
    block.acceleration = F_spring / block.m
    
    # Update motion using standard kinematics
    block.velocity = block.velocity + block.acceleration * dt
    block.pos = block.pos + block.velocity * dt
    
    # Update visuals
    spring.axis = block.pos - wall.pos
    
    # Plot data
    pos_curve.plot(t, block.pos.x)
    # Plot the ideal theoretical position for comparison
    analytical_pos = spring.equilibrium_pos.x + A * cos(omega_theory * t)
    analytical_curve.plot(t, analytical_pos)
    
    # Update time
    t = t + dt

print("Simulation finished.")
# Find the period from the simulation data by finding time between peaks
# This is a simple way to do it for this specific case
peak_times = pos_curve.data # list of (t, y) tuples
first_peak_t = peak_times[0][0]
# Find the next peak
for i in range(1, len(peak_times)):
    # if the slope changes from positive to negative, it's a peak
    if peak_times[i][1] < peak_times[i-1][1] and peak_times[i-2][1] < peak_times[i-1][1]:
        second_peak_t = peak_times[i-1][0]
        measured_period = second_peak_t - first_peak_t
        print(f"Measured Period from graph: {measured_period:.2f} s")
        break

print(f"Theoretical Period: {T_theory:.2f} s")
