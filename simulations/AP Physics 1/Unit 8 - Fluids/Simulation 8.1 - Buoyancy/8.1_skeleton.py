glowscript VPython

# AP Physics 2 - Unit 1: Fluids
# Simulation 1.1: Buoyancy
#
# Skeleton Program

# VISUALS
# A tank to hold the fluid
tank_wall_L = box(pos=vector(-5, 0, 0), size=vector(0.2, 10, 5), color=color.gray(0.7))
tank_wall_R = box(pos=vector(5, 0, 0), size=vector(0.2, 10, 5), color=color.gray(0.7))
tank_floor = box(pos=vector(0, -5, 0), size=vector(10.2, 0.2, 5), color=color.gray(0.7))

# The fluid (e.g., water)
fluid_level = 2.0
fluid = box(pos=vector(0, -1.5, 0), size=vector(10, 7, 4.9), color=color.blue, opacity=0.3)

# The object to be submerged
obj = box(pos=vector(0, 4, 0), size=vector(2, 2, 2), color=color.red)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8

# --- STUDENT TASK 1: Define Densities and Properties ---
# Density of the fluid (water is ~1000 kg/m^3)
rho_fluid = 1000

# Density of the object. Try changing this! What happens if it's > 1000? < 1000?
rho_object = 500 

# Calculate object's volume and mass
obj.V = obj.size.x * obj.size.y * obj.size.z
obj.m = rho_object * obj.V

obj.velocity = vector(0, 0, 0)

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK 2: Calculate Forces ---
    # There are two forces acting on the object: Gravity and Buoyancy.
    
    # 1. GRAVITATIONAL FORCE (Fg)
    #    This is constant and points down: Fg = m * g
    #    Fg = vector(0, -obj.m * g, 0)
    
    # 2. BUOYANT FORCE (Fb)
    #    This force points up. Its magnitude is the weight of the displaced fluid.
    #    Fb = rho_fluid * V_submerged * g
    #    The tricky part is finding the submerged volume, V_submerged.
    
    #    a. Find the y-coordinates of the top and bottom of the object.
    #       y_top = obj.pos.y + obj.size.y / 2
    #       y_bot = obj.pos.y - obj.size.y / 2
    #    b. If the object is fully submerged (y_top < fluid_level), then V_submerged = obj.V
    #    c. If the object is not submerged at all (y_bot > fluid_level), then V_submerged = 0
    #    d. If it's partially submerged, the submerged height is (fluid_level - y_bot).
    #       V_submerged = submerged_height * obj.size.x * obj.size.z
    
    #    Once you have V_submerged, you can find the buoyant force vector:
    #    Fb = vector(0, rho_fluid * V_submerged * g, 0)
    
    
    # --- STUDENT TASK 3: Update Motion ---
    # 1. Find the net force: F_net = Fg + Fb
    # 2. Find acceleration: a = F_net / m
    # 3. Update velocity and position.
    
    # (Optional: Add a simple drag force, F_drag = -c * v, to make it settle faster)
    
    # t = t + dt

print("Simulation finished.")
