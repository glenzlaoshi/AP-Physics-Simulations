glowscript VPython

# AP Physics 1 - Unit 3: Circular Motion and Gravitation
# Simulation 3.2: Orbital Mechanics
#
# Skeleton Program

# VISUALS
# The central body (e.g., a planet)
planet = sphere(pos=vector(0,0,0), radius=1e6, color=color.blue)

# The orbiting body (e.g., a satellite)
satellite = sphere(pos=vector(5e6, 0, 0), radius=2e5, color=color.yellow, make_trail=True)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 10 # Time step can be larger for astronomical simulations

# Universal Gravitational Constant
G = 6.67e-11

# Mass properties
planet.m = 6e24  # Mass of the Earth
satellite.m = 1000 # Mass of a satellite

# --- STUDENT TASK 1: Set Initial Velocity ---
# For a stable circular orbit, the gravitational force must provide the exact
# centripetal force required. This leads to a specific required speed:
# v = sqrt(G * M / r)

# Let's calculate that speed.
radius = mag(satellite.pos)
# v_circular = sqrt(G * planet.m / radius)

# The initial velocity should be tangential (in the y-direction).
# satellite.velocity = vector(0, v_circular, 0)

# What happens if the velocity is too slow or too fast? Try changing it!
# satellite.velocity = vector(0, v_circular * 0.7, 0) # Too slow
# satellite.velocity = vector(0, v_circular * 1.3, 0) # Too fast (elliptical)


# ANIMATION LOOP
while t < 50000:
    rate(200)
    
    # --- STUDENT TASK 2: Calculate Gravitational Force ---
    # The force of gravity is F = -G * M * m / r^2, in the direction of r_hat.
    
    # 1. Find the vector from the satellite to the planet.
    # r_vector = planet.pos - satellite.pos
    
    # 2. Find the magnitude of that vector (the distance r).
    # r_mag = mag(r_vector)
    
    # 3. Find the unit vector for the direction.
    # r_hat = norm(r_vector)
    
    # 4. Calculate the force magnitude.
    # F_mag = G * planet.m * satellite.m / r_mag**2
    
    # 5. Combine magnitude and direction to get the force vector.
    # F_gravity = F_mag * r_hat
    
    
    # --- STUDENT TASK 3: Update Motion ---
    # Once you have the force, use Newton's 2nd Law and kinematics.
    
    # 1. Calculate acceleration: a = F / m
    # satellite.acceleration = F_gravity / satellite.m
    
    # 2. Update velocity.
    # satellite.velocity = satellite.velocity + satellite.acceleration * dt
    
    # 3. Update position.
    # satellite.pos = satellite.pos + satellite.velocity * dt
    
    # 4. Update time.
    # t = t + dt


print("Simulation finished.")
