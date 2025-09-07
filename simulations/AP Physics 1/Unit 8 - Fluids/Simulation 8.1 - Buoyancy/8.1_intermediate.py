glowscript VPython

# AP Physics 2 - Unit 1: Fluids
# Simulation 1.1: Buoyancy
#
# Intermediate Program

# VISUALS
tank_wall_L = box(pos=vector(-5, 0, 0), size=vector(0.2, 10, 5), color=color.gray(0.7))
tank_wall_R = box(pos=vector(5, 0, 0), size=vector(0.2, 10, 5), color=color.gray(0.7))
tank_floor = box(pos=vector(0, -5, 0), size=vector(10.2, 0.2, 5), color=color.gray(0.7))
fluid_level = 2.0
fluid = box(pos=vector(0, -1.5, 0), size=vector(10, 7, 4.9), color=color.blue, opacity=0.3)
obj = box(pos=vector(0, 4, 0), size=vector(2, 2, 2), color=color.red)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
rho_fluid = 1000
rho_object = 1200 # This object is denser than water, so it should sink.

obj.V = obj.size.x * obj.size.y * obj.size.z
obj.m = rho_object * obj.V
obj.velocity = vector(0, 0, 0)

# The gravitational force is constant.
Fg = vector(0, -obj.m * g, 0)

print(f"Object density: {rho_object} kg/m^3")
print(f"Fluid density: {rho_fluid} kg/m^3")

# ANIMATION LOOP
while t < 10:
    rate(100)
    
    # --- STUDENT TASK: Calculate Buoyant Force ---
    # The buoyant force depends on the volume of the object that is submerged.
    
    # Find the y-coordinates of the top and bottom of the object.
    y_top = obj.pos.y + obj.size.y / 2
    y_bot = obj.pos.y - obj.size.y / 2
    
    # 1. Determine the submerged volume (V_submerged).
    #    - If y_top is below the fluid level, it's fully submerged.
    #    - If y_bot is above the fluid level, it's not submerged at all.
    #    - Otherwise, it's partially submerged.
    V_submerged = 0 # Replace this with your logic!
    if y_top < fluid_level:
        V_submerged = obj.V # Fully submerged
    elif y_bot < fluid_level:
        submerged_height = fluid_level - y_bot
        V_submerged = submerged_height * obj.size.x * obj.size.z # Partially submerged
    
    # 2. Calculate the buoyant force magnitude: Fb = rho_fluid * V_submerged * g
    # Fb_mag = rho_fluid * V_submerged * g
    
    # 3. Create the buoyant force vector (it points upwards).
    # Fb = vector(0, Fb_mag, 0)
    
    # For now, use a placeholder buoyant force.
    Fb = vector(0, 0, 0)
    
    # --- Update Motion ---
    # Once you have the correct Fb, the rest of the physics should work.
    F_net = Fg + Fb
    obj.acceleration = F_net / obj.m
    obj.velocity = obj.velocity + obj.acceleration * dt
    obj.pos = obj.pos + obj.velocity * dt
    
    # Prevent object from falling through the floor
    if obj.pos.y - obj.size.y/2 < tank_floor.pos.y + tank_floor.size.y/2:
        obj.pos.y = tank_floor.pos.y + tank_floor.size.y/2 + obj.size.y/2
        obj.velocity.y = 0
        
    t = t + dt

print("Simulation finished.")
