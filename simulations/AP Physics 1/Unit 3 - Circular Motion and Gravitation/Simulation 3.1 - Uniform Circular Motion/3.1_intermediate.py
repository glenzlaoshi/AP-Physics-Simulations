glowscript VPython

# AP Physics 1 - Unit 3: Circular Motion and Gravitation
# Simulation 3.1: Uniform Circular Motion
#
# Intermediate Program

# VISUALS
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

# Calculate the magnitude of the centripetal acceleration
a_mag = speed**2 / radius

print(f"Radius: {radius:.1f} m, Speed: {speed:.1f} m/s")
print(f"Centripetal acceleration magnitude: {a_mag:.2f} m/s^2")

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # The acceleration vector always points from the ball to the center (the origin).
    # The direction is -norm(ball.pos).
    ball.acceleration = -norm(ball.pos) * a_mag
    
    # Update velocity and position
    ball.velocity = ball.velocity + ball.acceleration * dt
    ball.pos = ball.pos + ball.velocity * dt
    
    # Update the string
    string.axis = ball.pos - post.pos
    
    t = t + dt

# --- STUDENT TASK: Visualize the Vectors ---
# Understanding circular motion requires seeing the velocity and acceleration vectors.
#
# 1. Create two `arrow` objects before the loop starts.
#    - `v_arrow = arrow(pos=ball.pos, shaftwidth=0.2, color=color.green)`
#    - `a_arrow = arrow(pos=ball.pos, shaftwidth=0.2, color=color.red)`
#
# 2. Inside the animation loop, update the position and axis of these arrows.
#    - The position should always be the ball's position.
#      `v_arrow.pos = ball.pos`
#      `a_arrow.pos = ball.pos`
#    - The axis should represent the vector quantity.
#      `v_arrow.axis = ball.velocity` (You might want to scale it to see it better)
#      `a_arrow.axis = ball.acceleration` (You might want to scale this one too)
#
# Try adding this code to see the vectors in action!

print("Simulation finished.")
