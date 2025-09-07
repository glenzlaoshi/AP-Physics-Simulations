glowscript VPython

# AP Physics 2 - Unit 4: Electric Circuits
# Simulation 4.1: RC Circuit
#
# Skeleton Program

# This simulation models the voltage and current in a simple RC circuit
# during charging and discharging.

# CIRCUIT PARAMETERS
R = 1000   # Resistance in Ohms
C = 5e-3   # Capacitance in Farads (5 mF)
V_battery = 10 # Voltage of the battery in Volts

# INITIAL CONDITIONS
t = 0
dt = 0.1 # Time step
Q = 0     # Initial charge on the capacitor is zero

# --- SETUP THE GRAPH ---
# We will plot Voltage across the capacitor and Current in the circuit
graph(title="RC Circuit Behavior", xtitle="Time (s)")
Vc_curve = gcurve(color=color.blue, label="Capacitor Voltage (V)")
I_curve = gcurve(color=color.red, label="Current (A)")

# --- SIMULATION STATE ---
# Let's model the charging phase first.
charging = True

# ANIMATION LOOP
while t < 30:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate Vc and I ---
    # 1. The voltage across the capacitor is Vc = Q / C.
    #    Vc = Q / C
    
    # 2. The current `I` depends on whether we are charging or discharging.
    #    - During CHARGING, the voltage across the resistor is (V_battery - Vc).
    #      So, by Ohm's Law, I = (V_battery - Vc) / R.
    #    - During DISCHARGING, the battery is removed. The capacitor provides the voltage.
    #      So, I = Vc / R.
    
    #    Use an if/else statement based on the `charging` variable.
    #    if charging:
    #        I = (V_battery - Vc) / R
    #    else:
    #        I = Vc / R
    
    
    # --- STUDENT TASK 2: Update the Charge on the Capacitor ---
    # Current is the rate of flow of charge: I = dQ / dt.
    # So, the change in charge in a small time step dt is dQ = I * dt.
    
    # 1. Calculate dQ.
    #    dQ = I * dt
    
    # 2. Update the total charge Q.
    #    - During CHARGING, charge increases: Q = Q + dQ
    #    - During DISCHARGING, charge decreases: Q = Q - dQ
    #    (Note the sign change!)
    
    
    # --- STUDENT TASK 3: Plotting and Time ---
    # 1. Plot the capacitor voltage and current vs. time.
    #    Vc_curve.plot(t, Vc)
    #    I_curve.plot(t, I)
    
    # 2. Advance time.
    #    t = t + dt
    
    # 3. Add logic to switch from charging to discharging.
    #    if t > 15:
    #        charging = False

print("Simulation finished.")
