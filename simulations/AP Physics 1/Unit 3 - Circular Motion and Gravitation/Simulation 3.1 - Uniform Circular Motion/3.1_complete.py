Web VPython 3.2
# AP Physics 1 - Unit 3: Circular Motion and Gravitation
# Simulation 3.1: Uniform Circular Motion
#
# Complete Program

# SCENE & VISUALS
scene.title = "Uniform Circular Motion"
scene.caption = "The green arrow is the velocity vector (tangent to the path).\nThe red arrow is the centripetal acceleration vector (points to the center)."

post = cylinder(pos=vector(0,0,0), axis=vector(0,0,1), radius=0.1, color=color.gray(0.5))
ball = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.blue, make_trail=True)
string = cylinder(pos=post.pos, axis=ball.pos - post.pos, radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
ball.mass = 0.5

radius = mag(ball.pos)
speed = 4.0

# Set initial velocity tangential to the circular path
ball.velocity = vector(0, speed, 0)

# Calculate the magnitude of the centripetal acceleration (a_c = v^2 / r)
a_mag = speed**2 / radius

# Calculate the required centripetal force (F_c = m * a_c)
Fc_mag = ball.mass * a_mag

print(f"Radius: {radius:.1f} m, Speed: {speed:.1f} m/s")
print(f"Centripetal acceleration: {a_mag:.2f} m/s^2")
print(f"Required Centripetal Force (Tension): {Fc_mag:.2f} N")

# VECTOR VISUALIZATION
# Create arrows to represent the velocity and acceleration vectors.
# We use a scale factor to make them a reasonable size on screen.
v_scale = 0.5
a_scale = 1.0

v_arrow = arrow(pos=ball.pos, shaftwidth=0.2, color=color.green, label="Velocity")
a_arrow = arrow(pos=ball.pos, shaftwidth=0.2, color=color.red, label="Acceleration")

# --- Click to Start / Pause ---
# Wait for the first click to start the simulation
scene.pause('Click to Start')
# Global variable to control the running state
running = True

# Function to running on click
def toggle_pause(evt):
    global running
    running = not running
# Bind the function to the click event
scene.bind('click', toggle_pause)
# --------------------------------

# ANIMATION LOOP
while t < 10:
    rate(1/dt)
    if running:
    
        # The acceleration vector always points from the ball to the center (the origin).
        # Its direction is given by -norm(ball.pos).
        ball.acceleration = -norm(ball.pos) * a_mag
    
        # Update velocity and position using basic kinematics
        ball.velocity = ball.velocity + ball.acceleration * dt
        ball.pos = ball.pos + ball.velocity * dt
    
        # Update the string to follow the ball
        string.axis = ball.pos - post.pos
    
        # Update the visualization arrows
        v_arrow.pos = ball.pos
        a_arrow.pos = ball.pos
    
        v_arrow.axis = ball.velocity * v_scale
        a_arrow.axis = ball.acceleration * a_scale
    
        # Update time
        t = t + dt

print("Simulation finished.")
