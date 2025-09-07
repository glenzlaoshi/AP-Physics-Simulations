glowscript VPython

# AP Physics C: E&M - Unit 4: Magnetic Fields
# Simulation C-EM.4: Field from a Current Loop (Biot-Savart Law)
#
# Complete Program

# --- SETUP ---
scene.title = "Magnetic Field of a Current Loop (Biot-Savart Law)"
scene.caption = "The yellow arrows represent the magnetic field calculated by integrating the Biot-Savart Law."

# --- CONSTANTS & PARAMETERS ---
mu_0 = 4*pi*1e-7

# --- LOOP SETUP ---
loop_radius = 2.0
I = 10.0 # Amperes
loop = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=loop_radius, color=color.orange, thickness=0.1)
# Arrow to show current direction
current_marker = arrow(pos=vector(loop_radius, 0, 0), axis=vector(0,1,0), color=color.red, shaftwidth=0.1)

# --- BIOT-SAVART CALCULATION FUNCTION ---
def calculate_B(point_of_interest):
    """Calculates the B-field at a point by numerically integrating the Biot-Savart Law."""
    N_segments = 50
    d_theta = 2*pi / N_segments
    B_total = vector(0,0,0)
    
    for i in range(N_segments):
        theta = i * d_theta
        pos1 = vector(loop_radius*cos(theta), loop_radius*sin(theta), 0)
        pos2 = vector(loop_radius*cos(theta+d_theta), loop_radius*sin(theta+d_theta), 0)
        dL = pos2 - pos1
        
        # Use the midpoint of the segment for r
        segment_midpoint = pos1 + dL/2
        r_vec = point_of_interest - segment_midpoint
        r_mag = mag(r_vec)
        
        if r_mag < 0.1: return vector(0,0,0) # Avoid singularity
        
        r_hat = norm(r_vec)
        
        # The Biot-Savart Law
        dB = (mu_0 / (4*pi)) * (I * cross(dL, r_hat)) / r_mag**2
        B_total += dB
        
    return B_total

# --- FIELD MAPPING ---
# Create a grid of arrows to visualize the B-field.
grid_range = 4
grid_spacing = 1
for x in arange(-grid_range, grid_range + grid_spacing, grid_spacing):
    for z in arange(-grid_range, grid_range + grid_spacing, grid_spacing):
        # Don't draw arrows inside the wire itself
        if abs(x-loop_radius)<0.5 and abs(z)<0.5: continue
        if abs(x+loop_radius)<0.5 and abs(z)<0.5: continue
        
        pos = vector(x, 0, z)
        B_field = calculate_B(pos)
        
        # Scale the arrow for visibility
        arrow_scale = 2e5
        arrow(pos=pos, axis=B_field*arrow_scale, color=color.yellow, shaftwidth=0.05)

# --- AXIS CALCULATION & VERIFICATION ---
# For points on the z-axis, compare the numerical result to the exact analytical formula.
print("Comparing numerical integration to analytical formula on the z-axis:")
print("-" * 60)
print(f"{'z (m)':<10} {'B_numerical (T)':<20} {'B_analytical (T)':<20} {'Error':<10}")
print("-" * 60)

for z in arange(0, 5, 0.5):
    # Numerical result from our function
    B_numerical = calculate_B(vector(0,0,z))
    
    # Analytical formula for the axis of a loop
    R = loop_radius
    B_analytical_mag = (mu_0 * I * R**2) / (2 * (z**2 + R**2)**(3/2))
    B_analytical = vector(0,0,B_analytical_mag)
    
    # Calculate percent error
    error = "N/A"
    if mag(B_analytical) > 0:
        error = f"{abs(100*(mag(B_numerical)-mag(B_analytical))/mag(B_analytical)):.2f}%"
    
    print(f'{z:<10.2f} {mag(B_numerical):<20.3e} {mag(B_analytical):<20.3e} {error:<10}")

