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

## Multiple Choice Questions

### Conceptual Questions

1.  A firecracker is thrown into the air. It explodes into many fragments. What happens to the center of mass of the system of fragments?
    a)  It falls straight down from the point of explosion.
    b)  It follows the same parabolic path as the firecracker would have if it had not exploded.
    c)  Its motion becomes chaotic and unpredictable.
    d)  It moves horizontally from the point of explosion.
2.  Which of the following forces can change the velocity of the center of mass of a system?
    a)  The force of a spring connecting two masses in the system.
    b)  The force of gravity acting on the system.
    c)  The force of an explosion within the system.
    d)  All of the above.
3.  Two objects of unequal mass are connected by a compressed spring. They are at rest on a frictionless surface. The spring is released. What can be said about the motion of the center of mass of the two-object system?
    a)  It moves in the direction of the heavier mass.
    b)  It moves in the direction of the lighter mass.
    c)  It remains at rest.
    d)  It oscillates back and forth.
4.  A system consists of two particles. Under what condition is the center of mass of the system located at the midpoint between the two particles?
    a)  The masses of the particles are equal.
    b)  The velocities of the particles are equal.
    c)  The net force on the system is zero.
    d)  The particles are at rest.
5.  The total momentum of a system of particles is equal to:
    a)  The sum of the momenta of all the particles.
    b)  The total mass of the system times the velocity of the center of mass.
    c)  Both a and b are correct.
    d)  Neither a nor b is correct.

### Problem-Solving Questions

6.  A 2 kg mass is at position (3, 0) and a 3 kg mass is at position (0, 5). What is the x-coordinate of the center of mass?
    a)  1.2 m
    b)  1.5 m
    c)  2.0 m
    d)  3.0 m
7.  A 1 kg mass is moving with velocity (4, 0) m/s and a 3 kg mass is moving with velocity (0, -2) m/s. What is the velocity of the center of mass of the system?
    a)  (1, -1.5) m/s
    b)  (4, -6) m/s
    c)  (1, -2) m/s
    d)  (2, -3) m/s
8.  A 5 kg object is subject to a net external force of (10, -20) N. What is the acceleration of the center of mass?
    a)  (50, -100) m/s²
    b)  (2, -4) m/s²
    c)  (0.5, -0.25) m/s²
    d)  (10, -20) m/s²
9.  A 3 kg projectile is launched with an initial velocity of (10, 20) m/s. At the peak of its trajectory, it explodes into two fragments. One 1 kg fragment has a velocity of (5, 0) m/s immediately after the explosion. What is the velocity of the 2 kg fragment? (Neglect air resistance).
    a)  (12.5, 0) m/s
    b)  (5, 0) m/s
    c)  (15, 0) m/s
    d)  (25, 0) m/s
10. A uniform flat plate is in the shape of a right triangle with vertices at (0,0), (L,0), and (0,H). What is the x-coordinate of its center of mass?
    a)  L/2
    b)  L/3
    c)  2L/3
    d)  L/4

### Computational Questions

11. In the simulation, the center of mass is calculated using `R_cm = (f1.m*f1.pos + f2.m*f2.pos + f3.m*f3.pos) / projectile.m`. Why is it valid to use `projectile.m` (the original mass) as the denominator?
    a)  Because mass is conserved; the sum of the fragments' masses equals the original projectile's mass.
    b)  It is an approximation that simplifies the calculation.
    c)  The code should have summed the masses of the fragments individually.
    d)  Because the fragments all have the same mass.
12. The simulation updates the velocity of each fragment using `f.velocity = f.velocity + vector(0, -g, 0) * dt`. Why is there no term related to the explosion force in this line?
    a)  The explosion force is an internal force and does not affect the motion of the individual fragments after the explosion.
    b)  The explosion force acts only for an instant and its effect is already included in the initial velocities of the fragments right after the explosion.
    c)  The explosion force is negligible compared to gravity.
    d)  It is a simplification in the simulation.
13. If you wanted to add air resistance to the simulation (e.g., a force `F_drag = -b*v²`), where would you add this force in the code?
    a)  It would be added to the net external force used to calculate the acceleration of the center of mass.
    b)  It would be applied to each fragment individually inside the `for` loop, affecting each fragment's acceleration.
    c)  It would only affect the projectile before the explosion.
    d)  It cannot be modeled in this type of simulation.
14. What would you expect to see if the `cm_marker.pos` was set to the position of just one of the fragments (e.g., `cm_marker.pos = f1.pos`) instead of the calculated `R_cm`?
    a)  The marker would still follow the original parabolic path.
    b)  The marker would follow the path of that one fragment, which is a different parabola from the original path.
    c)  The marker would stop at the point of explosion.
    d)  The simulation would produce an error.
15. The simulation demonstrates that the center of mass continues on its original trajectory. This is a direct consequence of:
    a)  Conservation of energy.
    b)  `F_net_external = M_total * a_cm`.
    c)  Hooke's Law.
    d)  The Euler-Cromer method.
