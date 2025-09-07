glowscript VPython

# AP Physics C: E&M - Unit 4: Magnetic Fields
# Simulation C-EM.4: Field from a Current Loop (Biot-Savart Law)
#
# Skeleton Program

# --- CONSTANTS & PARAMETERS ---
mu_0 = 4*pi*1e-7 # Permeability of free space

# --- SETUP ---
# A circular loop of wire in the xy-plane, centered at the origin
loop_radius = 2.0
I = 5.0 # Current in Amperes, flowing counter-clockwise

loop = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=loop_radius, color=color.orange, thickness=0.1)

# The point where we want to calculate the B-field
point_of_interest = vector(0, 0, 3) # A point on the z-axis
marker = sphere(pos=point_of_interest, radius=0.1, color=color.cyan)

# --- BIOT-SAVART LAW ---
# The magnetic field dB from a small segment of wire dL is:
# dB = (mu_0 / 4pi) * (I * dL x r_hat) / r^2
# To find the total B-field, we must integrate this over the entire loop.

# --- STUDENT TASK 1: Divide the Loop into Segments (dL) ---
# We will approximate the integral by breaking the loop into many small, straight vector segments, dL.

# 1. Choose a number of segments, N.
#    N_segments = 50
#    d_theta = 2*pi / N_segments

# 2. Loop from theta = 0 to 2*pi.
#    `for i in range(N_segments):`
#        `theta = i * d_theta`

# 3. Inside the loop, find the start and end points of a small segment.
#    - The position of a point on the loop is `vector(R*cos(theta), R*sin(theta), 0)`.
#    - Find the position of the start of the segment (`pos1`) at `theta`.
#    - Find the position of the end of the segment (`pos2`) at `theta + d_theta`.
#    - The vector dL is `pos2 - pos1`.


# --- STUDENT TASK 2: Calculate dB for one segment ---
# For each dL segment calculated above:

# 1. Find the vector `r` from the segment to the point of interest.
#    - A good approximation is to take `r` from the midpoint of the dL segment.
#    `r_vec = point_of_interest - (pos1 + dL/2)`
#    `r_mag = mag(r_vec)`
#    `r_hat = norm(r_vec)`

# 2. Calculate the cross product `dL x r_hat`.

# 3. Calculate the dB vector for this segment using the Biot-Savart Law.
#    `dB = (mu_0 / (4*pi)) * (I * cross(dL, r_hat)) / r_mag**2`


# --- STUDENT TASK 3: Integrate to find B_total ---
# 1. Before the loop, create a zero vector: `B_total = vector(0,0,0)`.
# 2. Inside the loop, add the `dB` you calculated to `B_total`.
#    `B_total = B_total + dB`

# After the loop, B_total will be the total magnetic field at the point of interest.

print("Setup complete. The next step is to implement the integration.")
