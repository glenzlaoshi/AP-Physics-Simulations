---
title: "4.1 - Field from a Current Loop"
layout: default
---
# Information: Magnetic Field from a Current Loop

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