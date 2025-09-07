glowscript VPython

# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.2: Projectile Motion
#
# Intermediate Program

# OBJECTS
ground = box(pos=vector(0, -0.5, 0), size=vector(40, 0.1, 10), color=color.green)
projectile = sphere(pos=vector(-18, 0, 0), radius=0.4, color=color.yellow, make_trail=True)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

# Initial speed and angle are defined.
v0 = 20
theta = radians(45)

# The initial velocity vector is calculated from speed and angle.
projectile.velocity = vector(v0 * cos(theta), v0 * sin(theta), 0)

# The acceleration of a projectile is constant and directed downwards.
projectile.acceleration = vector(0, -g, 0)

print(f"Launching with speed={v0} m/s at angle={degrees(theta):.1f} degrees.")

# ANIMATION LOOP
while projectile.pos.y >= 0:
    rate(100)
    
    # The kinematic equations are applied each time step.
    projectile.velocity = projectile.velocity + projectile.acceleration * dt
    projectile.pos = projectile.pos + projectile.velocity * dt
    t = t + dt

print("Simulation finished.")
print(f"Total time in air: {t:.2f} s")
print(f"Horizontal range: {projectile.pos.x:.2f} m")

# --- STUDENT TASK ---
# This simulation shows the path of a single projectile.
# A great way to understand projectile motion is to see the independence
# of horizontal and vertical motion.
#
# 1. Create a second ball, let's call it `dropped_ball`.
#    - It should start at the same height as the projectile, but at x=0.
#    - `dropped_ball = sphere(pos=vector(0, projectile.pos.y, 0), radius=0.4, color=color.red)`
#
# 2. Give the `dropped_ball` an initial velocity of zero.
#    - `dropped_ball.velocity = vector(0, 0, 0)`
#
# 3. Inside the animation loop, update the position of the `dropped_ball`.
#    - It has the same acceleration as the projectile!
#    - `dropped_ball.pos.y = dropped_ball.pos.y - 0.5 * g * t**2` (using kinematic equation)
#
# 4. Run the simulation. Do the two balls hit the ground at the same time?

