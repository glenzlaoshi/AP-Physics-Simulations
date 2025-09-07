---
title: "4.1 - Charged Particle in a B-Field"
layout: default
---
# Information: Charged Particle in a Magnetic Field

## 1. Introduction to the Unit: Magnetism

This unit introduces **magnetism**, a fundamental force that is deeply connected to electricity. Magnetic fields (B-fields) are created by moving electric charges, such as the current flowing in a wire. 

This simulation focuses on the other side of this interaction: how an existing magnetic field exerts a force on an individual moving charge. This magnetic force, often called the **Lorentz Force**, has some very unique properties that distinguish it from the electric force or gravity.

## 2. Relevant Physics Concepts

### The Magnetic Force on a Moving Charge

The magnetic force has two very important and unusual characteristics:
1.  It acts on a charge `q` only if the charge is **moving** (with velocity `v`). A stationary charge feels no magnetic force.
2.  The direction of the magnetic force `Fm` is always **perpendicular** to both the velocity `v` of the particle and the magnetic field `B`.

### The Cross Product

Because the force is perpendicular to two other vectors, we use a special vector operation called the **cross product** to describe it.

`Fm = q * (v x B)`

-   The magnitude of the force is given by `Fm = |q|vBsin(θ)`, where `θ` is the angle between the velocity and the magnetic field.
-   The direction is found using the **Right-Hand Rule**.

### Magnetic Force and Circular Motion

Since the magnetic force is always perpendicular to the velocity, it can only change the particle's **direction**, never its speed. The magnetic force does **no work** on the particle, and its kinetic energy remains constant.

When a charged particle enters a uniform magnetic field with a velocity that is perpendicular to the field, the magnetic force provides a perfect, constant-magnitude, center-seeking force. This is the exact requirement for **uniform circular motion**. The magnetic force acts as the centripetal force.

By setting the centripetal force equal to the magnetic force, we can find the radius of the particle's circular path:

`Fc = Fm`

`m*v² / r = q*v*B`

Solving for `r` gives the radius of the circular path:

**`r = m*v / (q*B)`**

## 3. The Simulation: A Particle in a Field

### Outline of the Simulation

The `intermediate.py` file shows a charged particle (a proton) entering a region of uniform magnetic field that points out of the screen. Your goal is to calculate the magnetic force on the particle at each moment and use it to trace the particle's path. Because the direction of the force is always changing (as the direction of velocity changes), the force must be recalculated inside the animation loop.

### Completing the `intermediate.py` File

#### **Task 1: Calculate the Magnetic Force**

The core of the simulation is to correctly calculate the Lorentz Force vector, `F = q * (v x B)`.

- **Example (The Cross Product):** VPython has a built-in function, `cross(A, B)`, that calculates the cross product of two vectors `A` and `B`. The code to calculate the `v x B` part of the formula is given as an example:
  ```python
  v_cross_B = cross(particle.velocity, B_field_vec)
  ```

- **Your Task (The Force Vector):** Now, use the result of the cross product to find the final force vector. Write the line of code to calculate `F_mag` by multiplying the particle's charge, `particle.q`, with the `v_cross_B` vector you just learned about.

#### **Task 2: Update Motion**

Once you have the force vector for the current instant, the rest of the simulation uses standard dynamics.

- **Your Task:** Write the line of code to calculate the `particle.acceleration` from the force `F_mag` and the particle's mass `particle.m`.
- **Your Task:** Write the two familiar lines of code to update the `particle.velocity` and `particle.pos` using the numerical integration method.

#### **Task 3: Analysis**

- **Your Task:** The particle should travel in a circle. The theoretical radius of this circle is given by the formula `r = mv / qB`. Write a line of code after the loop to calculate this `r_theory`. Compare it to the radius you observe in your simulation. Do they match?

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/4.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/8b19e5abb96c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>