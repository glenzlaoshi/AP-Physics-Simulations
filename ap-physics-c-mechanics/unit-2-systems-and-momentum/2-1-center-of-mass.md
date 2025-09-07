---
title: "2.1 - Center of Mass"
layout: default
---


## 1. Introduction to the Unit: Systems of Particles

This unit builds on the concept of momentum from AP Physics 1, but with a more rigorous, calculus-based approach. We introduce the concept of the **Center of Mass (CM)**, which is the mass-weighted average position of all the particles that make up a system.

The most powerful insight of this unit is that **the center of mass of a system moves as if all the system's mass were concentrated at that single point, and all the net external forces were applied at that point.**

This means that **internal forces**—forces that parts of the system exert on each other, like the forces in an explosion—have no effect on the motion of the center of mass. This allows us to analyze the overall motion of a complex system in a very simple way.

## 2. Relevant Physics Concepts

### Center of Mass Position (`R_cm`)

The position of the center of mass is a weighted average. For a system of discrete particles, the formula is a vector equation:

`R_cm = (m₁r₁ + m₂r₂ + m₃r₃ + ...) / (m₁ + m₂ + m₃ + ...)`

-   `m₁, m₂, ...` are the masses of the particles.
-   `r₁, r₂, ...` are the position vectors of the particles.
-   The denominator is simply the total mass of the system, `M_total`.

### Motion of the Center of Mass

By taking the time derivative of the position equation, we can find the velocity of the center of mass:

`V_cm = (m₁v₁ + m₂v₂ + ...) / M_total = P_system / M_total`

where `P_system` is the total momentum of the system. This gives the important relation `P_system = M_total * V_cm`.

Taking the derivative again gives us Newton's Second Law for a system:

**`F_net_external = M_total * a_cm`**

This is the key takeaway. The acceleration of the center of mass (`a_cm`) depends **only on the net external force**. In the case of a projectile flying through the air, the only external force is gravity. The forces of an explosion are **internal** to the system. Therefore, even if the projectile explodes, the center of mass of all its fragments must continue to move along the exact same parabolic trajectory it was on before the explosion.

## 3. The Simulation: The Exploding Projectile

### Outline of the Simulation

The `intermediate.py` file launches a projectile. At the peak of its trajectory, it explodes into three fragments. The fragments fly apart due to the internal forces of the explosion. Your task is to calculate the position of the center of mass of this system of fragments at each time step and verify that its motion is unaffected by the explosion.

### Completing the `intermediate.py` File

The code already handles the projectile launch and the creation of the fragments at the moment of explosion. Your work takes place in the `else` block, which runs after the explosion has occurred.

#### **Task 1: Move the Fragments**

After the explosion, each fragment is an independent projectile, moving only under the influence of the external force of gravity.

- **Your Task:** Inside the `else` block, you must loop through all the fragments in the `fragments` list. For each fragment `f`, write the two familiar lines of code to update its `velocity` and `pos` based on the constant downward acceleration of gravity, `-g`.

#### **Task 2: Calculate and Track the Center of Mass**

This is the main analysis. At each time step, you need to calculate the position of the center of mass (`R_cm`) of the three-fragment system.

- **Example (The Numerator):** The numerator of the `R_cm` formula is the sum of the `m*r` vectors for all fragments. The code to do this for the three fragments (`f1`, `f2`, `f3`) is given as an example:
  ```python
  sum_mr = f1.m*f1.pos + f2.m*f2.pos + f3.m*f3.pos
  ```

- **Your Task (The Denominator and `R_cm`):** The denominator is the total mass of the system, which is stored in `projectile.m`. Write the line of code to calculate the center of mass position vector, `R_cm`, by dividing `sum_mr` by the total mass.

- **Your Task (Update the Marker):** A white sphere, `cm_marker`, has been created to visualize the center of mass. Write the line of code to set its `.pos` property equal to the `R_cm` vector you just calculated.

When you run the completed simulation, you will see the fragments fly apart wildly, but the white marker will continue to trace a perfect parabola, exactly following the original path of the un-exploded projectile, proving that `F_net_external = M_total * a_cm`.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CMech/program/2.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/38b1bff5d4fb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>