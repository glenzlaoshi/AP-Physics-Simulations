glowscript VPython

# AP Physics 1 - Unit 3: Circular Motion and Gravitation
# Simulation 3.1: Uniform Circular Motion
#
# Skeleton Program

# VISUALS
# A central post for the rotation
post = cylinder(pos=vector(0,0,0), axis=vector(0,0,1), radius=0.1, color=color.gray(0.5))

# The object moving in a circle
ball = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.blue)

# The string connecting the ball to the center
string = cylinder(pos=post.pos, axis=ball.pos - post.pos, radius=0.05, color=color.yellow)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01

ball.mass = 0.5 # kg

# --- STUDENT TASK 1: Define Motion Parameters ---
# For circular motion, we need the radius and the speed.
radius = 5.0
speed = 4.0

# The initial velocity is tangential to the circle.
# If the ball starts at (radius, 0, 0), the velocity is in the +y direction.
# ball.velocity = vector(0, speed, 0)


# --- STUDENT TASK 2: Calculate Centripetal Acceleration ---
# The acceleration for uniform circular motion always points towards the center.
# Its magnitude is a_c = v^2 / r.

# The acceleration vector `a` needs to be updated continuously inside the loop
# because its direction is always changing.

# The direction towards the center is the opposite of the ball's position vector
# (if the center is at the origin). So, direction = -norm(ball.pos).

# The magnitude is speed^2 / radius.
# a_mag = speed**2 / radius

# So, inside the loop, you will have:
# ball.acceleration = -norm(ball.pos) * a_mag


# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 3: Implement Physics ---
    
    # 1. Calculate the acceleration vector (it changes direction!)
    # a_mag = speed**2 / radius
    # ball.acceleration = -norm(ball.pos) * a_mag
    
    # 2. Update velocity and position using the kinematic equations.
    # ball.velocity = ball.velocity + ball.acceleration * dt
    # ball.pos = ball.pos + ball.velocity * dt
    
    # 3. Update the string to follow the ball.
    # string.axis = ball.pos - post.pos
    
    # 4. Update time.
    # t = t + dt


print("Simulation finished.")
