---
title: "4.1 - Charged Particle in a B-Field"
layout: default
---


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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  A stationary proton is in a strong, uniform magnetic field. What is the force on the proton?
    a) It is directed along the magnetic field lines.
    b) It is directed perpendicular to the magnetic field lines.
    c) It is zero.
    d) It depends on the strength of the field.

2.  The magnetic force on a moving charged particle is always directed:
    a) In the same direction as the particle's velocity.
    b) In the same direction as the magnetic field.
    c) Perpendicular to both the velocity and the magnetic field.
    d) Opposite to the direction of the particle's velocity.

3.  A charged particle moves through a uniform magnetic field. The effect of the magnetic force is to change the particle's:
    a) Speed only.
    b) Direction of motion only.
    c) Both speed and direction of motion.
    d) Kinetic energy.

4.  A proton enters a uniform magnetic field that is directed into the page. The proton is moving from left to right. The initial direction of the magnetic force on the proton is:
    a) Upwards (towards the top of the page).
    b) Downwards (towards the bottom of the page).
    c) Into the page.
    d) Out of the page.

5.  Two particles with the same mass and charge enter a uniform magnetic field with the same velocity. Particle A has charge `+q` and Particle B has charge `-q`. How will their paths differ?
    a) They will not differ.
    b) They will curve in opposite directions.
    c) Particle A will travel in a larger circle.
    d) Particle B will travel in a larger circle.

### Problem-Solving Questions

1.  A proton (charge `q = 1.6e-19 C`) moves at `2.0e5 m/s` perpendicularly through a magnetic field of `0.5 T`. What is the magnitude of the magnetic force on it?
    a) 8.0e-15 N
    b) 1.6e-14 N
    c) 3.2e-14 N
    d) 6.4e-14 N

2.  An electron (`m = 9.11e-31 kg`, `q = -1.6e-19 C`) moves at `3.0e6 m/s` in a circular path in a uniform magnetic field of `0.01 T`. What is the radius of its path?
    a) 0.0017 m
    b) 0.0034 m
    c) 0.017 m
    d) 0.034 m

3.  A charged particle is moving in a circle of radius 2.0 m in a 0.25 T magnetic field. If its momentum (`p = mv`) is `8.0e-20 kg·m/s`, what is the magnitude of its charge?
    a) 1.6e-19 C
    b) 3.2e-19 C
    c) 4.0e-19 C
    d) 8.0e-19 C

4.  A particle with charge `+q` and mass `m` moves in a circle of radius `R` in a magnetic field `B`. A second particle with charge `+2q` and mass `m` moves at the same speed `v`. What is the radius of the second particle's path?
    a) R/2
    b) R
    c) 2R
    d) 4R

5.  An alpha particle (charge `+2e`, mass `4u`) and a proton (charge `+e`, mass `1u`) enter a magnetic field with the same velocity. What is the ratio of the radius of the alpha particle's path to the proton's path (`R_alpha / R_proton`)?
    a) 1/2
    b) 1
    c) 2
    d) 4

### Computational Questions

1.  The simulation calculates the magnetic force using `F_mag = particle.q * cross(particle.velocity, B_field_vec)`. The `cross()` function is necessary because:
    a) The force is a scalar.
    b) The force is always parallel to the velocity.
    c) The force's direction depends on the perpendicular relationship between velocity and B-field.
    d) The force is only present for positive charges.

2.  The simulation must recalculate the force inside the animation loop because:
    a) The magnetic field is changing.
    b) The particle's charge is changing.
    c) The particle's velocity vector is constantly changing direction.
    d) The particle's mass is changing.

3.  If you were to set the initial velocity of the particle to be parallel to the magnetic field vector, what would the `cross()` function return, and what would be the resulting force?
    a) A large vector, resulting in a large force.
    b) A vector perpendicular to the B-field, resulting in circular motion.
    c) A zero vector, resulting in zero force.
    d) The simulation would crash.

4.  The theoretical radius is calculated using `r_theory = (particle.m * v) / (particle.q * B)`. If you double the strength of the magnetic field `B` in the simulation, what would you expect to happen to the radius of the particle's path?
    a) It would be halved.
    b) It would remain the same.
    c) It would be doubled.
    d) It would be quadrupled.

5.  The simulation updates velocity using `particle.velocity = particle.velocity + particle.acceleration * dt`. Even though the force is always acting, the magnitude of `particle.velocity` (its speed) should remain constant. Why?
    a) Because the acceleration is always zero.
    b) Because the magnetic force is always perpendicular to the velocity, it does no work and cannot change the kinetic energy.
    c) This is a flaw in the simulation; the speed should increase.
    d) Because the particle is in a vacuum.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (b), 4. (a), 5. (b)
**Problem-Solving:** 1. (b), 2. (a), 3. (a), 4. (a), 5. (c)
**Computational:** 1. (c), 2. (c), 3. (c), 4. (a), 5. (b)
