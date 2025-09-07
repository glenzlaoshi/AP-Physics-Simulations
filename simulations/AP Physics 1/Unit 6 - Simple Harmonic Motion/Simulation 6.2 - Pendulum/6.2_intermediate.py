glowscript VPython

# AP Physics 1 - Unit 6: Simple Harmonic Motion
# Simulation 6.2: The Simple Pendulum
#
# Intermediate Program

# VISUALS
pivot = vector(0, 5, 0)
pivot_marker = sphere(pos=pivot, radius=0.1, color=color.gray(0.5))
bob = sphere(radius=0.5, color=color.blue)
rod = cylinder(pos=pivot, radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
bob.m = 1.0
rod.L = 4.0 # Set a fixed length for the pendulum

# Start the pendulum at a 20-degree angle from the vertical, at rest.
theta = radians(20)
omega = 0 # angular velocity

# Set initial position based on L and theta
bob.pos = pivot + vector(rod.L * sin(theta), -rod.L * cos(theta), 0)
rod.axis = bob.pos - pivot

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # The angular acceleration `alpha` depends on the current angle `theta`.
    # For a pendulum, alpha = -(g / L) * sin(theta).
    alpha = -(g / rod.L) * sin(theta)
    
    # Update the angular velocity and angle
    omega = omega + alpha * dt
    theta = theta + omega * dt
    
    # Update the positions of the bob and rod based on the new angle
    bob.pos = pivot + vector(rod.L * sin(theta), -rod.L * cos(theta), 0)
    rod.axis = bob.pos - pivot
    
    t = t + dt

# --- STUDENT TASK: Analyze the Motion ---
# The pendulum is swinging. Is this Simple Harmonic Motion?
# SHM occurs when the restoring force is proportional to displacement. For a pendulum,
# F = -mg*sin(theta). This is only proportional to theta when sin(theta) is close to theta,
# which is true for small angles.

# 1. GRAPH THE MOTION
#    - Before the loop, set up a graph: `graph(xtitle='time', ytitle='angle (rad)')`
#    - Before the loop, create a curve: `angle_curve = gcurve(color=color.blue)`
#    - Inside the loop, plot the angle vs. time: `angle_curve.plot(t, theta)`
#    - The graph should look sinusoidal, which is the hallmark of SHM.

# 2. MEASURE THE PERIOD (T)
#    - Look at your graph and find the time between two consecutive peaks.

# 3. CALCULATE THE THEORETICAL PERIOD (Small Angle Approximation)
#    - The formula for a simple pendulum at small angles is T = 2 * pi * sqrt(L / g).
#    - Calculate this value using `rod.L` and `g`.
#    - How does it compare to your measured period?

# 4. TEST THE APPROXIMATION
#    - Go back to the top and change the initial angle to something large, like 80 degrees.
#    - Rerun the simulation. Does the calculated theoretical period still match the measured period?

print("Simulation finished.")
