glowscript VPython

# AP Physics 1 - Unit 5: Momentum
# Simulation 5.1: 1D Collisions
#
# Complete Program: Elastic and Inelastic Collisions

# --- SETUP ---
scene.title = "1D Collision Simulator"

# Global variable to control which collision type to run
collision_type = 'elastic' # Can be 'elastic' or 'inelastic'

# VISUALS
track = box(pos=vector(0, -0.5, 0), size=vector(20, 0.1, 2), color=color.gray(0.8))
cart1 = box(pos=vector(-5, 0, 0), size=vector(1, 1, 1), color=color.blue)
cart2 = box(pos=vector(5, 0, 0), size=vector(1, 1, 1), color=color.red)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

cart1.m = 2.0
cart1.v_initial = vector(4, 0, 0)
cart1.velocity = cart1.v_initial

cart2.m = 3.0
cart2.v_initial = vector(-2, 0, 0)
cart2.velocity = cart2.v_initial

# --- Function to handle the collision physics ---
def handle_collision():
    global collision_type
    
    # --- Calculate initial momentum and kinetic energy ---
    p_initial = cart1.m * cart1.v_initial + cart2.m * cart2.v_initial
    ke_initial = 0.5 * cart1.m * mag2(cart1.v_initial) + 0.5 * cart2.m * mag2(cart2.v_initial)
    print(f"--- BEFORE COLLISION ---")
    print(f"Total Momentum: {p_initial.x:.2f}")
    print(f"Total Kinetic Energy: {ke_initial:.2f}")
    
    if collision_type == 'inelastic':
        # They stick together. Final velocity is found by momentum conservation.
        v_final = (cart1.m * cart1.v_initial + cart2.m * cart2.v_initial) / (cart1.m + cart2.m)
        cart1.velocity = v_final
        cart2.velocity = v_final
        # Stick the carts together visually
        cart2.pos.x = cart1.pos.x + 1
        
    elif collision_type == 'elastic':
        # Both momentum and kinetic energy are conserved. The 1D elastic collision formulas are:
        # v1_f = ((m1-m2)/(m1+m2))*v1_i + (2*m2/(m1+m2))*v2_i
        # v2_f = (2*m1/(m1+m2))*v1_i + ((m2-m1)/(m1+m2))*v2_i
        m1, m2 = cart1.m, cart2.m
        v1i, v2i = cart1.v_initial, cart2.v_initial
        
        v1f = ((m1 - m2) / (m1 + m2)) * v1i + ((2 * m2) / (m1 + m2)) * v2i
        v2f = ((2 * m1) / (m1 + m2)) * v1i + ((m2 - m1) / (m1 + m2)) * v2i
        
        cart1.velocity = v1f
        cart2.velocity = v2f

    # --- Calculate final momentum and kinetic energy ---
    p_final = cart1.m * cart1.velocity + cart2.m * cart2.velocity
    ke_final = 0.5 * cart1.m * mag2(cart1.velocity) + 0.5 * cart2.m * mag2(cart2.velocity)
    print(f"\n--- AFTER {collision_type.upper()} COLLISION ---")
    print(f"Total Momentum: {p_final.x:.2f}")
    print(f"Total Kinetic Energy: {ke_final:.2f}")
    
    if ke_initial != ke_final:
        print(f"Kinetic Energy Lost: {ke_initial - ke_final:.2f} J")

# --- Main Animation Loop ---
collision_occurred = False

def run_simulation(c_type):
    global collision_type, collision_occurred, t
    collision_type = c_type
    scene.caption = f"Running a {collision_type} collision."
    
    # Reset carts
    t = 0
    collision_occurred = False
    cart1.pos = vector(-5, 0, 0)
    cart2.pos = vector(5, 0, 0)
    cart1.velocity = cart1.v_initial
    cart2.velocity = cart2.v_initial
    sleep(2)
    
    while t < 4:
        rate(100)
        if not collision_occurred:
            cart1.pos = cart1.pos + cart1.velocity * dt
            cart2.pos = cart2.pos + cart2.velocity * dt
            
            # Collision detection
            if mag(cart1.pos - cart2.pos) < 1:
                handle_collision()
                collision_occurred = True
        else: # After collision, continue updating position
            cart1.pos = cart1.pos + cart1.velocity * dt
            # For inelastic, make sure cart2 stays stuck
            if collision_type == 'inelastic':
                cart2.pos.x = cart1.pos.x + 1
            else:
                cart2.pos = cart2.pos + cart2.velocity * dt
        t += dt

# Run both simulations
run_simulation('inelastic')
run_simulation('elastic')
scene.title = "Simulations Complete"
scene.caption = ""
