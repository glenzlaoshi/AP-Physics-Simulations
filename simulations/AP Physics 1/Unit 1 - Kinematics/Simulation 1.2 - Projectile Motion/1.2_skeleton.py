glowscript VPython

# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.2: Projectile Motion
#
# Skeleton Program

# OBJECTS
# The ground is a large, flat box.
ground = box(pos=vector(0, -0.5, 0), size=vector(40, 0.1, 10), color=color.green)

# The projectile is a small sphere.
projectile = sphere(pos=vector(-18, 0, 0), radius=0.4, color=color.yellow)

# A trail will help visualize the path.
attach_trail(projectile, color=color.yellow, radius=0.05)

# PARAMETERS & INITIAL CONDITIONS
# Time parameters
t = 0
dt = 0.01

# Physics parameters
g = 9.8  # acceleration due to gravity

# --- STUDENT TASK 1: Set Initial Velocity and Angle ---
# The projectile is fired from the cannon.
# We need to define its initial speed (v0) and launch angle (theta).

v0 = 20  # initial speed, m/s
theta = radians(45) # launch angle, converted to radians

# --- STUDENT TASK 2: Calculate Initial Velocity Components ---
# The initial velocity is a vector. You need to calculate its x and y components
# from the speed (v0) and angle (theta).
# projectile.velocity = vector(v0 * cos(theta), v0 * sin(theta), 0)


# --- STUDENT TASK 3: Define Acceleration ---
# What is the acceleration of a projectile after it is launched?
# (Hint: It's constant and points downwards).
# projectile.acceleration = vector(0, -g, 0)


# ANIMATION LOOP
# The loop runs as long as the projectile is above the ground.
while projectile.pos.y >= 0:
    rate(100)
    
    # --- STUDENT TASK 4: Update Motion ---
    # Just like in the 1D motion simulation, you need to update the
    # projectile's velocity and position inside the loop.
    
    # 1. Update velocity
    # projectile.velocity = projectile.velocity + projectile.acceleration * dt
    
    # 2. Update position
    # projectile.pos = projectile.pos + projectile.velocity * dt
    
    # 3. Update time
    # t = t + dt


# --- END OF SIMULATION ---
print("Simulation finished.")
print(f"Total time in air: {t:.2f} s")
print(f"Horizontal range: {projectile.pos.x:.2f} m")
