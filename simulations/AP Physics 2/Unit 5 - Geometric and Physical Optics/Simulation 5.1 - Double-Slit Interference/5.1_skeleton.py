glowscript VPython

# AP Physics 2 - Unit 6: Geometric and Physical Optics
# Simulation 6.1: Double-Slit Interference
#
# Skeleton Program

# This simulation calculates and displays the interference pattern from two slits.

# --- SETUP ---
# A barrier with two slits in it
slit_separation = 0.5 # (d) distance between the centers of the slits
barrier = box(pos=vector(0,0,0), size=vector(0.1, 3, 3), color=color.gray(0.5))
slit1_pos = vector(0, slit_separation/2, 0)
slit2_pos = vector(0, -slit_separation/2, 0)

# A screen to project the pattern onto
screen_dist = 10 # (L) distance from the barrier to the screen
screen = box(pos=vector(screen_dist, 0, 0), size=vector(0.1, 10, 10), color=color.gray(0.9))

# Light source properties
wavelength = 0.1 # (lambda) wavelength of the light

# --- ANALYSIS ---
# We want to find the intensity of light at different points on the screen.
# Let's pick a point `P` on the screen to analyze.
P = vector(screen_dist, 2.0, 0) # A point 2m up the screen
marker = sphere(pos=P, radius=0.1, color=color.yellow)

# --- STUDENT TASK 1: Calculate Path Length Difference ---
# The core of interference is the difference in the distance traveled by
# light from each slit to the point P.

# 1. Calculate the distance from slit 1 to P (r1).
#    r1 = mag(P - slit1_pos)

# 2. Calculate the distance from slit 2 to P (r2).
#    r2 = mag(P - slit2_pos)

# 3. Find the path length difference.
#    path_diff = abs(r1 - r2)


# --- STUDENT TASK 2: Determine Interference Type ---
# Compare the path length difference to the wavelength.

# 1. For CONSTRUCTIVE interference (a bright spot), the path difference
#    is an integer multiple of the wavelength.
#    path_diff = m * wavelength, where m = 0, 1, 2, ...

# 2. For DESTRUCTIVE interference (a dark spot), the path difference
#    is a half-integer multiple of the wavelength.
#    path_diff = (m + 0.5) * wavelength, where m = 0, 1, 2, ...

# 3. Check if the interference at point P is closer to constructive or destructive.
#    - Divide the path difference by the wavelength.
#      `m_value = path_diff / wavelength`
#    - If `m_value` is close to an integer (0, 1, 2...), it's constructive.
#    - If `m_value` is close to a half-integer (0.5, 1.5, 2.5...), it's destructive.


# The complete program will do this for ALL points on the screen to draw the pattern.
print("Calculation finished.")
