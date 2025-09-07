glowscript VPython

# AP Physics 2 - Unit 1: Fluids
# Simulation 1.1: Buoyancy
#
# Complete Program

# --- SETUP ---
scene.title = "Buoyancy Simulation"

# VISUALS
tank_wall_L = box(pos=vector(-5, 0, 0), size=vector(0.2, 10, 5), color=color.gray(0.7))
tank_wall_R = box(pos=vector(5, 0, 0), size=vector(0.2, 10, 5), color=color.gray(0.7))
tank_floor = box(pos=vector(0, -5, 0), size=vector(10.2, 0.2, 5), color=color.gray(0.7))

fluid_level = 2.0
fluid = box(pos=vector(0, (fluid_level - 5)/2, 0), size=vector(10, fluid_level + 5, 4.9), color=color.blue, opacity=0.3)

obj = box(pos=vector(0, 4, 0), size=vector(2, 2, 2), color=color.red)

# PARAMETERS & INITIAL CONDITIONS
t = 0
dt = 0.01
g = 9.8
rho_fluid = 1000 # Density of water

# --- Controls for changing the object's density ---
def set_density(rho):
    global rho_object, obj
    rho_object = rho
    obj.m = rho_object * obj.V
    # Reset the simulation
    reset_sim()

menu_options = {
    "Wood (floats)": 700,
    "Ice (floats)": 917,
    "Water (neutral)": 1000,
    "Aluminum (sinks)": 2700,
    "Iron (sinks)": 7870
}

def select_material(m):
    set_density(menu_options[m.selected])

# Dropdown menu to select material
material_menu = menu(choices=list(menu_options.keys()), bind=select_material)

# Set initial density
rho_object = 700
obj.V = obj.size.x * obj.size.y * obj.size.z
obj.m = rho_object * obj.V

# Force arrows
fg_arrow = arrow(color=color.green, shaftwidth=0.2, label="Gravity")
fb_arrow = arrow(color=color.yellow, shaftwidth=0.2, label="Buoyancy")

# --- Simulation Reset Function ---
def reset_sim():
    global t, obj
    t = 0
    obj.pos = vector(0, 4, 0)
    obj.velocity = vector(0, 0, 0)
    scene.caption.text = f"Object Density: {rho_object} kg/m^3. Fluid Density: {rho_fluid} kg/m^3."

# --- Main Animation Loop ---
reset_sim()

while True: # Loop forever, reset by menu
    rate(100)
    
    # --- Calculate Forces ---
    # 1. Gravitational Force (constant)
    Fg = vector(0, -obj.m * g, 0)
    
    # 2. Buoyant Force (depends on submerged volume)
    y_top = obj.pos.y + obj.size.y / 2
    y_bot = obj.pos.y - obj.size.y / 2
    
    V_submerged = 0
    if y_top < fluid_level:
        V_submerged = obj.V # Fully submerged
    elif y_bot < fluid_level:
        submerged_height = fluid_level - y_bot
        V_submerged = submerged_height * obj.size.x * obj.size.z # Partially submerged
    
    Fb_mag = rho_fluid * V_submerged * g
    Fb = vector(0, Fb_mag, 0)
    
    # Add a simple drag force to make it settle nicely
    F_drag = -0.5 * obj.velocity
    
    # --- Update Motion ---
    F_net = Fg + Fb + F_drag
    obj.acceleration = F_net / obj.m
    obj.velocity = obj.velocity + obj.acceleration * dt
    obj.pos = obj.pos + obj.velocity * dt
    
    # --- Collision Detection ---
    # Stop the object if it hits the bottom
    if y_bot < tank_floor.pos.y + tank_floor.size.y/2:
        obj.pos.y = tank_floor.pos.y + tank_floor.size.y/2 + obj.size.y/2
        # Dampen bouncing
        if obj.velocity.y < 0: obj.velocity.y = 0
        
    # --- Update Visuals ---
    force_scale = 0.001
    fg_arrow.pos = obj.pos
    fg_arrow.axis = Fg * force_scale
    fb_arrow.pos = obj.pos
    fb_arrow.axis = Fb * force_scale
    
    t = t + dt
