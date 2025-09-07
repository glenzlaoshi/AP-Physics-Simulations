---
title: "1.1 - Motion with Variable Force"
layout: default
---
# Information: Motion with Variable Force

## 1. Introduction to the Unit: Calculus in Mechanics

Welcome to AP Physics C! This course differs from AP Physics 1 primarily through the use of **calculus**. While Physics 1 often restricts problems to constant forces and accelerations, Physics C uses calculus to analyze more complex and realistic scenarios where forces are **variable**.

Calculus provides the mathematical language to describe and work with changing quantities.
-   **Velocity** is the time derivative of position: `v = dx/dt`
-   **Acceleration** is the time derivative of velocity: `a = dv/dt`

Conversely, we can use integration to find changes in velocity and position:
-   `Δv = ∫a(t) dt`
-   `Δx = ∫v(t) dt`

This simulation focuses on how to solve problems when the force, and therefore the acceleration, is not constant.

## 2. Relevant Physics Concepts

### Variable Forces

A variable force is one whose magnitude or direction changes depending on an object's position, velocity, or time. A classic example, and the one used in this simulation, is the **spring force**, described by Hooke's Law:

`F = -kx`

This force is dependent on the object's position `x`. The farther the spring is stretched, the stronger the restoring force becomes. Since the force is not constant, the acceleration is not constant, and the standard kinematic equations (`v = v₀ + at`, etc.) **do not apply**.

### Newton's Second Law and Differential Equations

Newton's Second Law, `F_net = ma`, is still the central principle. However, when we substitute our calculus definitions, we get:

`F_net = m * (d²x / dt²)`

For a mass-spring system, this becomes ` -kx = m * (d²x / dt²)`. This is a **differential equation**. While there are analytical methods to solve such equations, a powerful and general approach is to solve them on a computer.

### Numerical Integration

To solve these problems on a computer, we use **numerical integration**. We break the motion into a series of very small time steps (`dt`). In each step, we assume the acceleration is approximately constant and update the object's velocity and position. This is often called the **Euler-Cromer method**.

The process for each time step is:
1.  Use the object's current `position` to calculate the `Force` at that instant.
2.  Use that `Force` to calculate the `acceleration` at that instant (`a = F/m`).
3.  Use that `acceleration` to update the `velocity` (`v_new = v_old + a*dt`).
4.  Use the **new** `velocity` to update the `position` (`x_new = x_old + v_new*dt`).
5.  Repeat for the next time step.

This step-by-step calculation allows us to simulate motion even when the forces are complex.

## 3. The Simulation: The Oscillating Cart

### Outline of the Simulation

The `intermediate.py` file already contains a complete simulation of a cart attached to a spring. It correctly calculates the variable spring force and uses numerical integration to model the resulting motion. Your task is not to build the simulation, but to **analyze its accuracy** by comparing the numerical result to the exact, analytical solution.

### Completing the `intermediate.py` File

#### **Analysis and Comparison**

The motion of a mass on a spring is Simple Harmonic Motion (SHM). The exact solution, found by solving the differential equation, is `x(t) = A * cos(ωt)`, where `A` is the amplitude and `ω = sqrt(k/m)` is the angular frequency.

Your task is to plot both the simulation data and this exact theoretical solution on the same graph to see how well our numerical method works.

- **Example (Graphing the Simulation):** The first step is to plot the position of the cart from the simulation. You will need to create a `graph` and a `gcurve` for the simulation data (`sim_curve`). The code to plot the data inside the loop is:
  ```python
  sim_curve.plot(t, cart.pos.x)
  ```

- **Your Task (Graphing the Theory):** Now, you need to plot the exact solution on a second curve (`theory_curve`).
    1.  First, before the loop, calculate the angular frequency `omega` using the formula `ω = sqrt(k/m)`. The simulation variables are `spring.k` and `cart.m`.
    2.  The amplitude `A` is the cart's starting x-position.
    3.  Inside the `while` loop, write the line of code to calculate the theoretical position, `x_theory`, for the current time `t`.
    4.  Write the line of code to plot `x_theory` vs. `t` on the `theory_curve`.

When you run the code, you will see two curves. The blue curve is the result of our step-by-step numerical integration. The red curve is the perfect, exact mathematical solution. How well do they line up? What might happen to the accuracy of the blue curve if you were to increase the size of the time step `dt`?

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CMech/program/1.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/b731d6e48ea0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>