glowscript VPython

# AP Physics 1 - Unit 4: Energy
# Simulation 4.1: Conservation of Energy (Roller Coaster)
#
# Skeleton Program

# VISUALS
# The track is a curved path. We can define it with a function.
def track_path(x):
    """Defines the y-position of the track at a given x-position."""
    # A simple path with two hills
    return 5 * cos(0.2 * x) + 5

# Draw the track using a series of small cylinders
for x_pos in arange(-20, 20, 0.2):
    cylinder(pos=vector(x_pos, track_path(x_pos), 0), axis=vector(0.2, track_path(x_pos+0.2) - track_path(x_pos), 0), radius=0.2, color=color.gray(0.6))

# The roller coaster cart
cart = sphere(radius=0.5, color=color.red, make_trail=True)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
cart.m = 1.0

# --- STUDENT TASK 1: Set Initial State ---
# Place the cart at the top of the first hill, starting from rest.
cart.pos = vector(-16, track_path(-16), 0)
cart.velocity = vector(0, 0, 0)

# --- STUDENT TASK 2: Calculate Total Energy ---
# The total mechanical energy of the system is E = KE + PE.
# At the start, the cart is at rest, so KE = 0.

# 1. Calculate the initial Potential Energy (PE).
#    PE = m * g * h, where h is the cart's y-position.
#    initial_PE = cart.m * g * cart.pos.y

# 2. The total energy is equal to the initial potential energy.
#    total_energy = initial_PE
#    This total energy should remain constant throughout the ride!


# ANIMATION LOOP
while cart.pos.x < 20:
    rate(100)
    
    # --- STUDENT TASK 3: Apply Conservation of Energy ---
    # At any point on the track, Total Energy = PE + KE.
    
    # 1. Calculate the current Potential Energy (PE) based on the cart's height.
    #    current_PE = cart.m * g * cart.pos.y
    
    # 2. Calculate the current Kinetic Energy (KE) by rearranging the formula:
    #    KE = Total Energy - PE
    #    current_KE = total_energy - current_PE
    
    # 3. From kinetic energy, find the cart's speed.
    #    KE = 0.5 * m * v^2  =>  v = sqrt(2 * KE / m)
    #    speed = sqrt(2 * current_KE / cart.m)
    
    # 4. The velocity vector is tangent to the track. This is complex to calculate.
    #    For this simulation, we can approximate the direction as mostly horizontal.
    #    Let's just move the cart along the x-axis and set its y-position from the track function.
    
    # 5. Update position and time.
    #    cart.pos.x = cart.pos.x + speed * dt
    #    cart.pos.y = track_path(cart.pos.x)
    #    t = t + dt


print("Simulation finished.")
