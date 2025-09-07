glowscript VPython

# AP Physics C: Mechanics - Unit 4
# Simulation C-M.2: Center of Mass Motion
#
# Skeleton Program

# This simulation shows that the center of mass of a system moves as if all the
# system's mass were concentrated there and all external forces were applied there.

# --- SETUP ---
ground = box(pos=vector(0,-50,0), size=vector(200, 2, 10), color=color.green)

# --- PROJECTILE ---
# A single projectile that will explode at its peak.
projectile = sphere(pos=vector(-90, 0, 0), radius=2, color=color.yellow)
projectile.m = 5.0 # Total mass
projectile.velocity = vector(30, 60, 0)
g = 9.8

# --- SIMULATION ---
t = 0
dt = 0.01
exploded = False
fragments = []

# ANIMATION LOOP
while projectile.pos.y >= 0 or len(fragments) > 0:
    rate(100)
    
    if not exploded:
        # --- Before explosion: standard projectile motion ---
        F_gravity = vector(0, -projectile.m * g, 0)
        projectile.acceleration = F_gravity / projectile.m
        projectile.velocity += projectile.acceleration * dt
        projectile.pos += projectile.velocity * dt
        
        # --- Explosion Condition ---
        # Explode when the projectile reaches the peak of its trajectory (vy is close to 0)
        if projectile.velocity.y < 0:
            print("BOOM!")
            projectile.visible = False
            exploded = True
            
            # --- STUDENT TASK 1: Create the Fragments ---
            # The projectile breaks into pieces. The sum of the fragment masses must equal
            # the original mass. The explosion force is internal, so the velocity of the
            # center of mass should be conserved right before and after the explosion.
            
            # Let's create 3 fragments.
            # f1 = sphere(pos=projectile.pos, radius=1, color=color.red, make_trail=True)
            # f1.m = 2.0
            # f1.velocity = projectile.velocity + vector(-20, 20, 20) # Add explosion velocity
            
            # f2 = sphere(pos=projectile.pos, radius=1, color=color.cyan, make_trail=True)
            # f2.m = 2.0
            # f2.velocity = projectile.velocity + vector(20, 20, -20)
            
            # f3 = sphere(pos=projectile.pos, radius=1, color=color.orange, make_trail=True)
            # f3.m = 1.0
            # f3.velocity = projectile.velocity + vector(0, -40, 0)
            
            # fragments = [f1, f2, f3]

    else:
        # --- After explosion: move fragments and track Center of Mass ---
        
        # --- STUDENT TASK 2: Move the Fragments ---
        # Each fragment is now an independent projectile under gravity.
        # Loop through the `fragments` list.
        # for f in fragments:
        #     f.acceleration = vector(0, -g, 0)
        #     f.velocity += f.acceleration * dt
        #     f.pos += f.velocity * dt
        
        # --- STUDENT TASK 3: Calculate Center of Mass ---
        # The position of the center of mass is given by:
        # R_cm = (m1*r1 + m2*r2 + m3*r3 + ...) / (m1 + m2 + m3 + ...)
        
        # 1. Initialize a zero vector for the numerator: `sum_mr = vector(0,0,0)`
        # 2. Loop through the fragments and add `f.m * f.pos` to `sum_mr`.
        # 3. The total mass is `projectile.m`.
        # 4. Calculate R_cm.
        #    `R_cm = sum_mr / projectile.m`
        
        # The key insight is that R_cm should follow the original parabolic path!
        
    t += dt

print("Simulation finished.")
