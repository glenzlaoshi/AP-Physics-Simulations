glowscript VPython

# AP Physics C: E&M - Unit 1: Electrostatics
# Simulation C-EM.1: Gauss's Law
#
# Intermediate Program

# --- CONSTANTS & PARAMETERS ---
k = 9e9
epsilon_0 = 1 / (4 * pi * k)

# --- SETUP ---
# A single point charge at the origin
Q_enclosed = 5e-9
source_charge = sphere(pos=vector(0,0,0), radius=0.3, color=color.red, q=Q_enclosed)

# A spherical Gaussian surface
gauss_radius = 2.0
gauss_surface = sphere(pos=vector(0,0,0), radius=gauss_radius, color=color.cyan, opacity=0.2)

# --- E-Field Calculation ---
def calculate_E(pos, charge):
    r_vec = pos - charge.pos
    if mag(r_vec) < 0.1: return vector(0,0,0)
    return (k * charge.q / mag2(r_vec)) * norm(r_vec)

# --- FLUX CALCULATION ---
# We will break the spherical surface into patches and sum the flux.

# --- STUDENT TASK 1: Create Surface Patches ---
# We can create points on the surface using spherical coordinates (theta, phi).
# Then, for each point, we can create a small box to represent the area patch.

# 1. Define the number of steps for theta and phi.
#    n_theta = 10
#    n_phi = 10

# 2. Loop through theta (from 0 to pi) and phi (from 0 to 2*pi).
#    `for theta in arange(0, pi, pi/n_theta):`
#        `for phi in arange(0, 2*pi, 2*pi/n_phi):`

# 3. Inside the loop, find the position of the patch:
#    `x = gauss_radius * sin(theta) * cos(phi)`
#    `y = gauss_radius * sin(theta) * sin(phi)`
#    `z = gauss_radius * cos(theta)`
#    `patch_pos = vector(x,y,z)`

# --- STUDENT TASK 2: Calculate Flux through each patch ---
# For each patch created above:

# 1. The area vector `dA` for a spherical patch points radially outward.
#    Its direction is `norm(patch_pos)`.
#    Its magnitude is a small area element `dA_mag` (this is complex, but we can approximate).
#    Let's approximate `dA_mag = (Area_sphere) / (n_theta * n_phi)`
#    `dA_vec = norm(patch_pos) * (4*pi*gauss_radius**2) / (n_theta*n_phi)`

# 2. Calculate the E-field at `patch_pos`.
#    `E = calculate_E(patch_pos, source_charge)`

# 3. Calculate the flux through the patch: `dFlux = dot(E, dA_vec)`

# 4. Add this `dFlux` to a running total `total_flux`.

# --- STUDENT TASK 3: Compare with Theory ---
# 1. After the loops finish, print your calculated `total_flux`.
# 2. Calculate the theoretical flux: `flux_theory = Q_enclosed / epsilon_0`.
# 3. How close is your numerical result to the theoretical one?

print("When complete, the program will calculate the total electric flux.")
