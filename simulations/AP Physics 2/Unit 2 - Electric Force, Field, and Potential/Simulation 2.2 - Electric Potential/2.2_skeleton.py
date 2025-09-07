glowscript VPython

# AP Physics 2 - Unit 3: Electric Force, Field, and Potential
# Simulation 3.2: Electric Potential
#
# Skeleton Program

# PARAMETERS
k = 9e9 # Coulomb's constant

# VISUALS
# Create source charges
source1 = sphere(pos=vector(-3, 0, 0), radius=0.5, color=color.red)
source1.q = 3e-9 # +3 nC

source2 = sphere(pos=vector(3, 0, 0), radius=0.5, color=color.blue)
source2.q = -3e-9 # -3 nC

sources = [source1, source2]

# The point in space where we want to find the potential
point_of_interest = vector(0, 4, 0)
marker = sphere(pos=point_of_interest, radius=0.1, color=color.yellow)

# --- STUDENT TASK 1: Calculate Potential from a Single Source ---
# Electric potential (V) is a SCALAR quantity. V = k * q / r.
# The total potential is the simple sum of the potentials from each source.

# 1. Find the distance from source1 to the point of interest.
#    r1 = mag(point_of_interest - source1.pos)

# 2. Calculate the potential at the point due to source1.
#    V1 = k * source1.q / r1


# --- STUDENT TASK 2: Calculate the Net Potential ---
# 1. Calculate the potential from source2 (V2).
#    (Remember that q is negative for source2, so the potential will be negative).

# 2. The net potential is the scalar sum.
#    V_net = V1 + V2


# --- STUDENT TASK 3: Potential Energy ---
# If you place a charge `q_test` at the point of interest, its electric
# potential energy would be U = q_test * V_net.

# 1. Define a test charge.
#    q_test = 1e-9 # 1 nC

# 2. Calculate its potential energy.
#    U = q_test * V_net

# The result will be printed to the output.
# V_net = 0 # Replace with your calculation
# print(f"The electric potential at the yellow point is {V_net:.2f} Volts.")

print("Calculation finished.")
