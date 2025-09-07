glowscript VPython

# AP Physics C: Mechanics - Unit 4
# Simulation C-M.2: Center of Mass Motion
#
# Intermediate Program

# --- SETUP ---
ground = box(pos=vector(0,-50,0), size=vector(200, 2, 10), color=color.green)
projectile = sphere(pos=vector(-90, 0, 0), radius=2, color=color.yellow, make_trail=True)
projectile.m = 5.0
projectile.velocity = vector(30, 60, 0)
g = 9.8

# --- SIMULATION ---
t = 0
dt = 0.01
exploded = False
fragments = []

# A marker to track the center of mass
cm_marker = sphere(radius=1.5, color=color.white, make_trail=True, trail_color=color.white, trail_radius=0.8)

# ANIMATION LOOP
while projectile.pos.y >= 0 or len(fragments) > 0:
    rate(100)
    
    if not exploded:
        F_gravity = vector(0, -projectile.m * g, 0)
        projectile.acceleration = F_gravity / projectile.m
        projectile.velocity += projectile.acceleration * dt
        projectile.pos += projectile.velocity * dt
        cm_marker.pos = projectile.pos # Before explosion, CM is the projectile
        
        if projectile.velocity.y < 0:
            projectile.visible = False
            exploded = True
            
            # Create fragments. Note that the sum of explosion velocities should be zero
            # to conserve momentum at the moment of explosion.
            v_explosion1 = vector(-40, 30, 30)
            v_explosion2 = vector(30, 30, -30)
            # We calculate the third velocity to ensure momentum is conserved.
            v_explosion3 = -(2.0*v_explosion1 + 2.0*v_explosion2) / 1.0
            
            f1 = sphere(pos=projectile.pos, m=2.0, radius=1, color=color.red, make_trail=True, velocity = projectile.velocity + v_explosion1)
            f2 = sphere(pos=projectile.pos, m=2.0, radius=1, color=color.cyan, make_trail=True, velocity = projectile.velocity + v_explosion2)
            f3 = sphere(pos=projectile.pos, m=1.0, radius=0.8, color=color.orange, make_trail=True, velocity = projectile.velocity + v_explosion3)
            fragments = [f1, f2, f3]

    else:
        # --- STUDENT TASK 1: Move the Fragments ---
        # Each fragment moves under the influence of gravity.
        # Loop through the fragments and update their velocity and position.
        # for f in fragments:
        #     f.acceleration = vector(0, -g, 0)
        #     f.velocity += f.acceleration * dt
        #     f.pos += f.velocity * dt
        
        # --- STUDENT TASK 2: Calculate and Track Center of Mass ---
        # R_cm = (m1*r1 + m2*r2 + ...) / M_total
        
        # 1. Calculate the numerator of the CM formula (sum of m*r for all fragments).
        #    `sum_mr = f1.m*f1.pos + f2.m*f2.pos + f3.m*f3.pos`
        
        # 2. Calculate the CM position vector.
        #    `R_cm = sum_mr / projectile.m`
        
        # 3. Update the position of the white CM marker.
        #    `cm_marker.pos = R_cm`
        
        # If done correctly, the white trail of the CM marker should perfectly
        # overlap the yellow trail of the original projectile.
        
        # Remove fragments that fall below the ground
        for f in fragments[:]:
            if f.pos.y < ground.pos.y:
                f.visible = False
                fragments.remove(f)
    t += dt

print("Simulation finished.")
