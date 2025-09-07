glowscript VPython

# AP Physics C: E&M - Unit 1: Electrostatics
# Simulation C-EM.1: Gauss's Law
#
# Skeleton Program

# Gauss's Law states that the total electric flux through a closed surface
# is equal to the charge enclosed divided by epsilon_0.

# --- CONSTANTS & PARAMETERS ---
k = 9e9
epsilon_0 = 1 / (4 * pi * k)

# --- SETUP ---
# 1. A Charge Distribution
# We'll use a line of discrete point charges.
line_charge_L = 5
N_charges = 11
Q_total = 5e-9 # Total charge of the line

source_charges = []
for i in range(N_charges):
    x = line_charge_L * (i/(N_charges-1) - 0.5)
    charge = sphere(pos=vector(x,0,0), radius=0.2, color=color.red)
    charge.q = Q_total / N_charges
    source_charges.append(charge)

# 2. A Gaussian Surface
# We'll use a cylinder enclosing the line of charge.
gauss_radius = 2
gauss_height = 7
gauss_surface = cylinder(pos=vector(0,0,-gauss_height/2), axis=vector(0,0,gauss_height), 
                         radius=gauss_radius, color=color.cyan, opacity=0.3)

# --- E-Field Calculation Function (from previous sims) ---
def calculate_E(pos, charges):
    E_net = vector(0,0,0)
    for s in charges:
        r_vec = pos - s.pos
        if mag(r_vec) < 0.1: return vector(0,0,0)
        E_net += (k * s.q / mag2(r_vec)) * norm(r_vec)
    return E_net

# --- FLUX CALCULATION ---
# To find the total flux, we must sum the flux through each small patch of our surface.
# Flux = sum(E . dA), where dA is the area vector of a small patch.

# --- STUDENT TASK 1: Analyze the Surface ---
# Our cylindrical surface has three parts: the top cap, the bottom cap, and the curved wall.
# We need to calculate the flux through each part and add them together.

# --- STUDENT TASK 2: Flux through the Top Cap ---
# 1. Break the top cap into small area patches.
# 2. For each patch:
#    a. Find its position.
#    b. Find its area vector, dA. For the top cap, dA points in the +z direction.
#    c. Calculate the E-field at the patch's position.
#    d. Calculate the flux through the patch: dFlux = dot(E, dA).
# 3. Sum the flux from all patches on the top cap.

# --- STUDENT TASK 3: Flux through the Bottom Cap and Wall ---
# 1. Repeat the process for the bottom cap (dA points in -z direction).
# 2. Repeat for the curved wall (dA points radially outwards).

# --- STUDENT TASK 4: Verify Gauss's Law ---
# 1. Sum the flux from all three parts to get the total flux.
# 2. Calculate the theoretical flux: Q_enclosed / epsilon_0.
# 3. Compare your results!

print("Simulation setup is complete. The next step is to implement the flux calculation.")
