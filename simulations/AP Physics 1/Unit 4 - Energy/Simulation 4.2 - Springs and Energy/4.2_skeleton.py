glowscript VPython

# AP Physics 1 - Unit 4: Energy
# Simulation 4.2: Springs and Energy
#
# Skeleton Program

# VISUALS
# A wall to anchor the spring
wall = box(pos=vector(-10, 0, 0), size=vector(0.2, 4, 4), color=color.gray(0.7))

# A block attached to the spring
block = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.cyan)

# The spring itself
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.5, coils=20, thickness=0.1, color=color.orange)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

block.m = 1.0 # Mass of the block
spring.k = 15 # Spring constant (N/m)

# The position where the spring is neither stretched nor compressed
spring.equilibrium_pos = vector(-4, 0, 0)

# --- STUDENT TASK 1: Set Initial State ---
# Let's pull the block to a starting position and release it from rest.
block.pos = vector(2, 0, 0)
block.velocity = vector(0, 0, 0)

# --- STUDENT TASK 2: Calculate Total Energy ---
# The total mechanical energy is E = KE + PE_spring.
# At the start, the block is at rest, so KE = 0.

# 1. Calculate the initial displacement of the spring from equilibrium.
#    x_vector = block.pos - spring.equilibrium_pos
#    x_mag = mag(x_vector)

# 2. Calculate the initial Spring Potential Energy (PE_spring).
#    PE_spring = 0.5 * k * x^2
#    initial_PE = 0.5 * spring.k * x_mag**2

# 3. The total energy is equal to the initial potential energy.
#    total_energy = initial_PE
#    This total energy should remain constant!


# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 3: Apply Energy Conservation ---
    # At any point, Total Energy = PE_spring + KE.
    
    # 1. Calculate the current displacement `x` and PE_spring.
    #    x_vector = block.pos - spring.equilibrium_pos
    #    x_mag = mag(x_vector)
    #    current_PE = 0.5 * spring.k * x_mag**2
    
    # 2. Calculate the current Kinetic Energy (KE).
    #    current_KE = total_energy - current_PE
    
    # 3. From KE, find the block's speed.
    #    speed = sqrt(2 * current_KE / block.m)
    
    # 4. Determine the direction of velocity. The block moves towards equilibrium
    #    if stretched, and away from it if it's on the other side.
    #    This is tricky! An easier way is to use forces (see SHM unit).
    #    For now, let's use a trick: we know the direction must be along the x-axis.
    #    We can use the force direction `F = -k*x` to find the acceleration direction.
    
    # --- Let's switch to using forces, which is more direct for this problem ---
    
    # 1. Calculate the force vector: F = -k * x
    #    x_vector = block.pos - spring.equilibrium_pos
    #    F_spring = -spring.k * x_vector
    
    # 2. Calculate acceleration: a = F / m
    #    block.acceleration = F_spring / block.m
    
    # 3. Update velocity and position.
    #    block.velocity = block.velocity + block.acceleration * dt
    #    block.pos = block.pos + block.velocity * dt
    
    # 4. Update the spring's appearance and time.
    #    spring.axis = block.pos - wall.pos
    #    t = t + dt

print("Simulation finished.")
