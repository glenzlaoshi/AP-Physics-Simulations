---
title: "5.1 - Maxwell-Ampere Law"
layout: default
---


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

## Multiple Choice Questions

### Conceptual Questions

1.  According to the Maxwell-Ampere Law, what is a possible source of a magnetic field?
    a)  Only a constant electric current.
    b)  Only a changing electric field.
    c)  Both a constant electric current and a changing electric field.
    d)  A constant magnetic field.
2.  Why was Ampere's original law considered incomplete?
    a)  It did not account for the magnetic field created by a changing electric flux, such as in a charging capacitor.
    b)  It only worked for straight wires.
    c)  It did not correctly predict the magnetic field inside a solenoid.
    d)  It violated the conservation of charge.
3.  What is "displacement current"?
    a)  The physical flow of charges through the empty space in a capacitor.
    b)  A theoretical concept representing the effect of a changing electric field as a source of a magnetic field.
    c)  The current that is displaced to the sides of a conductor.
    d)  The current created by a changing magnetic field.
4.  In the region between the plates of a charging parallel-plate capacitor, which of the following is true?
    a)  There is a magnetic field but no electric field.
    b)  There is an electric field but no magnetic field.
    c)  There are both an electric field and a magnetic field.
    d)  There is neither an electric field nor a magnetic field.
5.  If the rate of change of the electric flux through an Amperian loop is zero, what can be concluded about the magnetic field around the loop?
    a)  The magnetic field must be zero.
    b)  The magnetic field is constant in time.
    c)  The magnetic field is caused only by the conventional current enclosed by the loop.
    d)  The magnetic field is uniform in space.

### Problem-Solving Questions

6.  A parallel-plate capacitor with circular plates of radius R is being charged by a current I. What is the magnitude of the magnetic field at a radius r < R from the center of the plates?
    a)  `B = (μ₀ * I * r) / (2 * π * R^2)`
    b)  `B = (μ₀ * I * R) / (2 * π * r^2)`
    c)  `B = (μ₀ * I) / (2 * π * r)`
    d)  `B = (μ₀ * I * r^2) / (2 * π * R^3)`
7.  A circular parallel-plate capacitor of radius R is being charged with a current I. At what distance from the center of the capacitor is the induced magnetic field one-half of its maximum value? (The maximum value occurs at r=R).
    a)  r = R/4
    b)  r = R/2
    c)  r = R
    d)  r = 2R
8.  The electric field between the plates of a circular capacitor is given by `E = (5.0 * 10^5 V/m) * sin(100t)`. The plates have a radius of 0.1 m. What is the maximum magnitude of the induced magnetic field at r = 0.1 m? (μ₀ = 4π x 10⁻⁷ T·m/A, ε₀ = 8.85 x 10⁻¹² C²/N·m²)
    a)  `2.8 x 10⁻⁷ T`
    b)  `5.5 x 10⁻⁷ T`
    c)  `1.4 x 10⁻⁷ T`
    d)  `8.8 x 10⁻⁷ T`
9.  A charging capacitor has a displacement current of 2.0 A. What is the rate of change of the electric flux, `dΦE/dt`? (ε₀ = 8.85 x 10⁻¹² C²/N·m²)
    a)  `2.26 x 10¹¹ V·m/s`
    b)  `1.77 x 10⁻¹¹ V·m/s`
    c)  `4.43 x 10¹¹ V·m/s`
    d)  `8.85 x 10⁻¹² V·m/s`
10. A long straight wire carries a current I. A parallel plate capacitor with circular plates is placed so the wire passes through the center of the plates, perpendicular to them. The capacitor is being charged with a current `I_c`. What is the magnetic field at a distance r from the wire, between the plates?
    a)  `B = (μ₀ * I) / (2 * π * r)`
    b)  `B = (μ₀ * I_c * r) / (2 * π * R^2)`
    c)  `B = (μ₀ / (2 * π * r)) * (I + I_c * r^2 / R^2)`
    d)  `B = (μ₀ / (2 * π * r)) * (I + I_c)`

### Computational Questions

11. In the simulation, the rate of change of the electric field is calculated as `dE_dt = I_charge / (Area * epsilon_0)`. Why is the `Area` in this calculation the area of the capacitor plates and not the area of the Amperian loop?
    a)  The electric field is uniform and depends on the total charge on the plate, which is related to the plate area.
    b)  It is a mistake in the code; it should be the area of the Amperian loop.
    c)  The `Area` variable is actually the area of the Amperian loop.
    d)  The electric field change is only at the edge of the plates.
12. The simulation calculates the rate of change of flux as `dFlux_dt = dE_dt * loop_area`. Why is `loop_area` used here instead of the full plate area?
    a)  Because the Maxwell-Ampere law relates the B-field on the loop to the flux *through that specific loop*.
    b)  To make the resulting B-field smaller and easier to visualize.
    c)  It's an approximation that is only valid for small loops.
    d)  The flux is zero outside the loop.
13. If you were to modify the simulation to calculate the magnetic field *outside* the capacitor plates (at a radius `r > R`), how would the calculation of `dFlux_dt` change?
    a)  `dFlux_dt` would be calculated using the area of the capacitor plate (`πR²`) instead of the loop area, because the E-field is zero outside the plates.
    b)  `dFlux_dt` would be zero.
    c)  `dFlux_dt` would be calculated using the area `πr²`.
    d)  `dFlux_dt` would become negative.
14. In the simulation, the B-field is calculated using `B_mag = (mu_0 * epsilon_0 * dFlux_dt) / (2 * pi * r_loop)`. If you double the charging current `I_charge`, what happens to `B_mag`?
    a)  It is halved.
    b)  It remains the same.
    c)  It is doubled.
    d)  It is quadrupled.
15. The simulation sets the `axis` of the B-field arrow to `B_dir * B_mag * scale_factor`. Why is the `B_dir` vector necessary?
    a)  It ensures the B-field arrow points in the correct tangential direction around the Amperian loop.
    b)  It converts the scalar `B_mag` into a vector pointing away from the center.
    c)  It normalizes the `B_mag` value.
    d)  It points the arrow in the direction of the electric field.
