glowscript VPython

# AP Physics 1 - Unit 6: Simple Harmonic Motion
# Simulation 6.2: The Simple Pendulum
#
# Skeleton Program

# VISUALS
# The pivot point for the pendulum
pivot = vector(0, 5, 0)
pivot_marker = sphere(pos=pivot, radius=0.1, color=color.gray(0.5))

# The pendulum bob (the mass at the end)
bob = sphere(pos=pivot + vector(3, -4, 0), radius=0.5, color=color.blue)

# The rod connecting the pivot to the bob
rod = cylinder(pos=pivot, axis=bob.pos - pivot, radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

bob.m = 1.0 # Mass of the bob
rod.L = mag(rod.axis) # Length of the pendulum

# --- STUDENT TASK 1: Set Initial Conditions ---
# We define the pendulum's state by its angle `theta` from the vertical.
# Let's start it at a small angle (e.g., 15 degrees) and release from rest.
# theta = radians(15)

# The angular velocity `omega` is initially zero because it's released from rest.
# omega = 0

# The angular acceleration `alpha` will be calculated in the loop.
# alpha = 0


# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 2: Calculate Angular Acceleration (alpha) ---
    # For a pendulum, the restoring force is the tangential component of gravity:
    # F_restore = -m * g * sin(theta)
    # The torque is tau = F_restore * L
    # From Newton's 2nd Law for rotation, tau = I * alpha, where I = m * L^2 for a simple pendulum.
    # So, (-m * g * sin(theta)) * L = (m * L^2) * alpha
    # Solving for alpha gives: alpha = -(g / L) * sin(theta)
    
    # 1. Calculate alpha using the formula above.
    # alpha = -(g / rod.L) * sin(theta)
    
    
    # --- STUDENT TASK 3: Update Angular Motion ---
    # Use rotational kinematic equations.
    
    # 1. Update angular velocity.
    # omega = omega + alpha * dt
    
    # 2. Update the angle.
    # theta = theta + omega * dt
    
    
    # --- STUDENT TASK 4: Update Visuals and Time ---
    # Update the bob's position based on the new angle `theta`.
    # The position is determined by L and theta.
    # bob.pos = pivot + vector(rod.L * sin(theta), -rod.L * cos(theta), 0)
    
    # Update the rod.
    # rod.axis = bob.pos - pivot
    
    # Update time.
    # t = t + dt


print("Simulation finished.")
