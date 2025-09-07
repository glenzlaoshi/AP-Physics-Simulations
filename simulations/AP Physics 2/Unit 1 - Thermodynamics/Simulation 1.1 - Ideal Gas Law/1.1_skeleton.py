glowscript VPython

# AP Physics 2 - Unit 2: Thermodynamics
# Simulation 2.1: Ideal Gas Law
#
# Skeleton Program

# VISUALS
# A containing box
L = 5.0 # Side length of the box
container = box(pos=vector(0,0,0), size=vector(L,L,L), color=color.white, opacity=0.2)

# PARAMETERS
N = 50  # Number of particles
m = 1.0   # Mass of each particle
k = 1.38e-23 # Boltzmann constant (for reference, not used directly yet)

# --- STUDENT TASK 1: Create the Gas Particles ---
# We need to create N spheres and store them in a list.

# particles = []
# for i in range(N):
#     # Create a sphere with a random initial position inside the container.
#     particle_pos = vector.random() * L/2
#     p = sphere(pos=particle_pos, radius=0.1, color=color.red)
#     
#     # Give it a random initial velocity.
#     # The magnitude of the velocity is related to temperature.
#     temp = 300 # Kelvin
#     v_mag = sqrt(3 * k * temp / m) # This is the RMS speed, a good starting point
#     p.velocity = vector.random() * v_mag
#     
#     # Add the new particle to our list.
#     particles.append(p)


# ANIMATION LOOP
t = 0
dt = 0.001

while t < 10:
    rate(200)
    
    # --- STUDENT TASK 2: Move the Particles ---
    # Loop through all the particles in your list.
    # for p in particles:
    #     p.pos = p.pos + p.velocity * dt
    
    
    # --- STUDENT TASK 3: Handle Wall Collisions ---
    # For each particle, check if it has hit a wall.
    # If a particle's position (e.g., p.pos.x) exceeds the boundary (L/2),
    # it has hit a wall.
    
    # for p in particles:
    #     # Check for collision with left/right walls
    #     if abs(p.pos.x) > L/2:
    #         # Reverse the x-component of velocity
    #         p.velocity.x = -p.velocity.x
    #     
    #     # Check for collision with top/bottom walls
    #     if abs(p.pos.y) > L/2:
    #         # Reverse the y-component of velocity
    #         p.velocity.y = -p.velocity.y
    #     
    #     # Check for collision with front/back walls
    #     if abs(p.pos.z) > L/2:
    #         # Reverse the z-component of velocity
    #         p.velocity.z = -p.velocity.z
    
    # t = t + dt

print("Simulation finished.")
