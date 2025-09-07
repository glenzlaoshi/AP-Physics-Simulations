glowscript VPython

# AP Physics 2 - Unit 5: Magnetism & Electromagnetism
# Simulation 5.1: Charged Particle in a B-Field
#
# Intermediate Program

# --- SETUP ---
B_field_mag = 0.5 # Tesla
B_field_vec = vector(0, 0, B_field_mag)
for x in arange(-5, 5.1, 2):
    for y in arange(-5, 5.1, 2):
        arrow(pos=vector(x,y,-5), axis=vector(0,0,2), color=color.cyan, shaftwidth=0.05)

# --- PARTICLE ---
particle = sphere(pos=vector(-3, 0, 0), radius=0.2, color=color.yellow, make_trail=True)
particle.m = 1.67e-27
particle.q = 1.6e-19
particle.velocity = vector(0, 2e5, 0)

# --- SIMULATION ---
t = 0
dt = 1e-9

# --- Force Arrow ---
# Let's visualize the force acting on the particle.
F_arrow = arrow(pos=particle.pos, color=color.red, shaftwidth=0.1)

# ANIMATION LOOP
while t < 1e-6:
    rate(500)
    
    # --- STUDENT TASK 1: Calculate the Force ---
    # The magnetic force is F = q * (v x B).
    # Use the `cross()` function to calculate the cross product.
    
    # v_cross_B = cross(particle.velocity, B_field_vec)
    # F_mag = particle.q * v_cross_B
    
    # For now, use a placeholder force that points to the center.
    F_mag = -particle.pos.norm() * 1e-13
    
    # --- STUDENT TASK 2: Update Motion ---
    # Once you have the correct force, the rest of the simulation works.
    # Uncomment the lines below.
    
    # particle.acceleration = F_mag / particle.m
    # particle.velocity = particle.velocity + particle.acceleration * dt
    # particle.pos = particle.pos + particle.velocity * dt
    
    # Update the force arrow to show the direction of the force.
    F_arrow.pos = particle.pos
    F_arrow.axis = F_mag * 1e11 # Scale for visibility
    
    t = t + dt

# --- STUDENT TASK 3: Analysis ---
# The path should be a circle. The radius of this circle is given by:
# F_c = F_b  =>  mv^2/r = qvB  =>  r = mv / qB

# 1. Calculate the theoretical radius using the formula above.
#    r_theory = (particle.m * mag(particle.velocity)) / (particle.q * B_field_mag)

# 2. Measure the radius from your simulation. Does it match?
#    (The particle starts at x=-3, so the center is at (0,0) and the radius is 3).

print("Simulation finished.")
