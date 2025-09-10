---
title: "4.1 - Conservation of Energy"
layout: default
---


## 1. Introduction to the Unit: Energy

So far, we have analyzed motion using forces and kinematics (vectors). Energy provides a new, powerful, and often much simpler way to understand and solve problems in physics. The key difference is that energy is a **scalar** (a number without a direction), which makes the math easier.

The most important concept in this unit is the **Law of Conservation of Energy**: energy cannot be created or destroyed; it can only be transformed from one form to another. 

In this unit, we focus on **Mechanical Energy**, which is the sum of an object's energy of motion (Kinetic Energy) and its stored energy of position (Potential Energy). In a "closed system" where we can ignore forces like friction, the total mechanical energy remains constant.

## 2. Relevant Physics Concepts

### Kinetic Energy (`KE`)

This is the energy of motion. Any object with mass `m` moving with speed `v` has kinetic energy.

`KE = (1/2) * m * v²`

### Potential Energy (`PE`)

This is stored energy an object has because of its position or configuration.

-   **Gravitational Potential Energy (`PEg`):** Energy stored by lifting an object to a height `h` in a gravitational field. It represents the potential to do work if the object is released.
    `PEg = m * g * h`

-   **Elastic (Spring) Potential Energy (`PEs`):** Energy stored in a spring when it is compressed or stretched by a distance `x` from its equilibrium position.
    `PEs = (1/2) * k * x²` (where `k` is the spring constant)

### Conservation of Mechanical Energy

In any system where we can ignore non-conservative forces like friction and air drag, the total mechanical energy does not change. Energy simply transforms between kinetic and potential forms.

`E_total = KE + PE = constant`

This means the energy at the beginning of a process is equal to the energy at the end:

`KE_initial + PE_initial = KE_final + PE_final`

This is an extremely powerful tool. If we know a roller coaster's total energy at the top of a hill, we can instantly find its speed at the bottom by figuring out how much of its initial potential energy was converted into kinetic energy.

## 3. The Simulation: The Roller Coaster

### Outline of the Simulation

The `skeleton.py` file shows a roller coaster cart on a frictionless track. Instead of using forces (which would be very complicated on a curved track), we will use the principle of energy conservation to find the cart's speed at any point.

### Completing the `skeleton.py` File

#### **Task 1 & 2: Initial State and Total Energy**

The simulation begins with the cart at rest (`v=0`) at the top of the first hill. At this specific point, its kinetic energy is zero.

- **Your Task:** The cart's total mechanical energy is established at this moment. Since `KE=0`, the total energy is equal to the cart's initial gravitational potential energy. Write the line of code to calculate this initial `PE` (`m*g*h`) and set the variable `total_energy` equal to it. This `total_energy` value should remain constant for the entire simulation.

#### **Task 3: Applying Energy Conservation in the Loop**

Inside the animation loop, the cart is at a new position, and we need to find its speed. We will use the `total_energy` you calculated.

1.  **Calculate Current Potential Energy (Example):** At any point, the cart has a potential energy that depends on its current height (`cart.pos.y`). The code for this is given as an example:
    ```python
    current_PE = cart.m * g * cart.pos.y
    ```

2.  **Calculate Current Kinetic Energy (Your Task):** You know the `total_energy` (which is constant) and you just found the `current_PE`. Based on the conservation of energy equation (`total_energy = current_PE + current_KE`), write the line of code to calculate the `current_KE`.

3.  **Calculate Speed (Your Task):** The formula for kinetic energy is `KE = 0.5 * m * v²`. Now that you know the `current_KE`, you must rearrange this formula to solve for the speed `v`. Write the line of code to calculate the cart's `speed`.

#### **Updating the Cart's Position**

- **Your Task:** The simulation simplifies the cart's movement. Once you have the `speed`, you only need to update its x-position. The y-position is automatically set by the `track_path()` function. Write the line of code to update `cart.pos.x` using its `speed` and the time step `dt`.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/4.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/8f311f113c43" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  A roller coaster car is released from rest at the top of a hill. At which point in its journey (on a frictionless track) will its kinetic energy be at a maximum?
    a) At the top of the highest hill.
    b) At the top of any hill.
    c) At the lowest point of the track.
    d) Halfway down the first hill.

2.  Two objects, one with mass `m` and one with mass `2m`, are both dropped from the same height `h`. Ignoring air resistance, how do their speeds compare just before they hit the ground?
    a) The object with mass `2m` has a greater speed.
    b) The object with mass `m` has a greater speed.
    c) They have the same speed.
    d) The ratio of their speeds is 2:1.

3.  Which of the following is a "non-conservative" force that would cause the total mechanical energy of a system to decrease?
    a) Gravity.
    b) The normal force.
    c) Tension in a string.
    d) Friction.

4.  If the speed of an object is doubled, its kinetic energy is:
    a) Halved.
    b) Doubled.
    c) Quadrupled.
    d) Unchanged.

5.  A pendulum swings back and forth. At the very bottom of its swing, its energy is:
    a) Entirely potential.
    b) Entirely kinetic.
    c) Half potential, half kinetic.
    d) Zero.

### Problem-Solving Questions

1.  A 2 kg ball is at the top of a 10 m high hill, at rest. What is its total mechanical energy relative to the ground? (Use g = 9.8 m/s²)
    a) 20 J
    b) 98 J
    c) 196 J
    d) 0 J

2.  The same 2 kg ball from the previous question rolls down the frictionless hill. What is its speed at the bottom (h=0)?
    a) 9.9 m/s
    b) 14 m/s
    c) 19.8 m/s
    d) 196 m/s

3.  A 50 kg skateboarder is moving at 5 m/s at the bottom of a ramp. What is the maximum height `h` she can reach on the other side if she just lets herself roll without pushing? (Ignore friction.)
    a) 1.28 m
    b) 2.55 m
    c) 5.1 m
    d) 12.5 m

4.  A 0.5 kg block is dropped from a height of 20 m. What is its kinetic energy just before it hits the ground?
    a) 10 J
    b) 98 J
    c) 196 J
    d) 490 J

5.  A roller coaster car with a mass of 500 kg is at a point on the track 15 m above the ground and is traveling at 10 m/s. What is its total mechanical energy? (Use g = 9.8 m/s²)
    a) 25,000 J
    b) 73,500 J
    c) 98,500 J
    d) 122,500 J

### Computational Questions

1.  In the simulation, `total_energy` is calculated once at the beginning and never changed. This is a direct application of what principle?
    a) Newton's Second Law.
    b) The Law of Conservation of Momentum.
    c) The Law of Conservation of Energy.
    d) The definition of kinetic energy.

2.  The simulation calculates the cart's speed using `speed = sqrt(2 * current_KE / cart.m)`. This is a rearrangement of which formula?
    a) `PE = mgh`
    b) `KE = 0.5 * m * v²`
    c) `F = ma`
    d) `v = d/t`

3.  If you were to add friction to the simulation, how would the `total_energy` variable need to be handled?
    a) It would remain constant.
    b) It would need to be decreased inside the loop to account for energy lost to heat.
    c) It would need to be increased inside the loop.
    d) The concept of total energy would no longer apply.

4.  The simulation calculates `current_KE = total_energy - current_PE`. What would happen if the cart started with some initial velocity at the top of the hill?
    a) This calculation would still be correct.
    b) The `total_energy` would initially be zero.
    c) The initial `total_energy` would need to include both potential and kinetic energy.
    d) The simulation would crash.

5.  The simulation updates the cart's horizontal position with `cart.pos.x = cart.pos.x + speed * dt`. Why is this a simplification of real roller coaster motion?
    a) Because real roller coasters do not have speed.
    b) Because this assumes the velocity is purely horizontal, which is only true at the very bottom of a dip.
    c) Because `dt` should be `t`.
    d) Because real roller coasters do not conserve energy.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (d), 4. (c), 5. (b)
**Problem-Solving:** 1. (c), 2. (b), 3. (a), 4. (b), 5. (c)
**Computational:** 1. (c), 2. (b), 3. (b), 4. (c), 5. (b)
