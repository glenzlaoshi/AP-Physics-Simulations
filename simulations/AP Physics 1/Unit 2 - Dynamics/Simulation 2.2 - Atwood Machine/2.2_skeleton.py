glowscript VPython

# AP Physics 1 - Unit 2: Dynamics
# Simulation 2.2: Atwood Machine
#
# Skeleton Program

# VISUALS
# The pulley is a cylinder
pulley = cylinder(pos=vector(0, 5, 0), axis=vector(0, 0, 1), radius=0.5, color=color.gray(0.7))

# The two masses (blocks)
mass1 = box(pos=vector(-2, 3, 0), size=vector(1, 1, 1), color=color.red)
mass2 = box(pos=vector(2, 1, 0), size=vector(1, 1, 1), color=color.blue)

# The strings connecting the masses to the pulley
string1 = cylinder(pos=mass1.pos + vector(0, 0.5, 0), axis=pulley.pos - mass1.pos - vector(0,0.5,0), radius=0.05, color=color.yellow)
string2 = cylinder(pos=mass2.pos + vector(0, 0.5, 0), axis=pulley.pos - mass2.pos - vector(0,0.5,0), radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

# --- STUDENT TASK 1: Define Masses ---
# Set the mass for each block in kg.
mass1.m = 2.0
mass2.m = 2.5 # Let's make mass2 heavier

# --- STUDENT TASK 2: Analyze the Physics ---
# The system will accelerate because the gravitational forces are unbalanced.
# Let's define the acceleration `a` as a scalar (a magnitude).
# If mass2 is heavier, it will accelerate downwards, and mass1 will accelerate upwards.

# 1. Write the net force equation for mass1 (vertical direction):
#    F_net1 = Tension - mass1.m * g = mass1.m * a

# 2. Write the net force equation for mass2 (vertical direction):
#    F_net2 = mass2.m * g - Tension = mass2.m * a

# 3. Solve these two equations for the acceleration, `a`.
#    (Hint: Add the two equations together to eliminate Tension).
#    You should get: a = g * (m2 - m1) / (m1 + m2)

# --- STUDENT TASK 3: Calculate Acceleration ---
# Use the formula you derived to calculate the magnitude of the acceleration.
# a = g * (mass2.m - mass1.m) / (mass1.m + mass2.m)

# Now, create acceleration vectors for each block.
# Remember, if `a` is positive, mass1 goes UP and mass2 goes DOWN.
# mass1.acceleration = vector(0, a, 0)
# mass2.acceleration = vector(0, -a, 0)

# Initialize velocity for both blocks
mass1.velocity = vector(0, 0, 0)
mass2.velocity = vector(0, 0, 0)

# ANIMATION LOOP
while t < 3:
    rate(100)
    
    # --- STUDENT TASK 4: Update Motion ---
    # Assuming you have calculated the acceleration vectors,
    # update the velocity and position for BOTH blocks.
    
    # For mass1:
    # mass1.velocity = mass1.velocity + mass1.acceleration * dt
    # mass1.pos = mass1.pos + mass1.velocity * dt
    
    # For mass2:
    # mass2.velocity = mass2.velocity + mass2.acceleration * dt
    # mass2.pos = mass2.pos + mass2.velocity * dt
    
    # Update the strings to follow the blocks
    # string1.pos = mass1.pos + vector(0, 0.5, 0)
    # string1.axis = pulley.pos - string1.pos
    # string2.pos = mass2.pos + vector(0, 0.5, 0)
    # string2.axis = pulley.pos - string2.pos
    
    # Update time
    # t = t + dt

print("Simulation finished.")
