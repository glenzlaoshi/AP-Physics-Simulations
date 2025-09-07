glowscript VPython

# AP Physics C: E&M - Unit 3: Electric Circuits
# Simulation C-EM.3: The LR Circuit
#
# Complete Program

# --- SETUP ---
scene.title = "LR Circuit Current Buildup and Decay"

# --- CIRCUIT PARAMETERS ---
R = 10     # Ohms
L = 2      # Henrys
V_battery = 10 # Volts
tau = L / R

scene.caption = f"Time Constant (tau = L/R) = {tau:.2f} seconds. This is the time to reach ~63% of max current."

# --- INITIAL CONDITIONS ---
t = 0
dt = 0.001
I = 0

# --- GRAPHING SETUP ---
g = graph(title="Current vs. Time in an LR Circuit", xtitle="Time (s)", ytitle="Current (A)", fast=False)
I_curve = gcurve(graph=g, color=color.cyan, label="Current I(t)")
# Plot the theoretical maximum current
I_max = V_battery / R
max_line = gcurve(graph=g, color=color.red, label="Max Current (V/R)", linestyle='dotted')
max_line.plot([(0, I_max), (5*tau, I_max)])

# --- UI CONTROLS ---
energizing = True

def toggle_state(button):
    global energizing
    energizing = not energizing
    if energizing:
        button.text = "<b>State:</b> Energizing (Battery connected)"
    else:
        button.text = "<b>State:</b> Decaying (Battery removed)"

button(text="<b>State:</b> Energizing (Battery connected)", bind=toggle_state)

# --- VISUAL REPRESENTATION ---
# We can represent the inductor's stored energy (0.5*L*I^2) by its color
inductor_vis = box(pos=vector(-2,0,0), size=vector(2,1,1), color=color.gray(0.8))
inductor_label = label(pos=inductor_vis.pos, text="I = 0.00 A", yoffset=1.5)

# --- ANIMATION LOOP ---
while t < 5 * tau:
    rate(1000)
    
    # --- Physics Calculation using Kirchhoff's Loop Rule ---
    if energizing:
        # V_batt - I*R - L*(dI/dt) = 0
        dI_dt = (V_battery - I*R) / L
    else: # Decaying
        # -I*R - L*(dI/dt) = 0
        dI_dt = -I*R / L
    
    # Update current using the calculated derivative
    I += dI_dt * dt
    
    # Prevent current from going negative due to numerical error
    if I < 0: I = 0
    
    # --- Update Graph ---
    I_curve.plot(t, I)
    
    # --- Update Visuals ---
    # Color the inductor based on the current (related to stored energy)
    color_val = I / I_max
    inductor_vis.color = vector(color_val, 0.2, 1-color_val) # Becomes more red as I increases
    inductor_label.text = f"I = {I:.2f} A"
    
    # Update time
    t += dt

print("Simulation finished.")
