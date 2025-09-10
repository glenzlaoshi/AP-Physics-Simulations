---
title: "4.1 - Field from a Current Loop"
layout: default
---


## 1. Introduction to the Unit: Sources of Magnetic Fields

This unit delves into the origin of magnetic fields. The fundamental source of any magnetic field is a **moving electric charge**, or more macroscopically, an **electric current**. We will explore the two primary laws used to calculate the magnetic field created by a specific arrangement of currents:

1.  **Ampere's Law:** A powerful tool that is very useful for calculating the B-field in situations with high symmetry (e.g., around a long, straight wire). It is analogous to Gauss's Law for electric fields.
2.  **The Biot-Savart Law:** A more general and fundamental law that allows you to calculate the magnetic field from any arbitrary shape of current-carrying wire. It is analogous to Coulomb's Law for electric fields. 

This simulation focuses on using the Biot-Savart Law to find the field from a circular loop of current.

## 2. Relevant Physics Concepts

### The Biot-Savart Law

This law gives the contribution to the magnetic field (`dB`) from an infinitesimally small segment of wire (`dL`) carrying a current `I`.

`dB = (μ₀ / 4π) * (I * dL x r_hat) / r²`

This is a complex vector equation:
-   `μ₀` is the **permeability of free space**, a fundamental constant.
-   `I` is the current in the wire.
-   `dL` is an infinitesimal vector that points along the wire in the direction of the current.
-   `r` is the distance from the wire segment `dL` to the point in space where you are calculating the field.
-   `r_hat` is the unit vector pointing from the wire segment to that point.
-   `x` denotes the **cross product**, which means the resulting `dB` field is perpendicular to both the wire segment `dL` and the position vector `r`.

### Integration

To find the total magnetic field `B` at a point, one must integrate (sum up) all the infinitesimal `dB` contributions from every segment of the wire.

`B = ∫ dB`

For most non-trivial shapes, this integral is difficult or impossible to solve analytically. This makes it a perfect problem to solve numerically with a computer simulation.

### Field on the Axis of a Current Loop

For the special case of a point on the central axis of a circular current loop (radius `R`), the integral can be solved. The result for the magnitude of the B-field at a distance `z` along the axis is:

`B_axis = (μ₀ * I * R²) / (2 * (z² + R²)^(3/2))`

We will use this exact formula to verify the result of our numerical integration.

## 3. The Simulation: Integrating the Law

### Outline of the Simulation

The `intermediate.py` file shows a circular loop of wire. The simulation will calculate the magnetic field at a specific point on the axis of the loop. It does this by breaking the loop into a large number of small segments (`dL`) and adding up the `dB` contribution from each segment, effectively performing a numerical integration.

### Completing the `intermediate.py` File

Your task is to complete the calculation inside the `for` loop, which iterates through each segment of the wire.

#### **Task 1: Define the `dL` vector**

- **Your Task:** The code loops through angles to define points along the ring. A `dL` vector is a small, straight segment of this ring. You can find it by taking the vector difference between two adjacent points on the loop, `pos2 - pos1`. Write the line of code to define `dL`.

#### **Task 2: Apply the Biot-Savart Law**

- **Example (The `r` vector):** The vector `r` points from the wire segment to the point of interest. The code to calculate this `r_vec` (from the midpoint of the `dL` segment) is given as an example.

- **Your Task (Biot-Savart Calculation):** This is the main step. You need to write the single line of code that calculates the `dB` vector using the Biot-Savart formula. This will require you to:
    1.  Calculate the magnitude of `r_vec` (`r_mag`).
    2.  Calculate the unit vector `r_hat`.
    3.  Calculate the cross product of `dL` and `r_hat` using `cross()`.
    4.  Combine all the pieces (`μ₀`, `I`, the cross product, `r_mag²`) into the full formula.

- **Your Task (Integration):** Add the `dB` vector you just calculated to the `B_total` variable. The `for` loop will take care of the summation.

#### **Task 3: Compare with Theory**

- **Your Task:** After the loop, calculate the theoretical B-field magnitude, `B_theory_z`, using the provided analytical formula for a point on the axis. All the necessary variables (`μ₀`, `I`, `R`, `z`) are available.
- **Analysis:** The program will print your numerical result (`B_total`) and the theoretical result. How closely do they match? What could you change to improve the accuracy of the numerical integration?

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CEM/program/4.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/49dd495f5da0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The Biot-Savart Law is used to calculate the magnetic field contribution from:
    a) A large, symmetric charge distribution.
    b) A changing electric flux.
    c) An infinitesimal segment of a current-carrying wire.
    d) A single stationary point charge.

2.  The direction of the magnetic field `dB` calculated from the Biot-Savart law is:
    a) In the same direction as the current element `dL`.
    b) In the same direction as the position vector `r`.
    c) Parallel to both `dL` and `r`.
    d) Perpendicular to both `dL` and `r`.

3.  A circular loop of wire carries a current in the counter-clockwise direction when viewed from above. At the exact center of the loop, the magnetic field points:
    a) Radially outward.
    b) Radially inward.
    c) Upwards.
    d) Downwards.

4.  According to the formula for the B-field on the axis of a current loop, what happens to the field at the center of the loop (`z=0`) if the radius `R` is doubled while the current `I` is kept constant?
    a) It is quartered.
    b) It is halved.
    c) It is doubled.
    d) It is quadrupled.

5.  Ampere's Law is most useful for calculating the magnetic field in situations with high symmetry, while the Biot-Savart Law is:
    a) Only useful for situations with no symmetry.
    b) A more general law that can be applied to any current distribution.
    c) Only applicable to straight wires.
    d) A simplified version of Ampere's Law.

### Problem-Solving Questions

1.  A circular loop of wire with radius `R` carries a current `I`. The magnetic field at the center of the loop (`z=0`) is `B_center = μ₀I / (2R)`. If a second loop has radius `2R` and carries current `2I`, what is the magnetic field at its center?
    a) `B_center / 4`
    b) `B_center / 2`
    c) `B_center`
    d) `2 * B_center`

2.  A small segment of wire `dL` points in the +x direction. The position vector `r` from this segment to a point of interest points in the +y direction. The current `I` is positive. In which direction does the magnetic field contribution `dB` point?
    a) +x direction
    b) -x direction
    c) +z direction
    d) -z direction

3.  The magnetic field on the axis of a current loop of radius R is `B(z) = (μ₀IR²) / (2(z² + R²)^(3/2))`. What is the approximate behavior of the field far from the loop (`z >> R`)?
    a) It is constant.
    b) It falls off as `1/z`.
    c) It falls off as `1/z²`.
    d) It falls off as `1/z³`.

4.  To find the total magnetic field `B` from a wire of a given shape, one must perform which mathematical operation on the `dB` contributions from the Biot-Savart Law?
    a) A dot product.
    b) A cross product.
    c) A derivative.
    d) An integral.

5.  A current `I` flows in a square loop of side length `L`. What is the magnitude of the magnetic field at the center of the square? (This requires integrating the Biot-Savart law for each side). The result is `B = (2√2 * μ₀I) / (πL)`. If you double the side length `L`, the field at the center will be:
    a) Doubled.
    b) Halved.
    c) Quadrupled.
    d) Quartered.

### Computational Questions

1.  The simulation calculates the total B-field by summing `dB` in a `for` loop. This numerical summation is an approximation of a:
    a) Surface integral.
    b) Volume integral.
    c) Line integral.
    d) Time derivative.

2.  The code calculates `dB` using the `cross(dL, r_hat)` function. This directly implements which part of the Biot-Savart Law?
    a) The `1/r²` dependence.
    b) The vector cross product.
    c) The constant `μ₀ / 4π`.
    d) The integration over the wire.

3.  The simulation calculates `dL` as the vector difference between two adjacent points on the loop (`pos2 - pos1`). This provides a small, straight vector that approximates:
    a) The radius of the loop.
    b) The circumference of the loop.
    c) An infinitesimal segment of the curved wire.
    d) The magnetic field vector.

4.  If you increase the number of segments (`n_segments`) in the simulation, what is the expected effect on the result?
    a) The calculated `B_total` will become less accurate.
    b) The simulation will run faster.
    c) The calculated `B_total` will more closely approximate the true value of the integral.
    d) The theoretical value `B_theory_z` will change.

5.  The simulation compares the numerical result `B_total` to the analytical formula `B_theory_z`. This comparison is only valid because the point of interest is located:
    a) At the center of the loop.
    b) On the axis of the loop.
    c) Very far from the loop.
    d) On the wire of the loop itself.

---
### Answer Key
**Conceptual:** 1. (c), 2. (d), 3. (c), 4. (b), 5. (b)
**Problem-Solving:** 1. (c), 2. (c), 3. (d), 4. (d), 5. (b)
**Computational:** 1. (c), 2. (b), 3. (c), 4. (c), 5. (b)
