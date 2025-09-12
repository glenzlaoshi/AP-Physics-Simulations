---
title: "3.1 - Physical Pendulum"
layout: default
---


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

## Multiple Choice Questions

### Conceptual Questions

1.  What is the primary difference between a simple pendulum and a physical pendulum?
    a)  A simple pendulum does not oscillate, while a physical pendulum does.
    b)  A simple pendulum assumes a massless string and a point mass, while a physical pendulum is any rigid swinging object.
    c)  A simple pendulum is not affected by gravity.
    d)  A physical pendulum always has a longer period than a simple pendulum.
2.  For a physical pendulum, the restoring torque is provided by:
    a)  The tension in the string.
    b)  The force of gravity acting on the pivot point.
    c)  The force of gravity acting on the center of mass.
    d)  Air resistance.
3.  The period of a physical pendulum is given by `T = 2π * sqrt(I / (mgd))`. If you take the same pendulum to a planet with twice the gravitational acceleration `g`, what happens to its period?
    a)  It is doubled.
    b)  It is halved.
    c)  It decreases by a factor of `√2`.
    d)  It increases by a factor of `√2`.
4.  Why is the small angle approximation (`sin(θ) ≈ θ`) used when deriving the formula for the period of a pendulum?
    a)  To make the torque constant.
    b)  To show that the motion is Simple Harmonic Motion, which has a well-defined period.
    c)  Because the formula is only valid for small angles.
    d)  To simplify the calculation of the moment of inertia.
5.  A uniform rod is pivoted at one end and swings as a physical pendulum. Where could you pivot the same rod to make its period of oscillation as long as possible?
    a)  At the center of mass.
    b)  At the end of the rod.
    c)  As close to the center of mass as possible, but not exactly at it.
    d)  The pivot point does not affect the period.

### Problem-Solving Questions

6.  A uniform rod of length L and mass M is pivoted at one end. What is its moment of inertia about the pivot?
    a)  `(1/12)ML²`
    b)  `(1/3)ML²`
    c)  `(1/2)ML²`
    d)  `ML²`
7.  A uniform rod of length 2.0 m and mass 3.0 kg is pivoted at one end. What is the period of its small oscillations? (g = 9.8 m/s²)
    a)  1.8 s
    b)  2.3 s
    c)  2.9 s
    d)  3.5 s
8.  A flat circular disk of radius R and mass M is pivoted at its rim. Its moment of inertia about the center is `(1/2)MR²`. Using the parallel axis theorem (`I = I_cm + Md²`), what is its moment of inertia about the pivot at the rim?
    a)  `(1/2)MR²`
    b)  `MR²`
    c)  `(3/2)MR²`
    d)  `2MR²`
9.  A physical pendulum consists of a uniform sphere of mass M and radius R attached to the end of a massless rod of length L. The system is pivoted at the other end of the rod. The moment of inertia of the sphere about its center is `(2/5)MR²`. What is the distance `d` from the pivot to the center of mass of the system?
    a)  L
    b)  R
    c)  L + R
    d)  `sqrt(L² + R²)`
10. A physical pendulum has a moment of inertia of 0.5 kg·m², a mass of 2.0 kg, and the distance from the pivot to its center of mass is 0.4 m. What is the restoring torque when it is displaced by an angle of 30 degrees from the vertical? (g = 9.8 m/s²)
    a)  -3.92 N·m
    b)  -6.79 N·m
    c)  -7.84 N·m
    d)  -0.25 N·m

### Computational Questions

11. In the simulation, the angular acceleration is calculated as `alpha = torque.z / I_rod`. Why is only the z-component of the torque used?
    a)  Because the pendulum is swinging in the x-y plane, so the rotation is about the z-axis.
    b)  It is an approximation; the other components are negligible.
    c)  The torque has no other components.
    d)  To make the calculation simpler.
12. The simulation updates the angular velocity with `omega = omega + alpha * dt`. If you were to simulate the pendulum on the Moon (where g is about 1/6 of Earth's), what would be the primary change in the simulation's behavior?
    a)  The calculated `alpha` would be smaller, leading to a longer period of oscillation.
    b)  The moment of inertia `I_rod` would decrease.
    c)  The time step `dt` would need to be larger.
    d)  The simulation would run faster.
13. The simulation uses `rod.rotate(angle=d_theta, axis=vector(0,0,1))`. What does the `axis` parameter specify?
    a)  The direction of gravity.
    b)  The axis about which the rotation occurs.
    c)  The direction of the rod's center of mass.
    d)  The direction of the angular velocity vector.
14. The theoretical period is calculated using `T_theory = 2*pi*sqrt(I_rod / (rod_m*g*d))`. This formula is based on the small angle approximation. How would the actual period measured from the simulation for a *large* starting angle (e.g., 90 degrees) compare to `T_theory`?
    a)  The measured period would be shorter than `T_theory`.
    b)  The measured period would be longer than `T_theory`.
    c)  The measured period would be exactly equal to `T_theory`.
    d)  The pendulum would no longer oscillate.
15. If you replaced the uniform rod in the simulation with a point mass at the end of a massless string of the same length L (a simple pendulum), what change would you need to make to the `I_rod` variable for the theoretical period calculation to be correct?
    a)  `I_rod` should be set to `rod_m * L²`.
    b)  `I_rod` should be set to `(1/12) * rod_m * L²`.
    c)  `I_rod` should be set to `0`.
    d)  No change is needed.
