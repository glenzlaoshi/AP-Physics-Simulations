glowscript VPython

# AP Physics 2 - Unit 5: Magnetism & Electromagnetism
# Simulation 5.2: Faraday's Law of Induction
#
# Complete Program

# --- SETUP ---
scene.title = "Faraday's Law: Move the Magnet"
scene.caption = "Drag the bar magnet through the coil. The induced EMF (voltage) is plotted.\nLenz's Law: The coil color shows the direction of induced current, which creates a B-field to oppose the change in flux."

# Coil
N = 20
coil_radius = 1.0
coil_pos = vector(0,0,0)
coil_rings = []
for i in range(N):
    z = i * 0.1 - (N-1)*0.05
    ring_obj = ring(pos=vector(0,0,z), axis=vector(0,0,1), radius=coil_radius, thickness=0.05, color=color.gray(0.7))
    coil_rings.append(ring_obj)

# Magnet (modeled as two monopoles)
magnet_strength = 100
N_pole = sphere(pos=vector(0,0,5), radius=0.5, color=color.red, qm=magnet_strength)
S_pole = sphere(pos=vector(0,0,6), radius=0.5, color=color.blue, qm=-magnet_strength)
magnet = compound([N_pole, S_pole], make_trail=False)

# --- B-Field Calculation ---
def get_B(pos):
    B_net = vector(0,0,0)
    for pole in [N_pole, S_pole]:
        r_vec = pos - pole.pos
        r_mag = mag(r_vec)
        if r_mag < 0.1: continue
        B_net += (pole.qm / r_mag**2) * norm(r_vec)
    return B_net

# --- SIMULATION VARIABLES ---
t = 0
dt = 0.01
flux_old = 0

# --- GRAPH & METER ---
g = graph(title="Induced EMF vs. Time", xtitle="Time (s)", ytitle="EMF (Volts)", fast=False, width=600, height=250)
emf_curve = gcurve(graph=g, color=color.orange)
emf_label = label(pos=vector(0,3,0), text="EMF: 0.00 V")

# --- DRAGGING LOGIC ---
dragged_obj = None
def grab(evt): global dragged_obj; dragged_obj = magnet
def move(evt): 
    global dragged_obj
    if dragged_obj: dragged_obj.pos = scene.mouse.pos; dragged_obj.pos.x=0; dragged_obj.pos.y=0
def drop(evt): global dragged_obj; dragged_obj = None

scene.bind('mousedown', grab); scene.bind('mousemove', move); scene.bind('mouseup', drop)

# --- ANIMATION LOOP ---
while True:
    rate(100)
    
    # --- Calculate Magnetic Flux ---
    # Approximate by finding the B-field at the center of the coil.
    B_at_center = get_B(coil_pos)
    B_normal = B_at_center.z # Component of B perpendicular to the coil area
    Area = pi * coil_radius**2
    flux_new = B_normal * Area
    
    # --- Calculate Induced EMF via Faraday's Law ---
    dFlux = flux_new - flux_old
    # Avoid division by zero on the first frame
    if dt > 0: 
        EMF = -N * dFlux / dt
    else:
        EMF = 0
    
    # Update flux_old for the next iteration
    flux_old = flux_new
    
    # --- Update Visuals (Lenz's Law) ---
    # The induced current creates a B-field to oppose the change in flux.
    # A positive EMF corresponds to a counter-clockwise current (viewed from +z).
    # This CCW current creates a B-field in the +z direction.
    # We color the coil based on the sign of the EMF.
    if EMF > 0.1: # Threshold to avoid noise
        for r in coil_rings: r.color = color.yellow # CCW current
    elif EMF < -0.1:
        for r in coil_rings: r.color = color.cyan # CW current
    else:
        for r in coil_rings: r.color = color.gray(0.7) # No current

    # Update the graph and label
    emf_curve.plot(t, EMF)
    emf_label.text = f"EMF: {EMF:.2f} V"
    
    t += dt
