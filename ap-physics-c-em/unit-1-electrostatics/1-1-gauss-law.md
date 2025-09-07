---
title: "1.1 - Gauss's Law"
layout: default
---
# Information: Gauss's Law

## 1. Introduction to the Unit: Electrostatics & Gauss's Law

This unit builds on the electrostatics concepts from AP Physics 2, but with a more rigorous, calculus-based foundation. We begin with the concept of **electric flux**, which is a measure of the amount of electric field "flowing" through a surface.

This leads us to **Gauss's Law**, one of the four fundamental **Maxwell's Equations** that govern all of electricity and magnetism. Gauss's Law provides a powerful alternative to Coulomb's Law for calculating the electric field. While Coulomb's Law is always true, Gauss's Law is often much simpler to apply in situations that have a high degree of symmetry (like spheres, cylinders, or planes of charge).

## 2. Relevant Physics Concepts

### Electric Flux (`ΦE`)

Imagine an electric field as lines in space. Electric flux is a scalar quantity that represents the net number of electric field lines passing through a given surface.

-   For a uniform field `E` and a flat area `A`, the flux is `ΦE = E * A * cos(θ)`, where `θ` is the angle between the field and the direction normal (perpendicular) to the surface.
-   More generally, flux is calculated by an integral over the surface: `ΦE = ∫ E ⋅ dA`.
-   `dA` is the **area vector**, which has a magnitude equal to a tiny area `dA` and a direction that is normal to the surface.
-   The dot product `E ⋅ dA` selects only the component of the electric field that is perpendicular to the surface at that point.

### Gauss's Law

Gauss's Law states that the net electric flux through any imaginary **closed surface** (called a "Gaussian surface") is directly proportional to the **net electric charge enclosed** by that surface.

`ΦE = ∮ E ⋅ dA = Q_enclosed / ε₀`

-   The circle on the integral sign means the integral is taken over a closed surface.
-   `Q_enclosed` is the total charge inside the surface.
-   `ε₀` (epsilon-naught) is the permittivity of free space, a fundamental constant of the universe.

This law is incredibly powerful. It means that no matter how complex the charges are *outside* the surface, they do not contribute to the total flux. It also means you can change the shape or size of your Gaussian surface, and as long as you don't change the amount of charge you are enclosing, the total flux remains exactly the same.

## 3. The Simulation: Verifying Gauss's Law

### Outline of the Simulation

The `intermediate.py` file shows a single point charge at the origin, surrounded by a spherical Gaussian surface. Your goal is to verify Gauss's Law by numerically calculating the total flux (`∮ E ⋅ dA`) and comparing it to the theoretical value (`Q_enclosed / ε₀`). To do this, you will break the spherical surface into many small patches, calculate the flux through each patch, and sum them up.

### Completing the `intermediate.py` File

#### **Task 1: Create Surface Patches**

- **Your Task:** The code sets up nested `for` loops to go through spherical coordinates `theta` and `phi`. Inside these loops, you need to write the code to find the `(x, y, z)` coordinates of a patch on the surface of a sphere with radius `gauss_radius`. The conversion formulas are:
  - `x = r * sin(θ) * cos(φ)`
  - `y = r * sin(θ) * sin(φ)`
  - `z = r * cos(θ)`

#### **Task 2: Calculate Flux Through a Patch**

For each patch, you need to calculate `dΦ = E ⋅ dA`.

- **Example (Area Vector `dA`):** For a sphere, the area vector `dA` always points radially outward. The calculation for its magnitude is complex, so the code to create the full `dA_vec` for a small patch is provided as an example.

- **Your Task (E-field):** Write the line of code to call the provided `calculate_E` function. This will find the electric field vector `E` at the position of your patch (`patch_pos`).

- **Your Task (Flux `dΦ`):** The flux through the small patch is the dot product of the E-field and the area vector. VPython has a built-in function `dot(A, B)`. Write the line of code to calculate `dFlux` by taking the dot product of the `E` vector and the `dA_vec`.

- **Your Task (Summation):** Add the `dFlux` you just calculated to the `total_flux` variable. The loops will then handle the rest of the summation over the entire surface.

#### **Task 3: Compare with Theory**

- **Your Task:** After the loops are complete, the final step is to compare your numerical result to the theory. Write the line of code to calculate the theoretical flux, `flux_theory`, using the simple formula from Gauss's Law: `Q_enclosed / epsilon_0`.
- **Analysis:** The program will print both your `total_flux` and the `flux_theory`. How close are they? What happens to the accuracy if you increase the number of patches (`n_theta` and `n_phi`)?

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CEM/program/1.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/f851b40dd418" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>