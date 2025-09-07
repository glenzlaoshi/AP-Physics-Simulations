glowscript VPython

# AP Physics 1 - Unit 7: Torque and Rotation
# Simulation 7.1: Rotational Kinematics
#
# Skeleton Program

# VISUALS
# A disk that will rotate around the z-axis
disk = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.2), radius=4, color=color.purple)
# A reference line on the disk to make the rotation easy to see
ref_line = box(pos=vector(2,0,0.1), size=vector(4, 0.2, 0.2), color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

# Rotational properties of the disk
disk.m = 2.0 # Mass
# For a solid disk, the moment of inertia is I = 0.5 * M * R^2
disk.I = 0.5 * disk.m * disk.radius**2

# --- STUDENT TASK 1: Define Rotational Dynamics ---
# We will apply a constant torque to the disk.
# Torque is the rotational equivalent of force.
torque = 5.0 # N*m (applied in the positive z-direction, causing counter-clockwise rotation)

# The disk starts from rest.
omega = 0 # Angular velocity
alpha = 0 # Angular acceleration
theta = 0 # Angle of rotation


# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 2: Calculate Angular Acceleration ---
    # Use the rotational version of Newton's Second Law: tau = I * alpha
    # Solve for alpha.
    # alpha = torque / disk.I
    
    
    # --- STUDENT TASK 3: Update Rotational Motion ---
    # Use the rotational kinematic equations, which are analogous to the linear ones.
    
    # 1. Update angular velocity.
    #    omega = omega + alpha * dt
    
    # 2. Update the angle of rotation.
    #    theta = theta + omega * dt
    
    
    # --- STUDENT TASK 4: Update Visuals and Time ---
    # Rotate the disk and the reference line by the angle `theta`.
    # The `rotate` function modifies the object's orientation.
    # disk.rotate(angle=omega*dt, axis=vector(0,0,1))
    # ref_line.rotate(angle=omega*dt, axis=vector(0,0,1))
    
    # Update time.
    # t = t + dt


print("Simulation finished.")
