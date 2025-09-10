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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  An object is in Simple Harmonic Motion (SHM). At the equilibrium position, which of the following is at its maximum?
    a) The magnitude of acceleration.
    b) The magnitude of the restoring force.
    c) The speed.
    d) The potential energy.

2.  A mass is oscillating on a spring. If you increase the amplitude of the oscillation (i.e., you pull the mass back further initially), what happens to the period of the motion?
    a) The period increases.
    b) The period decreases.
    c) The period remains the same.
    d) It depends on the spring constant.

3.  The defining characteristic of the restoring force that leads to Simple Harmonic Motion is that the force is:
    a) Constant.
    b) Directly proportional to the velocity.
    c) Directly proportional to the displacement and in the same direction.
    d) Directly proportional to the displacement and in the opposite direction.

4.  A mass `m` is attached to a spring with constant `k`, and it oscillates with a period `T`. If the mass is replaced with a new mass `4m`, what is the new period?
    a) T/2
    b) T
    c) 2T
    d) 4T

5.  The position-time graph of an object undergoing SHM is a sine wave. What is the shape of the velocity-time graph?
    a) Also a sine wave, in phase with the position.
    b) A cosine wave (a sine wave shifted by 90 degrees).
    c) A straight line.
    d) A parabola.

### Problem-Solving Questions

1.  A 0.5 kg mass is attached to a spring with a spring constant of 50 N/m. What is the period of its oscillation?
    a) 0.1 s
    b) 0.628 s
    c) 1.0 s
    d) 10.0 s

2.  A mass-spring system oscillates with a period of 2.0 s. If the mass is 1.0 kg, what is the spring constant `k`?
    a) 1.0 N/m
    b) 9.87 N/m
    c) 19.7 N/m
    d) 39.5 N/m

3.  A spring has a constant `k = 200 N/m`. How much mass must be attached to the spring so that the system oscillates with a frequency of 5 Hz? (Remember `f = 1/T`)
    a) 0.2 kg
    b) 0.81 kg
    c) 1.25 kg
    d) 5.0 kg

4.  A block on a spring is pulled to a position of `x = +A` and released. How long does it take for the block to first reach the equilibrium position `x = 0`?
    a) T/4
    b) T/2
    c) T
    d) 2T

5.  A mass `m` on a spring with constant `k` has a period `T`. What is the period if the spring is cut in half? (Hint: cutting a spring in half doubles its spring constant).
    a) T / sqrt(2)
    b) T / 2
    c) T * sqrt(2)
    d) 2T

### Computational Questions

1.  In the simulation, you are asked to plot `block.pos.x` versus `t`. The resulting graph should have what characteristic shape?
    a) A straight line with a positive slope.
    b) A parabola.
    c) A sinusoidal wave (like a sine or cosine curve).
    d) A circle.

2.  The simulation asks you to measure the period from the graph by finding the time between two consecutive peaks. This graphical measurement should be very close to the value calculated from:
    a) `2 * pi * sqrt(k / m)`
    b) `(1 / (2 * pi)) * sqrt(k / m)`
    c) `2 * pi * sqrt(m / k)`
    d) `A * cos(t)`

3.  If you were to modify the simulation by doubling the initial displacement (the amplitude `A`), how would the values on the y-axis of your position-time graph change?
    a) The maximum and minimum values would double.
    b) The values would be halved.
    c) The values would not change.
    d) The graph would shift upwards.

4.  The simulation uses the force `F = -kx` to calculate acceleration, which then updates velocity and position. This step-by-step calculation is an example of:
    a) The analytical solution.
    b) Numerical integration.
    c) Energy conservation.
    d) The Fourier transform.

5.  To plot the data inside the loop, the correct VPython command would be:
    a) `pos_curve.plot(pos=block.pos.x, t)`
    b) `plot(pos_curve, t, block.pos.x)`
    c) `pos_curve.plot(t, block.pos.x)`
    d) `graph(t, block.pos.x)`

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (d), 4. (c), 5. (b)
**Problem-Solving:** 1. (b), 2. (b), 3. (a), 4. (a), 5. (a)
**Computational:** 1. (c), 2. (c), 3. (a), 4. (b), 5. (c)
