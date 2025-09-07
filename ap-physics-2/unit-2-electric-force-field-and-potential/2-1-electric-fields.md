---
title: "2.1 - Electric Fields"
layout: default
---
# Information: Electric Fields

## 1. Introduction to the Unit: Electrostatics

This unit begins our study of electricity by looking at **electrostatics**: the physics of stationary electric charges. The fundamental new property we introduce is **electric charge**, which comes in two types, positive and negative. The fundamental rule is that like charges repel each other, and opposite charges attract.

To describe how charges influence each other across empty space, we use the concept of a **field**. We say that a "source charge" creates an **electric field** in the space around it. Any other "test charge" that is placed in this field will experience a force. This field model is one of the most important concepts in electricity and magnetism.

## 2. Relevant Physics Concepts

### Coulomb's Law

This law describes the magnitude of the electric force (`Fe`) between two point charges, `q1` and `q2`, separated by a distance `r`.

`Fe = k * |q1 * q2| / r²`

-   `k` is Coulomb's constant, approximately `9 x 10⁹ N·m²/C²`.
-   The force is a **vector**, directed along the line connecting the two charges. It is repulsive for like charges and attractive for opposite charges.

### The Electric Field (`E`)

The electric field is a vector field that describes the influence of a source charge `Q` on the space around it. It is defined as the force per unit charge that a positive test charge would experience.

`E = F / q_test`

-   The direction of the E-field at a point is the direction of the force a **positive** test charge would feel at that point.
-   The E-field from a single source charge `Q` has a magnitude `E = k * |Q| / r²`.
-   The field lines point **away** from positive source charges and **towards** negative source charges.

### The Principle of Superposition

If there are multiple source charges, the net electric field at any point in space is simply the **vector sum** of the individual electric fields created by each source charge.

`E_net = E1 + E2 + E3 + ...`

This principle is key to calculating the field for any arrangement of charges.

## 3. The Simulation: Mapping the Field

### Outline of the Simulation

The `intermediate.py` file shows two source charges (a positive red one and a negative blue one, which form a **dipole**). It also shows a yellow "test charge" that you can drag with your mouse. An orange arrow represents the electric field at the test charge's location. Your goal is to complete the function that calculates the net electric field at any given point by applying the principle of superposition.

### Completing the `intermediate.py` File

Your work will be done inside the function `calculate_E_field(position, source_charges)`.

#### **Task 1: Sum the Fields from All Sources**

The function must loop through the list of `source_charges` and add up their individual contributions to the electric field at the given `position`.

- **Example (The `r` vector):** For each source charge `s` in the loop, the first step is to find the vector `r_vec` that points from the source charge to the `position` where we are calculating the field. The code for this is:
  ```python
  r_vec = position - s.pos
  ```

- **Your Task (E-field from one source):** Now, you need to calculate the electric field vector, `E_source`, created by this single source `s`. The formula is `E = (k*q/r²) * r_hat`. You will need to:
    1.  Find the magnitude of `r_vec` (`r_mag`).
    2.  Find the direction unit vector of `r_vec` (`r_hat`).
    3.  Combine these with the source's charge `s.q` and Coulomb's constant `k` to write the line of code that calculates `E_source`.

- **Your Task (Superposition):** The net field `E_net` is the vector sum of the fields from all sources. Add the `E_source` vector you just calculated to the `E_net` variable. The `for` loop will then repeat this process for the next source charge, automatically summing the vectors for you.

#### **Task 2: Update the E-field Arrow**

- **Your Task:** The main animation loop continuously calls your `calculate_E_field` function. Once your function is working correctly, you just need to make the orange arrow (`E_arrow`) visualize the result. Set the arrow's `.axis` property equal to the `E_at_point` vector that is returned by your function. You will need to multiply the result by a scaling factor (e.g., `1e-4`) to make the arrow a reasonable size on the screen.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/2.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/695dc7931799" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>