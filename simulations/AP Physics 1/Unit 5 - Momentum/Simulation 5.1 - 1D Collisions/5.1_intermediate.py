glowscript VPython

# AP Physics 1 - Unit 5: Momentum
# Simulation 5.1: 1D Collisions
#
# Intermediate Program: Perfectly Inelastic Collisions

# VISUALS
track = box(pos=vector(0, -0.5, 0), size=vector(20, 0.1, 2), color=color.gray(0.8))
cart1 = box(pos=vector(-5, 0, 0), size=vector(1, 1, 1), color=color.blue)
cart2 = box(pos=vector(5, 0, 0), size=vector(1, 1, 1), color=color.red)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

cart1.m = 2.0
cart1.velocity = vector(3, 0, 0)

cart2.m = 3.0 # Let's make the masses different
cart2.velocity = vector(-1, 0, 0)

# --- Calculate Initial State ---
p1_initial = cart1.m * cart1.velocity
p2_initial = cart2.m * cart2.velocity
total_p_initial = p1_initial + p2_initial
print(f"Initial momentum of system: {total_p_initial}")

collision_occurred = False

# ANIMATION LOOP
while t < 5:
    rate(100)
    
    # Move the carts
    cart1.pos = cart1.pos + cart1.velocity * dt
cart2.pos = cart2.pos + cart2.velocity * dt
    
    # Detect collision
    if mag(cart1.pos - cart2.pos) < 1 and not collision_occurred:
        print("\nCollision!")
        
        # --- STUDENT TASK: Implement Inelastic Collision ---
        # In a perfectly inelastic collision, the objects stick together.
        # We can find their new, common velocity using conservation of momentum.
        # p_initial = p_final
        # m1*v1_i + m2*v2_i = (m1 + m2) * v_f
        # v_f = (m1*v1_i + m2*v2_i) / (m1 + m2)
        
        # 1. Calculate the final velocity vector using the formula above.
        #    (Hint: `total_p_initial` is the numerator!)
        # v_final = total_p_initial / (cart1.m + cart2.m)
        
        # 2. Set the velocity of BOTH carts to this new final velocity.
        # cart1.velocity = v_final
        # cart2.velocity = v_final
        
        # For now, we'll just stop them.
        v_final = vector(0,0,0) # Replace this!
cart1.velocity = v_final
cart2.velocity = v_final
        
        # --- Verify Conservation of Momentum ---
        p1_final = cart1.m * cart1.velocity
p2_final = cart2.m * cart2.velocity
total_p_final = p1_final + p2_final
print(f"Final momentum of system: {total_p_final}")
        
        collision_occurred = True
        
    t = t + dt

print("\nSimulation finished.")
