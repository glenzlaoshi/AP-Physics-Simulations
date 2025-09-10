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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  In any collision between two objects in an isolated system, which of the following is always conserved?
    a) Kinetic energy.
    b) Velocity.
    c) Momentum.
    d) Both momentum and kinetic energy.

2.  A "perfectly inelastic" collision is one in which:
    a) The objects bounce off each other perfectly.
    b) Momentum is lost, but kinetic energy is conserved.
    c) Kinetic energy is lost, but momentum is conserved.
    d) The objects pass through each other.

3.  Two objects of equal mass are moving towards each other with equal speeds. They undergo a perfectly inelastic collision. What is the velocity of the combined mass after the collision?
    a) Zero.
    b) The same as the initial speed of one of the masses.
    c) Double the initial speed.
    d) It cannot be determined.

4.  A small car and a large truck have a head-on collision. Which of the following statements is true about the forces they experience during the collision?
    a) The truck experiences a greater force.
    b) The car experiences a greater force.
    c) They experience the same magnitude of force.
    d) The force depends on their final velocities.

5.  In an elastic collision, which of the following is true?
    a) Only momentum is conserved.
    b) Only kinetic energy is conserved.
    c) Both momentum and kinetic energy are conserved.
    d) Neither momentum nor kinetic energy is conserved.

### Problem-Solving Questions

1.  A 2 kg cart moving at 3 m/s collides with a 1 kg cart that is at rest. They stick together. What is their final velocity?
    a) 1 m/s
    b) 2 m/s
    c) 3 m/s
    d) 6 m/s

2.  A 4 kg ball moving at 5 m/s to the right collides with a 6 kg ball moving at 2 m/s to the left. They stick together. What is their final velocity?
    a) 0.8 m/s to the right.
    b) 0.8 m/s to the left.
    c) 3.2 m/s to the right.
    d) 3.2 m/s to the left.

3.  A 1000 kg car traveling at 20 m/s rear-ends a 1500 kg car that is at rest. They lock bumpers. What is the final speed of the two cars?
    a) 4 m/s
    b) 8 m/s
    c) 10 m/s
    d) 20 m/s

4.  A 0.5 kg piece of clay moving at 10 m/s is thrown at a 2.0 kg block of wood at rest. The clay sticks to the wood. What is the final speed of the clay-wood combination?
    a) 2.0 m/s
    b) 2.5 m/s
    c) 5.0 m/s
    d) 10.0 m/s

5.  A 3 kg object moving at 4 m/s has a perfectly inelastic collision with a stationary object. After the collision, the combined mass moves at 1 m/s. What is the mass of the stationary object?
    a) 3 kg
    b) 6 kg
    c) 9 kg
    d) 12 kg

### Computational Questions

1.  The simulation calculates the final velocity as `v_final = total_p_initial / (cart1.m + cart2.m)`. This equation is a direct application of:
    a) Conservation of Energy.
    b) Conservation of Momentum for a perfectly inelastic collision.
    c) Hooke's Law.
    d) Newton's Law of Universal Gravitation.

2.  The collision logic is placed inside an `if` statement that checks if the distance between the carts is less than a certain value. Why is this approach used?
    a) To make the simulation run faster.
    b) To detect when the carts are touching so the collision physics can be applied.
    c) To calculate the kinetic energy of the system.
    d) To ensure the carts do not move.

3.  After calculating `v_final`, the code sets `cart1.velocity = v_final` and `cart2.velocity = v_final`. What does this represent physically?
    a) That the carts have bounced off each other.
    b) That the carts have stuck together and now move as a single object.
    c) That energy was conserved in the collision.
    d) That the carts have stopped moving.

4.  If you were to modify the simulation to model an *elastic* collision instead of a perfectly inelastic one, what would be the most significant change in the outcome?
    a) The total momentum after the collision would be greater.
    b) The carts would bounce off each other instead of sticking together.
    c) The total kinetic energy after the collision would be less.
    d) The final velocities would always be zero.

5.  The simulation calculates `total_p_initial` before the main loop starts. Why does this work for this specific simulation?
    a) Because momentum is not conserved.
    b) Because the velocities of the carts do not change before the collision (no friction or other forces).
    c) Because the masses of the carts are changing.
    d) It does not work; it should be calculated inside the loop.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (a), 4. (c), 5. (c)
**Problem-Solving:** 1. (b), 2. (a), 3. (b), 4. (a), 5. (c)
**Computational:** 1. (b), 2. (b), 3. (b), 4. (b), 5. (b)
