---
title: "5.1 - 1D Collisions"
layout: default
---


## 1. Introduction to the Unit: Momentum

This unit introduces a new and powerful concept for analyzing the interactions between objects: **momentum**. Momentum can be thought of as "mass in motion." It is a vector quantity, defined as the product of an object's mass and its velocity.

`p = m * v`

The most important principle in this unit is the **Law of Conservation of Momentum**. This fundamental law states that for any system with no external net forces acting on it, the total momentum of the system remains constant. This is especially useful for analyzing collisions, where the forces involved are internal to the system of colliding objects.

For any collision between two objects, the total momentum *before* the collision is equal to the total momentum *after* the collision.

## 2. Relevant Physics Concepts

### Conservation of Momentum

For a collision between two objects, `m1` and `m2`, the conservation of momentum is written as:

`p_initial = p_final`

`m1*v1_initial + m2*v2_initial = m1*v1_final + m2*v2_final`

This vector equation holds true for all types of collisions.

### Types of Collisions

We categorize collisions based on whether or not kinetic energy (`KE`) is also conserved.

1.  **Elastic Collision:** A collision where kinetic energy is conserved (`KE_initial = KE_final`). Think of the ideal collision between two billiard balls. Momentum is also conserved.
2.  **Inelastic Collision:** A collision where kinetic energy is **not** conserved (`KE_initial > KE_initial`). Some energy is converted into other forms, like heat, sound, or the deformation of the objects. Momentum is still conserved.
3.  **Perfectly Inelastic Collision:** This is the most extreme inelastic collision, where the objects **stick together** after they collide. They then move as a single object with a single, common final velocity. This is the type of collision you will model first.

### Solving for a Perfectly Inelastic Collision

Since the two objects stick together, they have a combined mass of `(m1 + m2)` and a single final velocity, `v_final`. The conservation of momentum equation simplifies to:

`m1*v1_initial + m2*v2_initial = (m1 + m2) * v_final`

We can easily rearrange this to solve for the final velocity:

**`v_final = (m1*v1_initial + m2*v2_initial) / (m1 + m2)`**

Notice that the final velocity is the total initial momentum of the system divided by the total mass of the system.

## 3. The Simulation: The Collision

### Outline of the Simulation

The `intermediate.py` file shows two carts on a frictionless track moving towards each other. The code can already detect when they collide. Your task is to implement the physics for a **perfectly inelastic collision** by applying the Law of Conservation of Momentum to calculate the single velocity the carts have after they stick together.

### Completing the `intermediate.py` File

The code that needs to be written is inside the `if mag(cart1.pos - cart2.pos) < 1:` block, which runs only at the moment of collision.

#### **Implementing the Inelastic Collision**

- **Example (The Numerator):** The numerator in the formula for `v_final` is the total initial momentum of the system. The code calculates this for you before the loop begins and stores it in the variable `total_p_initial`.
  ```python
  total_p_initial = cart1.m * cart1.velocity + cart2.m * cart2.velocity
  ```

- **Your Task (The Denominator):** The denominator in the formula is the total mass of the system. This is simply `cart1.m + cart2.m`.

- **Your Task (Calculate Final Velocity):** Write the line of code to calculate the final velocity vector, `v_final`. You will need to divide the `total_p_initial` vector by the total mass of the two carts.

- **Your Task (Update Velocities):** After the collision, both carts move together with this new final velocity. Write the two lines of code that set the `.velocity` property of *both* `cart1` and `cart2` equal to the `v_final` vector you just calculated.

When you run the code, you should see the carts collide, stick together, and move off with a new velocity. The program will print the momentum before and after the collision to verify that it was conserved.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/5.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/1dbff434d2e3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>