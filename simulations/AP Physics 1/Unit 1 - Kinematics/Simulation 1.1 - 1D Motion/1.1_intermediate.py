glowscript VPython

# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.1: 1D Motion
#
# Intermediate Program: Constant Velocity

# OBJECTS
ground = box(pos=vector(0, -0.5, 0), size=vector(20, 0.1, 4), color=color.green)
car = box(pos=vector(-9, 0, 0), size=vector(1, 0.5, 0.75), color=color.blue)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

# --- Constant Velocity Motion ---
# The car starts with a constant velocity in the x-direction.
car.velocity = vector(2, 0, 0) 

# For constant velocity, acceleration is zero.
car.acceleration = vector(0, 0, 0)

# ANIMATION LOOP - CONSTANT VELOCITY
# This loop runs for 5 seconds.
while t < 5:
    rate(100)
    
    # Position is updated based on constant velocity.
    # New_Position = Old_Position + Velocity * dt
    car.pos = car.pos + car.velocity * dt
    
    # Advance the clock
    t = t + dt

print("Part 1 (Constant Velocity) finished.")
print("Time:", t, "s")
print("Position:", car.pos)


# --- STUDENT TASK: Add Accelerated Motion ---
# Now, let's give the car a non-zero acceleration.
#
# 1. Define a new acceleration vector. Let's say 0.5 m/s^2.
# car.acceleration = vector(0.5, 0, 0)
#
# 2. Write a new `while` loop that runs as long as the car is on the screen.
#
# 3. Inside the new loop, you must update BOTH velocity and position.
#    car.velocity = car.velocity + car.acceleration * dt
#    car.pos = car.pos + car.velocity * dt
#
# 4. Don't forget to update time!
#    t = t + dt

# --- Your new animation loop goes here ---
# while car.pos.x < 10:
#     rate(100)
#     ... your code here ...


print("Simulation finished.")

