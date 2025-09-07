glowscript VPython

# AP Physics C: E&M - Unit 5: Electromagnetism
# Simulation C-EM.5: The Maxwell-Ampere Law
#
# Complete Program

# --- SETUP ---
scene.title = "Induced Magnetic Field from a Changing Electric Field"
scene.caption = "A capacitor is charged by a current. The growing E-field between the plates induces a curling B-field."

# --- CONSTANTS & PARAMETERS ---
mu_0 = 4*pi*1e-7
epsilon_0 = 8.85e-12

# --- CAPACITOR SETUP ---
plate_radius = 2.0
plate_sep = 0.5
plate_L = plate(pos=vector(0,0,-plate_sep/2), axis=vector(0,0,-1), radius=plate_radius, color=vector(0.7,0.7,0.3))
plate_R = plate(pos=vector(0,0,plate_sep/2), axis=vector(0,0,1), radius=plate_radius, color=vector(0.3,0.3,0.7))

# --- CHARGING PROCESS (from RC circuit) ---
# We model the charging from an RC circuit to get a non-constant dE/dt.
R = 1000
C = 5e-3
V_battery = 10
tau = R*C

Q = 0 # Charge on the capacitor
I = 0 # Current

# --- VISUALIZATION ---
# Arrows to represent the E-field
E_arrows = []
for r in arange(0, plate_radius, 0.8):
    if r==0: continue
    for theta in arange(0, 2*pi, pi/4):
        pos = vector(r*cos(theta), r*sin(theta), 0)
        E_arrows.append(arrow(pos=pos, axis=vector(0,0,0), color=color.orange, shaftwidth=0.02))

# Arrows to represent the induced B-field
B_arrows = []
r_b_loop = 1.5 # Radius where we will draw the B-field
loop_vis = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=r_b_loop, color=color.cyan, thickness=0.02, opacity=0.5)
for theta in arange(0, 2*pi, pi/6):
    pos = vector(r_b_loop*cos(theta), r_b_loop*sin(theta), 0)
    B_arrows.append(arrow(pos=pos, axis=vector(0,0,0), color=color.cyan, shaftwidth=0.05))

# --- ANIMATION LOOP ---
t = 0
dt = 0.05

while t < 3*tau:
    rate(50)
    
    # --- RC Circuit Physics ---
    # Calculate current and charge from the RC circuit behavior
    Vc = Q / C
    I = (V_battery - Vc) / R
    Q += I * dt
    
    # --- Maxwell-Ampere Law Physics ---
    Area = pi * plate_radius**2
    E_mag = Q / (Area * epsilon_0)
    
    # The rate of change of the E-field is dE/dt = I / (A*e0)
    dE_dt = I / (Area * epsilon_0)
    
    # The rate of change of flux through our Amperian loop of radius r_b_loop
    dFlux_dt = dE_dt * (pi * r_b_loop**2)
    
    # From Maxwell-Ampere Law, B * (2*pi*r) = mu_0 * e0 * dFlux_dt
    # Note: mu_0 * e0 = 1/c^2
    B_mag = (mu_0 * epsilon_0 * dFlux_dt) / (2 * pi * r_b_loop)
    
    # --- Update Visuals ---
    # Update E-field arrows (they point from positive to negative plate)
    E_axis = vector(0,0,-E_mag*1e-7) # Scale for visibility
    for a in E_arrows: a.axis = E_axis
    
    # Update B-field arrows (they curl around the E-field)
    for b_arrow in B_arrows:
        theta = atan2(b_arrow.pos.y, b_arrow.pos.x)
        # Right-hand rule: if E is into screen and increasing, B is CCW.
        B_dir = vector(-sin(theta), cos(theta), 0)
        b_arrow.axis = B_dir * B_mag * 5e6 # Scale for visibility
    
    # Update plate colors based on charge
    charge_color = min(1, Q/(C*V_battery))
    plate_R.color = vector(0.3+charge_color*0.4, 0.3+charge_color*0.4, 0.7)
    plate_L.color = vector(0.7, 0.7-charge_color*0.4, 0.3-charge_color*0.4)
    
    t += dt

scene.caption = "Simulation finished. The B-field is strongest when the E-field is changing most rapidly (at the beginning)."
print("Simulation finished.")
