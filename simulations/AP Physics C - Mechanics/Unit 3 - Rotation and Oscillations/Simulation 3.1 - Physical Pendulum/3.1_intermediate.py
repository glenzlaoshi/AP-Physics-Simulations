glowscript VPython

# AP Physics C: Mechanics - Units 5-6
# Simulation C-M.3: The Physical Pendulum
#
# Intermediate Program

# --- SETUP ---
pivot_pos = vector(0, 5, 0)
pivot_marker = sphere(pos=pivot_pos, radius=0.1, color=color.gray(0.7))

rod_L = 4.0
rod_m = 1.0
rod = cylinder(pos=pivot_pos, axis=vector(0, -rod_L, 0), radius=0.2, color=color.orange)
cm_marker = sphere(radius=0.25, color=color.cyan)

# --- PARAMETERS ---
t = 0
dt = 0.01
g = 9.8

theta = radians(45)
omega = 0

# --- Moment of Inertia Calculation ---
# For a thin rod pivoted about its end, I = (1/3)mL^2.
I_rod = (1/3) * rod_m * rod_L**2
print(f"Moment of Inertia (I) = {I_rod:.2f} kg*m^2")

# Set initial rotation
rod.rotate(angle=theta, axis=vector(0,0,1), origin=pivot_pos)

# --- ANIMATION LOOP ---
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate Torque and Alpha ---
    # Torque = r x F. Here, r is the vector from pivot to CM, and F is gravity.
    r_vec = (rod.pos + rod.axis/2) - pivot_pos
    Fg_vec = vector(0, -rod_m * g, 0)
    
    # 1. Calculate the torque vector.
    #    torque = cross(r_vec, Fg_vec)
    
    # 2. Calculate the scalar angular acceleration, alpha.
    #    alpha = torque.z / I_rod
    
    # For now, use a placeholder value for alpha.
    alpha = 0 # Replace this!
    
    # --- STUDENT TASK 2: Update Motion ---
    # Once you have the correct alpha, the rest of the simulation works.
    # Uncomment the lines below.
    
    # omega = omega + alpha * dt
    # d_theta = omega * dt # The change in angle this frame
    # theta = theta + d_theta
    
    # rod.rotate(angle=d_theta, axis=vector(0,0,1), origin=pivot_pos)
    
    # Update the center of mass marker
    cm_marker.pos = pivot_pos + rod.axis/2
    
    t = t + dt

# --- STUDENT TASK 3: Analysis ---
# The theoretical period of a physical pendulum is T = 2*pi*sqrt(I / (mgd)),
# where d is the distance from the pivot to the center of mass.

# 1. Calculate the theoretical period.
#    d = rod_L / 2
#    T_theory = 2 * pi * sqrt(I_rod / (rod_m * g * d))

# 2. Graph the angle vs. time and measure the period from the graph.
#    Does your measurement match the theory?

print("Simulation finished.")
