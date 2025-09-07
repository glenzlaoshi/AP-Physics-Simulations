glowscript VPython

# AP Physics C: Mechanics - Units 1-3
# Simulation C-M.1: Motion with Variable Force
#
# Skeleton Program

# This simulation uses numerical integration to solve for motion when
# acceleration is NOT constant, a common scenario in Physics C.

# --- SETUP ---
# A cart on a track attached to a spring
wall = box(pos=vector(-10,0,0), size=vector(0.2, 2, 2), color=color.gray(0.7))
cart = box(pos=vector(5, 0, 0), size=vector(1,1,1), color=color.blue, make_trail=True)
spring = helix(pos=wall.pos, axis=cart.pos-wall.pos, radius=0.4, color=color.orange)

# --- PARAMETERS ---
t = 0
dt = 0.01 # The time step for our numerical integration

cart.m = 0.5 # kg
spring.k = 2.0 # N/m
spring.eq_pos = vector(0,0,0) # Equilibrium position of the spring

# Initial conditions: pull the cart back and release from rest
cart.pos = vector(8, 0, 0)
cart.velocity = vector(0, 0, 0)

# --- ANIMATION LOOP ---
# The core of the simulation is a step-by-step calculation inside the loop.
while t < 15:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate the Variable Force ---
    # The force is no longer constant. It changes as the cart's position changes.
    # For a spring, the force is given by Hooke's Law: F = -k*x
    
    # 1. Calculate the displacement vector `x` from the equilibrium position.
    #    x_vec = cart.pos - spring.eq_pos
    
    # 2. Calculate the force vector `F`.
    #    F_vec = -spring.k * x_vec
    
    
    # --- STUDENT TASK 2: Numerical Integration (Euler-Cromer Method) ---
    # Since force (and thus acceleration) is not constant, we can't use the
    # standard kinematic formulas. We must update the motion step-by-step.
    
    # 1. Calculate acceleration at this instant: a = F/m
    #    cart.acceleration = F_vec / cart.m
    
    # 2. Update velocity over the small time step `dt`.
    #    cart.velocity = cart.velocity + cart.acceleration * dt
    
    # 3. Update position using the *new* velocity.
    #    cart.pos = cart.pos + cart.velocity * dt
    
    
    # --- STUDENT TASK 3: Update Visuals and Time ---
    # 1. Update the spring's appearance.
    #    spring.axis = cart.pos - wall.pos
    
    # 2. Advance time.
    #    t = t + dt

print("Simulation finished.")
