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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  An object will float in a fluid if:
    a) The object's density is greater than the fluid's density.
    b) The object's density is less than the fluid's density.
    c) The object's mass is greater than the fluid's mass.
    d) The object's volume is less than the fluid's volume.

2.  A large steel ship floats on water. This is possible because:
    a) Steel is less dense than water.
    b) The buoyant force depends on the weight of the ship, not its density.
    c) The ship's shape displaces a large volume of water, making its *average* density less than water.
    d) The buoyant force is equal to the weight of the ship itself.

3.  According to Archimedes' Principle, the buoyant force on a submerged object is equal to the:
    a) Weight of the object.
    b) Volume of the object.
    c) Weight of the fluid displaced by the object.
    d) Volume of the fluid displaced by the object.

4.  A block of wood is floating in a bucket of water. If you take this setup to the Moon, where gravity is weaker, what will happen to the block?
    a) It will float higher (less of it will be submerged).
    b) It will float lower (more of it will be submerged).
    c) It will float at the same level.
    d) It will sink.

5.  Two objects of the exact same size and shape but different masses are submerged in a fluid. How do the buoyant forces on them compare?
    a) The heavier object experiences a greater buoyant force.
    b) The lighter object experiences a greater buoyant force.
    c) They experience the same buoyant force.
    d) It depends on the depth.

### Problem-Solving Questions

(Use density of water = 1000 kg/m³ and g = 9.8 m/s²)

1.  A block of wood has a volume of 0.5 m³ and a density of 600 kg/m³. What is the mass of the block?
    a) 300 kg
    b) 500 kg
    c) 600 kg
    d) 1200 kg

2.  A 0.2 m³ object is fully submerged in water. What is the magnitude of the buoyant force acting on it?
    a) 196 N
    b) 980 N
    c) 1960 N
    d) 2000 N

3.  A 10 kg block of aluminum (density = 2700 kg/m³) is fully submerged in water. What is the buoyant force on the block?
    a) 36.3 N
    b) 98 N
    c) 270 N
    d) 26460 N

4.  A block of material has a weight of 50 N. When fully submerged in water, its apparent weight is 30 N. What is the buoyant force on the block?
    a) 20 N
    b) 30 N
    c) 50 N
    d) 80 N

5.  An object with a volume of 0.04 m³ floats in water with 75% of its volume submerged. What is the mass of the object?
    a) 3 kg
    b) 4 kg
    c) 30 kg
    d) 40 kg

### Computational Questions

1.  The simulation calculates the buoyant force using `Fb_mag = rho_fluid * V_submerged * g`. This is a direct implementation of:
    a) Newton's Second Law.
    b) The definition of density.
    c) Archimedes' Principle.
    d) Hooke's Law.

2.  In the simulation, why is it necessary to calculate `V_submerged` inside the loop?
    a) Because the total volume of the block is changing.
    b) Because the density of the fluid is changing.
    c) Because the amount of the block that is underwater changes as it moves.
    d) It is not necessary; it could be calculated once at the beginning.

3.  The buoyant force vector is created as `Fb = vector(0, Fb_mag, 0)`. The direction `vector(0, 1, 0)` signifies that the buoyant force always acts:
    a) Downwards.
    b) Upwards.
    c) In the direction of motion.
    d) Perpendicular to the motion.

4.  If you set the object's density (`rho_object`) to be greater than the fluid's density (`rho_fluid`) in the simulation, what do you expect to happen?
    a) The object will float.
    b) The object will remain suspended wherever it is placed.
    c) The object will sink.
    d) The simulation will crash.

5.  The net force is calculated as `F_net = Fg + Fb`. Given that `Fg` is a downward vector and `Fb` is an upward vector, this is a vector addition that finds:
    a) The sum of the magnitudes of the two forces.
    b) The difference between the magnitudes of the two forces.
    c) The product of the two forces.
    d) The ratio of the two forces.

---
### Answer Key
**Conceptual:** 1. (b), 2. (c), 3. (c), 4. (c), 5. (c)
**Problem-Solving:** 1. (a), 2. (c), 3. (a), 4. (a), 5. (c)
**Computational:** 1. (c), 2. (c), 3. (b), 4. (c), 5. (b)
