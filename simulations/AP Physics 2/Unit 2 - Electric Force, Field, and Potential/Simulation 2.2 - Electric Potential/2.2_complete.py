glowscript VPython

# AP Physics 2 - Unit 3: Electric Force, Field, and Potential
# Simulation 3.2: Electric Potential
#
# Complete Program: Equipotential Line Mapper

# --- SETUP ---
scene.title = "Equipotential Map and E-Field Lines"
scene.caption = "Colors show the electric potential (red=high, blue=low). Lines of the same color are equipotentials.\n The orange lines show the E-Field, which is always perpendicular to the equipotentials."

# PARAMETERS
k = 9e9

# --- SOURCE CHARGES ---
source1 = sphere(pos=vector(-3, 0, 0), radius=0.5, color=color.red, q=3e-9)
source2 = sphere(pos=vector(3, 0, 0), radius=0.5, color=color.blue, q=-3e-9)
sources = [source1, source2]

# --- CALCULATION FUNCTIONS ---
def calculate_V(pos, charge_list):
    """Calculates the net scalar potential V at a position."""
    V_net = 0
    for s in charge_list:
        r = mag(pos - s.pos)
        if r < 0.1: return 1e6 if s.q > 0 else -1e6 # Avoid singularity
        V_net += k * s.q / r
    return V_net

def calculate_E(pos, charge_list):
    """Calculates the net E-field vector at a position."""
    E_net = vector(0,0,0)
    for s in charge_list:
        r_vec = pos - s.pos
        r_mag = mag(r_vec)
        if r_mag < 0.1: return vector(0,0,0)
        E_net += (k * s.q / r_mag**2) * norm(r_vec)
    return E_net

# --- EQUIPOTENTIAL MAP ---
# Create a grid of points and calculate the potential at each.
grid_min, grid_max, spacing = -8, 8.1, 0.5
potential_data = []
for x in arange(grid_min, grid_max, spacing):
    row = []
    for y in arange(grid_min, grid_max, spacing):
        V = calculate_V(vector(x,y,0), sources)
        row.append(V)
    potential_data.append(row)

# Find min and max potential for color mapping
V_max = max(max(row) for row in potential_data if row)
V_min = min(min(row) for row in potential_data if row)

# Create a grid of colored boxes to display the map
for i, x in enumerate(arange(grid_min, grid_max, spacing)):
    for j, y in enumerate(arange(grid_min, grid_max, spacing)):
        V = potential_data[i][j]
        # Normalize potential to a 0-1 scale for coloring
        color_val = (V - V_min) / (V_max - V_min) if (V_max - V_min) > 0 else 0.5
        # Use a color gradient (blue -> black -> red)
        red_val = color_val
        blue_val = 1 - color_val
        box(pos=vector(x,y,-0.1), size=vector(spacing, spacing, 0.1), color=vector(red_val, 0, blue_val))

# --- E-FIELD LINES ---
# Draw E-field lines by creating curves that follow the field direction.
# Start test charges near the positive source.
num_field_lines = 16
for i in range(num_field_lines):
    angle = 2 * pi * i / num_field_lines
    start_pos = source1.pos + vector(0.6*cos(angle), 0.6*sin(angle), 0)
    field_line = curve(pos=[start_pos], color=color.orange, radius=0.05)
    
    current_pos = start_pos
    # Trace the line for a fixed number of steps or until it hits a charge
    for _ in range(200):
        E_vec = calculate_E(current_pos, sources)
        if mag(E_vec) == 0: break
        # Move a small step in the direction of the E-field
        current_pos = current_pos + norm(E_vec) * 0.3
        field_line.append(current_pos)
        # Stop if we get too close to the negative charge
        if mag(current_pos - source2.pos) < 0.6: break

print("Equipotential map and E-field lines generated.")
