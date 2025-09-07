glowscript VPython

# AP Physics 1 - Unit 2: Dynamics
# Simulation 2.1: Forces on an Inclined Plane
#
# Skeleton Program

# VISUALS
# The inclined plane (a rotated box)
angle = radians(20) # 20 degree incline
plane = box(pos=vector(0, -0.5, 0), size=vector(12, 0.2, 4), color=color.blue)
plane.rotate(angle=angle, axis=vector(0, 0, 1))

# The block on the plane
block = box(pos=vector(-4, 0.2, 0), size=vector(1, 1, 1), color=color.red)
# We need to rotate the block's position to match the plane's angle
block.pos = rotate(block.pos, angle=angle, axis=vector(0,0,1))


# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

block.mass = 1.0 # kg
mu_k = 0.2 # coefficient of kinetic friction

# Initial motion
block.velocity = vector(0, 0, 0)
block.acceleration = vector(0, 0, 0)


# --- STUDENT TASKS ---

# The core of this simulation is calculating the net force on the block.
# Force is a vector! F_net = F_gravity + F_normal + F_friction

# 1. GRAVITATIONAL FORCE (Fg)
#    - This force always points straight down.
#    - Fg = vector(0, -block.mass * g, 0)

# 2. NORMAL FORCE (Fn)
#    - This force is perpendicular to the plane, pointing away from it.
#    - First, find the component of gravity perpendicular to the plane.
#      Fg_perp_mag = block.mass * g * cos(angle)
#    - The normal force magnitude is equal and opposite to Fg_perp.
#    - The direction is tricky! It's perpendicular to the plane.
#      normal_direction = vector(sin(angle), cos(angle), 0)
#    - Fn = normal_direction * Fg_perp_mag

# 3. FRICTIONAL FORCE (Fk)
#    - This force opposes the motion, so it points up the incline.
#    - The magnitude is Fk_mag = mu_k * Fn_mag.
#    - The direction is parallel to the plane, pointing upwards.
#      friction_direction = vector(cos(angle), sin(angle), 0)
#    - Fk = friction_direction * Fk_mag

# 4. NET FORCE (F_net)
#    - Sum the force vectors: F_net = Fg + Fn + Fk

# 5. ACCELERATION
#    - Use Newton's Second Law: a = F_net / m
#    - block.acceleration = F_net / block.mass


# ANIMATION LOOP
while block.pos.x < 6:
    rate(100)
    
    # --- STUDENT TASK: Implement Physics ---
    # All the force calculations and the update to acceleration
    # should happen *inside* the loop if any forces depend on changing
    # conditions (like velocity for air drag). For this problem, 
    # the forces are constant, so you could calculate them once outside the loop.
    
    # Let's assume you have calculated `block.acceleration`.
    
    # Update velocity and position
    # block.velocity = block.velocity + block.acceleration * dt
    # block.pos = block.pos + block.velocity * dt
    # t = t + dt


print("Simulation finished.")
