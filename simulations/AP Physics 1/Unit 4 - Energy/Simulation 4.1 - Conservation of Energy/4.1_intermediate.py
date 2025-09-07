glowscript VPython

# AP Physics 1 - Unit 4: Energy
# Simulation 4.1: Conservation of Energy (Roller Coaster)
#
# Intermediate Program

# VISUALS
def track_path(x):
    return 5 * cos(0.2 * x) + 5

for x_pos in arange(-20, 20, 0.2):
    cylinder(pos=vector(x_pos, track_path(x_pos), 0), axis=vector(0.2, track_path(x_pos+0.2) - track_path(x_pos), 0), radius=0.2, color=color.gray(0.6))

cart = sphere(radius=0.5, color=color.red, make_trail=True)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
cart.m = 1.0

# Start the cart at the top of the first hill from rest.
cart.pos = vector(-15.7, track_path(-15.7), 0)

# Calculate the initial energy of the system.
# Since it starts from rest, KE = 0.
initial_PE = cart.m * g * cart.pos.y
total_energy = initial_PE # This value should not change!

print(f"Initial Height: {cart.pos.y:.2f} m")
print(f"Total Mechanical Energy: {total_energy:.2f} J (should be conserved)")

# ANIMATION LOOP
while cart.pos.x < 20:
    rate(100)
    
    # --- STUDENT TASK 1: Calculate Speed using Energy Conservation ---
    
    # 1. Calculate the cart's current Potential Energy (PE) at its current position.
    #    current_PE = cart.m * g * cart.pos.y
    
    # 2. Calculate the cart's current Kinetic Energy (KE).
    #    KE = Total Energy - PE
    #    current_KE = total_energy - current_PE
    
    # 3. Calculate the cart's speed (v) from its kinetic energy.
    #    (KE = 0.5*m*v^2)
    #    speed = sqrt(2 * current_KE / cart.m)
    
    # For now, let's use a placeholder speed.
    speed = 2.0 # Replace this with your calculation!
    
    # --- STUDENT TASK 2: Update Position ---
    # We will move the cart along the x-axis and use the track_path function
    # to determine its height. This simplifies the vector math.
    
    # Update the x-position based on the calculated speed.
    # cart.pos.x = cart.pos.x + speed * dt
    
    # Set the y-position according to the track.
    # cart.pos.y = track_path(cart.pos.x)
    
    # Update time
    # t = t + dt


# --- STUDENT TASK 3: Graphing ---
# VPython has powerful graphing tools. Can you plot PE and KE vs. time?
# 1. Before the loop, set up a graph:
#    graph(title='Energy vs. Time', xtitle='t', ytitle='Energy (J)')
#    pe_curve = gcurve(color=color.blue, label='Potential Energy')
#    ke_curve = gcurve(color=color.red, label='Kinetic Energy')
# 2. Inside the loop, plot the values:
#    pe_curve.plot(t, current_PE)
#    ke_curve.plot(t, current_KE)

print("Simulation finished.")
