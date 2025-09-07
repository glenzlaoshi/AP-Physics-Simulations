glowscript VPython

# AP Physics 2 - Unit 3: Electric Force, Field, and Potential
# Simulation 3.2: Electric Potential
#
# Intermediate Program

# PARAMETERS
k = 9e9

# VISUALS
source1 = sphere(pos=vector(-3, 0, 0), radius=0.5, color=color.red, q=3e-9)
source2 = sphere(pos=vector(3, 0, 0), radius=0.5, color=color.blue, q=-3e-9)
sources = [source1, source2]

# --- Function to calculate potential at a point ---
def calculate_V(position, source_charges):
    V_net = 0
    for s in source_charges:
        r = mag(position - s.pos)
        if r == 0: continue # Avoid division by zero
        # Potential is a scalar: V = k*q/r
        V_net += k * s.q / r
    return V_net

# --- STUDENT TASK 1: Create a Grid of Points ---
# To create a potential map, we need to calculate the potential at many points.
# We can create a grid of `box` objects to represent these points.

# 1. Define grid parameters.
#    grid_min = -8
#    grid_max = 8
#    grid_spacing = 1

# 2. Create a list to hold the grid points.
#    grid_points = []

# 3. Write a nested loop to create the grid.
#    for x in arange(grid_min, grid_max, grid_spacing):
#        for y in arange(grid_min, grid_max, grid_spacing):
#            # Create a small, flat box at each grid location
#            point = box(pos=vector(x,y,0), size=vector(grid_spacing, grid_spacing, 0.1))
#            grid_points.append(point)


# --- STUDENT TASK 2: Color the Grid ---
# Now, loop through your `grid_points` list.
# For each `point` in the list:

# 1. Calculate the potential `V` at that point's position.
#    `V_at_point = calculate_V(point.pos, sources)`

# 2. Assign a color to the point based on the value of `V`.
#    This is tricky. You need to map a range of potential values to a range of colors.
#    A simple way is to use a color gradient.
#    - Find the min and max potential values across your whole grid first.
#    - Then, for each point, normalize its potential to a value between 0 and 1.
#      `color_val = (V_at_point - V_min) / (V_max - V_min)`
#    - Set the point's color.
#      `point.color = vector(color_val, 0, 1 - color_val)` (maps from blue to red)

print("When complete, the colored grid will show the equipotential map.")
