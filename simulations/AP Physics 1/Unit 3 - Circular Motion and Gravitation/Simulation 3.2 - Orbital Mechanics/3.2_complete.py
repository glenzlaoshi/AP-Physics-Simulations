Web VPython 3.2
# AP Physics 1 - Unit 3: Circular Motion and Gravitation
# Simulation 3.2: Orbital Mechanics
#
# Complete Program

# This program demonstrates how different initial velocities lead to different orbits.
# It resets and runs the simulation four times.

# --- Click to Start / Pause ---
# Wait for the first click to start the simulation
scene.pause('Click to Start')
# Global variable to control the running state
running = True

# Function to running on click
def toggle_pause(evt):
    global running
    running = not running
# Bind the function to the click event
scene.bind('click', toggle_pause)
# --------------------------------

def run_orbit_simulation(initial_v_factor, label_text):
    """
    Runs a single orbit simulation with a given initial velocity factor.
    """
    # SCENE & VISUALS
    scene.title = "Orbital Mechanics Demonstration"
    scene.caption = f"Current Simulation: {label_text}"
    
    planet = sphere(pos=vector(0,0,0), radius=1e6, color=color.blue)
    satellite = sphere(pos=vector(5e6, 0, 0), radius=3e5, color=color.yellow, make_trail=True)
    trail_label = label(pos=satellite.pos + vector(0, 1e6, 0), text=label_text, box=False, opacity=0)

    # PARAMETERS & INITIAL CONDITIONS
    t = 0
    dt = 5
    G = 6.67e-11
    planet.m = 6e24
    satellite.m = 1000

    # Calculate the required speed for a perfect circular orbit
    radius = mag(satellite.pos)
    v_circular = sqrt(G * planet.m / radius)
    
    # Set the satellite's initial velocity based on the factor provided
    satellite.velocity = vector(0, v_circular * initial_v_factor, 0)
    
    print(f"\n--- Running: {label_text} ---")
    print(f"Initial speed: {mag(satellite.velocity):.2f} m/s")

    # ANIMATION LOOP
    # Run for one period (or until it crashes or gets too far)
    period = 2 * pi * radius / v_circular
    while t < period * 1.5 and mag(satellite.pos) > planet.radius and mag(satellite.pos) < 2.5 * radius:
        rate(500)
        if running:
            # Calculate Gravitational Force
            r_vector = planet.pos - satellite.pos
            r_mag = mag(r_vector)
            r_hat = norm(r_vector)
            F_mag = G * planet.m * satellite.m / r_mag**2
            F_gravity = F_mag * r_hat
        
            # Update Motion using Newton's 2nd Law and Kinematics
            satellite.acceleration = F_gravity / satellite.m
            satellite.velocity = satellite.velocity + satellite.acceleration * dt
            satellite.pos = satellite.pos + satellite.velocity * dt
            t = t + dt
    
    print("Simulation segment finished.")
    sleep(2) # Pause for 2 seconds before the next run

# --- Main Program Execution ---
# Run the simulation for different scenarios.

# 1. Velocity is too slow -> Orbit decays
run_orbit_simulation(0.7, "Too Slow: Orbit Decays")

# 2. Velocity is correct for a circular orbit
run_orbit_simulation(1.0, "Correct Speed: Circular Orbit")

# 3. Velocity is too fast -> Elliptical orbit
run_orbit_simulation(1.4, "Too Fast: Elliptical Orbit")

# 4. Velocity is much faster -> Escape velocity
run_orbit_simulation(1.8, "Much Faster: Escape Trajectory")

scene.caption = "All simulations complete."
