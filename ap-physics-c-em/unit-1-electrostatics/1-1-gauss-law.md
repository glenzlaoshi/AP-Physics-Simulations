---
title: "1.1 - Gauss's Law"
layout: default
---


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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  Gauss's Law relates the electric flux through a closed surface to:
    a) The net charge outside the surface.
    b) The net charge enclosed by the surface.
    c) The surface area of the surface.
    d) The electric field at a single point on the surface.

2.  A spherical Gaussian surface surrounds a point charge `+q`. If the radius of the Gaussian surface is doubled, the total electric flux through the surface will:
    a) Be quartered.
    b) Be halved.
    c) Remain the same.
    d) Be doubled.

3.  For which of the following charge distributions would Gauss's Law be most useful for easily calculating the electric field?
    a) A single point charge.
    b) An electric dipole.
    c) An infinitely long, uniformly charged wire.
    d) A finite, charged rod.

4.  The electric field is zero everywhere inside a hollow, charged conducting sphere. According to Gauss's Law, this implies that for any Gaussian surface placed inside the sphere:
    a) The net enclosed charge must be zero.
    b) The electric flux must be zero.
    c) The surface area must be zero.
    d) Both a and b are correct.

5.  A Gaussian surface encloses no net charge. Which of the following statements must be true?
    a) The electric field is zero everywhere on the surface.
    b) The electric field is uniform everywhere on the surface.
    c) The net electric flux through the surface is zero.
    d) The number of charges inside and outside the surface is equal.

### Problem-Solving Questions

1.  A point charge of +5.0 μC is at the center of a cube with sides of length 0.2 m. What is the total electric flux through the surface of the cube? (Use ε₀ = 8.85e-12 C²/N·m²)
    a) 5.65e5 N·m²/C
    b) 1.41e5 N·m²/C
    c) 2.26e6 N·m²/C
    d) Zero.

2.  An infinitely long line of charge has a uniform linear charge density `λ`. Using a cylindrical Gaussian surface of radius `r` and length `L`, what is the `Q_enclosed`?
    a) `λL`
    b) `λ / L`
    c) `λ * 2πr`
    d) `λ * 2πrL`

3.  Using Gauss's Law for the infinite line of charge from the previous question, the electric field at a distance `r` is found to be `E = λ / (2πε₀r)`. This field strength is proportional to:
    a) `r`
    b) `r²`
    c) `1/r`
    d) `1/r²`

4.  A large, flat, non-conducting sheet has a uniform surface charge density `σ`. The electric field created by this sheet is `E = σ / (2ε₀)`. What is the electric flux through a small patch of area `A` on a Gaussian surface that is parallel to the sheet?
    a) `E * A`
    b) Zero, because the E-field is parallel to the surface patch.
    c) `σ * A`
    d) `σ * A / ε₀`

5.  A solid insulating sphere of radius `R` has a total charge `Q` distributed uniformly throughout its volume. What is the electric field at a distance `r > R` from the center?
    a) `kQ / R²`
    b) `kQ / r²`
    c) `kQr / R³`
    d) Zero.

### Computational Questions

1.  The simulation calculates the total flux by summing `dFlux` over many small patches. This numerical summation is an approximation of which mathematical operation?
    a) A line integral (`∫ E ⋅ dl`)
    b) A surface integral (`∮ E ⋅ dA`)
    c) A derivative (`dE/dA`)
    d) A simple multiplication (`E * A`)

2.  The flux through a single patch is calculated as `dFlux = dot(E, dA_vec)`. The dot product is used because:
    a) It correctly multiplies the magnitudes of the vectors.
    b) It finds the component of the E-field that is perpendicular to the surface patch area.
    c) It finds the component of the E-field that is parallel to the surface patch area.
    d) It is the only way to multiply vectors in VPython.

3.  In the simulation, the area vector `dA_vec` for a patch on the sphere always points radially outward. Why is this the correct direction?
    a) Because the E-field points radially outward.
    b) By convention, the area vector for a closed surface points outward.
    c) Because the charge is positive.
    d) To make the dot product with the E-field equal to zero.

4.  If you increase the number of patches in the simulation (e.g., increase `n_theta` and `n_phi`), what will happen to the accuracy of the calculated `total_flux`?
    a) It will become less accurate.
    b) It will become more accurate, getting closer to the theoretical value.
    c) The accuracy will not change.
    d) The simulation will run faster.

5.  The theoretical flux is calculated as `flux_theory = Q_enclosed / epsilon_0`. If you were to add a second charge *outside* the Gaussian surface in the simulation, how would this affect `flux_theory`?
    a) It would increase.
    b) It would decrease.
    c) It would not change.
    d) It would depend on the sign of the second charge.

---
### Answer Key
**Conceptual:** 1. (b), 2. (c), 3. (c), 4. (d), 5. (c)
**Problem-Solving:** 1. (a), 2. (a), 3. (c), 4. (b), 5. (b)
**Computational:** 1. (b), 2. (b), 3. (b), 4. (b), 5. (c)
