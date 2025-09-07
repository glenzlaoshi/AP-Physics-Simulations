glowscript VPython

# AP Physics 2 - Unit 7: Modern Physics
# Simulation 7.1: The Photoelectric Effect
#
# Skeleton Program

# --- CONSTANTS & PARAMETERS ---
h = 6.626e-34 # Planck's constant (J*s)
e = 1.602e-19 # Elementary charge (for converting J to eV)

# --- SETUP ---
# A metal plate that will be struck by light
metal_plate = box(pos=vector(-5, 0, 0), size=vector(0.2, 5, 5), color=color.gray(0.8))

# A light beam represented by a cylinder
light_beam = cylinder(pos=vector(5, 0, 0), axis=vector(-10, 0, 0), radius=1, color=color.yellow, opacity=0.5)

# --- PHYSICS OF THE EFFECT ---

# 1. WORK FUNCTION (phi)
#    - Every metal has a work function, which is the minimum energy
#      needed to eject an electron from its surface.
#    - It's usually given in electron-volts (eV).
work_function_eV = 2.75 # Work function for Sodium in eV
#    - Let's convert it to Joules for our calculations.
#      phi = work_function_eV * e

# 2. PHOTON ENERGY (E_photon)
#    - Light is made of photons. The energy of a single photon depends on its frequency (f).
#    - E_photon = h * f
#    - Frequency is related to wavelength (lambda) and the speed of light (c):
#      f = c / lambda, where c = 3e8 m/s.

#    - Let's choose a wavelength for our light.
#      wavelength = 500e-9 # 500 nm (green light)
#      c = 3e8
#      frequency = c / wavelength
#      E_photon = h * frequency


# --- STUDENT TASK 1: Will an electron be ejected? ---
# An electron is ejected ONLY IF the energy of one photon is greater than the work function.

# 1. Compare E_photon and phi.
#    if E_photon > phi:
#        print("Electron is ejected!")
#    else:
#        print("Photon energy is too low. No electron is ejected.")


# --- STUDENT TASK 2: Calculate Max Kinetic Energy ---
# If an electron is ejected, its maximum kinetic energy (KE_max) is the
# leftover energy after overcoming the work function.

# 1. Use the photoelectric effect equation: KE_max = E_photon - phi
#    if E_photon > phi:
#        KE_max_joules = E_photon - phi
#        # Convert it to eV for easier interpretation
#        KE_max_eV = KE_max_joules / e
#        print(f"Max KE of ejected electron: {KE_max_eV:.2f} eV")


# --- STUDENT TASK 3: What about intensity? ---
# The intensity of the light corresponds to the NUMBER of photons per second,
# not the energy of each individual photon.
# - If electrons are being ejected, increasing the intensity will eject MORE electrons per second.
# - If no electrons are being ejected, increasing the intensity does NOTHING.

print("Calculation finished.")
