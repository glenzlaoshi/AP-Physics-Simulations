glowscript VPython

# AP Physics 1 - Unit 2: Dynamics
# Simulation 2.1: Forces on an Inclined Plane
#
# Intermediate Program

# VISUALS
angle = radians(20)
plane = box(pos=vector(0, -0.5, 0), size=vector(12, 0.2, 4), color=color.blue)
plane.rotate(angle=angle, axis=vector(0, 0, 1))

block = box(pos=vector(-4, 0.2, 0), size=vector(1, 1, 1), color=color.red)
block.pos = rotate(block.pos, angle=angle, axis=vector(0,0,1))

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
block.mass = 1.0
mu_k = 0.2

block.velocity = vector(0, 0, 0)

# FORCE CALCULATIONS (Part 1)

# The gravitational force is constant and points straight down.
Fg = vector(0, -block.mass * g, 0)

# To find the other forces, we need directions relative to the incline.
# Parallel direction (down the incline)
parallel_axis = vector(cos(angle), sin(angle), 0)
# Perpendicular direction (away from the incline)
perp_axis = vector(sin(angle), cos(angle), 0)

# Let's calculate the magnitude of the gravity component perpendicular to the plane.
Fg_perp_mag = block.mass * g * cos(angle)

# The normal force (Fn) is equal and opposite to the perpendicular component of gravity.
Fn_mag = Fg_perp_mag
Fn = perp_axis * Fn_mag

# --- STUDENT TASKS ---

# 1. CALCULATE KINETIC FRICTION FORCE (Fk)
#    - The magnitude of kinetic friction is mu_k * Fn_mag.
#      Fk_mag = mu_k * Fn_mag
#    - The direction opposes motion. Since the block will slide DOWN the incline,
#      friction must point UP the incline. The direction vector for that is `parallel_axis`
#      but pointed the other way.
#      Fk = -parallel_axis * Fk_mag

# 2. CALCULATE NET FORCE (F_net)
#    - Sum the three force vectors: gravity, normal, and friction.
#      F_net = Fg + Fn + Fk

# 3. CALCULATE ACCELERATION (a)
#    - Use Newton's Second Law: a = F_net / m
#      block.acceleration = F_net / block.mass

# Initialize a placeholder until you calculate the real one.
block.acceleration = vector(0,0,0)

# ANIMATION LOOP
while block.pos.x < 6:
    rate(100)
    
    # --- STUDENT TASK 4: UNCOMMENT THE CODE BELOW ---
    # Once you have calculated `block.acceleration` above, uncomment these lines.
    
    # block.velocity = block.velocity + block.acceleration * dt
    # block.pos = block.pos + block.velocity * dt
    # t = t + dt

print("Simulation finished.")
