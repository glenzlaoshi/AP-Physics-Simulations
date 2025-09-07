glowscript VPython

# AP Physics 1 - Unit 2: Dynamics
# Simulation 2.1: Forces on an Inclined Plane
#
# Complete Program

# SCENE & VISUALS
scene.title = "Forces on an Inclined Plane"
scene.caption = "The simulation shows the force vectors acting on the block."

angle = radians(25) # 25 degree incline
plane = box(pos=vector(0, -0.5, 0), size=vector(12, 0.2, 4), color=color.blue)
plane.rotate(angle=angle, axis=vector(0, 0, 1))

block = box(pos=vector(-4, 0.2, 0), size=vector(1, 1, 1), color=color.red)
block.pos = rotate(block.pos, angle=angle, axis=vector(0,0,1))

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
block.mass = 1.0
mu_k = 0.15 # Coefficient of kinetic friction

block.velocity = vector(0, 0, 0)

# FORCE CALCULATIONS
# We define the axes relative to the incline for convenience.
parallel_axis = vector(cos(angle), sin(angle), 0) # Points down the incline
perp_axis = vector(sin(angle), cos(angle), 0)     # Points perpendicular to and away from the incline

# 1. Gravitational Force (Fg)
Fg = vector(0, -block.mass * g, 0)

# 2. Normal Force (Fn)
# The magnitude of the normal force balances the perpendicular component of gravity.
Fn_mag = block.mass * g * cos(angle)
Fn = Fn_mag * perp_axis # The direction is perpendicular to the surface.

# 3. Kinetic Friction Force (Fk)
# The magnitude depends on the normal force and the coefficient of kinetic friction.
Fk_mag = mu_k * Fn_mag
# The direction opposes the motion (which is down the incline), so it points up the incline.
Fk = -Fk_mag * parallel_axis

# 4. Net Force (F_net)
F_net = Fg + Fn + Fk

# 5. Acceleration (a)
# From Newton's Second Law, a = F_net / m.
block.acceleration = F_net / block.mass

# VISUALIZE FORCES WITH ARROWS
# The arrows will move with the block. Their `pos` is the block's position.
# The `axis` represents the direction and magnitude of the force vector.

# Scale factor to make arrows visible but not too large
force_scale = 0.5

# Arrow for Normal Force
fn_arrow = arrow(color=color.yellow, shaftwidth=0.1)
fn_arrow.pos = block.pos
fn_arrow.axis = Fn * force_scale

# Arrow for Gravity
fg_arrow = arrow(color=color.green, shaftwidth=0.1)
fg_arrow.pos = block.pos
fg_arrow.axis = Fg * force_scale

# Arrow for Friction
fk_arrow = arrow(color=color.orange, shaftwidth=0.1)
fk_arrow.pos = block.pos
fk_arrow.axis = Fk * force_scale

print(f"Angle: {degrees(angle):.1f} degrees")
print(f"Net Force: {F_net}")
print(f"Acceleration: {block.acceleration}")

# ANIMATION LOOP
while block.pos.x < 6:
    rate(100)
    
    # Update motion
    block.velocity = block.velocity + block.acceleration * dt
    block.pos = block.pos + block.velocity * dt
    t = t + dt
    
    # Update the positions of the force arrows so they stick to the block
    fn_arrow.pos = block.pos
    fg_arrow.pos = block.pos
    fk_arrow.pos = block.pos

print("Simulation finished.")
print(f"Final velocity: {block.velocity.mag:.2f} m/s")
