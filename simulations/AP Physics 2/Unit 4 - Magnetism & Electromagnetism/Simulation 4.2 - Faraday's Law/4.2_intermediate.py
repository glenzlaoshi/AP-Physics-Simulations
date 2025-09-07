glowscript VPython

# AP Physics 2 - Unit 5: Magnetism & Electromagnetism
# Simulation 5.2: Faraday's Law of Induction
#
# Intermediate Program

# --- SETUP ---
N = 10
coil_radius = 1.0
coil_pos = vector(0,0,0)
for i in range(N): ring(pos=vector(0,0,i*0.1-(N-1)*0.05), axis=vector(0,0,1), radius=coil_radius, thickness=0.05, color=color.gray(0.7))

magnet_strength = 100
N_pole = sphere(pos=vector(0,0,5), radius=0.5, color=color.red, qm=magnet_strength)
S_pole = sphere(pos=vector(0,0,6), radius=0.5, color=color.blue, qm=-magnet_strength)
magnet = compound([N_pole, S_pole])

# --- B-Field Function ---
def get_B(pos):
    B_net = vector(0,0,0)
    for pole in [N_pole, S_pole]:
        r_vec = pos - pole.pos
        r_mag = mag(r_vec)
        if r_mag < 0.1: continue
        B_net += (pole.qm / r_mag**2) * norm(r_vec)
    return B_net

# --- SIMULATION ---
t = 0
dt = 0.01
flux_old = 0
magnet.velocity = vector(0,0,-3)

# --- Graphing ---
graph(title="Magnetic Flux and Induced EMF", xtitle="Time (s)")
flux_curve = gcurve(color=color.purple, label="Magnetic Flux")
emf_curve = gcurve(color=color.orange, label="Induced EMF")

# ANIMATION LOOP
while t < 4:
    rate(100)
    magnet.pos += magnet.velocity * dt
    
    # --- Calculate Magnetic Flux ---
    # We approximate by finding the B-field at the center of the coil.
    B_at_center = get_B(coil_pos)
    B_normal = B_at_center.z # Component of B perpendicular to the coil
    Area = pi * coil_radius**2
    flux_new = B_normal * Area
    
    # Plot the flux
    flux_curve.plot(t, flux_new)
    
    # --- STUDENT TASK: Calculate Induced EMF ---
    # Faraday's Law: EMF = -N * (dFlux / dt)
    # Approximate dFlux/dt as (flux_new - flux_old) / dt
    
    # 1. Calculate the change in flux.
    #    dFlux = flux_new - flux_old
    
    # 2. Calculate the EMF.
    #    EMF = -N * dFlux / dt
    
    # 3. Plot the EMF.
    #    emf_curve.plot(t, EMF)
    
    # 4. Update flux_old for the next iteration.
    #    flux_old = flux_new
    
    t = t + dt

print("Simulation finished.")
