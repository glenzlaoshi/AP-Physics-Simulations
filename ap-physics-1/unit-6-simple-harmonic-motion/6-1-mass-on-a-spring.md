---
title: "6.1 - Mass on a Spring"
layout: default
---


## 1. Introduction to the Unit: Simple Harmonic Motion (SHM)

This unit focuses on a special and very common type of repeating motion called **Simple Harmonic Motion (SHM)**. SHM occurs whenever an object moves back and forth about an equilibrium position, and the force trying to restore it to equilibrium is directly proportional to the object's displacement from that equilibrium.

This relationship is written as `F ∝ -x`. The negative sign is crucial: it signifies that the **restoring force** always acts in the opposite direction of the displacement, pulling or pushing the object back towards the center.

The classic textbook example of SHM, and the one we will model here, is a mass attached to a spring on a frictionless surface.

## 2. Relevant Physics Concepts

### The Restoring Force in a Spring

The force exerted by an ideal spring is given by **Hooke's Law**: `F = -kx`.
-   `k` is the spring constant, a measure of stiffness.
-   `x` is the displacement from the spring's natural length (its equilibrium position).

Because this force is directly proportional to the displacement (`F ∝ -x`), a mass-spring system is the perfect example of an object that will undergo SHM.

### Terminology of SHM

-   **Amplitude (A):** The maximum displacement from the equilibrium position.
-   **Period (T):** The time it takes to complete one full cycle of motion (e.g., from maximum stretch, to maximum compression, and back to maximum stretch).
-   **Frequency (f):** The number of cycles completed per second. `f = 1/T`.

### The Period of a Mass-Spring System

For a mass-spring system, the period of oscillation does **not** depend on the amplitude of the motion. Whether you stretch the spring a little or a lot, the time for one full oscillation remains the same! The period is determined only by the mass `m` and the spring constant `k`:

**`T = 2π * sqrt(m / k)`**

### Graphs of SHM

A key feature of SHM is that the graph of an object's position versus time is a **sinusoidal wave** (a sine or cosine curve). This is considered the hallmark of SHM. When you plot the motion of the mass on the spring, you should see this characteristic wave shape.

## 3. The Simulation: Analyzing the Oscillation

### Outline of the Simulation

The `intermediate.py` file already contains the code to make the block oscillate using Hooke's Law and `F=ma`. Your task is not to build the simulation, but to **analyze** the motion to verify that it is SHM and to check if its period matches the theoretical formula.

### Completing the `intermediate.py` File

#### **Task 1: Graph the Motion**

The best way to analyze the motion is to create a graph of the block's position versus time.

- **Your Task:** Before the `while` loop, you need to create a graphing window. The VPython command is `graph()`. You can give it titles like this: `graph(xtitle='time', ytitle='position')`.
- **Your Task:** Next, still before the loop, you need to create a data series to plot. The command is `gcurve()`. You can assign it to a variable and set its color: `pos_curve = gcurve(color=color.green)`.
- **Your Task:** Finally, *inside* the `while` loop, you must add the line that plots the data at each time step. The command is `.plot()`. You need to plot the time `t` on the x-axis and the block's x-position `block.pos.x` on the y-axis.

#### **Task 2: Measure the Period from the Graph**

Once you have a graph, you can measure the period `T`. The period is the time difference between two consecutive peaks (or any two identical points on consecutive cycles). Run the simulation and inspect the graph to find the time of the first peak and the time of the second peak. The difference between them is your measured period.

#### **Task 3: Compare with Theory**

- **Example (The Formula):** The theoretical period for a mass-spring system is given by the formula `T = 2π * sqrt(m / k)`.
- **Your Task:** Write a line of code to calculate the theoretical period, `T_theory`, using the simulation's variables `block.m` and `spring.k`. VPython knows `pi` and `sqrt()`.
- **Analysis:** Print both your measured period and your calculated theoretical period. Do they match? They should be very close, confirming that our simulation correctly models the physics of a mass-spring system.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/6.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/365551f9167c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>