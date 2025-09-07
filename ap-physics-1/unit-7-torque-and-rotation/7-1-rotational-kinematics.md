---
title: "7.1 - Rotational Kinematics"
layout: default
---
# Information: Rotational Kinematics

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