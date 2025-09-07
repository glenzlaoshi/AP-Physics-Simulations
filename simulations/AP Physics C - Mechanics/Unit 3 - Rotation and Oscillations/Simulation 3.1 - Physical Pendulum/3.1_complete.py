glowscript VPython

# --- Click to Start / Pause ---
# Wait for the first click to start the simulation
scene.waitfor('click')

# Global variable to control the running state
running = True

# Function to toggle the running state on click
def toggle_pause(evt):
    global running
    running = not running

# Bind the function to the click event
scene.bind('click', toggle_pause)
# --------------------------------


# AP Physics C: Mechanics - Units 5-6
# Simulation C-M.3: The Physical Pendulum
#
# Complete Program

# --- SETUP ---
scene.title = "Physical Pendulum vs. Simple Pendulum"

pivot_pos = vector(0, 5, 0)
pivot_marker = sphere(pos=pivot_pos, radius=0.1, color=color.gray(0.7))

# --- Physical Pendulum (a uniform rod) ---
rod_L = 4.0
rod_m = 1.0
rod = cylinder(pos=pivot_pos, axis=vector(0, -rod_L, 0), radius=0.2, color=color.orange)
cm_marker = sphere(pos=pivot_pos + rod.axis/2, radius=0.25, color=color.cyan)

# --- Simple Pendulum (for comparison) ---
# Has the same length and mass, but all mass is at the end.
simple_bob = sphere(pos=pivot_pos + rod.axis, radius=0.3, color=color.white)
simple_rod = cylinder(pos=pivot_pos, axis=simple_bob.pos-pivot_pos, radius=0.05, color=color.gray(0.5))

# --- PARAMETERS & INITIAL CONDITIONS ---
t = 0
dt = 0.01
g = 9.8

# Initial angle for both pendulums
initial_theta = radians(60)

# State variables for the physical pendulum
pp = {'theta': initial_theta, 'omega': 0}
# State variables for the simple pendulum
sp = {'theta': initial_theta, 'omega': 0}

# Set initial rotation
rod.rotate(angle=pp['theta'], axis=vector(0,0,1), origin=pivot_pos)
cm_marker.pos = pivot_pos + rod.axis/2
simple_rod.rotate(angle=sp['theta'], axis=vector(0,0,1), origin=pivot_pos)
simple_bob.pos = pivot_pos + simple_rod.axis

# --- THEORETICAL CALCULATIONS ---
# Moment of inertia for a rod pivoted at its end
I_rod = (1/3) * rod_m * rod_L**2
# Distance from pivot to CM for the rod
d_rod = rod_L / 2
# Period of the physical pendulum
T_physical = 2 * pi * sqrt(I_rod / (rod_m * g * d_rod))

# Period of the simple pendulum (I = mL^2, d = L)
T_simple = 2 * pi * sqrt(rod_L / g)

scene.caption = f"Physical Pendulum Period (Orange): {T_physical:.2f} s\n" \
                f"Simple Pendulum Period (White): {T_simple:.2f} s"

# --- GRAPHING ---
g = graph(title="Angle vs. Time", xtitle="Time (s)", ytitle="Angle (rad)")
pp_curve = gcurve(color=color.orange, label="Physical Pendulum")
sp_curve = gcurve(color=color.white, label="Simple Pendulum")

# --- ANIMATION LOOP ---
while t < 10:
    rate(100)
    if running:
        # --- Physical Pendulum Physics ---
        r_vec = cm_marker.pos - pivot_pos
        torque = cross(r_vec, vector(0, -rod_m * g, 0))
        alpha_pp = torque.z / I_rod
        pp['omega'] += alpha_pp * dt
        d_theta_pp = pp['omega'] * dt
        pp['theta'] += d_theta_pp
        rod.rotate(angle=d_theta_pp, axis=vector(0,0,1), origin=pivot_pos)
        cm_marker.pos = pivot_pos + rod.axis/2
        
        # --- Simple Pendulum Physics ---
        alpha_sp = -(g / rod_L) * sin(sp['theta'])
        sp['omega'] += alpha_sp * dt
        d_theta_sp = sp['omega'] * dt
        sp['theta'] += d_theta_sp
        simple_rod.rotate(angle=d_theta_sp, axis=vector(0,0,1), origin=pivot_pos)
        simple_bob.pos = pivot_pos + simple_rod.axis
        
        # --- Plotting ---
        pp_curve.plot(t, pp['theta'])
        sp_curve.plot(t, sp['theta'])
        
        t += dt

print("Simulation finished. Note that the physical pendulum is slower because its mass is distributed, giving it a larger moment of inertia.")
