glowscript VPython

# AP Physics 1 - Unit 3: Circular Motion and Gravitation
# Simulation 3.2: Orbital Mechanics
#
# Intermediate Program

# VISUALS
planet = sphere(pos=vector(0,0,0), radius=1e6, color=color.blue)
satellite = sphere(pos=vector(5e6, 0, 0), radius=2e5, color=color.yellow, make_trail=True)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 10
G = 6.67e-11
planet.m = 6e24
satellite.m = 1000

# Set initial velocity for a stable circular orbit
radius = mag(satellite.pos)
v_circular = sqrt(G * planet.m / radius)
satellite.velocity = vector(0, v_circular, 0)

print(f"Required speed for circular orbit: {v_circular:.2f} m/s")

# ANIMATION LOOP
# Let's run it for one full orbit period.
# T = 2 * pi * r / v
period = 2 * pi * radius / v_circular

while t < period:
    rate(200)
    
    # --- Physics Calculations ---
    # Vector from satellite to planet
    r_vector = planet.pos - satellite.pos
    # Distance r
    r_mag = mag(r_vector)
    # Direction unit vector
    r_hat = norm(r_vector)
    
    # Force of gravity magnitude
    F_mag = G * planet.m * satellite.m / r_mag**2
    # Force of gravity vector
    F_gravity = F_mag * r_hat
    
    # --- STUDENT TASK 1: Update Motion ---
    # Now that you have the force vector `F_gravity`, you can find the
    # satellite's acceleration and update its motion.
    
    # 1. Calculate acceleration using Newton's 2nd Law (a = F/m).
    #    Remember to use the satellite's mass!
    # satellite.acceleration = F_gravity / satellite.m
    
    # 2. Update velocity and position using the kinematic equations.
    # satellite.velocity = satellite.velocity + satellite.acceleration * dt
    # satellite.pos = satellite.pos + satellite.velocity * dt
    
    # 3. Update time.
    # t = t + dt


# --- STUDENT TASK 2: Experiment ---
# What happens if you change the initial velocity?
# Go back to the top and try setting:
# satellite.velocity = vector(0, v_circular * 0.7, 0) # Too slow
# satellite.velocity = vector(0, v_circular * 1.4, 0) # Too fast
# Does the simulation behave as you expect?

print("Simulation finished.")
