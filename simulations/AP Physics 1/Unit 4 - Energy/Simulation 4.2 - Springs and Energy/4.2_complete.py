glowscript VPython

# AP Physics 1 - Unit 4: Energy
# Simulation 4.2: Springs and Energy
#
# Complete Program

# SCENE & VISUALS
scene.title = "Energy in a Mass-Spring System"
scene.caption = "The bar graph shows energy transforming between Spring Potential (orange) and Kinetic (cyan)."

wall = box(pos=vector(-10, 0, 0), size=vector(0.2, 4, 4), color=color.gray(0.7))
floor = box(pos=vector(0, -1.1, 0), size=vector(20, 0.2, 4), color=color.gray(0.7))
block = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.cyan)
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.5, coils=20, thickness=0.1, color=color.orange)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
block.m = 2.0 # Mass of the block
spring.k = 10 # Spring constant (N/m)

# The position where the spring is at its natural length
spring.equilibrium_pos = vector(-4, 0, 0)
# Add a visual marker for the equilibrium position
eq_marker = cylinder(pos=spring.equilibrium_pos + vector(0,-1,0), axis=vector(0,-0.5,0), radius=0.1, color=color.white)

# Start the block stretched from equilibrium and release from rest.
block.pos = vector(4, 0, 0)
block.velocity = vector(0, 0, 0)

# Calculate total energy of the system from initial conditions.
x_mag = mag(block.pos - spring.equilibrium_pos)
initial_PE = 0.5 * spring.k * x_mag**2
total_energy = initial_PE

print(f"Total Energy in System: {total_energy:.2f} J")

# ENERGY BAR GRAPH SETUP
bar_graph = graph(width=400, height=250, title="<b>Energy Distribution</b>", ymax=total_energy)
pe_bar = gvbars(color=color.orange, label="Potential")
ke_bar = gvbars(color=color.cyan, label="Kinetic")

# ANIMATION LOOP
while t < 15:
    rate(100)
    
    # --- Physics based on Dynamics (Forces) ---
    
    # 1. Calculate the displacement vector from equilibrium.
    x_vector = block.pos - spring.equilibrium_pos
    
    # 2. Calculate the spring force using Hooke's Law (F = -kx).
    F_spring = -spring.k * x_vector
    
    # 3. Calculate acceleration using Newton's 2nd Law (a = F/m).
    block.acceleration = F_spring / block.m
    
    # 4. Update velocity and position.
    block.velocity = block.velocity + block.acceleration * dt
    block.pos = block.pos + block.velocity * dt
    
    # Update the spring's visual representation.
    spring.axis = block.pos - wall.pos
    
    # --- Verify and Visualize Energy Conservation ---
    
    # Calculate current potential and kinetic energy.
    current_PE = 0.5 * spring.k * mag(x_vector)**2
    current_KE = 0.5 * block.m * mag(block.velocity)**2
    
    # Update the energy bar graph.
    pe_bar.plot(pos=(0, current_PE/2), size=(1, current_PE))
    ke_bar.plot(pos=(1, current_KE/2), size=(1, current_KE))
    
    # Update time.
    t = t + dt

print("Simulation finished.")
