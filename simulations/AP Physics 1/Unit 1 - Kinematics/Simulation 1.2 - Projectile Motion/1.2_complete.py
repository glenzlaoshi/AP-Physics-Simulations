glowscript VPython

# AP Physics 1 - Unit 1: Kinematics
# Simulation 1.2: Projectile Motion
#
# Complete Program

# SCENE & OBJECTS
scene.title = "Simulation of Projectile Motion"
scene.caption = "A yellow ball is launched at an angle. A red ball is dropped at the same time.\nNotice they hit the ground simultaneously, showing independence of vertical and horizontal motion."

ground = box(pos=vector(0, -0.5, 0), size=vector(45, 0.1, 10), color=color.green)

# The launched projectile
projectile = sphere(pos=vector(-20, 0, 0), radius=0.4, color=color.yellow)
projectile.trail = attach_trail(projectile, color=color.yellow, radius=0.05)

# A second ball that will be dropped vertically
dropped_ball = sphere(pos=vector(projectile.pos.x, 15, 0), radius=0.4, color=color.red)
dropped_ball.trail = attach_trail(dropped_ball, color=color.red, radius=0.05)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

# Initial speed and angle for the launched projectile
v0 = 25
theta = radians(50)

# Set initial positions and velocities
projectile.pos = vector(-20, 0.4, 0)
projectile.velocity = vector(v0 * cos(theta), v0 * sin(theta), 0)
projectile.acceleration = vector(0, -g, 0)

dropped_ball.pos = vector(-20, 15, 0) # Start at a height of 15m
dropped_ball.velocity = vector(0, 0, 0) # Starts from rest
dropped_ball.acceleration = vector(0, -g, 0)

print(f"Launching projectile with speed={v0} m/s at angle={degrees(theta):.1f} degrees.")
print(f"Dropping red ball from height={dropped_ball.pos.y} m.")

# GRAPHING SETUP
graph_window = graph(title='Projectile Motion', xtitle='Time (s)', ytitle='Value')
pos_y_curve = gcurve(color=color.yellow, label="Projectile Y-Position (m)")
vel_y_curve = gcurve(color=color.red, label="Projectile Y-Velocity (m/s)")
pos_x_curve = gcurve(color=color.blue, label="Projectile X-Position (m)")

# ANIMATION LOOP
# The loop runs as long as either ball is above the ground.
while projectile.pos.y >= 0 or dropped_ball.pos.y >= 0:
    rate(100)
    
    # Update motion for the launched projectile
    if projectile.pos.y >= 0:
        projectile.velocity = projectile.velocity + projectile.acceleration * dt
        projectile.pos = projectile.pos + projectile.velocity * dt
        
        # Plot data for the projectile
        pos_y_curve.plot(t, projectile.pos.y)
        vel_y_curve.plot(t, projectile.velocity.y)
        pos_x_curve.plot(t, projectile.pos.x)

    # Update motion for the dropped ball
    if dropped_ball.pos.y >= 0:
        dropped_ball.velocity = dropped_ball.velocity + dropped_ball.acceleration * dt
        dropped_ball.pos = dropped_ball.pos + dropped_ball.velocity * dt

    # Update time
    t = t + dt

# --- END OF SIMULATION ---
print("Simulation finished.")
print(f"Projectile landed at x = {projectile.pos.x:.2f} m after {t:.2f} s")

# Calculate theoretical range and time to compare
theoretical_time = (v0*sin(theta) + sqrt((v0*sin(theta))**2 + 2*g*projectile.pos.y)) / g
theoretical_range = v0 * cos(theta) * theoretical_time
print(f"Theoretical time: {theoretical_time:.2f} s")
