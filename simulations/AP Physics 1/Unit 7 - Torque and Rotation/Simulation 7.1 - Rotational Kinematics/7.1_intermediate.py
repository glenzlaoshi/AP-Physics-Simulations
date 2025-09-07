glowscript VPython

# AP Physics 1 - Unit 7: Torque and Rotation
# Simulation 7.1: Rotational Kinematics
#
# Intermediate Program

# VISUALS
disk = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.2), radius=4, color=color.purple)
ref_line = box(pos=vector(2,0,0.1), size=vector(4, 0.2, 0.2), color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

disk.m = 2.0
disk.I = 0.5 * disk.m * disk.radius**2

# Apply a constant torque
torque_mag = 5.0

# The disk starts from rest
omega = 0 # angular velocity
theta = 0 # angle

# Calculate the constant angular acceleration from the torque
# tau = I * alpha  =>  alpha = tau / I
alpha = torque_mag / disk.I

print(f"Moment of Inertia (I): {disk.I:.2f} kg*m^2")
print(f"Constant Angular Acceleration (alpha): {alpha:.2f} rad/s^2")

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # Update rotational kinematics
    omega = omega + alpha * dt
    d_theta = omega * dt # change in angle for this time step
    theta = theta + d_theta
    
    # Rotate the objects. We rotate by the small change in angle `d_theta` each frame.
    disk.rotate(angle=d_theta, axis=vector(0,0,1))
    ref_line.rotate(angle=d_theta, axis=vector(0,0,1))
    
    t = t + dt

# --- STUDENT TASK: Graph the Motion ---
# The relationship between theta, omega, and alpha is analogous to x, v, and a
# in linear motion. Let's prove it with graphs.

# 1. Set up a graph before the loop:
#    `graph(title='Rotational Motion', xtitle='time', ytitle='value')`
#    `theta_curve = gcurve(color=color.blue, label='angle (rad)')`
#    `omega_curve = gcurve(color=color.red, label='ang. vel (rad/s)')`
#    `alpha_curve = gcurve(color=color.green, label='ang. accel (rad/s^2)')`

# 2. Inside the loop, plot the values:
#    `theta_curve.plot(t, theta)`
#    `omega_curve.plot(t, omega)`
#    `alpha_curve.plot(t, alpha)`

# 3. Analyze the graphs:
#    - Is the angular acceleration constant?
#    - Is the angular velocity a straight line (linear function of time)?
#    - Is the angle a curve (quadratic function of time)?

print("Simulation finished.")
