glowscript VPython

# AP Physics 2 - Unit 5: Magnetism & Electromagnetism
# Simulation 5.1: Charged Particle in a B-Field
#
# Complete Program

# --- SETUP ---
scene.title = "Motion of a Charge in a Uniform Magnetic Field"

# B-Field Visualization
B_field_mag = 0.5 # Tesla
B_field_vec = vector(0, 0, B_field_mag)
for x in arange(-5, 5.1, 2):
    for y in arange(-5, 5.1, 2):
        arrow(pos=vector(x,y,-5), axis=vector(0,0,2), color=color.cyan, shaftwidth=0.05)

# --- PARTICLE ---
particle = sphere(radius=0.2, color=color.yellow, make_trail=True)

# Particle properties
particle.m = 1.67e-27 # Mass of a proton
particle.q = 1.6e-19  # Charge of a proton

# --- UI CONTROLS ---
running = True

def run_pause(button):
    global running
    running = not running
    if running: button.text = "Pause"
    else: button.text = "Run"

button(bind=run_pause, text="Pause")

def set_path_type(m):
    reset_sim(m.selected)

menu(choices=['Circular Path', 'Helical Path'], bind=set_path_type)

# --- SIMULATION & RESET FUNCTION ---
def reset_sim(path_type):
    global t, particle
    t = 0
    particle.clear_trail()
    particle.pos = vector(-4, 0, 0)
    
    v_mag = 2e5
    if path_type == 'Circular Path':
        # Velocity is purely perpendicular to B-field
        particle.velocity = vector(0, v_mag, 0)
        scene.caption = "Velocity is perpendicular to B-field, causing circular motion."
    elif path_type == 'Helical Path':
        # Velocity has components both perpendicular and parallel to B-field
        particle.velocity = vector(0, v_mag, v_mag * 0.5)
        scene.caption = "Velocity has a component parallel to B-field, causing helical motion."
    
    # Theoretical radius of the circle/helix
    v_perp = mag(vector(particle.velocity.x, particle.velocity.y, 0))
    r_theory = (particle.m * v_perp) / (abs(particle.q) * B_field_mag)
    scene.caption += f"\nTheoretical Radius: {r_theory:.2f} m"

# --- Main Loop ---
t = 0
dt = 1e-10 # Use a very small time step for accuracy
reset_sim('Circular Path')

while True:
    rate(1000)
    if not running: continue

    # Calculate the magnetic force: F = q * (v x B)
    F_mag = particle.q * cross(particle.velocity, B_field_vec)
    
    # Update motion
    particle.acceleration = F_mag / particle.m
    particle.velocity = particle.velocity + particle.acceleration * dt
    particle.pos = particle.pos + particle.velocity * dt
    
    t += dt
    
    # Reset if it goes too far
    if mag(particle.pos) > 10:
        reset_sim(menu().selected)
