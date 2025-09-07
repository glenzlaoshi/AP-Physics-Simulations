glowscript VPython

# AP Physics C: E&M - Unit 5: Electromagnetism
# Simulation C-EM.5: The Maxwell-Ampere Law
#
# Intermediate Program

# --- CONSTANTS & PARAMETERS ---
mu_0 = 4*pi*1e-7
epsilon_0 = 8.85e-12

# --- SETUP ---
plate_radius = 2.0
plate_sep = 0.5
plate_L = plate(pos=vector(0,0,-plate_sep/2), axis=vector(0,0,-1), radius=plate_radius, color=color.gray(0.7))
plate_R = plate(pos=vector(0,0,plate_sep/2), axis=vector(0,0,1), radius=plate_radius, color=color.gray(0.7))

# --- CHARGING PROCESS ---
I_charge = 0.1 # Assume a constant charging current
Area = pi * plate_radius**2

# The rate of change of the E-field is constant if the current is constant.
# E = Q/(A*e0) = (I*t)/(A*e0)  =>  dE/dt = I/(A*e0)
dE_dt = I_charge / (Area * epsilon_0)

# --- VISUALIZATION ---
# We'll visualize the induced B-field at a specific radius.
r_loop = 1.5 # Radius of our Amperian loop
loop_vis = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=r_loop, color=color.yellow, thickness=0.05)

# --- STUDENT TASK 1: Calculate d(Flux_E)/dt ---
# The rate of change of electric flux through our yellow loop.

# 1. The area of the Amperian loop.
#    loop_area = pi * r_loop**2

# 2. The rate of change of flux.
#    dFlux_dt = dE_dt * loop_area


# --- STUDENT TASK 2: Calculate the Induced B-field ---
# Use the result from the Maxwell-Ampere Law:
# B * (2*pi*r) = mu_0 * epsilon_0 * d(Flux_E)/dt

# 1. Solve for the magnitude of B at radius `r_loop`.
#    B_mag = (mu_0 * epsilon_0 * dFlux_dt) / (2 * pi * r_loop)

# 2. The B-field is constant as long as the charging current is constant.
#    Print out the value of B_mag.


# --- STUDENT TASK 3: Visualize the B-field ---
# The B-field curls around the changing E-field.
# Let's draw some arrows on our yellow loop to show it.

# 1. Choose a number of arrows to draw.
#    N_arrows = 8

# 2. Loop from 0 to 2*pi.
#    `for theta in arange(0, 2*pi, 2*pi/N_arrows):`

# 3. Inside the loop, find the position of the arrow.
#    `pos = vector(r_loop*cos(theta), r_loop*sin(theta), 0)`

# 4. Find the direction of the B-field at that point. It's tangential to the loop.
#    `B_dir = vector(-sin(theta), cos(theta), 0)` for CCW field.

# 5. Create the arrow.
#    `arrow(pos=pos, axis=B_dir * B_mag * 1e6, ...)` (scale for visibility)

print("Calculation finished.")
