glowscript VPython

# AP Physics 2 - Unit 3: Electric Force, Field, and Potential
# Simulation 3.1: Electric Fields
#
# Complete Program: E-Field Mapping

# --- SETUP ---
scene.title = "Electric Field Mapper"
scene.caption = "Drag the source charges (red and blue spheres) to see the E-field map update in real time."

# PARAMETERS
k = 9e9 # Coulomb's constant

# --- SOURCE CHARGES ---
# Create draggable source charges
source1 = sphere(pos=vector(-2, 2, 0), radius=0.5, color=color.red)
source1.q = 2e-9

source2 = sphere(pos=vector(2, -2, 0), radius=0.5, color=color.blue)
source2.q = -2e-9

sources = [source1, source2]

# --- E-FIELD MAP ---
# Create a grid of arrows to represent the field.
field_arrows = []
grid_spacing = 1.5
for x in arange(-10, 11, grid_spacing):
    for y in arange(-10, 11, grid_spacing):
        # Don't draw an arrow right on top of a source charge
        is_on_source = False
        for s in sources:
            if mag(vector(x,y,0) - s.pos) < 1:
                is_on_source = True
        if not is_on_source:
            arrow_pos = vector(x, y, 0)
            # Create a placeholder arrow
            f_arrow = arrow(pos=arrow_pos, axis=vector(0,0,0), color=color.orange, shaftwidth=0.05)
            field_arrows.append(f_arrow)

# --- CALCULATION FUNCTION ---
def calculate_E_field(position, source_charges):
    """Calculates the net E-field vector at a given position from a list of sources."""
    E_net = vector(0,0,0)
    for s in source_charges:
        r_vec = position - s.pos
        r_mag = mag(r_vec)
        if r_mag < 0.1: return vector(0,0,0) # Avoid singularity
        r_hat = norm(r_vec)
        # E = k*q/r^2 * r_hat
        E_source = k * s.q / r_mag**2 * r_hat
        E_net = E_net + E_source
    return E_net

# --- UPDATE FUNCTION ---
def update_field_map():
    """Recalculates and updates all the arrows in the field map."""
    for f_arrow in field_arrows:
        E_at_point = calculate_E_field(f_arrow.pos, sources)
        
        # Color and scale the arrow based on field strength
        E_mag = mag(E_at_point)
        # Use a logarithmic scale for color to handle large variations
        color_val = log(E_mag + 1)
        f_arrow.color = vector(color_val, 0.5, 1-color_val) # Maps strength to a color gradient
        
        # Scale the arrow's length for better visualization
        arrow_scale = 1.5 / (E_mag**0.5 + 1) # Non-linear scaling
        f_arrow.axis = norm(E_at_point) * arrow_scale

# --- DRAGGING LOGIC ---
# Make the source charges draggable
dragged_obj = None

def grab(evt):
    global dragged_obj
    for s in sources:
        if s.pos == scene.mouse.pick.pos:
            dragged_obj = s
            break

def move(evt):
    global dragged_obj
    if dragged_obj:
        dragged_obj.pos = scene.mouse.pos
        dragged_obj.pos.z = 0
        update_field_map() # Update the map as you drag

def drop(evt):
    global dragged_obj
    dragged_obj = None

scene.bind('mousedown', grab)
scene.bind('mousemove', move)
scene.bind('mouseup', drop)

# --- INITIAL RUN ---
update_field_map()
print("E-Field map generated. Drag the charges to see it update.")
