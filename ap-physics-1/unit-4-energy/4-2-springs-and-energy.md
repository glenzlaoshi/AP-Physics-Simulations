---
title: "4.2 - Springs and Energy"
layout: default
---
# Information: Springs and Energy

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