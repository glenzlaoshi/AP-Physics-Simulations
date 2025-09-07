glowscript VPython

# AP Physics 2 - Unit 5: Magnetism & Electromagnetism
# Simulation 5.1: Charged Particle in a B-Field
#
# Skeleton Program

# --- SETUP ---
# Create a region of uniform magnetic field pointing in the +z direction (out of the screen)
B_field_mag = 0.5 # Tesla
B_field_vec = vector(0, 0, B_field_mag)

# Visualize the B-field with a grid of arrows
for x in arange(-5, 5.1, 2):
    for y in arange(-5, 5.1, 2):
        arrow(pos=vector(x,y,-5), axis=vector(0,0,2), color=color.cyan, shaftwidth=0.05)

# --- PARTICLE ---
# Create a charged particle
particle = sphere(pos=vector(-5, 0, 0), radius=0.2, color=color.yellow, make_trail=True)

# Particle properties
particle.m = 1.67e-27 # Mass of a proton
particle.q = 1.6e-19  # Charge of a proton

# Give it an initial velocity perpendicular to the B-field
particle.velocity = vector(0, 2e5, 0) # 2.0 x 10^5 m/s

# --- SIMULATION ---
t = 0
dt = 1e-9 # Time step needs to be very small for this simulation

# ANIMATION LOOP
while t < 1e-6:
    rate(200)
    
    # --- STUDENT TASK 1: Calculate the Magnetic Force ---
    # The magnetic force is given by the Lorentz Force Law: F = q * (v x B)
    # where `v x B` is the cross product of the velocity and B-field vectors.
    
    # 1. Calculate the cross product.
    #    v_cross_B = cross(particle.velocity, B_field_vec)
    
    # 2. Calculate the force vector.
    #    F_mag = particle.q * v_cross_B
    
    
    # --- STUDENT TASK 2: Update Motion ---
    # This is the same as in previous dynamics simulations.
    
    # 1. Calculate acceleration: a = F / m
    #    particle.acceleration = F_mag / particle.m
    
    # 2. Update velocity.
    #    particle.velocity = particle.velocity + particle.acceleration * dt
    
    # 3. Update position.
    #    particle.pos = particle.pos + particle.velocity * dt
    
    # 4. Update time.
    #    t = t + dt


# --- STUDENT TASK 3: Analysis ---
# What kind of path does the particle follow? Why?
# The force is always perpendicular to the velocity. What does this mean for the particle's speed?
# Does the magnetic force do work on the particle?

print("Simulation finished.")
