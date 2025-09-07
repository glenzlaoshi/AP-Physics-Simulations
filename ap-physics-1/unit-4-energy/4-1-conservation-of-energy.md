---
title: "4.1 - Conservation of Energy"
layout: default
---
# Information: Conservation of Energy

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