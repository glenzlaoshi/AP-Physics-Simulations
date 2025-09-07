glowscript VPython

# AP Physics C: E&M - Unit 3: Electric Circuits
# Simulation C-EM.3: The LR Circuit
#
# Skeleton Program

# This simulation models the current in a simple LR circuit when it is
# connected to and disconnected from a battery.

# --- CIRCUIT PARAMETERS ---
R = 10     # Resistance in Ohms
L = 2      # Inductance in Henrys
V_battery = 10 # Voltage of the battery in Volts

# --- INITIAL CONDITIONS ---
t = 0
dt = 0.001 # A small time step is needed
I = 0       # Initial current in the circuit is zero

# --- SETUP THE GRAPH ---
graph(title="LR Circuit Behavior", xtitle="Time (s)", ytitle="Current (A)")
I_curve = gcurve(color=color.cyan, label="Inductor Current")

# --- SIMULATION STATE ---
# True when connected to battery, False when battery is removed and circuit is shorted.
energizing = True

# --- ANIMATION LOOP ---
while t < 1.0:
    rate(1000)
    
    # --- STUDENT TASK 1: Apply Kirchhoff's Loop Rule ---
    # The sum of voltages around a closed loop is zero.
    
    # 1. During the ENERGIZING phase (connected to battery):
    #    V_battery - I*R - V_inductor = 0
    #    The voltage across the inductor is V_inductor = L * (dI/dt).
    #    So, V_battery - I*R - L*(dI/dt) = 0.
    
    # 2. During the DE-ENERGIZING phase (battery removed):
    #    -I*R - L*(dI/dt) = 0
    
    
    # --- STUDENT TASK 2: Calculate the Rate of Change of Current (dI/dt) ---
    # Rearrange the loop rule equation to solve for dI/dt.
    
    # 1. For the ENERGIZING phase:
    #    dI_dt = (V_battery - I*R) / L
    
    # 2. For the DE-ENERGIZING phase:
    #    dI_dt = -I*R / L
    
    # Use an if/else statement based on the `energizing` variable.
    # if energizing:
    #     dI_dt = (V_battery - I*R) / L
    # else:
    #     dI_dt = -I*R / L
    
    
    # --- STUDENT TASK 3: Update the Current ---
    # Use the definition of the derivative: dI = (dI/dt) * dt
    
    # 1. Calculate the change in current, dI.
    #    dI = dI_dt * dt
    
    # 2. Add this change to the total current.
    #    I = I + dI
    
    
    # --- STUDENT TASK 4: Plotting and Time ---
    # 1. Plot the current vs. time.
    #    I_curve.plot(t, I)
    
    # 2. Advance time.
    #    t = t + dt
    
    # 3. Add logic to switch from energizing to de-energizing.
    #    if t > 0.5:
    #        energizing = False

print("Simulation finished.")
