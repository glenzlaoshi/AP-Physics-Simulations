---
title: "2.2 - Electric Potential"
layout: default
---


## 1. Introduction to the Unit: Electric Potential

In our study of mechanics, we found that analyzing a system using **energy** (a scalar) was often much easier than using **forces** (vectors). The same is true in electrostatics. This unit introduces the concept of **Electric Potential**, which is an energy-based way to describe the influence of source charges on the space around them.

Electric Potential, commonly known as **voltage**, is a scalar property of space itself. Just as gravity creates a gravitational field, electric charges create an electric field and also an electric potential field. By knowing the potential at two different points, we can easily calculate the work required to move a charge between them.

## 2. Relevant Physics Concepts

### Electric Potential (`V`)

Electric Potential is defined as the electric potential energy (`Ue`) per unit charge (`q`).

`V = Ue / q`

-   The unit of electric potential is the **Volt (V)**, where `1 Volt = 1 Joule / Coulomb`.
-   Because it is a scalar, potential has a magnitude and a sign, but **no direction**. This makes calculations much simpler than with vector fields.

### Potential from a Point Charge

The electric potential `V` at a distance `r` from a single source charge `Q` is given by:

`V = k * Q / r`

-   `k` is Coulomb's constant (`9 x 10⁹ N·m²/C²`).
-   Note that the distance `r` is **not** squared, unlike in the formulas for force and E-field.
-   The potential is positive for a positive source charge `Q` and negative for a negative `Q`.

### Superposition for Potential

Since potential is a scalar, the net potential at a point from multiple source charges is the simple **algebraic sum** of the potentials from each individual charge. There are no vectors to worry about.

`V_net = V1 + V2 + V3 + ... = k*q1/r1 + k*q2/r2 + ...`

### Equipotential Lines

An **equipotential line** (or surface, in 3D) is a set of all points in space that have the same electric potential. 
-   It takes **no work** to move a charge along an equipotential line, because there is no change in its potential energy.
-   A key relationship is that electric field lines are always **perpendicular** to equipotential lines.

## 3. The Simulation: Mapping Equipotentials

### Outline of the Simulation

The `intermediate.py` file shows two source charges (a dipole). Your goal is to create an **equipotential map**. You will do this by calculating the electric potential `V` at every point on a grid and then assigning a color to each point based on its potential value. The result will be a contour map where regions of the same color represent equipotential lines.

### Completing the `intermediate.py` File

The file already provides the function `calculate_V` which correctly finds the potential at any given point. Your task is to use this function to build the map.

#### **Task 1: Create a Grid of Points**

To make a map, we need to sample the potential at many different locations. 

- **Your Task:** Write a nested `for` loop to create a 2D grid of points. The outer loop should go through the x-coordinates and the inner loop should go through the y-coordinates. Inside the inner loop, create a small `box` object at each `(x,y)` location and add it to the `grid_points` list.

#### **Task 2: Color the Grid by Potential**

Now that you have a list of points, you need to loop through them and set their color based on the potential at their location.

- **Example (Calculating Potential):** For each `point` in your `grid_points` list, the first step is to calculate the potential `V` at that point's position. The code for this is given as an example:
  ```python
  V_at_point = calculate_V(point.pos, sources)
  ```

- **Your Task (Color Mapping):** Now you must convert the number `V_at_point` into a color. To do this, you need to map the range of potential values to a color gradient. For this simulation, you can assume the potential ranges from a minimum of `V_min = -100` to a maximum of `V_max = 100`.

  1.  **Normalize the potential:** Convert `V_at_point` into a number between 0 and 1. A simple way is `color_val = (V_at_point - V_min) / (V_max - V_min)`. Write the code to do this.
  2.  **Set the color:** Use this `color_val` to set the `point.color` property. The vector `vector(color_val, 0, 1 - color_val)` will create a gradient that goes from blue (low potential) to red (high potential). Write the line of code to set the point's color.

When you run the code, you will see the equipotential map appear.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/2.2-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/44577f0aac2e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  Electric potential is a ________ quantity, and electric field is a ________ quantity.
    a) scalar, scalar
    b) scalar, vector
    c) vector, scalar
    d) vector, vector

2.  If you move a positive charge along an equipotential line, the work done by the electric field is:
    a) Positive.
    b) Negative.
    c) Zero.
    d) It depends on the direction of movement.

3.  How are electric field lines and equipotential lines oriented with respect to each other?
    a) They are always parallel.
    b) They are always perpendicular.
    c) They are in the same direction.
    d) The angle between them depends on the charge.

4.  A positive charge is released from rest in an electric field. It will move towards a region of:
    a) Higher electric potential.
    b) Lower electric potential.
    c) The same electric potential.
    d) Zero electric field.

5.  Two point charges, `+q` and `-q`, are placed on the x-axis. At the midpoint between them, which of the following is true?
    a) The electric field is zero, and the electric potential is zero.
    b) The electric field is non-zero, and the electric potential is zero.
    c) The electric field is zero, and the electric potential is non-zero.
    d) The electric field is non-zero, and the electric potential is non-zero.

### Problem-Solving Questions

(Use k = 9 x 10⁹ N·m²/C²)

1.  What is the electric potential at a distance of 0.2 m from a +5.0 nC point charge?
    a) 112.5 V
    b) 225 V
    c) 450 V
    d) 900 V

2.  How much work is required to move a +2.0 μC charge from a point with a potential of 50 V to a point with a potential of 150 V?
    a) 1.0 x 10⁻⁴ J
    b) 2.0 x 10⁻⁴ J
    c) 3.0 x 10⁻⁴ J
    d) 4.0 x 10⁻⁴ J

3.  A +4 nC charge is at the origin. A -2 nC charge is at x = 0.06 m. What is the net electric potential at the point x = 0.03 m on the x-axis?
    a) 300 V
    b) 600 V
    c) 900 V
    d) 1800 V

4.  An electron (charge = -1.6e-19 C) is accelerated from rest through a potential difference of 1000 V. What is its final kinetic energy?
    a) 1.6e-22 J
    b) 1.6e-19 J
    c) 1.6e-16 J
    d) 1000 J

5.  Four equal positive charges `+q` are placed at the corners of a square with side length `s`. What is the electric potential at the center of the square?
    a) Zero.
    b) `4kq / s`
    c) `4√2 * kq / s`
    d) `8kq / s²`

### Computational Questions

1.  The simulation calculates the net potential at a point by algebraically summing the potential from each source charge. This works because electric potential is a:
    a) Vector.
    b) Scalar.
    c) Force.
    d) Field line.

2.  The simulation creates a contour map where regions of the same color represent:
    a) Regions of constant electric field.
    b) Equipotential lines.
    c) The path a charge would follow.
    d) Regions of constant force.

3.  The code normalizes the potential using `(V_at_point - V_min) / (V_max - V_min)` to get a value between 0 and 1. What is this value used for?
    a) To calculate the force.
    b) To determine the direction of the E-field.
    c) To map the potential to a color gradient.
    d) To calculate the kinetic energy.

4.  If you were to modify the simulation to have two positive source charges instead of a dipole, how would the equipotential line exactly at the midpoint between them look?
    a) It would be a point of very high potential.
    b) It would be a point of very low (negative) potential.
    c) It would be a point where V=0.
    d) It would be a "saddle point" where the potential is a minimum along one axis and a maximum along another.

5.  The simulation calculates potential using `V = k*Q/r`. If you wanted to calculate the electric *field* magnitude instead, you would need to change the formula to:
    a) `E = k*Q/r²`
    b) `E = k*Q*r`
    c) `E = Q/k*r`
    d) `E = V/r`

---
### Answer Key
**Conceptual:** 1. (b), 2. (c), 3. (b), 4. (b), 5. (b)
**Problem-Solving:** 1. (b), 2. (b), 3. (b), 4. (c), 5. (c)
**Computational:** 1. (b), 2. (b), 3. (c), 4. (d), 5. (a)
