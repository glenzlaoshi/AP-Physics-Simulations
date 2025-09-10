---
title: "5.1 - Double-Slit Interference"
layout: default
---


## 1. Introduction to the Unit: Physical Optics

This unit explores the **wave nature of light**. While in some cases light behaves like a particle (a photon), in many situations it exhibits classic wave behaviors like **diffraction** (bending around obstacles) and **interference** (adding up or cancelling out).

The phenomenon of interference is a hallmark of waves and provides some of the strongest evidence for light's wave nature. When two or more waves overlap in space, the resulting wave is the sum of the individual waves. This is called the principle of **superposition**.

The most famous demonstration of this is **Young's Double-Slit Experiment**, which is what this simulation models. It shows that when light passes through two tiny slits, it creates a pattern of bright and dark bands on a screen, which can only be explained by the constructive and destructive interference of light waves.

## 2. Relevant Physics Concepts

### Huygens' Principle

This principle states that every point on a wavefront can be treated as a source of new, secondary, circular wavelets. When light passes through a narrow slit, the slit acts like a new source of light, sending out waves in all directions on the other side.

### Path Length Difference

In the double-slit experiment, light passes through two slits, so each slit becomes a new source of waves. These two sets of waves travel towards a distant screen.

Consider a single point on the screen. It is some distance `r1` from the first slit and a different distance `r2` from the second slit. The difference between these two distances, `|r1 - r2|`, is called the **path length difference**.

Whether the waves interfere constructively or destructively at that point depends entirely on this path length difference, compared to the wavelength (`λ`) of the light.

### Constructive and Destructive Interference

-   **Constructive Interference (Bright Fringe):** If the path length difference is an integer multiple of the wavelength (`0, λ, 2λ, 3λ, ...`), the waves arrive at the screen "in phase" (crest meets crest). They add up to create a bright spot.
    The condition is: `d * sin(θ) = mλ`, for `m = 0, 1, 2, ...`

-   **Destructive Interference (Dark Fringe):** If the path length difference is a half-integer multiple of the wavelength (`0.5λ, 1.5λ, 2.5λ, ...`), the waves arrive "out of phase" (crest meets trough). They cancel each other out to create a dark spot.
    The condition is: `d * sin(θ) = (m + 0.5)λ`, for `m = 0, 1, 2, ...`

In these equations, `d` is the distance between the slits and `θ` is the angle from the center of the barrier to the point on the screen.

## 3. The Simulation: The Interference Pattern

### Outline of the Simulation

The `intermediate.py` file sets up the double-slit experiment. The code loops through many different points on the screen. For each point, it calculates the `path_diff` by finding the difference in distance from that point to each of the two slits. Your task is to use this `path_diff` to calculate the resulting light intensity at that point, which will form the interference pattern.

### Completing the `intermediate.py` File

Your task is to calculate the `intensity` of the light for each point on the screen inside the `for` loop.

- **Example (Phase Difference):** A path length difference corresponds to a **phase difference** (`Δφ`) between the two waves. The relationship is `Δφ = (2π/λ) * path_diff`. The code to calculate this is given as an example:
  ```python
  phase_diff = (2 * pi / wavelength) * path_diff
  ```

- **Your Task (Intensity):** The intensity of the combined waves at that point depends on the phase difference. The formula is `I = I_max * cos²(Δφ / 2)`. We can assume the maximum intensity `I_max` is 1. Your task is to write the line of code to calculate the `intensity` using the `phase_diff` you were given. (Hint: In VPython, `cos(x)**2` is the syntax for `cos²(x)`).

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/5.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/e28523e546db" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The pattern of bright and dark fringes in a double-slit experiment is a direct result of which wave phenomenon?
    a) Reflection.
    b) Refraction.
    c) Polarization.
    d) Interference.

2.  For constructive interference to occur at a point on a screen, the path length difference from the two slits to that point must be:
    a) An integer multiple of the wavelength.
    b) A half-integer multiple of the wavelength.
    c) Equal to the distance between the slits.
    d) Zero.

3.  In a double-slit experiment, if the distance between the slits (`d`) is decreased, what happens to the spacing between the bright fringes on the screen?
    a) It decreases.
    b) It increases.
    c) It remains the same.
    d) It depends on the screen distance.

4.  If you perform a double-slit experiment with red light and then repeat it with blue light, how will the pattern change? (Note: Red light has a longer wavelength than blue light).
    a) The blue light fringes will be more spread out.
    b) The red light fringes will be more spread out.
    c) The patterns will be identical.
    d) No pattern will be formed with blue light.

5.  According to Huygens' Principle, each point on a wavefront acts as a source of:
    a) New photons.
    b) Secondary wavelets.
    c) Electric charge.
    d) Magnetic field lines.

### Problem-Solving Questions

1.  In a double-slit experiment, the slits are separated by 0.1 mm (1e-4 m). Light with a wavelength of 500 nm (5e-7 m) is used. What is the angle `θ` of the first-order bright fringe (m=1)?
    a) 0.005 radians
    b) 0.05 radians
    c) 0.1 radians
    d) 0.5 radians

2.  Using the information from the previous question (`d`=0.1 mm, `λ`=500 nm), if the screen is 2.0 m away, what is the distance from the central maximum to the first-order bright fringe? (Use the small angle approximation `sin(θ) ≈ tan(θ) = y/L`).
    a) 0.005 m
    b) 0.01 m
    c) 0.02 m
    d) 0.05 m

3.  A double-slit experiment produces its third-order bright fringe (m=3) at an angle of 1.5 degrees. If the slit separation is 0.12 mm, what is the wavelength of the light?
    a) 436 nm
    b) 549 nm
    c) 873 nm
    d) 1047 nm

4.  At a certain point on the screen in a double-slit experiment, the path length difference is 1200 nm. If the wavelength of the light is 600 nm, this point will be:
    a) A bright fringe (constructive interference).
    b) A dark fringe (destructive interference).
    c) Neither bright nor dark.
    d) The central maximum.

5.  At another point on the screen, the path length difference is 900 nm. If the wavelength of the light is 600 nm, this point will be:
    a) A bright fringe (constructive interference).
    b) A dark fringe (destructive interference).
    c) The central maximum.
    d) A second-order bright fringe.

### Computational Questions

1.  The simulation calculates the intensity using `I = cos(phase_diff / 2)**2`. This formula shows that the intensity will be at a maximum (equal to 1) when the phase difference is:
    a) An odd multiple of π (π, 3π, 5π...).
    b) An even multiple of π (0, 2π, 4π...).
    c) A multiple of π/2.
    d) Always equal to 1.

2.  The phase difference is calculated as `phase_diff = (2 * pi / wavelength) * path_diff`. This means a path difference of one full wavelength corresponds to a phase difference of:
    a) π/2 radians.
    b) π radians.
    c) 2π radians.
    d) 0 radians.

3.  The simulation loops through points on a screen and calculates the intensity at each one. This process of building up a pattern from individual point calculations is a way to model:
    a) The particle nature of light.
    b) The wave superposition and interference.
    c) The photoelectric effect.
    d) The quantization of energy.

4.  If you were to modify the simulation to use a longer `wavelength`, how would the calculated `phase_diff` for a given `path_diff` change?
    a) It would increase.
    b) It would decrease.
    c) It would remain the same.
    d) It would become zero.

5.  The simulation calculates `path_diff` as `abs(r1 - r2)`. Why is the absolute value function `abs()` used?
    a) Because distance cannot be negative.
    b) To ensure the phase difference is always positive.
    c) To make the pattern symmetric.
    d) It is not necessary and could be removed.

---
### Answer Key
**Conceptual:** 1. (d), 2. (a), 3. (b), 4. (b), 5. (b)
**Problem-Solving:** 1. (a), 2. (b), 3. (c), 4. (a), 5. (b)
**Computational:** 1. (b), 2. (c), 3. (b), 4. (b), 5. (a)
