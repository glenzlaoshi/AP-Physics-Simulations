glowscript VPython

# AP Physics 2 - Unit 6: Geometric and Physical Optics
# Simulation 6.1: Double-Slit Interference
#
# Intermediate Program

# --- SETUP ---
slit_separation = 0.5 # d
barrier = box(pos=vector(0,0,0), size=vector(0.1, 3, 3), color=color.gray(0.5))
slit1_pos = vector(0, slit_separation/2, 0)
slit2_pos = vector(0, -slit_separation/2, 0)

screen_dist = 10 # L
screen = box(pos=vector(screen_dist, 0, 0), size=vector(0.1, 10, 10), opacity=0.3)

wavelength = 0.1 # lambda

# --- ANALYSIS ---
# We will loop through different points on the screen and draw the pattern.

# Create a list to hold the bars of our interference pattern
pattern_bars = []

# Loop through different y-positions on the screen
for y_pos in arange(-5, 5, 0.1):
    # This is the point P on the screen we are analyzing
    P = vector(screen_dist, y_pos, 0)
    
    # --- STUDENT TASK 1: Calculate Path Difference ---
    # Calculate the distance from each slit to point P.
    r1 = mag(P - slit1_pos)
    r2 = mag(P - slit2_pos)
    path_diff = abs(r1 - r2)
    
    # --- STUDENT TASK 2: Calculate Phase Difference and Intensity ---
    # The path difference leads to a phase difference between the two waves.
    # phase_diff = (2 * pi / wavelength) * path_diff
    
    # The resulting intensity of the light at point P is given by:
    # I = I_max * cos^2(phase_diff / 2)
    # We can let I_max = 1, so the intensity will be between 0 and 1.
    
    # 1. Calculate the phase difference.
    #    phase_diff = (2 * pi / wavelength) * path_diff
    
    # 2. Calculate the intensity (a value from 0 to 1).
    #    intensity = cos(phase_diff / 2)**2
    
    # For now, use a placeholder
    intensity = 1.0 # Replace this!
    
    # --- Draw the result ---
    # We draw a box at point P. Its color will represent the intensity.
    bar = box(pos=P, size=vector(0.1, 0.1, 1), color=vector(intensity, intensity, 0))
    pattern_bars.append(bar)


# --- STUDENT TASK 3: Analysis ---
# The formula for the position of bright fringes (constructive interference)
# for small angles is: y = m * lambda * L / d

# 1. Calculate the position of the first bright fringe (m=1).
#    y_bright_1 = 1 * wavelength * screen_dist / slit_separation

# 2. Does your calculated position match the center of the first bright yellow
#    bar on the screen (not counting the central one)?

print("Simulation finished.")
