glowscript VPython

# AP Physics 2 - Unit 2: Thermodynamics
# Simulation 2.1: Ideal Gas Law
#
# Complete Program

# --- SETUP ---
scene.title = "Ideal Gas Law Simulation (PV=nRT)"

# PARAMETERS
N = 150      # Number of particles
m = 1.0      # Mass of particles (arbitrary units)
k_B = 1.38e-23 # Boltzmann Constant

# VISUALS
L = 5.0 # Initial side length of the box
container = box(pos=vector(0,0,0), size=vector(L,L,L), color=color.white, opacity=0.1)

# Create particles
particles = []
for i in range(N):
    p = sphere(pos=(L/2)*vector.random(), radius=0.1, color=color.yellow)
    # Velocity will be set by the temperature slider
    p.velocity = vector(0,0,0)
    particles.append(p)

# --- UI CONTROLS ---
running = True

def run_pause(button):
    global running
    running = not running
    if running: button.text = "Pause"
    else: button.text = "Run"

button(bind=run_pause, text="Pause")

# Temperature Slider
def set_temp(s):
    global particles, m
    T = s.value
    # v_rms = sqrt(3*k*T/m). We use arbitrary units where 3k/m = 1 for simplicity.
    v_rms = sqrt(T)
    # Rescale velocities of all particles
    for p in particles:
        p.velocity = v_rms * p.velocity.norm()
    temp_label.text = f'{T:.0f} K'

scene.append_to_caption('\nTemperature: ')
temp_slider = slider(min=100, max=1000, value=300, bind=set_temp)
temp_label = wtext(text=f'{temp_slider.value:.0f} K')
set_temp(temp_slider) # Set initial velocities

# Volume Slider
def set_volume(s):
    global L, container
    L = s.value
    container.size = vector(L,L,L)
    volume_label.text = f'{L**3:.1f} m^3'

scene.append_to_caption('\nVolume (side length): ')
vol_slider = slider(min=2, max=10, value=5, bind=set_volume)
volume_label = wtext(text=f'{vol_slider.value**3:.1f} m^3')

# --- MEASUREMENT VARIABLES ---
t = 0
dt = 0.002
total_momentum_transfer = 0

# --- ANIMATION LOOP ---
while True:
    rate(500)
    if not running: continue

    # Move particles and handle collisions
    total_ke = 0
    for p in particles:
        p.pos = p.pos + p.velocity * dt
        total_ke += 0.5 * m * mag2(p.velocity)
        
        # Wall collisions
        if abs(p.pos.x) > L/2:
            # Momentum transferred to wall is 2*m*|vx|
            total_momentum_transfer += 2 * m * abs(p.velocity.x)
            p.velocity.x = -p.velocity.x
        if abs(p.pos.y) > L/2:
            total_momentum_transfer += 2 * m * abs(p.velocity.y)
            p.velocity.y = -p.velocity.y
        if abs(p.pos.z) > L/2:
            total_momentum_transfer += 2 * m * abs(p.velocity.z)
            p.velocity.z = -p.velocity.z
    t += dt

    # --- CALCULATIONS & DISPLAY ---
    if t > 0:
        # Pressure = Force / Area = (delta_p / delta_t) / Area
        avg_force = total_momentum_transfer / t
        area = 6 * L**2 # Total area of all 6 walls
        pressure = avg_force / area
        
        # Temperature is related to average KE
        # KE_avg = 3/2 * k_B * T  => T = (2/3) * KE_avg / k_B
        avg_ke = total_ke / N
        temperature = (2/3) * avg_ke / (k_B / m) # Divide by m to match arbitrary mass units
        
        volume = L**3
        n_moles = N / (6.022e23) # Avogadro's number
        R = (pressure * volume) / (n_moles * temperature)
        
        # Update display text
        scene.caption = f"P={pressure:.2f} Pa, V={volume:.1f} m^3, T={temperature:.0f} K\n" \
                        f"PV/nT = R = {R:.2f} J/(mol*K) (Ideal Gas Constant is ~8.314)"
