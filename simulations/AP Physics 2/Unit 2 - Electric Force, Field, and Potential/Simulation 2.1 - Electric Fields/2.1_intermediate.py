glowscript VPython

# AP Physics 2 - Unit 3: Electric Force, Field, and Potential
# Simulation 3.1: Electric Fields
#
# Intermediate Program

# PARAMETERS
k = 9e9

# VISUALS
# A dipole configuration
source1 = sphere(pos=vector(-2, 0, 0), radius=0.5, color=color.red)
source1.q = 2e-9

source2 = sphere(pos=vector(2, 0, 0), radius=0.5, color=color.blue)
source2.q = -2e-9

sources = [source1, source2]

# A test charge that we can drag around
test_charge = sphere(pos=vector(0, 3, 0), radius=0.2, color=color.yellow, make_trail=True)
test_charge.q = 1e-9

# An arrow to represent the E-field at the test charge's location
E_arrow = arrow(shaftwidth=0.1, color=color.orange)

# --- Function to calculate E-field ---
def calculate_E_field(position, source_charges):
    E_net = vector(0,0,0)
    # --- STUDENT TASK 1: Sum the fields from all sources ---
    # Loop through each `s` in the `source_charges` list.
    # For each source, calculate the E-field it produces at `position`.
    # E = k * q_source / r^2, in the direction of r_hat.
    # Add this E-field vector to `E_net`.
    
    # for s in source_charges:
    #     r_vec = position - s.pos
    #     r_mag = mag(r_vec)
    #     if r_mag == 0: continue # Avoid division by zero
    #     r_hat = norm(r_vec)
    #     E_source = k * s.q / r_mag**2 * r_hat
    #     E_net = E_net + E_source
        
    return E_net

# --- Draggable Test Charge ---
# We can make the test charge draggable with the mouse.
scene.bind('mousemove', def():
    # This function runs every time the mouse moves
    # We'll make the test charge follow the mouse in the xy-plane
    test_charge.pos = scene.mouse.pos
    test_charge.pos.z = 0
)

# ANIMATION LOOP
while True:
    rate(100)
    
    # --- STUDENT TASK 2: Update the E-field Arrow ---
    # 1. Calculate the E-field at the test charge's current position.
    #    E_at_point = calculate_E_field(test_charge.pos, sources)
    
    # 2. Update the E-field arrow's position and axis.
    #    E_arrow.pos = test_charge.pos
    #    E_arrow.axis = E_at_point * 1e-4 # Scale for visibility
    
    # For now, use a placeholder
    E_arrow.pos = test_charge.pos
    E_arrow.axis = vector(1,0,0)

