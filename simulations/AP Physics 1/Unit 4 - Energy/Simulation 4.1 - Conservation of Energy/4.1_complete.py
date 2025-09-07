glowscript VPython

# AP Physics 1 - Unit 4: Energy
# Simulation 4.1: Conservation of Energy (Roller Coaster)
#
# Complete Program

# SCENE & VISUALS
scene.title = "Energy Conservation on a Roller Coaster"
scene.caption = "The bar graph shows how energy transforms between Potential (blue) and Kinetic (red). Total energy remains constant."

# The track is defined by a function for its y-position.
def track_path(x):
    # A path with two hills of different heights
    return 3 * cos(0.2 * x) + 0.5 * x + 4

# Draw the track by connecting a series of points
track = curve(color=color.gray(0.6), radius=0.2)
for x_pos in arange(-20, 20, 0.1):
    track.append(pos=vector(x_pos, track_path(x_pos), 0))

# The roller coaster cart
cart = sphere(radius=0.5, color=color.red, make_trail=True)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.005 # Use a smaller time step for better accuracy
g = 9.8
cart.m = 1.0

# Start the cart at the top of the first hill, from rest.
cart.pos = vector(-20, track_path(-20), 0)

# Calculate the initial total energy of the system.
# Since it starts from rest, initial KE is 0.
initial_PE = cart.m * g * cart.pos.y
total_energy = initial_PE

print(f"Initial Height: {cart.pos.y:.2f} m")
print(f"Total Mechanical Energy: {total_energy:.2f} J (This should be conserved)")

# ENERGY BAR GRAPH SETUP
bar_graph = graph(width=400, height=250, title="<b>Energy Distribution</b>", ymax=total_energy)
pe_bar = gvbars(color=color.blue, label="Potential")
ke_bar = gvbars(color=color.red, label="Kinetic")

# ANIMATION LOOP
while cart.pos.x < 20:
    rate(200)
    
    # --- Physics Calculations based on Energy Conservation ---
    
    # 1. Calculate current Potential Energy (PE)
    current_PE = cart.m * g * cart.pos.y
    
    # 2. Calculate current Kinetic Energy (KE)
    # If PE were to exceed total_energy (e.g. due to numerical error), cap KE at 0.
    current_KE = max(0, total_energy - current_PE)
    
    # 3. Calculate the cart's speed from its KE
    speed = sqrt(2 * current_KE / cart.m)
    
    # --- Update Motion ---
    # To move the cart along the curve, we find the direction of the track.
    # We can approximate the tangent vector by looking at a point just ahead.
    next_x = cart.pos.x + 0.01
    next_y = track_path(next_x)
    direction = norm(vector(next_x - cart.pos.x, next_y - cart.pos.y, 0))
    
    # Update velocity and position
    cart.velocity = speed * direction
    cart.pos = cart.pos + cart.velocity * dt
    
    # Update the energy bar graph
    pe_bar.plot(pos=(0, current_PE/2), size=(1, current_PE))
    ke_bar.plot(pos=(1, current_KE/2), size=(1, current_KE))
    
    # Update time
    t = t + dt

print("Simulation finished.")
print(f"Final Position: {cart.pos}")
print(f"Final Speed: {speed:.2f} m/s")
