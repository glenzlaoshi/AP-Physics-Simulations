---
title: "4.2 - Springs and Energy"
layout: default
---


## 1. Introduction to the Unit: Energy (continued)

This simulation continues our exploration of the Law of Conservation of Energy. In the previous simulation, we saw how energy transformed between Kinetic Energy (`KE`) and Gravitational Potential Energy (`PEg`).

Here, we focus on a different type of stored energy: **Elastic Potential Energy (`PEs`)**. This is the energy that is stored in a deformable object, like a spring, when it is stretched or compressed. The principles are the same: in a closed system, energy will transform between kinetic and elastic potential forms, but the total amount of mechanical energy will remain constant.

## 2. Relevant Physics Concepts

### Elastic Potential Energy (`PEs`)

When you do work to compress or stretch a spring, you are storing energy in it. This stored energy is called elastic potential energy. Its magnitude is given by:

`PEs = (1/2) * k * x²`

-   `k` is the **spring constant**, a measure of the spring's stiffness (in N/m).
-   `x` is the **displacement** (distance) the spring is stretched or compressed from its natural, equilibrium length.
-   Notice that the energy is proportional to `x²`. This means the energy is always positive, and it increases rapidly as you stretch or compress the spring further.

### Conservation of Energy in a Mass-Spring System

Consider a block of mass `m` attached to a spring on a frictionless, horizontal surface. The total mechanical energy of this system is:

`E_total = KE + PEs = (1/2)mv² + (1/2)kx²`

As the block oscillates back and forth, energy continuously transforms between these two forms:
-   At the **endpoints** of the motion (maximum stretch or compression), the block is momentarily at rest (`v=0`). Here, all the energy is potential: `E_total = (1/2)kx²`.
-   As the block moves towards the **equilibrium position** (`x=0`), the potential energy is converted to kinetic energy. 
-   At the **equilibrium position** (`x=0`), the potential energy is zero, and the kinetic energy is at its maximum. The block has its maximum speed here: `E_total = (1/2)mv_max²`.

Throughout this entire process, the value of `E_total` remains constant.

## 3. The Simulation: The Oscillating Block

### Outline of the Simulation

The `skeleton.py` file shows a block attached to a spring on a frictionless surface. In this simulation, we will take a slightly different approach. Instead of using energy to find the speed, we will use **forces** (from the previous unit) to model the motion. Then, we will calculate the KE and PE at each step to **verify** that energy is, in fact, conserved.

### Completing the `intermediate.py` File

#### **Task 1: Calculate the Spring Force**

The force a spring exerts is given by **Hooke's Law**: `F = -kx`. The negative sign shows that it is a "restoring force"—it always pulls or pushes the block back towards the equilibrium position.

- **Your Task:** First, you must calculate the displacement vector, `x_vector`, which is the difference between the block's current position and its equilibrium position. 
- **Your Task:** Next, use `x_vector` and the spring constant `spring.k` to calculate the force vector, `F_spring`.

#### **Task 2: Update the Motion**

This part uses the same dynamics and kinematics from previous units.

- **Your Task:** Use the `F_spring` you just calculated to find the `block.acceleration` using Newton's Second Law (`a = F/m`).
- **Your Task:** Once you have the acceleration, write the two familiar lines of code to update the `block.velocity` and `block.pos` inside the animation loop.

#### **Task 3: Verify Energy Conservation**

This is the key analysis step. Now that the block is moving, we want to check if our simulation is conserving energy.

- **Example (Potential Energy):** The code to calculate the spring's current potential energy is given as an example:
  ```python
  current_PE = 0.5 * spring.k * mag(block.pos - spring.equilibrium_pos)**2
  ```
- **Your Task (Kinetic Energy):** Write the line of code to calculate the `current_KE` of the block using its mass (`block.m`) and its current velocity (`block.velocity`). Remember that `KE = (1/2)mv²` and the square of a vector's magnitude in VPython is `mag2(v)`.

When you run the code, the program will print the PE, KE, and their sum. If your physics implementation is correct, you should see the individual PE and KE values change dramatically, but their sum should remain constant!

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/4.2-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/f7b66e77f9bf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  A block is oscillating on a frictionless surface attached to a spring. At which point is the system's potential energy at a maximum?
    a) At the equilibrium position (`x=0`).
    b) At the points of maximum compression and maximum stretch.
    c) When the kinetic energy is also at a maximum.
    d) The potential energy is constant.

2.  For the same oscillating block, at which point is its speed at a maximum?
    a) At the equilibrium position (`x=0`).
    b) At the points of maximum compression and maximum stretch.
    c) When the potential energy is also at a maximum.
    d) The speed is constant.

3.  Spring A is stiffer than Spring B (`kA > kB`). If both springs are stretched by the same distance, which spring stores more potential energy?
    a) Spring A.
    b) Spring B.
    c) They store the same amount of energy.
    d) It depends on the mass attached to the spring.

4.  According to Hooke's Law (`F = -kx`), the force exerted by a spring is a "restoring force." This means it is always directed:
    a) In the same direction as the displacement.
    b) Perpendicular to the displacement.
    c) Towards the equilibrium position.
    d) Away from the equilibrium position.

5.  A mass is hung vertically from a spring, stretching it by a distance `d`. If the mass is then pulled down an additional distance `x` and released, the total mechanical energy of the system (relative to the lowest point) will be conserved if we ignore air resistance. What forms of energy are transforming during its oscillation?
    a) Kinetic and Elastic Potential Energy only.
    b) Kinetic and Gravitational Potential Energy only.
    c) Elastic and Gravitational Potential Energy only.
    d) Kinetic, Elastic Potential, and Gravitational Potential Energy.

### Problem-Solving Questions

1.  A spring with a spring constant `k = 200 N/m` is compressed by 0.1 m. How much potential energy is stored in the spring?
    a) 1 J
    b) 2 J
    c) 10 J
    d) 20 J

2.  A 2 kg block is attached to a spring (`k = 50 N/m`). The spring is stretched by 0.4 m from equilibrium and the block is released from rest. What is the total mechanical energy of the system?
    a) 4 J
    b) 8 J
    c) 10 J
    d) 20 J

3.  Using the information from the previous question (2 kg block, k=50 N/m, stretched 0.4 m), what is the maximum speed of the block as it passes through the equilibrium position?
    a) 2.0 m/s
    b) 2.8 m/s
    c) 4.0 m/s
    d) 10.0 m/s

4.  A 1 kg block sliding on a frictionless surface with a speed of 4 m/s hits a spring and compresses it. If the spring constant is `k = 100 N/m`, what is the maximum compression of the spring?
    a) 0.16 m
    b) 0.4 m
    c) 0.8 m
    d) 1.6 m

5.  A spring stores 25 J of potential energy when it is stretched by 0.2 m. What is the spring constant `k`?
    a) 625 N/m
    b) 1250 N/m
    c) 2500 N/m
    d) 5000 N/m

### Computational Questions

1.  The simulation calculates the spring force using `F_spring = -spring.k * x_vector`. Why is the negative sign crucial for creating an oscillation?
    a) It makes the force attractive, pulling the block towards the spring.
    b) It ensures the force always opposes the displacement, pulling the block back towards equilibrium.
    c) It is required to conserve energy.
    d) It makes the block slow down over time.

2.  The simulation verifies energy conservation by calculating `current_PE + current_KE` in every frame. If the simulation were perfectly accurate, this sum should:
    a) Increase over time.
    b) Decrease over time.
    c) Remain constant.
    d) Oscillate like the position.

3.  The potential energy is calculated using `mag(block.pos - spring.equilibrium_pos)**2`. Why is the `mag()` function used here?
    a) Because potential energy is a vector.
    b) To get the scalar distance `x` from the vector displacement.
    c) To ensure the result is negative.
    d) To get the direction of the energy.

4.  If you double the spring constant `spring.k` in the simulation but start the block from the same initial position, what would happen to the frequency of oscillation?
    a) It would decrease.
    b) It would remain the same.
    c) It would increase.
    d) It would become zero.

5.  The simulation uses `a = F/m` and then updates velocity and position. If you were to instead use an energy-based approach to find the speed at each step (like in the roller coaster simulation), which piece of information would you NOT need to calculate inside the loop?
    a) The block's potential energy.
    b) The block's kinetic energy.
    c) The force on the block.
    d) The block's position.

---
### Answer Key
**Conceptual:** 1. (b), 2. (a), 3. (a), 4. (c), 5. (d)
**Problem-Solving:** 1. (a), 2. (a), 3. (a), 4. (b), 5. (b)
**Computational:** 1. (b), 2. (c), 3. (b), 4. (c), 5. (c)
