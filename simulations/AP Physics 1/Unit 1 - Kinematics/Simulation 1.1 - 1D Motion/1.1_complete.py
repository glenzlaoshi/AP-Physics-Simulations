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


# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.1: 1D Motion
#
# Complete Program

# SCENE & OBJECTS
# The scene title will appear above the simulation
scene.title = "Simulation of 1D Motion: Constant Velocity and Constant Acceleration"
scene.caption = "Below the simulation, graphs show position, velocity, and acceleration vs. time."

ground = box(pos=vector(0, -0.5, 0), size=vector(20, 0.1, 4), color=color.green)
car = box(pos=vector(-9, 0, 0), size=vector(1, 0.5, 0.75), color=color.blue)
# Attach a trail to the car to visualize its path
attach_trail(car, color=color.yellow, radius=0.05)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

# --- Part 1: Constant Velocity ---
print("Starting Part 1: Constant Velocity")
car.velocity = vector(2, 0, 0)      # Constant velocity (2 m/s)
car.acceleration = vector(0, 0, 0)  # No acceleration

# GRAPHING SETUP
# We create a window for the graphs
graph_window = graph(title='Motion Graphs', xtitle='Time (s)', ytitle='Value')
# Create curve objects to plot data
pos_curve = gcurve(color=color.blue, label="Position (m)")
vel_curve = gcurve(color=color.red, label="Velocity (m/s)")
acc_curve = gcurve(color=color.purple, label="Acceleration (m/s^2)")

# ANIMATION LOOP 1: CONSTANT VELOCITY
# This loop runs for 4 seconds.
while t < 4:
    rate(100)
    if running:
        # Kinematic equations
        car.pos = car.pos + car.velocity * dt
        t = t + dt
        
        # Plot data
        pos_curve.plot(t, car.pos.x)
        vel_curve.plot(t, car.velocity.x)
        acc_curve.plot(t, car.acceleration.x)

print("End of Part 1. Position:", car.pos)
print("---")


# --- Part 2: Constant Acceleration ---
print("Starting Part 2: Constant Acceleration")
car.acceleration = vector(0.5, 0, 0) # Positive acceleration (0.5 m/s^2)

# ANIMATION LOOP 2: CONSTANT ACCELERATION
# This loop runs until the car reaches the end of the track.
while car.pos.x < 10:
    rate(100)
    
    # Kinematic equations
    # Velocity is no longer constant; it changes with acceleration.
    car.velocity = car.velocity + car.acceleration * dt
    car.pos = car.pos + car.velocity * dt
    t = t + dt
    
    # Plot data
    pos_curve.plot(t, car.pos.x)
    vel_curve.plot(t, car.velocity.x)
    acc_curve.plot(t, car.acceleration.x)

print("End of Part 2. Final Position:", car.pos)
print("Final Velocity:", car.velocity)
print("Simulation finished.")

