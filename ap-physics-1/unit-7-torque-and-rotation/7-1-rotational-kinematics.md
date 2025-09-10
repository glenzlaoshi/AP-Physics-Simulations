---
title: "7.1 - Rotational Kinematics"
layout: default
---


## 1. Introduction to the Unit: Torque and Rotation

This unit introduces the final major topic of AP Physics 1: the motion of rotating objects. The exciting part of this unit is that it doesn't require learning entirely new physics; instead, we will see that every concept from linear (or "translational") motion has a direct rotational equivalent. By understanding these analogies, you can re-apply everything you already know about kinematics and dynamics to rotating systems.

| Linear Concept | Rotational Concept | Description |
| :--- | :--- | :--- |
| Position (`x`) | **Angular Position (`θ`)** | How far an object has turned. |
| Velocity (`v`) | **Angular Velocity (`ω`)** | How fast an object is turning. |
| Acceleration (`a`) | **Angular Acceleration (`α`)** | The rate at which an object's turning speed changes. |
| Mass (`m`) | **Moment of Inertia (`I`)** | An object's resistance to being rotated. |
| Force (`F`) | **Torque (`τ`)** | A "twist" or "turn" that causes rotation. |

## 2. Relevant Physics Concepts

### Rotational Kinematics

Just like linear kinematics, rotational kinematics describes the motion of rotating objects using a set of equations. For a constant angular acceleration `α`, these equations are:

-   `ω_f = ω_i + α*t`
-   `Δθ = ω_i*t + (1/2)α*t²`
-   `ω_f² = ω_i² + 2α*Δθ`

Notice how these are identical in form to the linear kinematic equations!

### Rotational Dynamics

-   **Torque (`τ`):** Torque is the rotational equivalent of force. It is a measure of how effectively a force can cause an object to rotate. It depends on the force, where it's applied, and in what direction.

-   **Moment of Inertia (`I`):** This is the rotational equivalent of mass. It represents an object's inherent resistance to changing its state of rotation. Crucially, `I` depends not just on an object's mass, but on *how that mass is distributed* relative to the axis of rotation. An object with more mass further from the center is harder to rotate. For a solid disk of mass `M` and radius `R` rotating about its center, the formula is `I = (1/2)MR²`.

-   **Newton's Second Law for Rotation:** This is the central equation of rotational dynamics and is the rotational analog of `F_net = m*a`:

    **`τ_net = I * α`**

    The net torque on an object is equal to its moment of inertia times its resulting angular acceleration.

## 3. The Simulation: The Spinning Disk

### Outline of the Simulation

The `skeleton.py` file shows a solid disk that is free to rotate about its center. We will apply a constant **torque** to the disk and use the principles of rotational dynamics and kinematics to model its resulting spinning motion.

### Completing the `skeleton.py` File

#### **Task 2: Calculate Angular Acceleration**

Your first goal is to find the angular acceleration (`alpha`) that results from the applied torque.

- **Example (Moment of Inertia):** Before you can use Newton's Second Law for Rotation, you need the disk's moment of inertia. The formula for a solid disk is `I = (1/2)MR²`. The code for this is given as an example:
  ```python
  disk.I = 0.5 * disk.m * disk.radius**2
  ```

- **Your Task (Angular Acceleration):** Now, use the rotational version of Newton's Second Law, `τ_net = I * α`. Rearrange this formula to solve for `alpha`. Write the line of code to calculate `alpha` using the given `torque` and the `disk.I` you just learned about.

#### **Task 3: Update Rotational Motion**

Now that you have a constant angular acceleration, you can update the disk's rotational motion inside the `while` loop. This is perfectly analogous to the numerical integration you did for linear motion.

- **Example (Angular Velocity):** The first step is to update the angular velocity `omega` based on the angular acceleration `alpha`. The code for this is given as an example:
  ```python
  omega = omega + alpha * dt
  ```

- **Your Task (Angle):** The second step is to update the total angle of rotation, `theta`, based on the new angular velocity `omega`. Write the line of code to do this.

#### **Task 4: Update Visuals**

- **Your Task:** To make the disk actually spin in the animation, you need to use the `.rotate()` method. This function rotates an object by a certain angle around a specified axis. You should rotate the `disk` and the `ref_line` by the small change in angle that occurs in one time step (`omega * dt`). The axis of rotation is the z-axis, which is represented by `vector(0,0,1)`.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/7.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/8663d99a8e62" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The rotational equivalent of mass is:
    a) Torque.
    b) Angular velocity.
    c) Moment of inertia.
    d) Angular acceleration.

2.  Two solid disks have the same mass, but Disk A has twice the radius of Disk B. How does the moment of inertia of Disk A (`IA`) compare to that of Disk B (`IB`)? (For a solid disk, `I = 1/2 * MR²`)
    a) `IA = IB`
    b) `IA = 2 * IB`
    c) `IA = 4 * IB`
    d) `IA = IB / 2`

3.  A spinning ice skater pulls her arms in. What happens to her angular velocity?
    a) It increases.
    b) It decreases.
    c) It remains the same.
    d) It depends on the direction she is spinning.

4.  If the net torque on an object is zero, its angular acceleration must be:
    a) Zero.
    b) Constant but not necessarily zero.
    c) Increasing.
    d) Decreasing.

5.  A wheel is rotating with a constant angular acceleration. Which of the following statements is true?
    a) Its angular velocity is constant.
    b) Its angular displacement is constant.
    c) The net torque on it is constant and non-zero.
    d) The net torque on it is zero.

### Problem-Solving Questions

1.  A wheel starts from rest and has a constant angular acceleration of 2.0 rad/s². What is its angular velocity after 5.0 seconds?
    a) 2.0 rad/s
    b) 5.0 rad/s
    c) 10.0 rad/s
    d) 25.0 rad/s

2.  A solid disk with a mass of 4 kg and a radius of 0.5 m is free to rotate. What is its moment of inertia? (`I = 1/2 * MR²`)
    a) 0.5 kg·m²
    b) 1.0 kg·m²
    c) 2.0 kg·m²
    d) 4.0 kg·m²

3.  A net torque of 10 N·m is applied to the disk from the previous question (`I = 0.5 kg·m²`). What is the resulting angular acceleration?
    a) 5 rad/s²
    b) 10 rad/s²
    c) 20 rad/s²
    d) 50 rad/s²

4.  A spinning top slows down from an initial angular velocity of 30 rad/s to 10 rad/s in 4 seconds. What is its angular acceleration?
    a) -2.5 rad/s²
    b) -5.0 rad/s²
    c) -7.5 rad/s²
    d) -10.0 rad/s²

5.  A flywheel accelerates from rest with `α = 3 rad/s²`. How many revolutions has it turned after 4 seconds? (Hint: Find `Δθ` in radians first, then convert. 1 rev = 2π rad).
    a) 1.9 rev
    b) 3.8 rev
    c) 12 rev
    d) 24 rev

### Computational Questions

1.  The simulation calculates angular acceleration using `alpha = torque / disk.I`. This is a rearrangement of which fundamental physics principle?
    a) `F = ma`
    b) `τ = Iα` (Newton's Second Law for Rotation)
    c) `KE = 1/2 * mv²`
    d) `p = mv`

2.  In the simulation loop, the angular velocity is updated with `omega = omega + alpha * dt`. This is the rotational analog of which linear kinematics equation?
    a) `x = x + v*dt`
    b) `v = v + a*dt`
    c) `a = F/m`
    d) `KE = 1/2 * mv²`

3.  The simulation uses `disk.rotate(angle = omega * dt, axis=vector(0,0,1))`. What does the `axis` parameter define?
    a) The direction of the torque.
    b) The line about which the disk is spinning.
    c) The direction of the angular velocity.
    d) The direction of the angular acceleration.

4.  If you were to double the applied `torque` in the simulation, what would happen to the calculated `alpha`?
    a) It would be halved.
    b) It would remain the same.
    c) It would be doubled.
    d) It would be quadrupled.

5.  The moment of inertia `disk.I` is calculated before the loop starts. Why is it not necessary to recalculate it inside the loop?
    a) Because the torque is constant.
    b) Because the angular acceleration is constant.
    c) Because the mass and radius of the disk are not changing.
    d) It is necessary, and this is a flaw in the simulation.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (a), 4. (a), 5. (c)
**Problem-Solving:** 1. (c), 2. (a), 3. (c), 4. (b), 5. (b)
**Computational:** 1. (b), 2. (b), 3. (b), 4. (c), 5. (c)
