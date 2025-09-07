glowscript VPython

# AP Physics C: E&M - Unit 5: Electromagnetism
# Simulation C-EM.5: The Maxwell-Ampere Law
#
# Skeleton Program

# This simulation shows that a changing electric flux creates a magnetic field.

# --- CONSTANTS & PARAMETERS ---
mu_0 = 4*pi*1e-7
epsilon_0 = 8.85e-12

# --- SETUP ---
# A parallel plate capacitor
plate_radius = 2.0
plate_sep = 0.5 # separation
plate_L = plate(pos=vector(0,0,-plate_sep/2), axis=vector(0,0,-1), radius=plate_radius, color=color.gray(0.7))
plate_R = plate(pos=vector(0,0,plate_sep/2), axis=vector(0,0,1), radius=plate_radius, color=color.gray(0.7))

# --- CHARGING PROCESS ---
# We'll assume the capacitor is being charged by a constant current, I.
# This is a simplification of the RC circuit.
I_charge = 0.1 # Amps

# The charge Q on the plates increases over time: Q(t) = I * t
# The surface charge density sigma is Q / Area.
# The E-field between the plates is E = sigma / epsilon_0 = Q / (A * epsilon_0).
# So, the E-field increases linearly with time.

t = 0
dt = 0.01

# --- ANIMATION LOOP ---
while t < 5:
    rate(50)
    
    # --- STUDENT TASK 1: Calculate the Changing E-Field and Flux ---
    
    # 1. Calculate the charge on the positive plate at time `t`.
    #    Q = I_charge * t
    
    # 2. Calculate the magnitude of the E-field between the plates.
    #    Area = pi * plate_radius**2
    #    E_mag = Q / (Area * epsilon_0)
    #    E_vec = vector(0, 0, -E_mag) # Points from positive (R) to negative (L) plate
    
    # 3. Calculate the electric flux (Flux_E) through a loop between the plates.
    #    Let's consider a loop of radius `r` (where r < plate_radius).
    #    Flux_E = E_mag * (pi * r**2)
    
    # 4. Calculate the RATE OF CHANGE of electric flux (d(Flux_E)/dt).
    #    Since E changes linearly with t, Flux_E also changes linearly.
    #    dE_dt = (I_charge / (Area * epsilon_0))
    #    dFlux_dt = dE_dt * (pi * r**2)
    
    
    # --- STUDENT TASK 2: Apply the Maxwell-Ampere Law ---
    # The law is: integral(B . dL) = mu_0 * (I_enclosed + epsilon_0 * d(Flux_E)/dt)
    # Inside the capacitor, the enclosed conventional current (I_enclosed) is zero.
    # So, integral(B . dL) = mu_0 * epsilon_0 * d(Flux_E)/dt
    
    # For a circular loop of radius `r`, the integral on the left is B * (2*pi*r).
    # So, B * (2*pi*r) = mu_0 * epsilon_0 * d(Flux_E)/dt
    
    # 1. Solve for the magnitude of the induced magnetic field, B.
    #    B = (mu_0 * epsilon_0 * d(Flux_E)/dt) / (2*pi*r)
    
    # The direction of B is tangential to the loop (it curls around the E-field).

    # t = t + dt

print("Simulation finished.")
