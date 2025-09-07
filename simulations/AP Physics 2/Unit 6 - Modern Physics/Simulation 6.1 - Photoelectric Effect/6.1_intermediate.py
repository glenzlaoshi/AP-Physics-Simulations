glowscript VPython

# AP Physics 2 - Unit 7: Modern Physics
# Simulation 7.1: The Photoelectric Effect
#
# Intermediate Program

# --- CONSTANTS & PARAMETERS ---
h = 6.626e-34
e = 1.602e-19
c = 3e8
me = 9.11e-31 # mass of electron

# --- SETUP ---
metal_plate = box(pos=vector(-5, 0, 0), size=vector(0.2, 5, 5), color=color.gray(0.8))

# --- PHYSICS ---
# Metal properties
work_function_eV = 2.75 # Sodium
phi = work_function_eV * e

# Light properties
wavelength = 400e-9 # 400 nm (violet light)
frequency = c / wavelength
E_photon = h * frequency

print(f"Work function: {work_function_eV:.2f} eV")
print(f"Photon energy: {E_photon/e:.2f} eV")

# --- Ejection Logic ---
KE_max = 0
if E_photon > phi:
    # Electrons will be ejected
    KE_max = E_photon - phi
    print(f"Electrons ARE ejected with KE_max = {KE_max/e:.2f} eV")
else:
    print("Electrons are NOT ejected.")

# --- VISUALIZATION ---
# We will create "photons" and, if they have enough energy, "electrons".

# Create a list to hold our particles (photons and electrons)
particles = []

# ANIMATION LOOP
while True:
    rate(30)
    
    # --- STUDENT TASK 1: Create Photons ---
    # Every few frames, create a new photon particle.
    # A photon is just a sphere that moves towards the plate.
    # `p = sphere(pos=vector(5, random(-2,2), 0), radius=0.1, color=color.yellow)`
    # `p.velocity = vector(-20, 0, 0)`
    # `particles.append(p)`
    
    # --- STUDENT TASK 2: Move Particles and Detect Collision ---
    # Loop through all particles in the `particles` list.
    # `for p in particles:`
    #   `p.pos = p.pos + p.velocity * dt`
    
    #   If a particle `p` hits the metal plate (`p.pos.x < -5`):
    #   1. Make the photon invisible: `p.visible = False`
    #   2. Check if electrons are ejected (`KE_max > 0`).
    #   3. If so, create a new electron particle at the collision point.
    #      `e_particle = sphere(pos=p.pos, radius=0.08, color=color.cyan)`
    #      - Calculate its speed from KE_max: v = sqrt(2*KE_max/me)
    #      - Give it a random velocity away from the plate.
    #      `e_particle.velocity = vector(v, random(-v,v)/2, random(-v,v)/2)`
    #      - Add the electron to your `particles` list.

    # --- STUDENT TASK 3: Clean up ---
    # Remove particles that are far off-screen to save memory.

print("Simulation finished.")
