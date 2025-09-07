glowscript VPython

# AP Physics 1 - Unit 7: Torque and Rotation
# Simulation 7.1: Rotational Kinematics
#
# Complete Program

# SCENE & VISUALS
scene.title = "Rotational Kinematics of a Solid Disk"

disk = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.2), radius=4, color=color.purple)
# Add a reference line to see the rotation clearly
ref_line = box(pos=vector(2,0,0.1), size=vector(4, 0.2, 0.2), color=color.yellow)
# Add an arrow to represent the applied torque
torque_arrow = arrow(pos=vector(0, 4.2, 0), axis=vector(-2,0,0), color=color.orange, shaftwidth=0.3)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

disk.m = 2.0 # Mass in kg
disk.I = 0.5 * disk.m * disk.radius**2 # Moment of inertia for a solid disk

# Apply a constant torque (in the z-direction, causing counter-clockwise rotation)
torque_vec = vector(0, 0, 5.0) # N*m

# The disk starts from rest
omega_vec = vector(0, 0, 0) # Angular velocity vector
theta = 0 # Total angle of rotation

# Calculate the constant angular acceleration vector from tau = I * alpha
alpha_vec = torque_vec / disk.I

scene.caption = f"A constant torque of {torque_vec.z} N*m is applied, causing a constant angular acceleration of {alpha_vec.z:.2f} rad/s^2."

# --- GRAPHING SETUP ---
rot_graph = graph(title="Rotational Motion vs. Time", xtitle="Time (s)")
# Create separate plotting windows for clarity
plot_theta = gdisplay(graph=rot_graph, y=0, height=200, ytitle="Angle (rad)", color=color.blue)
plot_omega = gdisplay(graph=rot_graph, y=200, height=200, ytitle="Ang. Vel (rad/s)", color=color.red)
plot_alpha = gdisplay(graph=rot_graph, y=400, height=200, ytitle="Ang. Accel (rad/s^2)", color=color.green)

theta_curve = gcurve(gdisplay=plot_theta, color=color.blue)
omega_curve = gcurve(gdisplay=plot_omega, color=color.red)
alpha_curve = gcurve(gdisplay=plot_alpha, color=color.green)

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # Update rotational kinematics (using vectors)
    omega_vec = omega_vec + alpha_vec * dt
    d_theta_vec = omega_vec * dt # Change in angle vector for this time step
    
    # Update the total angle scalar for plotting
    theta = theta + mag(d_theta_vec)
    
    # Rotate the objects. The axis of rotation is the z-axis.
    disk.rotate(angle=mag(d_theta_vec), axis=norm(torque_vec))
    ref_line.rotate(angle=mag(d_theta_vec), axis=norm(torque_vec))
    
    # Plot the scalar components of the rotational motion
    theta_curve.plot(t, theta)
    omega_curve.plot(t, omega_vec.z)
    alpha_curve.plot(t, alpha_vec.z)
    
    t = t + dt

# --- ANALYSIS ---
print("Simulation finished.")
print(f"Moment of Inertia (I): {disk.I:.2f} kg*m^2")
print(f"Final Angle: {theta:.2f} rad")
print(f"Final Angular Velocity: {omega_vec.z:.2f} rad/s")

# The graphs show that for a constant torque:
# - Angular acceleration is constant.
# - Angular velocity increases linearly.
# - Angle increases quadratically.
# This is perfectly analogous to 1D linear kinematics with constant acceleration.

