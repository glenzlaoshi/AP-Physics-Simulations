---
title: "6.2 - Pendulum"
layout: default
---
# Information: The Simple Pendulum

## 1. Introduction to the Unit: SHM (continued)

This simulation explores another classic oscillating system: the simple pendulum. A simple pendulum consists of a point mass (the "bob") suspended from a pivot by a massless string or rod. 

Like the mass-spring system, a pendulum swings back and forth about an equilibrium position. A key question we will investigate is whether this motion is truly **Simple Harmonic Motion (SHM)**. Recall that the strict condition for SHM is that the restoring force must be directly proportional to the displacement (`F ∝ -x`). We will see that a pendulum only meets this condition approximately, and only for small angles.

## 2. Relevant Physics Concepts

### The Restoring Force of a Pendulum

Two forces act on the pendulum bob: the tension `T` from the string, and the force of gravity `Fg = mg`.

To understand the motion, we break the gravity vector into two components:
1.  A component parallel to the string (`mg*cos(θ)`), which is cancelled out by the tension force.
2.  A component **tangential** to the circular path of the swing (`mg*sin(θ)`). 

This tangential component is the **restoring force**. It is what is always trying to pull the bob back to its lowest point (the equilibrium position). 

`F_restore = -mg * sin(θ)`

The negative sign is crucial; it indicates the force is always in the opposite direction of the angular displacement `θ`.

### The Small Angle Approximation

Is the pendulum's motion SHM? The restoring force is `F = -mg*sin(θ)`. This is proportional to `sin(θ)`, not to the displacement `θ` itself. Therefore, strictly speaking, a pendulum does **not** undergo true SHM.

However, for small angles (typically less than 15°), the value of `sin(θ)` is very close to the value of `θ` (when `θ` is measured in radians). This is known as the **small angle approximation**.

So, for small angles only, we can say: `F_restore ≈ -mg*θ`. Since `mg` is constant, the restoring force is *approximately* proportional to the displacement, and the motion is very close to being SHM.

### The Period of a Simple Pendulum

Using the small angle approximation, we can derive a formula for the period of a simple pendulum:

**`T = 2π * sqrt(L / g)`**

-   `L` is the length of the pendulum.
-   `g` is the acceleration due to gravity.

Notice that for small angles, the period does **not** depend on the mass of the bob or on the amplitude of the swing.

## 3. The Simulation: Analyzing the Swing

### Outline of the Simulation

The `intermediate.py` file already contains the code to make a pendulum swing. It correctly calculates the restoring force and updates the motion without using the small angle approximation. Your task is to analyze this motion to see when the small angle approximation is valid.

### Completing the `intermediate.py` File

#### **Task 1: Graph the Motion**

- **Your Task:** Just as with the mass-spring system, the first step in analysis is to plot the motion. Before the `while` loop, create a `graph` and a `gcurve`. Inside the loop, add the line to plot the pendulum's angle `theta` versus time `t`.

#### **Task 2: Measure the Period**

- **Your Task:** Run the simulation with the initial small angle (20 degrees). Look at the graph you created and measure the time between the first two peaks. This is your **measured period**.

#### **Task 3: Compare with Theory**

- **Example (The Formula):** The theoretical period *using the small angle approximation* is `T = 2π * sqrt(L / g)`. The code to calculate this is:
  ```python
  T_theory = 2 * pi * sqrt(rod.L / g)
  ```
- **Analysis:** Compare the period you measured from the graph with this `T_theory`. For the small 20-degree angle, they should be very close.

#### **Task 4: Test the Approximation**

- **Your Task:** This is the key conceptual step. Go back to the top of the code and change the initial angle from `radians(20)` to a large angle, like `radians(80)`.
- **Your Task:** Run the simulation again and measure the period from the new graph.
- **Analysis:** Is the new measured period still close to `T_theory`? You will find that for large angles, the actual period is noticeably **longer** than the period predicted by the small angle formula. This shows the limit of the approximation.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/6.2-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/92bcc34898ba" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>