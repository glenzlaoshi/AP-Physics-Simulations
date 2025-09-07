glowscript VPython

# AP Physics 2 - Unit 7: Modern Physics
# Simulation 7.1: The Photoelectric Effect
#
# Complete Program

# --- SETUP ---
scene.title = "The Photoelectric Effect"

# --- CONSTANTS ---
h = 6.626e-34 # Planck's constant
e = 1.602e-19 # Elementary charge
c = 3e8       # Speed of light
me = 9.11e-31 # Mass of electron

# --- VISUALS ---
metal_plate = box(pos=vector(-6, 0, 0), size=vector(0.2, 6, 6), color=color.gray(0.8))

# --- PARAMETERS & VARIABLES ---
# Dictionary of work functions for different metals (in eV)
work_functions = {"Sodium": 2.75, "Calcium": 2.87, "Zinc": 4.33, "Gold": 5.1}

# Simulation variables that will be controlled by UI
metal_name = "Sodium"
phi = work_functions[metal_name] * e # Work function in Joules
light_wavelength = 500e-9 # in meters
light_intensity = 0.5 # A value from 0 to 1

# Lists to hold moving particles
photons = []
electrons = []

# --- GRAPHING SETUP ---
# Plot KE_max vs. Frequency
ke_graph = graph(title="Max Kinetic Energy vs. Light Frequency", xtitle="Frequency (x10^14 Hz)", ytitle="KE_max (eV)", fast=False)
ke_curve = gdots(color=color.cyan, label='Simulation Data')

# --- UI CONTROLS ---
def set_metal(m):
    global metal_name, phi
    metal_name = m.selected
    phi = work_functions[metal_name] * e
    update_caption()
    # Add a data point for the new metal's cutoff frequency
    cutoff_freq = phi / h
    ke_curve.plot(cutoff_freq/1e14, 0)

menu(choices=list(work_functions.keys()), bind=set_metal)

def set_wavelength(s):
    global light_wavelength
    light_wavelength = s.value * 1e-9
    update_caption()

slider(min=200, max=750, value=500, bind=set_wavelength, text="Wavelength (nm)")

def set_intensity(s):
    global light_intensity
    light_intensity = s.value

slider(min=0.1, max=1.0, value=0.5, bind=set_intensity, text="Intensity")

# --- CAPTION & LABELS ---
scene.caption = ""
def update_caption():
    E_photon = h * (c / light_wavelength)
    ke_max = (E_photon - phi) / e # in eV
    scene.caption = f"<b>Metal:</b> {metal_name} (Work Function = {phi/e:.2f} eV)\n" \
                    f"<b>Light:</b> {light_wavelength*1e9:.0f} nm (Photon Energy = {E_photon/e:.2f} eV)\n"
    if ke_max > 0:
        scene.caption += f"<b style='color:cyan;'>Electrons are EJECTED</b> with KE_max = {ke_max:.2f} eV"
    else:
        scene.caption += f"<b style='color:red;'>Photon energy is TOO LOW to eject electrons.</b>"

# --- ANIMATION LOOP ---
update_caption()

while True:
    rate(50) # frames per second
    
    # --- Photon Creation ---
    # Create photons based on light intensity
    if random() < light_intensity:
        photon = sphere(pos=vector(5, random(-2.5, 2.5), 0), radius=0.1, color=color.yellow)
        photon.velocity = vector(-20, 0, 0)
        photons.append(photon)

    # --- Particle Motion & Collision ---
    for p in photons[:]: # Loop over a copy
        p.pos += p.velocity * 0.05
        if p.pos.x < metal_plate.pos.x:
            # Photon hits the plate
            E_photon = h * (c / light_wavelength)
            if E_photon > phi:
                # Eject an electron
                KE_max = E_photon - phi
                v_electron = sqrt(2 * KE_max / me)
                electron = sphere(pos=p.pos, radius=0.08, color=color.cyan, make_trail=True, trail_radius=0.02)
                electron.velocity = vector(random(0.1, 1)*v_electron, random(-0.5,0.5)*v_electron, 0)
                electrons.append(electron)
                # Add data point to graph
                ke_curve.plot( (c/light_wavelength)/1e14, KE_max/e )
            
            # Remove the photon
            p.visible = False
            photons.remove(p)
            del p

    for e in electrons[:]: # Loop over a copy
        e.pos += e.velocity * 1e-7
        if e.pos.x > 5:
            # Remove electron when it goes off-screen
            e.visible = False
            electrons.remove(e)
            del e
