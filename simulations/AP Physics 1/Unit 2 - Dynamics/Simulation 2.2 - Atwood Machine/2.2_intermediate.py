glowscript VPython

# AP Physics 1 - Unit 2: Dynamics
# Simulation 2.2: Atwood Machine
#
# Intermediate Program

# VISUALS
pulley = cylinder(pos=vector(0, 5, 0), axis=vector(0, 0, 1), radius=0.5, color=color.gray(0.7))
mass1 = box(pos=vector(-2, 3, 0), size=vector(1, 1, 1), color=color.red)
mass2 = box(pos=vector(2, 1, 0), size=vector(1, 1, 1), color=color.blue)
string1 = cylinder(pos=mass1.pos + vector(0, 0.5, 0), axis=pulley.pos - mass1.pos - vector(0,0.5,0), radius=0.05, color=color.yellow)
string2 = cylinder(pos=mass2.pos + vector(0, 0.5, 0), axis=pulley.pos - mass2.pos - vector(0,0.5,0), radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

mass1.m = 2.0
mass2.m = 2.5

print(f"Mass 1 (red): {mass1.m} kg")
print(f"Mass 2 (blue): {mass2.m} kg")

# --- STUDENT TASK 1: Calculate Acceleration ---
# For an Atwood machine, the acceleration of the system is given by:
# a = g * (m_heavier - m_lighter) / (m_total)

# Calculate the magnitude of the acceleration using the formula above.
# a_mag = g * (mass2.m - mass1.m) / (mass1.m + mass2.m)

# For now, let's use a placeholder value.
a_mag = 1.0 # Replace this with your calculation!

# --- STUDENT TASK 2: Define Acceleration Vectors ---
# Based on the scalar acceleration `a_mag`, create the acceleration VECTORS.
# The heavier mass (mass2) accelerates down, the lighter mass (mass1) accelerates up.

# mass1.acceleration = vector(0, a_mag, 0)
# mass2.acceleration = vector(0, -a_mag, 0)

# Initialize placeholder vectors
mass1.acceleration = vector(0,0,0)
mass2.acceleration = vector(0,0,0)

mass1.velocity = vector(0, 0, 0)
mass2.velocity = vector(0, 0, 0)

# ANIMATION LOOP
while t < 3:
    rate(100)
    
    # --- STUDENT TASK 3: UNCOMMENT THE UPDATE CODE ---
    # Once you have defined the acceleration vectors, uncomment the following lines.
    
    # Update velocities
    # mass1.velocity = mass1.velocity + mass1.acceleration * dt
    # mass2.velocity = mass2.velocity + mass2.acceleration * dt
    
    # Update positions
    # mass1.pos = mass1.pos + mass1.velocity * dt
    # mass2.pos = mass2.pos + mass2.velocity * dt
    
    # Update strings
    # string1.pos = mass1.pos + vector(0, 0.5, 0)
    # string1.axis = pulley.pos - string1.pos
    # string2.pos = mass2.pos + vector(0, 0.5, 0)
    # string2.axis = pulley.pos - string2.pos
    
    # Update time
    # t = t + dt

print("Simulation finished.")
