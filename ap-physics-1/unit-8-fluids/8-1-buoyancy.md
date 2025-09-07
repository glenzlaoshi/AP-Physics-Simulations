---
title: "8.1 - Buoyancy"
layout: default
---


## 1. Introduction to the Unit: Fluids

This unit introduces the study of **fluids**, which are substances that can flow—typically liquids and gases. We will explore the properties of fluids, such as density and pressure, and the forces they exert.

The central topic of this first simulation is **buoyancy**, which is the upward force a fluid exerts on any object submerged in it. This is the principle that explains why massive steel ships can float and why a balloon filled with helium rises. The key to understanding buoyancy is **Archimedes' Principle**.

## 2. Relevant Physics Concepts

### Density (`ρ`)

Density is a fundamental property of a substance, defined as its mass per unit volume: `ρ = m / V`. The density of an object compared to the density of the fluid it is in determines whether it will sink or float.

### Archimedes' Principle

This is the most important concept for this simulation. Archimedes' Principle states:

**The magnitude of the buoyant force on a submerged object is equal to the weight of the fluid that is displaced by the object.**

We can write this as an equation. The weight of the displaced fluid is its mass (`m_fluid`) times `g`. The mass of the displaced fluid is its density (`ρ_fluid`) times its volume (`V_displaced`). This gives the formula for the buoyant force, `Fb`:

`Fb = m_fluid * g = ρ_fluid * V_displaced * g`

-   `ρ_fluid` is the density of the fluid.
-   `V_displaced` is the volume of the part of the object that is *underwater*.

### Sinking and Floating

Any object in a fluid is subject to two main vertical forces:
1.  Its own weight (gravity), `Fg`, pulling it down.
2.  The buoyant force, `Fb`, pushing it up.

The net force (`F_net = Fb - Fg`) determines the object's motion.
-   If the object's weight is greater than the buoyant force (`Fg > Fb`), it will sink. This happens when the object's average density is greater than the fluid's density (`ρ_object > ρ_fluid`).
-   If the object's weight is less than the maximum buoyant force (`Fg < Fb`), it will float. It will rise until it displaces just enough fluid so that the buoyant force exactly balances its weight (`Fb = Fg`), at which point it will be in equilibrium.

## 3. The Simulation: To Sink or to Float?

### Outline of the Simulation

The `intermediate.py` file shows a block being dropped into a tank of fluid. The downward force of gravity on the block is constant. Your main task is to correctly calculate the upward buoyant force, which depends on how much of the block is submerged. The net force will then determine the block's acceleration.

### Completing the `intermediate.py` File

#### **Calculating the Buoyant Force**

The code to calculate the net force and update the motion is already written. Your entire task is to correctly calculate the buoyant force vector, `Fb`.

- **Example (Calculating Submerged Volume):** The most difficult part of the buoyant force calculation is finding the volume of the object that is currently underwater (`V_submerged`). The logic for this is provided in the code as an example. It checks if the object is fully submerged, partially submerged, or not submerged at all and calculates the correct volume.
  ```python
  y_top = obj.pos.y + obj.size.y / 2
  y_bot = obj.pos.y - obj.size.y / 2
  # ... (logic to find V_submerged) ...
  ```

- **Your Task (Buoyant Force Magnitude):** Now that you have the `V_submerged`, you can use Archimedes' Principle to find the magnitude of the buoyant force. Write the line of code to calculate `Fb_mag` using the formula `Fb = ρ_fluid * V_submerged * g`.

- **Your Task (Buoyant Force Vector):** The buoyant force always pushes straight up. Use the `Fb_mag` you just calculated to create the final buoyant force *vector*, `Fb`. The vector should have a positive y-component and zero x and z components.

Once you have correctly calculated `Fb`, the rest of the simulation code will use it to create the correct motion. Try changing the `rho_object` variable at the top of the code to see if you can predict whether the object will sink or float.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/8.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/e229822be3e4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>