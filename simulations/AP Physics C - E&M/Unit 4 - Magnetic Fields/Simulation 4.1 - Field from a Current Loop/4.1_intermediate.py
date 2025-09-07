glowscript VPython

# AP Physics C: E&M - Unit 4: Magnetic Fields
# Simulation C-EM.4: Field from a Current Loop (Biot-Savart Law)
#
# Intermediate Program

# --- CONSTANTS & PARAMETERS ---
mu_0 = 4*pi*1e-7

# --- SETUP ---
loop_radius = 2.0
I = 5.0
loop = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=loop_radius, color=color.orange, thickness=0.1)

# The point where we want to calculate the B-field
point_of_interest = vector(0, 0, 3)
marker = sphere(pos=point_of_interest, radius=0.1, color=color.cyan)
B_arrow = arrow(pos=point_of_interest, color=color.yellow, shaftwidth=0.1)

# --- NUMERICAL INTEGRATION ---
# We will sum the contributions from N small segments of the loop.
N_segments = 100
d_theta = 2*pi / N_segments
B_total = vector(0,0,0)

# Loop through each segment of the wire
for i in range(N_segments):
    theta = i * d_theta
    
    # --- STUDENT TASK 1: Define the dL vector ---
    # dL is a small vector segment of the loop wire.
    # We can find it by taking the difference between two nearby points on the loop.
    pos1 = vector(loop_radius*cos(theta), loop_radius*sin(theta), 0)
    pos2 = vector(loop_radius*cos(theta+d_theta), loop_radius*sin(theta+d_theta), 0)
    dL = pos2 - pos1
    
    # --- STUDENT TASK 2: Apply the Biot-Savart Law ---
    # dB = (mu_0 / 4pi) * (I * dL x r_hat) / r^2
    
    # 1. Define the vector `r` from the segment to the point of interest.
    #    Let's use the midpoint of the segment.
    #    `r_vec = point_of_interest - (pos1 + dL/2)`
    
    # 2. Calculate `r_mag` and `r_hat`.
    
    # 3. Calculate the cross product `cross(dL, r_hat)`.
    
    # 4. Calculate the `dB` vector using the formula.
    
    # 5. Add `dB` to the running total `B_total`.
    #    `B_total = B_total + dB`

# --- STUDENT TASK 3: Compare with Analytical Solution ---
# For a point on the axis of a current loop, the exact formula is:
# B_z = (mu_0 * I * R^2) / (2 * (z^2 + R^2)^(3/2))

# 1. Calculate the theoretical B-field using this formula.
#    z = point_of_interest.z
#    R = loop_radius
#    B_theory_z = (mu_0 * I * R**2) / (2 * (z**2 + R**2)**(3/2))

# 2. Print your numerical result (`B_total`) and the theoretical result.
#    How close are they?

# Update the arrow to show the calculated B-field
B_arrow.axis = B_total * 1e5 # Scale for visibility

print("Calculation finished.")
