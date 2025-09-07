glowscript VPython

# AP Physics C: E&M - Unit 3: Electric Circuits
# Simulation C-EM.3: The LR Circuit
#
# Intermediate Program

# --- CIRCUIT PARAMETERS ---
R = 10
L = 2
V_battery = 10

# The time constant for an LR circuit is tau = L/R.
tau = L / R
print(f"Time Constant (tau = L/R): {tau:.2f} s")

# --- INITIAL CONDITIONS ---
t = 0
dt = 0.001
I = 0

# --- GRAPHING ---
graph(title="LR Circuit: Energizing Phase", xtitle="Time (s)", ytitle="Current (A)")
I_curve = gcurve(color=color.cyan)

# --- ENERGIZING PHASE ---
# Let's model the first 3*tau seconds of the inductor energizing.
while t < 3 * tau:
    rate(1000)
    
    # From Kirchhoff's loop rule: V_batt - I*R - L*(dI/dt) = 0
    # So, dI/dt = (V_batt - I*R) / L
    dI_dt = (V_battery - I*R) / L
    
    # Update the current
    I = I + dI_dt * dt
    
    # Plot and update time
    I_curve.plot(t, I)
    t = t + dt

print(f"After energizing, I = {I:.2f} A")
print(f"Max possible current (V/R) = {V_battery/R:.2f} A")

# --- STUDENT TASK: Implement the De-energizing Phase ---
# Now, the battery is removed and the inductor is shorted across the resistor.

# 1. Write a new `while` loop that runs for another 3*tau seconds.

# 2. Inside the loop, recalculate dI/dt.
#    - The loop rule is now: -I*R - L*(dI/dt) = 0
#    - So, `dI_dt = -I*R / L`

# 3. Update the current `I` using your new `dI_dt`.
#    `I = I + dI_dt * dt`

# 4. Plot the new current and update time.
#    `I_curve.plot(t, I)`
#    `t = t + dt`

# Add your de-energizing loop here!

print("Simulation finished.")
