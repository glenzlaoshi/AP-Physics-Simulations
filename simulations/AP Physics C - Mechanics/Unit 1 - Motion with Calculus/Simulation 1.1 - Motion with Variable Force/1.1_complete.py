glowscript VPython

# AP Physics C: Mechanics - Units 1-3
# Simulation C-M.1: Motion with Variable Force
#
# Complete Program

# This program uses numerical integration to solve for motion under two
# different variable forces: a spring force and a velocity-dependent drag force.

# --- SETUP ---
scene.title = "Numerical Integration with Variable Forces"

# --- PARAMETERS ---
t = 0
dt = 0.01 # Time step

cart = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.blue, make_trail=True)
cart.m = 0.5

# --- UI CONTROLS ---
def set_force_type(m):
    """Resets and runs the simulation for the selected force type."""
    global F_type
    F_type = m.selected
    reset_sim()

menu(choices=['Spring Force (F = -kx)', 'Quadratic Drag (F = -cv^2)'], bind=set_force_type)

# Graph for plotting results
g = graph(title="Position vs. Time", xtitle="Time (s)", ytitle="Position (m) or Velocity (m/s)")
data_curve = gcurve(color=color.cyan, label="Simulation Data")
theory_curve = gcurve(color=color.red, label="Analytical Solution (if available)")

# --- SIMULATION FUNCTION ---
F_type = 'Spring Force (F = -kx)' # Initial value

def reset_sim():
    global t, cart, data_curve, theory_curve
    t = 0
    data_curve.delete()
    theory_curve.delete()
    
    if F_type == 'Spring Force (F = -kx)':
        g.title = "Position vs. Time for Spring Force"
        g.ytitle = "Position (m)"
        cart.pos = vector(8,0,0)
        cart.velocity = vector(0,0,0)
        cart.trail_color = color.cyan
    elif F_type == 'Quadratic Drag (F = -cv^2)':
        g.title = "Velocity vs. Time for Quadratic Drag"
        g.ytitle = "Velocity (m/s)"
        cart.pos = vector(-10,0,0)
        cart.velocity = vector(10,0,0)
        cart.trail_color = color.orange

# --- ANIMATION LOOP ---
def run_simulation():
    global t, cart
    reset_sim()
    
    # Spring-specific parameters
    k = 2.0
    eq_pos = vector(0,0,0)
    
    # Drag-specific parameters
    c = 0.1
    
    while t < 20:
        rate(100)
        
        # --- Calculate Force ---
        F_vec = vector(0,0,0)
        if F_type == 'Spring Force (F = -kx)':
            x_vec = cart.pos - eq_pos
            F_vec = -k * x_vec
        elif F_type == 'Quadratic Drag (F = -cv^2)':
            if mag(cart.velocity) > 0:
                # Force is |F| = c*v^2, direction is opposite to v
                F_vec = -c * mag2(cart.velocity) * norm(cart.velocity)

        # --- Numerical Integration ---
        acceleration = F_vec / cart.m
        cart.velocity = cart.velocity + acceleration * dt
        cart.pos = cart.pos + cart.velocity * dt
        
        # --- Plotting ---
        if F_type == 'Spring Force (F = -kx)':
            data_curve.plot(t, cart.pos.x)
            # Plot analytical solution for comparison
            omega = sqrt(k/cart.m)
            A = 8
            theory_curve.plot(t, A * cos(omega * t))
        elif F_type == 'Quadratic Drag (F = -cv^2)':
            data_curve.plot(t, cart.velocity.x)
            # No simple analytical solution for x(t) or v(t) with quadratic drag!
            # This demonstrates the power of numerical methods.
            
        t += dt

# --- Initial Run ---
run_simulation()

# The menu will trigger `reset_sim` which will then require the user to re-run `run_simulation`
# This is a simplified model. A more robust implementation would handle state changes better.
# For this educational purpose, the user can re-run the function as needed.
