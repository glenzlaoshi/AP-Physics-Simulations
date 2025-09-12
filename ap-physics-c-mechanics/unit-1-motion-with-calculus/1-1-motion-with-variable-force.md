---
title: "1.1 - Motion with Variable Force"
layout: default
---


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

## Multiple Choice Questions

### Conceptual Questions

1.  Under what condition is it invalid to use the standard kinematic equations (e.g., `Δx = v₀t + ½at²`)?
    a)  When the object is at rest.
    b)  When the acceleration is constant.
    c)  When the net force on the object is non-zero.
    d)  When the net force on the object is variable.
2.  For a particle moving in one dimension, the net force on it is given by `F(x) = -kx²`, where k is a positive constant. What can be said about the particle's acceleration?
    a)  The acceleration is constant.
    b)  The acceleration is zero.
    c)  The acceleration is a function of position.
    d)  The acceleration is a function of time only.
3.  The relationship between force and potential energy is `F = -dU/dx`. If a force is given by `F(x) = 3x²`, what is the change in potential energy when moving from x=0 to x=2?
    a)  -8 J
    b)  8 J
    c)  -12 J
    d)  12 J
4.  The Euler-Cromer method for numerical integration is an approximation. What is the primary source of error in this method?
    a)  The assumption that acceleration is constant over a small time step `dt`.
    b)  Computer floating-point precision errors.
    c)  The use of `v_new` instead of `v_old` to update the position.
    d)  The force calculation being incorrect.
5.  If the net force on an object is `F(t) = ct`, where c is a constant, what is the object's velocity as a function of time, assuming it starts from rest?
    a)  `v(t) = c`
    b)  `v(t) = ct`
    c)  `v(t) = (1/2)ct²`
    d)  `v(t) = (1/2)ct²/m`

### Problem-Solving Questions

6.  The position of a particle is given by `x(t) = 3t³ - 4t² + 2`. What is the particle's acceleration at t = 2 s?
    a)  10 m/s²
    b)  20 m/s²
    c)  28 m/s²
    d)  36 m/s²
7.  A particle's velocity is described by the function `v(t) = 3t² + 2t`. What is the displacement of the particle from t = 0 s to t = 3 s?
    a)  18 m
    b)  27 m
    c)  36 m
    d)  45 m
8.  An object of mass 2 kg is subjected to a force `F(x) = -4x`. If the object is released from rest at x = 3 m, what is its speed when it passes through the origin (x=0)?
    a)  3 m/s
    b)  `3√2` m/s
    c)  6 m/s
    d)  18 m/s
9.  The acceleration of a particle is given by `a(t) = 6t - 2`. If the particle has an initial velocity of 5 m/s at t=0, what is its velocity at t=4 s?
    a)  24 m/s
    b)  32 m/s
    c)  45 m/s
    d)  51 m/s
10. A force `F(x) = (4.0 N/m)x - (1.0 N/m³)x³` acts on a particle. How much work is done by this force as the particle moves from x = 1.0 m to x = 2.0 m?
    a)  2.25 J
    b)  3.75 J
    c)  5.25 J
    d)  6.00 J

### Computational Questions

11. In the simulation's numerical integration loop, why is the line `cart.pos = cart.pos + cart.velocity * dt` used instead of `cart.pos.x = cart.pos.x + cart.velocity.x * t`?
    a)  Because `t` represents the total elapsed time, not the small time step `dt` over which the velocity is assumed constant.
    b)  Because velocity is a vector, and this is vector addition.
    c)  The code `cart.pos.x = cart.pos.x + cart.velocity.x * t` would be more accurate.
    d)  It is a syntax requirement of the programming language.
12. What would be the most likely consequence of significantly *increasing* the value of `dt` in the simulation?
    a)  The simulation would run faster and become more accurate.
    b)  The simulation would run faster, but the numerical solution would diverge from the true analytical solution.
    c)  The simulation would run slower and become more accurate.
    d)  The simulation would run slower, and the numerical solution would diverge from the true analytical solution.
13. The simulation calculates the theoretical position using `x_theory = A * cos(omega * t)`. Why is it important to calculate `omega = sqrt(spring.k / cart.m)` *before* the main `while` loop begins?
    a)  Because `omega` is a constant that depends on the system's physical properties (k and m), not on time. Calculating it repeatedly would be inefficient.
    b)  It is not important; it could be calculated inside the loop with the same result.
    c)  The value of `spring.k` changes inside the loop.
    d)  The value of `cart.m` changes inside the loop.
14. If you wanted to model a force that also depends on velocity (like air drag, `F_drag = -bv`), where in the simulation loop would you add this force calculation?
    a)  Before the loop begins.
    b)  Inside the loop, before the net force is calculated.
    c)  Inside the loop, after the position is updated.
    d)  After the loop has finished.
15. The simulation updates velocity before position: `cart.velocity = cart.velocity + a * dt` is followed by `cart.pos = cart.pos + cart.velocity * dt`. This is the Euler-Cromer method. What would happen if you used the *old* velocity to update position (`cart.pos = cart.pos + v_old * dt`)?
    a)  The simulation would be more stable and accurate.
    b)  The total energy of the system would gradually and artificially increase over time.
    c)  The total energy of the system would gradually and artificially decrease over time.
    d)  The result would be identical.
