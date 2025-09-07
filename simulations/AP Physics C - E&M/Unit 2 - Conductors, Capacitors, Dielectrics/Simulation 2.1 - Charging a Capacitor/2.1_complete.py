glowscript VPython

# AP Physics C: E&M - Unit 2: Circuits
# Simulation 2.1: RC Circuit
#
# Complete Program

# --- SETUP ---
scene.title = "RC Circuit Charging and Discharging"

# CIRCUIT PARAMETERS
R = 1000   # Ohms
C = 5e-3   # Farads
V_battery = 10 # Volts
tau = R * C

# Add a caption to display the time constant
scene.caption = f"Time Constant (tau = RC) = {tau:.1f} seconds. This is the time to charge to ~63% of max voltage."

# INITIAL CONDITIONS
t = 0
dt = 0.05 # Smaller dt for more accuracy
Q = 0

# --- GRAPHING SETUP ---
g = graph(title="Capacitor Voltage and Current vs. Time", xtitle="Time (s)", fast=False)
Vc_curve = gcurve(graph=g, color=color.blue, label="Capacitor Voltage (V)")
I_curve = gcurve(graph=g, color=color.red, label="Current (A)")

# --- UI CONTROLS ---
charging = True
running = True

def toggle_charge(button):
    global charging
    charging = not charging
    if charging:
        button.text = "<b>State:</b> Charging"
    else:
        button.text = "<b>State:</b> Discharging"

button(text="<b>State:</b> Charging", bind=toggle_charge)

# --- VISUAL REPRESENTATION ---
# We can make a simple visual to show the state.
cap_box = box(pos=vector(-2,0,0), size=vector(1,2,2), color=color.gray(0.8))
cap_label = label(pos=cap_box.pos, text="Vc", yoffset=1.5*cap_box.size.y)
current_arrow = arrow(pos=vector(0,-2,0), axis=vector(0,4,0), color=color.yellow, shaftwidth=0.2)

# ANIMATION LOOP
while t < 8 * tau: # Run for a long time
    rate(200)
    
    # --- Physics Calculation ---
    # 1. Calculate capacitor voltage
    Vc = Q / C
    
    # 2. Calculate current based on state
    if charging:
        # Current is driven by difference between battery and capacitor
        I = (V_battery - Vc) / R
        # Charge is increasing
        Q += I * dt
    else: # Discharging
        # Current is driven by capacitor voltage only
        I = Vc / R
        # Charge is decreasing
        Q -= I * dt
    
    # Prevent charge from going negative due to numerical error
    if Q < 0: Q = 0
    
    # --- Update Graph ---
    Vc_curve.plot(t, Vc)
    I_curve.plot(t, I)
    
    # --- Update Visuals ---
    # Color the capacitor based on its voltage
    cap_box.color = vector(Vc/V_battery, Vc/V_battery, 0) # Becomes more yellow as Vc increases
    cap_label.text = f"Vc = {Vc:.2f} V"
    # Make the arrow size proportional to current
    current_arrow.shaftwidth = 0.1 + 50*abs(I)
    if I < 0: current_arrow.color = color.cyan
    else: current_arrow.color = color.yellow
    
    # Update time
    t += dt

print("Simulation finished.")
