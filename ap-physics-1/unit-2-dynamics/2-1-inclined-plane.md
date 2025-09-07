---
title: "2.1 - Forces on an Inclined Plane"
layout: default
---

## 1. Introduction to the Unit: Dynamics

In the previous unit, Kinematics, we learned how to describe motion (position, velocity, acceleration). Now, in Dynamics, we explore *why* things move the way they do. The cause of any change in motion is a **force**—a push or a pull.

This unit is built upon **Newton's Three Laws of Motion**, which are the foundation of classical mechanics:
1.  **First Law (Inertia):** An object in motion stays in motion, and an object at rest stays at rest, unless acted upon by a net external force.
2.  **Second Law (F=ma):** The net force acting on an object is equal to the object's mass times its acceleration (`F_net = m*a`). This is the central equation of dynamics.
3.  **Third Law (Action-Reaction):** For every action, there is an equal and opposite reaction.

By identifying all the forces acting on an object and using `F_net = m*a`, we can predict its resulting motion.

## 2. Relevant Physics Concepts

### Common Forces
- **Gravity (`Fg` or `W`):** The force of the Earth pulling on an object. Its magnitude is `mg`, and it **always points straight down**.
- **Normal Force (`Fn`):** A contact force from a surface that prevents an object from passing through it. The normal force is always directed **perpendicular** (or "normal") to the surface.
- **Friction (`Ff`):** A contact force that opposes motion or attempted motion between surfaces. The force of kinetic (sliding) friction is calculated as `Fk = μk * Fn`, where `μk` is the coefficient of kinetic friction.

### The Inclined Plane Problem

Analyzing forces on an inclined plane is a classic physics problem. The key trick is to **tilt your coordinate system**. Instead of the usual horizontal and vertical axes, we set our axes so that:
- The **x-axis** is parallel to the surface of the incline.
- The **y-axis** is perpendicular to the surface of the incline.

### Resolving the Force of Gravity

Because we've tilted our coordinate system, the force of gravity (which still points straight down) is now at an angle to our new axes. We must break it down into its x and y components in this new system.

If the incline has an angle `theta`:
- The component of gravity **perpendicular** to the plane is `Fg_perp = mg * cos(theta)`.
- The component of gravity **parallel** to the plane is `Fg_parallel = mg * sin(theta)`.

This is the most important step. The `Fg_parallel` component is what tries to pull the block down the ramp, while the `Fg_perp` component is what the Normal Force has to push against.

## 3. The Simulation: The Sliding Block

### Outline of the Simulation

The `skeleton.py` file shows a block resting on a tilted surface. Your goal is to correctly calculate all the forces acting on the block in a tilted coordinate system. The vector sum of these forces (`F_net`) will determine the block's acceleration down the ramp.

### Completing the `skeleton.py` File

#### **Force Calculation**

1.  **Gravitational Force (`Fg`):** This is the easiest force, but also the one that causes the most confusion! In the simulation's *un-tilted* world coordinates, it always points straight down. The skeleton file provides this for you: `Fg = vector(0, -block.m * g, 0)`.

2.  **Normal Force (`Fn`):** The normal force must perfectly balance the perpendicular component of gravity. Its magnitude is `Fn_mag = mg * cos(angle)`. The skeleton file provides a direction vector for you called `normal_direction`. Your task is to combine the magnitude and direction to create the final normal force vector, `Fn`.

3.  **Frictional Force (`Fk`):** The magnitude of kinetic friction is `Fk_mag = μk * Fn_mag`. Since the block will slide *down* the ramp, the friction force must oppose this motion and point *up* the ramp. The skeleton provides a `friction_direction` vector. Your task is to calculate the magnitude and combine it with the direction to create the friction force vector, `Fk`.

4.  **Net Force (`F_net`):** The net force is the vector sum of all the forces you just defined. Write the line of code to add the three force vectors (`Fg`, `Fn`, and `Fk`) together.

#### **Applying Newton's Second Law**

- **Acceleration (Example):** Once you have the net force, you can find the acceleration using Newton's Second Law. The code for this is:
  ```python
  block.acceleration = F_net / block.m
  ```
- **Updating Motion (Your Task):** Now that you have the block's (constant) acceleration, you must add the two familiar lines of code for numerical integration inside the `while` loop to update the block's `velocity` and `pos` over each time step `dt`.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/2.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/802926b2c58c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
