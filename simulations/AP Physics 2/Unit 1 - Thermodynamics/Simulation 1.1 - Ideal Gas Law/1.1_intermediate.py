glowscript VPython

# AP Physics 2 - Unit 2: Thermodynamics
# Simulation 2.1: Ideal Gas Law
#
# Intermediate Program

# VISUALS
L = 5.0
container = box(pos=vector(0,0,0), size=vector(L,L,L), color=color.white, opacity=0.2)

# PARAMETERS
N = 100
m = 1.0

# Create N particles with random positions and velocities
particles = []
# We need to keep track of the total kinetic energy to find temperature
total_ke = 0
for i in range(N):
    p = sphere(pos=(L/2)*vector.random(), radius=0.1, color=color.red)
    # Give a random velocity. The average KE is related to Temperature.
    p.velocity = vector.random() * 3 # Arbitrary speed for now
    particles.append(p)
    total_ke += 0.5 * m * mag2(p.velocity)

# ANIMATION LOOP
t = 0
dt = 0.002

while t < 10:
    rate(500)
    
    # Move all particles
    for p in particles:
        p.pos = p.pos + p.velocity * dt
        
        # Handle elastic collisions with the walls
        if abs(p.pos.x) > L/2:
            p.velocity.x = -p.velocity.x
        if abs(p.pos.y) > L/2:
            p.velocity.y = -p.velocity.y
        if abs(p.pos.z) > L/2:
            p.velocity.z = -p.velocity.z
            
    t = t + dt

# --- STUDENT TASK: Calculate Pressure ---
# Pressure = Force / Area.
# The force on a wall is the rate of change of momentum of the particles hitting it.
# F = delta_p / delta_t

# 1. Create a variable before the loop: `total_delta_p = 0`

# 2. Inside the loop, when a particle hits a specific wall (e.g., the right wall at x=L/2),
#    calculate the change in its momentum.
#    The particle's x-velocity goes from `v_x` to `-v_x`.
#    The change in momentum is `delta_p = p_final - p_initial = m*(-v_x) - m*(v_x) = -2*m*v_x`.
#    The momentum transferred TO THE WALL is the opposite: `+2*m*v_x`.

# 3. Add this momentum change to your total: `total_delta_p += 2 * m * p.velocity.x`
#    (Do this only when it hits the right wall).

# 4. After the loop, calculate the average force: `F_avg = total_delta_p / t`

# 5. Calculate the pressure on that wall: `Pressure = F_avg / Area`
#    The area of one wall is `L*L`.

# --- STUDENT TASK 2: Calculate Temperature ---
# The average kinetic energy of the particles is related to temperature:
# KE_avg = (3/2) * k * T, where k is the Boltzmann constant.
# T = (2/3) * KE_avg / k

# 1. Inside the loop, keep a running sum of the kinetic energy of all particles.
# 2. After the loop, find the average KE: `KE_avg = total_KE / N`
# 3. Use this to find the temperature.

print("Simulation finished.")
