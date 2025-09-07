---
title: "2.2 - Atwood Machine"
layout: default
---
# Information: Atwood Machine

## 1. Introduction to the Unit: Dynamics of Systems

This simulation builds on the core concepts of Dynamics (`F_net = m*a`). So far, we have analyzed single objects. However, many real-world scenarios involve multiple objects whose motions are connected or constrained. We call these **systems**.

An Atwood machine is a classic, simple system consisting of two masses connected by a string that passes over a pulley. Because they are connected, the motion of one mass directly affects the motion of the other. To solve for the motion of the system, we must analyze the forces on *each* mass individually and then combine their equations based on the constraint that links them.

## 2. Relevant Physics Concepts

### Tension (`T`)

Tension is the pulling force exerted by a string or rope. For the purposes of this problem, we make a few key assumptions about the string and pulley:
- The string is **massless** and does not stretch.
- The pulley is **massless** and **frictionless**.
- Under these assumptions, the tension force `T` is the **same** at all points along the string.

### Analyzing the Forces on Each Mass

Let's assume `m2` is heavier than `m1`.

- **Free-Body Diagram for `m1`:** There are two forces: `T` pulling up, and `m1*g` pulling down. The net force is `F_net1 = T - m1*g`.
- **Free-Body Diagram for `m2`:** There are two forces: `T` pulling up, and `m2*g` pulling down. The net force is `F_net2 = T - m2*g`.

### The Constraint

The string connects the two masses. This imposes a critical **constraint** on their motion: their accelerations must be equal in magnitude and opposite in direction. If `m1` accelerates upwards with `+a`, then `m2` must accelerate downwards with `-a`.

### Solving for the System's Acceleration

We can now use `F_net = m*a` for each block:
1.  `T - m1*g = m1*a`
2.  `T - m2*g = m2*(-a)`  which can be rewritten as `m2*g - T = m2*a`

This gives us two equations and two unknowns (`T` and `a`). By adding the two equations together, we can eliminate `T` and solve for `a`:

`(m2*g - T) + (T - m1*g) = m2*a + m1*a`
`g * (m2 - m1) = a * (m1 + m2)`

This gives the key result for the acceleration of the system:
**`a = g * (m2 - m1) / (m1 + m2)`**

## 3. The Simulation: Modeling the Motion

### Outline of the Simulation

The `skeleton.py` file shows two blocks (`mass1` and `mass2`) connected by strings over a pulley. Your goal is to use the formula for the system's acceleration to predict and model the motion of the blocks.

### Completing the `skeleton.py` File

#### **Task 3: Calculate Acceleration**

- **Example (Magnitude):** The main physics task is to calculate the magnitude of the system's acceleration. The formula we derived above is the key. The code to do this is:
  ```python
  a_mag = g * (mass2.m - mass1.m) / (mass1.m + mass2.m)
  ```
- **Your Task (Vectors):** The variable `a_mag` is just a number (a scalar). You need to create the full acceleration *vectors* for each block. Remember that `mass1` (the lighter one) accelerates up, while `mass2` (the heavier one) accelerates down. Write the two lines of code that set the `mass1.acceleration` and `mass2.acceleration` vector properties.

#### **Task 4: Update Motion**

Once you have the correct, constant acceleration vectors for each block, the rest of the simulation is a standard kinematics update. Inside the `while` loop, you need to update the motion for **both** blocks.

- **Your Task:** For `mass1`, write the two lines of code to update its `velocity` and `pos` properties using the standard numerical integration technique.
- **Your Task:** Do the same for `mass2`.
- **Your Task:** The skeleton file also includes lines to update the `string` visuals so they stay attached to the blocks. Make sure to uncomment these as well.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/2.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/802926b2c58c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
