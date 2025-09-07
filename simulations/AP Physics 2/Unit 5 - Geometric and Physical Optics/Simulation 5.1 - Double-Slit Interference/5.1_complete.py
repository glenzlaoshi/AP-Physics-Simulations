glowscript VPython

# AP Physics 2 - Unit 6: Geometric and Physical Optics
# Simulation 6.1: Double-Slit Interference
#
# Complete Program

# --- SETUP ---
scene.title = "Young's Double-Slit Experiment"
scene.caption = "Use the sliders to see how the interference pattern changes."

# --- PARAMETERS ---
# These will be controlled by sliders
wavelength = 600e-9 # 600 nm (orange light)
slit_separation = 3e-5 # 30 micrometers
screen_dist = 1.0      # 1 meter

# --- VISUALS ---
# We don't draw the slits, just the resulting pattern on the screen.
screen = box(pos=vector(0,0,0), size=vector(0.01, 0.1, 0.1), color=color.gray(0.8))
# A curve to draw the intensity graph
intensity_graph = curve(color=color.yellow)

# --- CALCULATION & DRAWING FUNCTION ---
def update_pattern():
    """Calculates and redraws the entire interference pattern."""
    global wavelength, slit_separation, screen_dist
    intensity_graph.clear()
    
    # Find the maximum possible intensity for normalization
    # This is not strictly necessary but makes the graph look consistent.
    I_max = 1.0
    
    # Loop through positions on the screen
    screen_height = 0.05 # meters
    for y in arange(-screen_height, screen_height, screen_height/1000):
        # Use the small angle approximation: sin(theta) is approx y/L
        # This is valid when L is much larger than y.
        theta = y / screen_dist
        
        # Path difference (d*sin(theta))
        path_diff = slit_separation * theta
        
        # Phase difference
        phase_diff = (2 * pi / wavelength) * path_diff
        
        # Intensity formula: I = I_max * cos^2(phase_diff / 2)
        intensity = I_max * cos(phase_diff / 2)**2
        
        # Draw a point on our graph. The x-coordinate represents the intensity.
        intensity_graph.append(pos=vector(intensity*0.01, y, 0))
    
    # Update the label for fringe spacing
    # Formula for fringe spacing: delta_y = lambda * L / d
    fringe_spacing = (wavelength * screen_dist / slit_separation) * 100 # in cm
    fringe_label.text = f'Fringe Spacing: {fringe_spacing:.2f} cm'

# --- UI CONTROLS ---
# Wavelength slider (in nm)
def set_wavelength(s):
    global wavelength
    wavelength = s.value * 1e-9 # convert nm to m
    wavelength_label.text = f'{s.value:.0f} nm'
    update_pattern()

scene.append_to_caption('\nWavelength (λ): ')
slider(min=400, max=750, value=600, bind=set_wavelength)
wavelength_label = wtext(text='600 nm')

# Slit Separation slider (in micrometers)
def set_separation(s):
    global slit_separation
    slit_separation = s.value * 1e-6 # convert um to m
    separation_label.text = f'{s.value:.1f} μm'
    update_pattern()

scene.append_to_caption('\nSlit Separation (d): ')
slider(min=10, max=100, value=30, step=0.1, bind=set_separation)
separation_label = wtext(text='30.0 μm')

# Screen Distance slider (in cm)
def set_distance(s):
    global screen_dist
    screen_dist = s.value / 100 # convert cm to m
    distance_label.text = f'{s.value:.0f} cm'
    update_pattern()

scene.append_to_caption('\nScreen Distance (L): ')
slider(min=50, max=200, value=100, bind=set_distance)
distance_label = wtext(text='100 cm')

scene.append_to_caption('\n\n')
fringe_label = wtext(text='Fringe Spacing: ...')

# --- INITIAL RUN ---
update_pattern()
