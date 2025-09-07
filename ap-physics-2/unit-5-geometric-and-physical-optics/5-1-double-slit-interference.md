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