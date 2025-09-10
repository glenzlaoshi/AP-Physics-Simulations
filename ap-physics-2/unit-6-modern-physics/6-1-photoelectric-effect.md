---
title: "6.1 - Photoelectric Effect"
layout: default
---


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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The photoelectric effect provides strong evidence for which of the following models of light?
    a) The wave model.
    b) The particle model (photons).
    c) The ray model.
    d) The ether model.

2.  In a photoelectric effect experiment, if you increase the intensity (brightness) of the light shining on the metal, what will happen?
    a) The kinetic energy of the ejected electrons will increase.
    b) The number of electrons ejected per second will increase.
    c) Both the kinetic energy and the number of electrons will increase.
    d) No electrons will be ejected.

3.  If the frequency of the light shining on a metal is below the metal's "cutoff frequency," what will happen?
    a) Electrons will be ejected with very low kinetic energy.
    b) Electrons will be ejected, but only after a time delay.
    c) No electrons will be ejected, regardless of the light's intensity.
    d) The work function of the metal will decrease.

4.  The "work function" of a metal refers to the:
    a) Total energy of the electrons in the metal.
    b) Minimum energy required to eject an electron from the metal surface.
    c) Kinetic energy of the ejected electrons.
    d) Energy of the photons hitting the metal.

5.  The maximum kinetic energy of an electron ejected in the photoelectric effect depends only on:
    a) The intensity of the light.
    b) The frequency of the light and the metal's work function.
    c) The number of photons hitting the surface per second.
    d) The temperature of the metal.

### Problem-Solving Questions

(Use h = 6.63e-34 J·s, c = 3.0e8 m/s, 1 eV = 1.6e-19 J)

1.  What is the energy of a single photon of blue light with a wavelength of 450 nm?
    a) 2.98e-19 J
    b) 4.42e-19 J
    c) 6.63e-19 J
    d) 1.49e-18 J

2.  The work function for a certain metal is 2.3 eV. What is the minimum frequency of light required to eject electrons from this metal?
    a) 3.5e14 Hz
    b) 5.5e14 Hz
    c) 7.5e14 Hz
    d) 9.5e14 Hz

3.  Light with a frequency of 7.0e14 Hz shines on a metal with a work function of 2.5 eV. What is the maximum kinetic energy of the ejected electrons, in eV?
    a) 0.4 eV
    b) 2.5 eV
    c) 2.9 eV
    d) 5.4 eV

4.  In a photoelectric effect experiment, the stopping potential (the voltage required to stop the most energetic electrons) is 1.5 V. What is the maximum kinetic energy of the ejected electrons?
    a) 1.5 J
    b) 1.5 eV
    c) 1.6e-19 J
    d) 9.11e-31 J

5.  A photon with an energy of 5.0 eV strikes a metal surface and ejects an electron with a kinetic energy of 2.0 eV. What is the work function of the metal?
    a) 2.0 eV
    b) 2.5 eV
    c) 3.0 eV
    d) 7.0 eV

### Computational Questions

1.  In the simulation, the condition to check if an electron is ejected is `if KE_max > 0`. This is equivalent to checking if:
    a) The light intensity is high enough.
    b) The photon's energy is greater than the work function.
    c) The wavelength is long enough.
    d) The metal is a conductor.

2.  The simulation calculates the electron's speed using a rearrangement of the formula `KE = 0.5*m*v²`. If you double the `KE_max`, the electron's speed `v` will:
    a) Be multiplied by √2.
    b) Be doubled.
    c) Be quadrupled.
    d) Remain the same.

3.  The simulation creates photons using a `sphere()` object. The color of these photons is set based on the light's wavelength. If you were to change the `wavelength` variable to a smaller value (e.g., from red to blue), what would happen to the energy of each simulated photon?
    a) It would decrease.
    b) It would remain the same.
    c) It would increase.
    d) It depends on the intensity.

4.  The simulation models the photoelectric effect as a one-to-one interaction between a photon and an electron. How is this represented in the code's logic?
    a) By creating many electrons for each photon.
    b) By checking for a collision (`p.pos.x < -5`) and then deciding whether to create a single new electron.
    c) By calculating the total energy of all photons first.
    d) By using the `rate()` function to control the flow of electrons.

5.  If you set the `work_function_eV` in the simulation to be very high (e.g., 10 eV), but use visible light (e.g., 550 nm, which is ~2.25 eV), what would you expect to see when the photons hit the metal plate?
    a) Many electrons would be ejected with high speed.
    b) A few electrons would be ejected with low speed.
    c) The photons would bounce off the plate.
    d) Nothing would happen; no electrons would be ejected.

---
### Answer Key
**Conceptual:** 1. (b), 2. (b), 3. (c), 4. (b), 5. (b)
**Problem-Solving:** 1. (b), 2. (b), 3. (a), 4. (b), 5. (c)
**Computational:** 1. (b), 2. (a), 3. (c), 4. (b), 5. (d)
