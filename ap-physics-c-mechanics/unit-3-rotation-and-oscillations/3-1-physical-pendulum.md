---
title: "3.1 - Physical Pendulum"
layout: default
---
# Information: The Physical Pendulum

## 1. Introduction to the Unit: Rotational Motion and Oscillations

This unit combines the principles of rotational motion with oscillatory motion. We will analyze the swinging motion of a **physical pendulum**. 

A **simple pendulum** (as studied in AP Physics 1) is an idealized model where all the mass is concentrated in a point-like "bob" at the end of a massless string. A **physical pendulum** is any real, rigid object that is free to swing about a pivot point that is not its center of mass. 

Because a physical pendulum has its mass distributed over a volume, we can no longer ignore its shape. We must use the concept of **moment of inertia (`I`)** to correctly describe its motion, and we must analyze the **torque** that causes it to swing.

## 2. Relevant Physics Concepts

### Rotational Dynamics of a Pendulum

-   **Restoring Torque (`τ`):** The force of gravity (`Fg = mg`) acts on the object's **center of mass (CM)**. Since this force is applied at a distance from the pivot, it creates a torque. This gravitational torque is the **restoring torque** that always tries to bring the object's CM back to the lowest point. The magnitude of this torque is:
    `τ = -mgd * sin(θ)`
    -   `d` is the distance from the pivot to the center of mass.
    -   `θ` is the angle of displacement from the vertical equilibrium position.
    -   The negative sign indicates it is a restoring torque.

-   **Moment of Inertia (`I`):** This is the object's resistance to rotation. It depends on the object's mass and how that mass is distributed. For a uniform rod of mass `m` and length `L` pivoted at one end, the moment of inertia is `I = (1/3)mL²`.

-   **Newton's Second Law for Rotation:** The net torque equals the moment of inertia times the angular acceleration (`α`).
    `τ_net = I * α`

### Period of a Physical Pendulum

By setting the restoring torque equal to `I*α`, we get:

`-mgd * sin(θ) = I * α`

For small angles, we can use the approximation `sin(θ) ≈ θ`. This shows that the motion is approximately Simple Harmonic Motion (SHM). By solving this equation, we can find the theoretical period of a physical pendulum for small angles:

**`T = 2π * sqrt(I / (mgd))`**

Note that if you substitute the values for a simple pendulum (`I = mL²` and `d = L`), this formula simplifies to the familiar `T = 2π * sqrt(L/g)`.

## 3. The Simulation: The Swinging Rod

### Outline of the Simulation

The `intermediate.py` file shows a uniform rod pivoted at its top end, free to swing under the influence of gravity. Your task is to complete the physics inside the animation loop by calculating the angular acceleration and updating the rod's motion, then comparing the result to the theoretical period.

### Completing the `intermediate.py` File

#### **Task 1: Calculate Torque and Angular Acceleration**

This is the core of the rotational dynamics.

- **Example (Torque):** The torque is calculated from the cross product of the position vector of the center of mass (`r_vec`) and the force of gravity vector (`Fg_vec`). The code to calculate the torque vector is given as an example:
  ```python
  torque = cross(r_vec, Fg_vec)
  ```

- **Your Task (Angular Acceleration):** The angular acceleration `alpha` is the rotational equivalent of `a = F/m`. It is found by dividing the torque by the moment of inertia. The moment of inertia for the rod, `I_rod`, is already calculated for you. Write the line of code to find `alpha` from the z-component of the `torque` vector (`torque.z`) and `I_rod`.

#### **Task 2: Update Motion**

This uses the principles of rotational kinematics.

- **Your Task:** Write the two lines of code to update the angular velocity `omega` and the change in angle `d_theta` using the `alpha` you just calculated and the time step `dt`.
- **Your Task:** Use the `.rotate()` method to visually rotate the `rod` object. The angle of rotation for this frame is the `d_theta` you just found.

#### **Task 3: Analysis**

- **Your Task:** The final step is to compare your simulation to the theory. Write a line of code to calculate the theoretical period, `T_theory`, using the formula `T = 2π * sqrt(I / (mgd))`. All the necessary variables (`I_rod`, `rod_m`, `g`, and `d=rod_L/2`) are available to you.
- **Analysis:** After you add graphing to the simulation (by plotting `theta` vs. `t`), you can measure the period directly from your simulation's graph. Compare this measured value to the `T_theory` you calculated. Do they match?

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CMech/program/3.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/2df8d6b59ee6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>