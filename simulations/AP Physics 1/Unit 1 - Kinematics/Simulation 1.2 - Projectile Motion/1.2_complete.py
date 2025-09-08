Web VPython 3.2
# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.2: Projectile Motion
#
# Complete Program

# SCENE & OBJECTS
scene.title = "Simulation of Projectile Motion"
scene.caption = "A yellow ball is launched at an angle. Once at the maximum height, a red ball is thrown straight up with the same vertical speed.\nNotice they hit the ground simultaneously, showing independence of vertical and horizontal motion."

ground = box(pos=vector(0, 0, 0), size=vector(45, 0.1, 10), color=color.green)

# The launched projectile
projectile = sphere(pos=vector(-20, 0, 0), radius=0.4, color=color.yellow)
projectile.trail = attach_trail(projectile, color=color.yellow, radius=0.05)

# A second ball that will be thrown vertically
thrown_ball = sphere(pos=vector(projectile.pos.x, 0, 0), radius=0.4, color=color.red)
thrown_ball.trail = attach_trail(thrown_ball, color=color.red, radius=0.05)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

# Initial speed and angle for the launched projectile
v0 = 20
theta = radians(50)

# Set initial positions and velocities
projectile.pos = vector(-20, projectile.radius, 0)
projectile.velocity = vector(v0 * cos(theta), v0 * sin(theta), 0)
projectile.acceleration = vector(0, -g, 0)

thrown_ball.pos = vector(-20-(2*thrown_ball.radius), thrown_ball.radius, 0) # Start at a height of 0m
thrown_ball.velocity = vector(0, v0*sin(theta), 0) # Starts with same vertical component of velocity
thrown_ball.acceleration = vector(0, -g, 0)

print(f"Launching projectile with speed={v0} m/s at angle={degrees(theta):.1f} degrees.")
print(f"Thrown red ball from ground={thrown_ball.pos.y} m.")

# GRAPHING SETUP
graph_window = graph(title='Projectile Motion', xtitle='Time (s)', ytitle='Value')
pos_y_curve = gcurve(color=color.yellow, label="Projectile Y-Position (m)")
vel_y_curve = gcurve(color=color.red, label="Projectile Y-Velocity (m/s)")
pos_x_curve = gcurve(color=color.blue, label="Projectile X-Position (m)")

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
# The loop runs as long as either ball is above the ground.
while projectile.pos.y-projectile.radius >= 0 or thrown_ball.pos.y-thrown_ball.radius >= 0:
    rate(100)
    if running:
        # Update motion for the launched projectile
        if projectile.pos.y >= 0:
            projectile.velocity = projectile.velocity + projectile.acceleration * dt
            projectile.pos = projectile.pos + projectile.velocity * dt
        
            # Plot data for the projectile
            pos_y_curve.plot(t, projectile.pos.y)
            vel_y_curve.plot(t, projectile.velocity.y)
            pos_x_curve.plot(t, projectile.pos.x)

        # Update motion for the thrown ball
        if thrown_ball.pos.y >= 0:
            thrown_ball.velocity = thrown_ball.velocity + thrown_ball.acceleration * dt
            thrown_ball.pos = thrown_ball.pos + thrown_ball.velocity * dt

        # Update time
        t = t + dt

# --- END OF SIMULATION ---
print("Simulation finished.")
print(f"Projectile landed at x = {projectile.pos.x:.2f} m after {t:.2f} s")

# Calculate theoretical range and time to compare
theoretical_time = (v0*sin(theta) + sqrt((v0*sin(theta))**2 + 2*g*projectile.pos.y)) / g
theoretical_range = v0 * cos(theta) * theoretical_time
print(f"Theoretical time: {theoretical_time:.2f} s")
