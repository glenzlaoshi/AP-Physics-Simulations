glowscript VPython

# AP Physics 2 - Unit 3: Electric Force, Field, and Potential
# Simulation 3.1: Electric Fields
#
# Skeleton Program

# PARAMETERS
k = 9e9 # Coulomb's constant

# VISUALS
# Create one or more "source" charges that create the electric field.
source_charge_1 = sphere(pos=vector(-2, 0, 0), radius=0.5, color=color.red)
source_charge_1.q = 2e-9 # Charge in Coulombs (e.g., +2 nC)

# Let's add a second source charge to make it interesting.
source_charge_2 = sphere(pos=vector(2, 0, 0), radius=0.5, color=color.blue)
source_charge_2.q = -2e-9 # A negative charge (-2 nC)

# Create a "test charge" to probe the field at a specific point.
test_charge = sphere(pos=vector(0, 3, 0), radius=0.2, color=color.yellow)
test_charge.q = 1e-9 # A small, positive test charge

# ANIMATION LOOP (not really an animation, just a calculation)
# We will calculate the force at the test charge's initial position.

# --- STUDENT TASK 1: Calculate Force from a Single Source ---
# The electric force is given by Coulomb's Law: F = k * q1 * q2 / r^2, in the direction of r_hat.

# 1. Find the vector from source_charge_1 to the test_charge.
#    r_vec_1 = test_charge.pos - source_charge_1.pos

# 2. Find the distance and the direction vector.
#    r_mag_1 = mag(r_vec_1)
#    r_hat_1 = norm(r_vec_1)

# 3. Calculate the force magnitude.
#    F_mag_1 = k * abs(source_charge_1.q * test_charge.q) / r_mag_1**2

# 4. Determine the direction. Since both charges are positive, the force is repulsive.
#    F_vec_1 = F_mag_1 * r_hat_1


# --- STUDENT TASK 2: Calculate the Net Force ---
# The total force on the test charge is the vector sum of the forces from ALL source charges.

# 1. Calculate the force from source_charge_2 on the test charge (F_vec_2).
#    (Be careful! Since source_charge_2 is negative, the force will be attractive).

# 2. Add the force vectors together.
#    F_net = F_vec_1 + F_vec_2


# --- STUDENT TASK 3: Calculate the Electric Field ---
# The electric field E at a point is defined as the force per unit charge.
# E = F_net / q_test

# 1. Calculate the E-field vector at the location of the test charge.
#    E_field = F_net / test_charge.q

# 2. Visualize the E-field vector with an arrow.
#    E_arrow = arrow(pos=test_charge.pos, axis=E_field * 1e-4, color=color.orange)
#    (The 1e-4 is a scaling factor to make the arrow a reasonable size).

print("Calculation finished. The orange arrow represents the E-Field at that point.")
