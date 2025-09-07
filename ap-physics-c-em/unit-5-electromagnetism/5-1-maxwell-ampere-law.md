---
title: "5.1 - Maxwell-Ampere Law"
layout: default
---
# Information: The Maxwell-Ampere Law

## 1. Introduction to the Unit: Electromagnetism & Maxwell's Equations

This unit represents the capstone of classical electricity and magnetism. We will see how the concepts of electric and magnetic fields, and their sources, are unified into a single, elegant theory described by **Maxwell's Equations**.

This simulation focuses on the final, crucial piece of this puzzle, which was James Clerk Maxwell's brilliant theoretical insight. He started with **Ampere's Law**, which relates a magnetic field to the electric current that creates it. He noticed a logical inconsistency in the law when applied to a charging capacitor and fixed it by proposing that a **changing electric field** can create a magnetic field, just as a current can. This new term is called **displacement current**.

## 2. Relevant Physics Concepts

### Ampere's Law

The original form of Ampere's Law states that the integral of the magnetic field around a closed loop (`∮ B⋅dL`) is proportional to the amount of conventional electric current (`I_enclosed`) passing through the surface defined by that loop.

`∮ B⋅dL = μ₀ * I_enclosed`

### The Problem: A Charging Capacitor

Consider the gap between the plates of a charging capacitor. If we draw an Amperian loop around this gap, there is no actual flow of charge (`I_enclosed = 0`) passing through the surface. The original Ampere's Law would incorrectly predict that the magnetic field here is zero. However, experiments show that there *is* a magnetic field, which means the law was incomplete.

### Maxwell's Addition: Displacement Current

Maxwell resolved this by noticing that as the capacitor charges, the electric field `E` in the gap is changing. This changing E-field creates a changing electric flux `ΦE`. He proposed that this changing electric flux acts as a source of the magnetic field, just like a real current.

He defined this effective current as the **displacement current (`I_d`)**:

`I_d = ε₀ * (dΦE / dt)`

-   `ε₀` is the permittivity of free space.
-   `dΦE / dt` is the rate of change of the electric flux.

### The Maxwell-Ampere Law

Maxwell added his displacement current term to the original Ampere's Law to create the complete and correct version, which is one of the four Maxwell's Equations:

`∮ B⋅dL = μ₀ * (I_enclosed + I_d) = μ₀*I_enclosed + μ₀ε₀*(dΦE/dt)`

This law shows that a circulating magnetic field can be created by two sources: a conventional current of moving charges (`I_enclosed`) OR a changing electric flux (`I_d`).

## 3. The Simulation: The Induced B-Field

### Outline of the Simulation

The `intermediate.py` file shows a parallel plate capacitor being charged by a constant current. This creates a constantly changing electric field in the gap. Your goal is to use the Maxwell-Ampere Law to calculate the magnetic field that is induced by this changing electric flux.

### Completing the `intermediate.py` File

#### **Task 1: Calculate the Rate of Change of Flux**

- **Example (Rate of Change of E-field):** If the capacitor is charged by a constant current `I`, the E-field between the plates increases at a constant rate. The code to calculate this rate, `dE_dt`, is given as an example.
  ```python
  dE_dt = I_charge / (Area * epsilon_0)
  ```

- **Your Task (Rate of Change of Flux):** The electric flux is `ΦE = E * A`. Therefore, the rate of change of flux is `dΦE/dt = (dE/dt) * A`. Write the line of code to calculate `dFlux_dt`. Be sure to use the area of the yellow Amperian loop (`loop_area`), not the full area of the capacitor plates.

#### **Task 2: Calculate the Induced B-Field**

Now you must apply the Maxwell-Ampere Law. In the gap between the plates, the conventional current `I_enclosed` is zero, so the law simplifies to `∮ B⋅dL = μ₀ε₀ * (dΦE/dt)`.

For a circular Amperian loop, the integral on the left side becomes `B * (2πr)`.

- **Your Task:** Rearrange the Maxwell-Ampere Law to solve for the magnitude of the magnetic field, `B_mag`, at the radius of your loop (`r_loop`). Write the line of code to perform this calculation using `dFlux_dt`, `r_loop`, and the physical constants `μ₀` and `ε₀`.

#### **Task 3: Visualize the B-Field**

- **Your Task:** The final step is to draw arrows to represent the B-field you calculated. The code already loops through several points on the yellow ring. Inside this loop, you need to create an `arrow` object.
    - The arrow's `pos` should be the position of the point on the loop.
    - The arrow's `axis` represents the B-field vector. The direction is tangential to the loop (the code provides a `B_dir` vector for you). The magnitude is the `B_mag` you calculated. You will need to multiply the final axis vector by a scaling factor to make it visible.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CEM/program/5.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/b7cee044c6aa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>