glowscript VPython

# AP Physics C: Mechanics - Units 1-3
# Simulation C-M.1: Motion with Variable Force
#
# Intermediate Program

# --- SETUP ---
wall = box(pos=vector(-10,0,0), size=vector(0.2, 2, 2), color=color.gray(0.7))
cart = box(pos=vector(5, 0, 0), size=vector(1,1,1), color=color.blue, make_trail=True)
spring = helix(pos=wall.pos, axis=cart.pos-wall.pos, radius=0.4, color=color.orange)

# --- PARAMETERS ---
t = 0
dt = 0.01
cart.m = 0.5
spring.k = 2.0
spring.eq_pos = vector(0,0,0)

cart.pos = vector(8, 0, 0)
cart.velocity = vector(0, 0, 0)

# --- ANIMATION LOOP ---
while t < 15:
    rate(100)
    
    # Calculate the variable spring force based on the cart's current position.
    x_vec = cart.pos - spring.eq_pos
    F_vec = -spring.k * x_vec
    
    # Use the force to find the current acceleration.
    cart.acceleration = F_vec / cart.m
    
    # Use the acceleration to update velocity and then position.
    cart.velocity = cart.velocity + cart.acceleration * dt
    cart.pos = cart.pos + cart.velocity * dt
    
    # Update visuals and time.
    spring.axis = cart.pos - wall.pos
    t = t + dt

# --- STUDENT TASK: Analysis and Comparison ---
# The motion we just simulated is Simple Harmonic Motion.
# The analytical solution (the exact answer from solving the differential equation)
# for this motion is x(t) = A * cos(omega * t), where A is the amplitude and
# omega = sqrt(k/m).

# 1. Set up a graph before the loop: `graph(title="Position vs. Time")`
#    - Create a curve for the simulation data: `sim_curve = gcurve(color=color.blue)`
#    - Create a curve for the analytical solution: `theory_curve = gcurve(color=color.red)`

# 2. Inside the loop, plot the simulation's position:
#    `sim_curve.plot(t, cart.pos.x)`

# 3. Inside the loop, calculate and plot the theoretical position:
#    - First, calculate omega: `omega = sqrt(spring.k / cart.m)`
#    - The amplitude `A` is the starting position, 8.
#    - `x_theory = 8 * cos(omega * t)`
#    - `theory_curve.plot(t, x_theory)`

# 4. How well does our numerical integration (the blue curve) match the exact
#    theoretical solution (the red curve)? Try making `dt` smaller or larger.

print("Simulation finished.")
