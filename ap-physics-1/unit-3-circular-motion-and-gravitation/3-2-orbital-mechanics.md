---
title: "3.2 - Orbital Mechanics"
layout: default
---
# Information: Orbital Mechanics

## 1. Introduction to the Unit: Gravitation

This topic is a perfect, real-world application of the principles of uniform circular motion. The force that keeps a satellite or a planet in its orbit is **gravity**. By understanding Newton's Law of Universal Gravitation, we can determine exactly how fast a satellite must travel to stay in a stable orbit.

In this unit, we see that the centripetal force (`Fc`) required to keep an object in a circular path is not a new force, but is in fact being **provided by** the gravitational force (`Fg`). By setting these two equal to each other, we can unlock the physics of orbital motion.

## 2. Relevant Physics Concepts

### Newton's Law of Universal Gravitation

Every object with mass in the universe attracts every other object with mass. The magnitude of this gravitational force is given by:

`Fg = G * (M * m) / r²`

-   `G` is the Universal Gravitational Constant (`6.67e-11 N·m²/kg²`).
-   `M` and `m` are the masses of the two objects.
-   `r` is the distance between the centers of the two objects.

The force is always attractive and acts along the line connecting the two objects.

### Orbital Speed for a Circular Orbit

For a satellite of mass `m` to have a stable circular orbit around a planet of mass `M`, the gravitational force must be providing the exact amount of centripetal force required.

-   Centripetal Force required: `Fc = m * v² / r`
-   Gravitational Force provided: `Fg = G * M * m / r²`

Setting them equal: `Fc = Fg`

`m * v² / r = G * M * m / r²`

Notice that the mass of the satellite (`m`) cancels from both sides! This means the required orbital speed does not depend on how heavy the satellite is. Solving for `v`, we get the speed required for a circular orbit:

**`v = sqrt(G * M / r)`**

### Types of Orbits

-   If a satellite's speed is exactly `v = sqrt(G*M/r)`, it will have a **perfectly circular orbit**.
-   If its speed is **less** than this value, gravity will be stronger than the required centripetal force, and the satellite will be pulled inwards in a decaying spiral.
-   If its speed is **greater** than this value, it will have enough energy to move further away from the planet, resulting in an **elliptical orbit**.

## 3. The Simulation: Satellite in Orbit

### Outline of the Simulation

The `skeleton.py` file shows a satellite in space near a larger planet. Your goal is to calculate the force of gravity acting on the satellite and use it to model the satellite's orbital path. Because the distance `r` and the direction of the force can change (especially in non-circular orbits), the force must be recalculated inside the animation loop.

### Completing the `skeleton.py` File

#### **Task 1: Set Initial Velocity**

To achieve a stable circular orbit, the satellite must start with a very specific tangential velocity. Your first task is to calculate this speed using the formula derived above.

- **Your Task:** Calculate the required speed, `v_circular`, using the formula `v = sqrt(G * M / r)`. The code provides all the necessary variables (`G`, `planet.m`, and `radius`).
- **Your Task:** Once you have the speed, you must create the initial velocity *vector*. The velocity must be tangential to the orbit. If the satellite starts on the positive x-axis, this tangential velocity will be in the positive y-direction. Write the line of code to set `satellite.velocity`.

#### **Task 2: Calculate Gravitational Force**

This must be done *inside* the `while` loop.

- **Example (The `r` vector):** The force calculation depends on the vector `r` that points from the object being pulled (the satellite) to the object doing the pulling (the planet). The code for this is given as an example:
  ```python
  r_vector = planet.pos - satellite.pos
  ```
- **Your Task (Magnitude and Direction):** From `r_vector`, you need two things: its magnitude (`r_mag`) and its direction (`r_hat`). Write the two lines of code to calculate these using the VPython functions `mag()` and `norm()`.
- **Your Task (Force Vector):** Now, calculate the magnitude of the gravitational force, `F_mag`, using Newton's Law of Gravitation. Then, combine the magnitude with the direction unit vector `r_hat` to get the final force vector, `F_gravity`.

#### **Task 3: Update Motion**

- **Your Task:** This part should be familiar. Once you have the net force (`F_gravity`), you must use it to find the satellite's acceleration (`a = F/m`). Remember to use the satellite's mass, `satellite.m`.
- **Your Task:** After finding the acceleration, write the two standard lines of code to update the `satellite.velocity` and `satellite.pos` over the time step `dt`.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/3.2-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/a508cfc93571" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>