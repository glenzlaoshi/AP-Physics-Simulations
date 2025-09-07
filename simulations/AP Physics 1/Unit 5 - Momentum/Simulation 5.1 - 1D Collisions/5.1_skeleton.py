glowscript VPython

# AP Physics 1 - Unit 5: Momentum
# Simulation 5.1: 1D Collisions
#
# Skeleton Program

# VISUALS
# A long track for the carts
track = box(pos=vector(0, -0.5, 0), size=vector(20, 0.1, 2), color=color.gray(0.8))

# Two carts on the track
cart1 = box(pos=vector(-5, 0, 0), size=vector(1, 1, 1), color=color.blue)
cart2 = box(pos=vector(5, 0, 0), size=vector(1, 1, 1), color=color.red)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

# --- STUDENT TASK 1: Set Masses and Initial Velocities ---
# Define mass and initial velocity for each cart.
cart1.m = 2.0
cart1.velocity = vector(3, 0, 0)

cart2.m = 2.0
cart2.velocity = vector(-1, 0, 0)

# A flag to make sure the collision code only runs once.
collision_occurred = False

# ANIMATION LOOP
while t < 5:
    rate(100)
    
    # --- STUDENT TASK 2: Move the Carts ---
    # Update the position of each cart based on its velocity.
    # cart1.pos = cart1.pos + cart1.velocity * dt
    # cart2.pos = cart2.pos + cart2.velocity * dt
    
    
    # --- STUDENT TASK 3: Detect Collision ---
    # A collision happens when the distance between the carts is less than
    # the sum of their half-widths (i.e., when they touch).
    # The width of each cart is 1, so the half-width is 0.5.
    
    # if mag(cart1.pos - cart2.pos) < 1 and not collision_occurred:
        # --- STUDENT TASK 4: Handle the Collision! ---
        # This is where the physics of momentum conservation goes.
        
        # For a PERFECTLY INELASTIC collision (they stick together):
        # The formula from conservation of momentum is:
        # v_final = (m1*v1_initial + m2*v2_initial) / (m1 + m2)
        
        # 1. Calculate the final velocity vector.
        # v_final = (cart1.m * cart1.velocity + cart2.m * cart2.velocity) / (cart1.m + cart2.m)
        
        # 2. Set both carts to have this new final velocity.
        # cart1.velocity = v_final
        # cart2.velocity = v_final
        
        # 3. Set the flag to true so this code doesn't run again.
        # collision_occurred = True
        

    # Update time
    # t = t + dt

print("Simulation finished.")
