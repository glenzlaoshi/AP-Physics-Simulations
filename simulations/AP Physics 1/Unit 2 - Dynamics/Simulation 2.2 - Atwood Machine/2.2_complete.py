glowscript VPython

# AP Physics 1 - Unit 2: Dynamics
# Simulation 2.2: Atwood Machine
#
# Complete Program

# SCENE & VISUALS
scene.title = "Atwood Machine"
scene.caption = "Two masses are connected by a string over a frictionless pulley."

pulley = cylinder(pos=vector(0, 5, 0), axis=vector(0, 0, 1), radius=0.5, color=color.gray(0.7))

# The two masses (blocks)
mass1 = box(pos=vector(-2, 3, 0), size=vector(1, 1, 1), color=color.red)
mass2 = box(pos=vector(2, 1, 0), size=vector(1, 1, 1), color=color.blue)

# The strings connecting the masses to the pulley
string1 = cylinder(radius=0.05, color=color.yellow)
string2 = cylinder(radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

# Define the mass properties for each block
mass1.m = 4.0
mass2.m = 4.5

print(f"Mass 1 (red): {mass1.m} kg")
print(f"Mass 2 (blue): {mass2.m} kg")

# PHYSICS CALCULATIONS
# Calculate the magnitude of the system's acceleration
# a = g * (m_heavier - m_lighter) / (m_total)
a_mag = g * (mass2.m - mass1.m) / (mass1.m + mass2.m)

print(f"Theoretical acceleration: {a_mag:.2f} m/s^2")

# Create acceleration vectors for each block based on the calculated magnitude.
# Mass1 (lighter) accelerates upwards.
mass1.acceleration = vector(0, a_mag, 0)
# Mass2 (heavier) accelerates downwards.
mass2.acceleration = vector(0, -a_mag, 0)

# Set initial velocities
mass1.velocity = vector(0, 0, 0)
mass2.velocity = vector(0, 0, 0)

# GRAPHING SETUP
graph_window = graph(title='Position vs. Time', xtitle='Time (s)', ytitle='Height (m)')
pos1_curve = gcurve(color=mass1.color, label=f"Mass 1 ({mass1.m} kg)")
pos2_curve = gcurve(color=mass2.color, label=f"Mass 2 ({mass2.m} kg)")

# ANIMATION LOOP
while t < 3.5:
    rate(100)
    
    # Update velocities
    mass1.velocity = mass1.velocity + mass1.acceleration * dt
    mass2.velocity = mass2.velocity + mass2.acceleration * dt
    
    # Update positions
    mass1.pos = mass1.pos + mass1.velocity * dt
    mass2.pos = mass2.pos + mass2.velocity * dt
    
    # Update the strings to follow the blocks
    string1.pos = mass1.pos + vector(0, 0.5, 0)
    string1.axis = pulley.pos - string1.pos
    string2.pos = mass2.pos + vector(0, 0.5, 0)
    string2.axis = pulley.pos - string2.pos
    
    # Plot the vertical position (y-component) of each mass
    pos1_curve.plot(t, mass1.pos.y)
    pos2_curve.plot(t, mass2.pos.y)
    
    # Update time
    t = t + dt

print("Simulation finished.")
print(f"Final velocity of mass 1: {mass1.velocity.y:.2f} m/s")
print(f"Final velocity of mass 2: {mass2.velocity.y:.2f} m/s")
