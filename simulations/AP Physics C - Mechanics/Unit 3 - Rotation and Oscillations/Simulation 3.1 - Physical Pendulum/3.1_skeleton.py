glowscript VPython

# AP Physics C: Mechanics - Units 5-6
# Simulation C-M.3: The Physical Pendulum
#
# Skeleton Program

# A physical pendulum is any rigid body that swings about a pivot.
# Unlike a simple pendulum, its mass is distributed.

# --- SETUP ---
# We'll model a uniform rod as our physical pendulum.
pivot_pos = vector(0, 5, 0)
pivot_marker = sphere(pos=pivot_pos, radius=0.1, color=color.gray(0.7))

# Rod properties
rod_L = 4.0 # Length of the rod
rod_m = 1.0 # Mass of the rod

rod = cylinder(pos=pivot_pos, axis=vector(0, -rod_L, 0), radius=0.2, color=color.orange)

# The center of mass (CM) for a uniform rod is at its geometric center.
cm_pos = pivot_pos + rod.axis/2
cm_marker = sphere(pos=cm_pos, radius=0.25, color=color.cyan)

# --- PARAMETERS ---
t = 0
dt = 0.01
g = 9.8

# Initial conditions: release from rest at an angle `theta`.
theta = radians(30) # Initial angle
omega = 0 # Initial angular velocity

# Set the initial orientation
rod.rotate(angle=theta, axis=vector(0,0,1), origin=pivot_pos)

# --- ANIMATION LOOP ---
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate Gravitational Torque ---
    # Torque (tau) = r x F, where r is the vector from the pivot to where the force is applied,
    # and F is the force.
    # For gravity, the force Fg acts on the center of mass.
    
    # 1. Find the vector `r` from the pivot to the center of mass.
    #    r_vec = rod.pos + rod.axis/2 - pivot_pos
    
    # 2. Define the gravitational force vector `Fg`.
    #    Fg = vector(0, -rod_m * g, 0)
    
    # 3. Calculate the torque using the cross product.
    #    torque = cross(r_vec, Fg)
    #    (Note: Torque is a vector! Its z-component will drive the rotation).
    
    
    # --- STUDENT TASK 2: Calculate Angular Acceleration (alpha) ---
    # Use the rotational version of Newton's 2nd Law: tau_net = I * alpha
    
    # 1. Find the moment of inertia `I` for a rod pivoted at one end.
    #    The formula is I = (1/3) * m * L^2.
    #    I = (1/3) * rod_m * rod_L**2
    
    # 2. Solve for alpha: alpha = tau_net / I.
    #    alpha = torque.z / I # We only care about the z-component for this 2D rotation.
    
    
    # --- STUDENT TASK 3: Update Motion ---
    # Use rotational kinematics.
    # omega = omega + alpha * dt
    # theta = theta + omega * dt
    
    # And update the visuals based on the new angle.

print("Simulation finished.")
