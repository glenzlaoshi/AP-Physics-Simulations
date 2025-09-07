glowscript VPython

# AP Physics 1 - Unit 6: Simple Harmonic Motion
# Simulation 6.1: Mass on a Spring
#
# Intermediate Program

# VISUALS
wall = box(pos=vector(-10, 0, 0), size=vector(0.2, 4, 4), color=color.gray(0.7))
floor = box(pos=vector(0, -1.1, 0), size=vector(20, 0.2, 4), color=color.gray(0.7))
block = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.green)
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.5, coils=20, thickness=0.1, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
block.m = 2.0
spring.k = 10
spring.equilibrium_pos = vector(-4, 0, 0)

block.pos = vector(4, 0, 0)
block.velocity = vector(0, 0, 0)

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # Calculate the displacement from equilibrium
    x_vec = block.pos - spring.equilibrium_pos
    
    # Calculate the spring force using Hooke's Law
    F_spring = -spring.k * x_vec
    
    # Calculate acceleration from Newton's 2nd Law
    block.acceleration = F_spring / block.m
    
    # Update motion
    block.velocity = block.velocity + block.acceleration * dt
    block.pos = block.pos + block.velocity * dt
    
    # Update visuals and time
    spring.axis = block.pos - wall.pos
    t = t + dt


# --- STUDENT TASK: Analyze the Motion ---
# The block is oscillating, but how can we describe this motion?

# 1. GRAPH THE MOTION
#    - Before the loop, create a graph: `graph(xtitle='time', ytitle='position')`
#    - Before the loop, create a curve: `pos_curve = gcurve(color=color.green)`
#    - Inside the loop, plot the x-position vs. time: `pos_curve.plot(t, block.pos.x)`
#    - Run the simulation again. The graph shows the Simple Harmonic Motion!

# 2. MEASURE THE PERIOD (T)
#    - The period is the time for one full oscillation (e.g., from one peak to the next).
#    - Look at your graph. At what time is the first peak? At what time is the second peak?
#    - The difference between these times is the measured period of oscillation.

# 3. CALCULATE THE THEORETICAL PERIOD
#    - The formula for the period of a mass-spring system is T = 2 * pi * sqrt(m / k).
#    - Calculate this value using `block.m` and `spring.k`.
#    - Does your calculated period match the period you measured from the graph?

print("Simulation finished.")
