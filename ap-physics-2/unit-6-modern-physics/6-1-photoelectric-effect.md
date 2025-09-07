---
title: "6.1 - Photoelectric Effect"
layout: default
---
# Information: The Photoelectric Effect

## 1. Introduction to the Unit: Modern Physics

This unit introduces **Modern Physics**, a collection of revolutionary ideas from the early 20th century that fundamentally changed our understanding of energy and matter, especially at the atomic scale. 

In the previous unit, we saw definitive proof that light behaves as a **wave** (the double-slit experiment). However, the Photoelectric Effect is a key experiment that shows that light also behaves as a **particle**. This baffling wave-particle duality is a cornerstone of quantum mechanics.

The core idea is that light energy is not a continuous wave, but is instead **quantized**, meaning it comes in discrete packets, or particles, called **photons**.

## 2. Relevant Physics Concepts

### The Photon Model of Light

In this model, a beam of light is a stream of massless particles called photons. The energy of a single photon is directly proportional to the frequency of the light.

`E_photon = h * f`

-   `h` is **Planck's constant** (`6.626 x 10⁻³⁴ J·s`).
-   `f` is the frequency of the light.
-   Since the speed of light `c = f*λ`, the energy can also be written in terms of wavelength `λ`: `E_photon = h*c / λ`.

### The Photoelectric Effect

This effect occurs when light shines on a metal surface, and electrons are ejected from the metal.

-   **Work Function (`Φ`): Privilege** Every metal holds onto its electrons with a certain amount of energy. The minimum energy required to free an electron from the surface is called the **work function**. This is a property of the specific metal.

-   **The Interaction:** The process is a one-to-one collision. A single photon interacts with a single electron.

-   **The Condition for Ejection:** For an electron to be ejected, the energy of the incoming photon must be greater than the work function (`E_photon > Φ`). 
    -   If `E_photon < Φ`, no electrons will be ejected, no matter how bright (intense) the light is.
    -   The **intensity** of the light corresponds to the *number* of photons, not the energy of each one.

### Kinetic Energy of Ejected Electrons

If a photon has enough energy to eject an electron, any leftover energy becomes the electron's kinetic energy (`KE`). The maximum possible kinetic energy is given by the famous photoelectric effect equation:

**`KE_max = E_photon - Φ`**  or  **`KE_max = hf - Φ`**

This equation shows that the maximum kinetic energy of the ejected electrons depends only on the light's frequency, not its intensity.

## 3. The Simulation: Light and Metal

### Outline of the Simulation

The `intermediate.py` file sets up a scene with a metal plate. The code at the top already calculates whether electrons will be ejected based on the chosen light wavelength and metal type, and it calculates `KE_max` if they are. Your task is to add the visual components: creating the photons and then creating the ejected electrons if the conditions are met.

### Completing the `intermediate.py` File

#### **Task 1: Create Photons**

- **Your Task:** Inside the `while` loop, you need to add code to create new photons periodically. A simple way to do this is with an `if` statement that runs on some frames (e.g., `if random() < 0.1:`). Inside the `if` block, create a new `sphere` to represent a photon, give it a velocity pointing towards the metal plate, and `append` it to the `particles` list.

#### **Task 2: Handle Collisions and Ejection**

This is the main physics logic. You need to loop through the `particles` list and check if any of them have hit the metal plate.

- **Example (Collision Detection):** The code to detect if a particle `p` has hit the plate is `if p.pos.x < -5:`.

- **Your Task (Ejection Logic):** Inside this `if` statement, you need to check if an electron should be ejected. The variable `KE_max` was already calculated for you at the start of the program. Write an `if` statement to check if `KE_max > 0`.

- **Your Task (Create an Electron):** If `KE_max` is greater than zero, you need to create a new `sphere` to represent an ejected electron. 
    1.  First, calculate the electron's maximum speed `v` from its `KE_max` using the kinetic energy formula `KE = (1/2)mv²`. You will need to rearrange it to solve for `v`.
    2.  Then, create the new electron sphere.
    3.  Give it a velocity vector pointing away from the plate with the speed you just calculated.
    4.  Finally, `append` the new electron to the `particles` list so it will also be animated.

After completing these steps, you will have a working visual model of the photoelectric effect. You can change the `wavelength` and `work_function_eV` variables at the top to see how they affect the outcome.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/6.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/814c132a1d6f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>