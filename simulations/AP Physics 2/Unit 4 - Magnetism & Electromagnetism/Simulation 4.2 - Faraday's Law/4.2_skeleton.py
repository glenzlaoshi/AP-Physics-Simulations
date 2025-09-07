glowscript VPython

# AP Physics 2 - Unit 5: Magnetism & Electromagnetism
# Simulation 5.2: Faraday's Law of Induction
#
# Skeleton Program

# --- SETUP ---
# A wire coil, represented by a series of rings
N = 10 # Number of turns
coil_radius = 1.0
coil_pos = vector(0,0,0)
coil_rings = []
for i in range(N):
    # Spread the rings out slightly to give the coil some thickness
    z = i * 0.1 - (N-1)*0.05
    ring = ring(pos=vector(0,0,z), axis=vector(0,0,1), radius=coil_radius, thickness=0.05, color=color.gray(0.7))
    coil_rings.append(ring)

# A bar magnet. We model it as two opposite magnetic monopoles (a simplification).
magnet_strength = 100 # Arbitrary units
N_pole = sphere(pos=vector(0,0,5), radius=0.5, color=color.red, qm=magnet_strength)
S_pole = sphere(pos=vector(0,0,6), radius=0.5, color=color.blue, qm=-magnet_strength)
magnet = compound([N_pole, S_pole])

# --- SIMULATION ---
t = 0
dt = 0.01

# We need to know the magnetic flux from the previous time step to find the change.
flux_old = 0

# Move the magnet with a constant velocity
magnet.velocity = vector(0,0,-2)

# --- Function to calculate B-field from our simplified magnet ---
def get_B(pos):
    # The B-field from a magnetic monopole is B = (mu_0/4pi) * qm / r^2 * r_hat
    # We'll absorb the constant into our magnet_strength.
    B_net = vector(0,0,0)
    for pole in [N_pole, S_pole]:
        r_vec = pos - pole.pos
        r_mag = mag(r_vec)
        if r_mag < 0.1: continue
        B_net += (pole.qm / r_mag**2) * norm(r_vec)
    return B_net

# ANIMATION LOOP
while t < 5:
    rate(100)
    
    # Move the magnet
    magnet.pos += magnet.velocity * dt
    
    # --- STUDENT TASK 1: Calculate Magnetic Flux ---
    # Magnetic flux (phi_B) is the amount of B-field passing through the coil's area.
    # For a uniform field, Flux = B_normal * Area.
    # Our field isn't uniform, so we approximate by finding the B-field at the center of the coil.
    
    # 1. Get the B-field vector at the center of the coil.
    #    B_at_center = get_B(coil_pos)
    
    # 2. Find the component of the B-field that is normal (perpendicular) to the coil.
    #    The coil's normal vector is along the z-axis: vector(0,0,1).
    #    B_normal = B_at_center.z
    
    # 3. Calculate the flux.
    #    Area = pi * coil_radius**2
    #    flux_new = B_normal * Area
    
    
    # --- STUDENT TASK 2: Calculate Induced EMF ---
    # Faraday's Law: EMF = -N * (dFlux / dt)
    # We can approximate dFlux/dt as (change in flux) / (change in time).
    # dFlux = flux_new - flux_old
    # dt is our time step.
    
    # 1. Calculate the change in flux.
    #    dFlux = flux_new - flux_old
    
    # 2. Calculate the EMF.
    #    EMF = -N * dFlux / dt
    
    # 3. Remember to update flux_old for the next loop iteration!
    #    flux_old = flux_new
    
    # t = t + dt

print("Simulation finished.")
