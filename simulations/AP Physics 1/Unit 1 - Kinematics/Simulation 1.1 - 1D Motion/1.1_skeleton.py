glowscript VPython

# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.1: 1D Motion
#
# Skeleton Program

# OBJECTS
# The ground is a long, flat box.
ground = box(pos=vector(0, -0.5, 0), size=vector(20, 0.1, 4), color=color.green)

# The car is a smaller box.
car = box(pos=vector(-9, 0, 0), size=vector(1, 0.5, 0.75), color=color.blue)

# PARAMETERS & INITIAL CONDITIONS
# Time parameters
t = 0           # starting time
dt = 0.01       # time step

# Motion parameters for the car
# --- STUDENT TASK 1: Define initial velocity ---
# Create a vector for the car's initial velocity.
# For constant velocity, let's say 2 m/s in the x-direction.
# car.velocity = vector(2, 0, 0)


# --- STUDENT TASK 2: Define acceleration ---
# Create a vector for the car's acceleration.
# For now, let's use zero acceleration (constant velocity).
# car.acceleration = vector(0, 0, 0)


# ANIMATION LOOP
# The loop will run as long as the car is on the screen.
while car.pos.x < 10:
    
    # Set the animation rate. 100 frames per second.
    rate(100)
    
    # --- STUDENT TASK 3: Update motion ---
    # To make the car move, you need to update its velocity and position
    # in each time step 'dt'.
    
    # 1. Update velocity: New_Velocity = Old_Velocity + Acceleration * dt
    # car.velocity = car.velocity + car.acceleration * dt
    
    # 2. Update position: New_Position = Old_Position + Velocity * dt
    # car.pos = car.pos + car.velocity * dt
    
    
    # --- STUDENT TASK 4: Update time ---
    # Advance the clock by one time step.
    # t = t + dt
    
    
# --- END OF SIMULATION ---
# After the loop, you can print final values.
print("Simulation finished.")
# print("Final time:", t)
# print("Final position:", car.pos)

