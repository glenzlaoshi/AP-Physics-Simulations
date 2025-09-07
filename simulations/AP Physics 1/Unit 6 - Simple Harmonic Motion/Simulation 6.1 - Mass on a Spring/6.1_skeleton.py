glowscript VPython

# AP Physics 1 - Unit 6: Simple Harmonic Motion
# Simulation 6.1: Mass on a Spring
#
# Skeleton Program

# This setup is very similar to the energy simulation (4.2),
# but our focus now is on the oscillatory motion itself.

# VISUALS
wall = box(pos=vector(-10, 0, 0), size=vector(0.2, 4, 4), color=color.gray(0.7))
floor = box(pos=vector(0, -1.1, 0), size=vector(20, 0.2, 4), color=color.gray(0.7))
block = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.green)
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.5, coils=20, thickness=0.1, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

block.m = 2.0 # Mass
spring.k = 10 # Spring constant

# The position where the net force on the block is zero.
spring.equilibrium_pos = vector(-4, 0, 0)

# Set the initial position of the block (stretched from equilibrium) and release from rest.
block.pos = vector(4, 0, 0)
block.velocity = vector(0, 0, 0)

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate the Force ---
    # The force that causes the oscillation is the spring force.
    # It is described by Hooke's Law: F = -k*x
    # where `x` is the displacement vector from the equilibrium position.
    
    # 1. Calculate the displacement vector, `x_vec`.
    #    x_vec = block.pos - spring.equilibrium_pos
    
    # 2. Calculate the spring force vector, `F_spring`.
    #    F_spring = -spring.k * x_vec
    
    
    # --- STUDENT TASK 2: Calculate Acceleration ---
    # Use Newton's Second Law, a = F_net / m.
    # Here, the net force is just the spring force.
    # block.acceleration = F_spring / block.m
    
    
    # --- STUDENT TASK 3: Update Motion ---
    # Use the standard kinematic updates.
    # block.velocity = block.velocity + block.acceleration * dt
    # block.pos = block.pos + block.velocity * dt
    
    
    # --- STUDENT TASK 4: Update Visuals and Time ---
    # Make the spring stretch and compress with the block.
    # spring.axis = block.pos - wall.pos
    # t = t + dt


print("Simulation finished.")
