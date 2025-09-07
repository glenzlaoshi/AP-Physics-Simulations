glowscript VPython

# AP Physics C: E&M - Unit 1: Electrostatics
# Simulation C-EM.1: Gauss's Law
#
# Complete Program

# --- SETUP ---
scene.title = "Verifying Gauss's Law"

# --- CONSTANTS & PARAMETERS ---
k = 9e9
epsilon_0 = 1 / (4 * pi * k)

# --- CHARGE CONFIGURATION ---
# A line of charge along the x-axis
line_charge_L = 4
N_charges = 21 # Use an odd number to center a charge at the origin
Q_total = 5e-9
source_charges = []
for i in range(N_charges):
    x = line_charge_L * (i/(N_charges-1) - 0.5)
    charge = sphere(pos=vector(x,0,0), radius=0.15, color=color.red)
    charge.q = Q_total / N_charges
    source_charges.append(charge)

# --- GAUSSIAN SURFACE ---
# A cylinder enclosing the charge
gauss_radius = 2.0
gauss_height = 6.0
gauss_surface = cylinder(pos=vector(0,0,-gauss_height/2), axis=vector(0,0,gauss_height), 
                         radius=gauss_radius, color=color.cyan, opacity=0.2)

# --- E-FIELD CALCULATION ---
def calculate_E(pos, charges):
    E_net = vector(0,0,0)
    for s in charges:
        r_vec = pos - s.pos
        if mag(r_vec) < 0.01: return vector(0,0,0)
        E_net += (k * s.q / mag2(r_vec)) * norm(r_vec)
    return E_net

# --- FLUX CALCULATION ---
# We numerically integrate the flux over the surface by breaking it into patches.
total_flux = 0

# 1. Flux through the cylindrical wall
n_phi = 20 # number of patches around circumference
n_z = 20   # number of patches along height
d_phi = 2*pi / n_phi
d_z = gauss_height / n_z
for i in range(n_z):
    z = -gauss_height/2 + (i + 0.5) * d_z
    for j in range(n_phi):
        phi = (j + 0.5) * d_phi
        patch_pos = vector(gauss_radius*cos(phi), gauss_radius*sin(phi), z)
        # Area vector dA points radially outward
        dA_vec = norm(vector(cos(phi), sin(phi), 0)) * (gauss_radius * d_phi) * d_z
        E_vec = calculate_E(patch_pos, source_charges)
        total_flux += dot(E_vec, dA_vec)
        # Visualize the E-field vector at the patch
        arrow(pos=patch_pos, axis=E_vec*1e-4, color=color.orange, shaftwidth=0.02)

# 2. Flux through the top and bottom caps
n_r = 10 # number of rings on the cap
d_r = gauss_radius / n_r
for i in range(n_r):
    r = (i + 0.5) * d_r
    for j in range(n_phi):
        phi = (j + 0.5) * d_phi
        dA_mag = (pi*(r+d_r)**2 - pi*r**2) / n_phi # Area of segment
        # Top cap
        pos_top = vector(r*cos(phi), r*sin(phi), gauss_height/2)
        dA_top = vector(0,0,1) * dA_mag
        E_top = calculate_E(pos_top, source_charges)
        total_flux += dot(E_top, dA_top)
        arrow(pos=pos_top, axis=E_top*1e-4, color=color.orange, shaftwidth=0.02)
        # Bottom cap
        pos_bot = vector(r*cos(phi), r*sin(phi), -gauss_height/2)
        dA_bot = vector(0,0,-1) * dA_mag
        E_bot = calculate_E(pos_bot, source_charges)
        total_flux += dot(E_bot, dA_bot)
        arrow(pos=pos_bot, axis=E_bot*1e-4, color=color.orange, shaftwidth=0.02)

# --- VERIFY GAUSS'S LAW ---
# Find the actual charge enclosed by the surface
Q_enclosed = 0
for s in source_charges:
    if abs(s.pos.z) < gauss_height/2 and mag(vector(s.pos.x, s.pos.y, 0)) < gauss_radius:
        Q_enclosed += s.q

# Calculate theoretical flux
flux_theory = Q_enclosed / epsilon_0

# --- DISPLAY RESULTS ---
scene.caption = f"<b>Numerical Flux (sum of E.dA):</b> {total_flux:.2f} V*m\n" \
                f"<b>Theoretical Flux (Q_enclosed/e0):</b> {flux_theory:.2f} V*m\n" \
                f"<b>Percent Difference:</b> {abs(100*(total_flux-flux_theory)/flux_theory):.2f}%"

print("Simulation finished.")
