glowscript VPython

# AP Physics C: Mechanics - Unit 4
# Simulation C-M.2: Center of Mass Motion
#
# Complete Program

# --- SETUP ---
scene.title = "Center of Mass of an Exploding Projectile"
scene.caption = "The projectile explodes at its peak. The fragments fly apart, but the white ball, representing the Center of Mass, continues on the original parabolic path."

ground = box(pos=vector(0,-50,0), size=vector(200, 2, 10), color=color.green)

# --- PROJECTILE ---
# This object represents the projectile before the explosion.
projectile = sphere(pos=vector(-90, 0, 0), radius=2, color=color.yellow, make_trail=True, trail_radius=0.8)
projectile.m = 5.0 # Total mass of the system
projectile.velocity = vector(30, 60, 0)
g = 9.8

# --- SIMULATION STATE ---
t = 0
dt = 0.01
exploded = False
fragments = []

# A marker to track the center of mass after the explosion.
cm_marker = sphere(radius=1.5, color=color.white, make_trail=True, trail_type="points", trail_radius=0.8, interval=5)

# --- ANIMATION LOOP ---
while projectile.pos.y >= 0 or len(fragments) > 0:
    rate(100)
    
    if not exploded:
        # --- BEFORE EXPLOSION: Standard projectile motion ---
        F_gravity = vector(0, -projectile.m * g, 0)
        projectile.acceleration = F_gravity / projectile.m
        projectile.velocity += projectile.acceleration * dt
        projectile.pos += projectile.velocity * dt
        
        # The CM marker just follows the projectile before the explosion.
        cm_marker.pos = projectile.pos
        
        # --- EXPLOSION ---
        # Explode at the peak of the trajectory (when vertical velocity becomes zero).
        if projectile.velocity.y < 0:
            print("BOOM! Explosion at peak.")
            projectile.visible = False # Hide the original projectile
            exploded = True
            
            # Create fragments. Their combined mass must be the total mass.
            # The explosion velocities are internal forces; their momentum sum must be zero.
            v_explosion1 = vector(-40, 30, 30)
            v_explosion2 = vector(30, 30, -30)
            # The third velocity is calculated to ensure momentum is conserved at the instant of explosion.
            # m1*v_exp1 + m2*v_exp2 + m3*v_exp3 = 0
            v_explosion3 = -(2.0*v_explosion1 + 2.0*v_explosion2) / 1.0
            
            f1 = sphere(pos=projectile.pos, m=2.0, radius=1, color=color.red, make_trail=True, velocity = projectile.velocity + v_explosion1)
            f2 = sphere(pos=projectile.pos, m=2.0, radius=1, color=color.cyan, make_trail=True, velocity = projectile.velocity + v_explosion2)
            f3 = sphere(pos=projectile.pos, m=1.0, radius=0.8, color=color.orange, make_trail=True, velocity = projectile.velocity + v_explosion3)
            fragments = [f1, f2, f3]

    else:
        # --- AFTER EXPLOSION: Track fragments and the Center of Mass ---
        sum_mr = vector(0,0,0)
        
        # Move each fragment as an independent projectile.
        for f in fragments:
            f.acceleration = vector(0, -g, 0)
            f.velocity += f.acceleration * dt
            f.pos += f.velocity * dt
            # Add its contribution to the center of mass calculation.
            sum_mr += f.m * f.pos
        
        # Calculate the position of the Center of Mass.
        R_cm = sum_mr / projectile.m
        cm_marker.pos = R_cm
        
        # Clean up fragments that have fallen off-screen.
        for f in fragments[:]:
            if f.pos.y < ground.pos.y:
                f.visible = False
                fragments.remove(f)
    
    t += dt

print("Simulation finished. Note how the white trail (Center of Mass) follows the original yellow trail.")
