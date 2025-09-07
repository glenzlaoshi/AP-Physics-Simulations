glowscript VPython

# AP Physics 1 - Unit 4: Energy
# Simulation 4.2: Springs and Energy
#
# Intermediate Program

# VISUALS
wall = box(pos=vector(-10, 0, 0), size=vector(0.2, 4, 4), color=color.gray(0.7))
block = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.cyan)
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.5, coils=20, thickness=0.1, color=color.orange)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
block.m = 1.0
spring.k = 15
spring.equilibrium_pos = vector(-4, 0, 0)

# Start the block stretched from equilibrium and release from rest.
block.pos = vector(2, 0, 0)
block.velocity = vector(0, 0, 0)

# Calculate total energy of the system.
x_mag = mag(block.pos - spring.equilibrium_pos)
initial_PE = 0.5 * spring.k * x_mag**2
total_energy = initial_PE

print(f"Spring constant k = {spring.k} N/m")
print(f"Initial stretch = {x_mag:.2f} m")
print(f"Total energy = {total_energy:.2f} J")

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate Forces ---
    # We will use dynamics (forces) to drive the motion, and then we will
    # verify that energy is conserved by calculating PE and KE.
    
    # 1. Calculate the displacement vector `x` from equilibrium.
    #    x_vector = block.pos - spring.equilibrium_pos
    
    # 2. Calculate the spring force vector using Hooke's Law (F = -kx).
    #    F_spring = -spring.k * x_vector
    
    # 3. Calculate acceleration using Newton's 2nd Law (a = F/m).
    #    block.acceleration = F_spring / block.m
    
    # For now, use a placeholder for acceleration.
    block.acceleration = vector(0,0,0)

    # --- STUDENT TASK 2: Update Motion ---
    # Uncomment these lines once you have calculated `block.acceleration`.
    # block.velocity = block.velocity + block.acceleration * dt
    # block.pos = block.pos + block.velocity * dt
    
    # Update the spring's visual representation
    spring.axis = block.pos - wall.pos
    
    # --- STUDENT TASK 3: Verify Energy Conservation ---
    # Inside the loop, calculate the current PE and KE and print them.
    # Do they add up to the `total_energy` you calculated at the start?
    
    # current_PE = 0.5 * spring.k * mag(block.pos - spring.equilibrium_pos)**2
    # current_KE = 0.5 * block.m * mag(block.velocity)**2
    # print(f"PE: {current_PE:.2f} J, KE: {current_KE:.2f} J, Total: {current_PE + current_KE:.2f} J")
    
    t = t + dt

print("Simulation finished.")
