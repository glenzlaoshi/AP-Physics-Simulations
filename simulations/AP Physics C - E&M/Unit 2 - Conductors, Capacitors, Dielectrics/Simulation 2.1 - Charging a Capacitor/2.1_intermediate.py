glowscript VPython

# AP Physics C: E&M - Unit 2: Circuits
# Simulation 2.1: RC Circuit
#
# Intermediate Program

# CIRCUIT PARAMETERS
R = 1000
C = 5e-3
V_battery = 10

# The "time constant" of the circuit, tau = R*C, is a measure of how quickly
# the capacitor charges or discharges.
tau = R * C
print(f"Time Constant (tau = RC): {tau:.2f} s")

# INITIAL CONDITIONS
t = 0
dt = 0.1
Q = 0

# GRAPHING
graph(title="RC Circuit: Charging Phase", xtitle="Time (s)")
Vc_curve = gcurve(color=color.blue, label="Capacitor Voltage (V)")
I_curve = gcurve(color=color.red, label="Current (A)")

# --- CHARGING PHASE ---
# Let's model the first 3*tau seconds of charging.
while t < 3 * tau:
    rate(100)
    
    # Voltage across the capacitor is Vc = Q/C
    Vc = Q / C
    
    # Current is driven by the difference between battery and capacitor voltage
    I = (V_battery - Vc) / R
    
    # Change in charge is dQ = I * dt
    dQ = I * dt
    
    # Add charge to the capacitor
    Q = Q + dQ
    
    # Plotting and time update
    Vc_curve.plot(t, Vc)
    I_curve.plot(t, I)
    t = t + dt

print(f"After charging, Vc = {Q/C:.2f} V")

# --- STUDENT TASK: Implement the Discharging Phase ---
# Now, the battery is removed and the capacitor discharges through the resistor.

# 1. Write a new `while` loop that runs for another 3*tau seconds.

# 2. Inside the loop, recalculate Vc and I.
#    - Vc is still Q/C.
#    - But now, the battery is gone! The current is driven ONLY by the capacitor's voltage.
#      `I = Vc / R`

# 3. Update the charge Q.
#    - The capacitor is now LOSING charge.
#      `dQ = I * dt`
#      `Q = Q - dQ`

# 4. Plot the new values and update time.
#    `Vc_curve.plot(t, Vc)`
#    `I_curve.plot(t, I)`
#    `t = t + dt`

# Add your discharging loop here!

print("Simulation finished.")
