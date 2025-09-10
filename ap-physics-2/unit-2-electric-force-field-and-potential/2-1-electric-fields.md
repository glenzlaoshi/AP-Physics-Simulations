---
title: "2.1 - Electric Fields"
layout: default
---


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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The electric field at a point in space is defined as the:
    a) Total charge at that point.
    b) Force per unit charge on a positive test charge placed at that point.
    c) Force per unit charge on a negative test charge placed at that point.
    d) Total force on all charges in the system.

2.  Electric field lines point:
    a) Away from positive charges and towards negative charges.
    b) Towards positive charges and away from negative charges.
    c) In the direction of the force on a negative charge.
    d) From a lower potential to a higher potential.

3.  The Principle of Superposition for electric fields states that the net electric field at a point is the:
    a) Product of the individual fields.
    b) Average of the individual fields.
    c) Scalar sum of the magnitudes of the individual fields.
    d) Vector sum of the individual fields.

4.  A small positive charge `+q` is placed at the center of a hollow conducting sphere that has a net charge of `+Q`. What is the direction of the electric field outside the sphere?
    a) Radially inward.
    b) Radially outward.
    c) Zero.
    d) It depends on the magnitude of `q` and `Q`.

5.  If the distance from a source charge is doubled, the strength of the electric field it creates is:
    a) Quartered.
    b) Halved.
    c) Doubled.
    d) Quadrupled.

### Problem-Solving Questions

(Use k = 9 x 10⁹ N·m²/C²)

1.  What is the magnitude of the electric field at a distance of 0.5 m from a +2.0 nC point charge?
    a) 18 N/C
    b) 36 N/C
    c) 72 N/C
    d) 144 N/C

2.  An electric field has a strength of 500 N/C. What is the magnitude of the force on a proton (charge = 1.6e-19 C) placed in this field?
    a) 3.1e-22 N
    b) 8.0e-17 N
    c) 500 N
    d) 3.1e21 N

3.  Two point charges, `q1 = +4 nC` and `q2 = -4 nC`, are separated by 0.2 m. What is the magnitude and direction of the electric field at the midpoint between them?
    a) Zero.
    b) 900 N/C, towards q1.
    c) 1800 N/C, towards q2.
    d) 3600 N/C, towards q2.

4.  A charge of `+Q` is at `x=0`. A charge of `-2Q` is at `x=d`. At which point on the x-axis is the electric field equal to zero?
    a) Between the charges.
    b) To the right of the -2Q charge.
    c) To the left of the +Q charge.
    d) The field is never zero on the x-axis.

5.  What is the magnitude of the force between a +10 μC charge and a -20 μC charge separated by 0.1 m?
    a) 18 N
    b) 90 N
    c) 180 N
    d) 1800 N

### Computational Questions

1.  The simulation calculates the net electric field using a `for` loop. This loop is a direct implementation of which physics principle?
    a) Coulomb's Law.
    b) The definition of charge.
    c) The Principle of Superposition.
    d) Gauss's Law.

2.  The code calculates `r_vec = position - s.pos`. This vector points from:
    a) The origin to the test position.
    b) The test position to the source charge.
    c) The source charge to the test position.
    d) The origin to the source charge.

3.  The final step in calculating the E-field from a single source is `E_source = (k * s.q / r_mag**2) * r_hat`. What is the purpose of multiplying by `r_hat`?
    a) To calculate the magnitude of the field.
    b) To give the electric field vector the correct direction.
    c) To make the field attractive.
    d) To convert the units to N/C.

4.  If you were to change the sign of the blue source charge from negative to positive in the simulation, how would the electric field at the midpoint between the two charges change?
    a) It would become zero.
    b) It would double in magnitude.
    c) It would point upwards.
    d) It would not change.

5.  The simulation visualizes the E-field with an arrow. The length of the arrow represents the field's ________, and the direction of the arrow represents the field's ________.
    a) Magnitude, Direction.
    b) Direction, Magnitude.
    c) Charge, Force.
    d) Force, Charge.

---
### Answer Key
**Conceptual:** 1. (b), 2. (a), 3. (d), 4. (b), 5. (a)
**Problem-Solving:** 1. (c), 2. (b), 3. (d), 4. (c), 5. (c)
**Computational:** 1. (c), 2. (c), 3. (b), 4. (a), 5. (a)
