---
title: "1.2 - Projectile Motion"
layout: default
---
# Information: 2D Projectile Motion

## 1. Introduction to the Unit: 2D Kinematics

This topic builds directly on 1D Kinematics. Instead of moving in a straight line, objects can now move in a two-dimensional plane (e.g., both horizontally and vertically). 

The single most important concept in 2D kinematics is the **independence of perpendicular motion**. This powerful idea means we can analyze the horizontal (x-direction) motion of an object completely separately from its vertical (y-direction) motion. The two components do not affect each other. The only thing they share is time (`t`).

The classic example of this is **projectile motion**: the motion of an object that is thrown or launched into the air and moves under the influence of gravity alone.

## 2. Relevant Physics Concepts

### The Independence of Motion

Imagine firing a cannonball from a cliff. Its motion can be broken down into two parts:

1.  **Horizontal (x-direction):** After the initial launch, there are no horizontal forces (we ignore air resistance). This means there is **zero horizontal acceleration**. The cannonball's horizontal velocity, `vx`, never changes.
2.  **Vertical (y-direction):** The only force acting on the cannonball is gravity, which pulls it straight down. This means there is a **constant downward acceleration**, `g` (approximately 9.8 m/s²). The vertical velocity, `vy`, is constantly changing.

### Equations for Projectile Motion

Because we can separate the components, we just use the 1D kinematic equations from the previous unit for each direction.

| Horizontal (x) Motion | Vertical (y) Motion |
| :--- | :--- |
| `ax = 0` | `ay = -g` |
| `vx = constant` | `vy_f = vy_i - g*t` |
| `x = x_i + vx*t` | `y = y_i + vy_i*t - 0.5*g*t²` |

### Initial Velocity Components

Typically, a projectile is launched with an initial speed `v0` at an angle `theta` above the horizontal. To analyze the motion, we must first break this initial velocity vector into its x and y components using trigonometry.

-   `vx_i = v0 * cos(theta)`
-   `vy_i = v0 * sin(theta)`

These initial components are then used in the kinematic equations above.

## 3. The Simulation: Modeling the Trajectory

### Outline of the Simulation

The `skeleton.py` file sets up a scene with a "projectile" (a sphere). Your goal is to use the principles of 2D kinematics to calculate the projectile's trajectory. You will give it an initial velocity and then, inside an animation loop, tell the computer how gravity affects its motion over time.

### Completing the `skeleton.py` File

#### **Task 1 & 2: Initial Velocity Components**

Before the simulation starts, you must calculate the initial x and y components of the projectile's velocity from the given speed `v0` and angle `theta`.

- **A Note on Angles:** Computer math functions like `cos()` and `sin()` expect angles to be in **radians**, not degrees. The skeleton file already converts the angle for you using `radians(45)`.

- **Example (x-component):** To calculate the initial x-velocity, you would write:
  ```python
  vx = v0 * cos(theta)
  ```
- **Your Task (y-component):** Following the example above, write the line of code to calculate the initial y-velocity, `vy`.

Once you have `vx` and `vy`, you can create the initial velocity vector for the VPython object:
`projectile.velocity = vector(vx, vy, 0)`

#### **Task 3: Define Acceleration**

After the projectile is launched, what is its acceleration? The only force is gravity. Therefore, the acceleration is constant and points downwards. Your task is to set the `projectile.acceleration` property to the correct vector value.

#### **Task 4: Update Motion in the Loop**

The animation loop runs as long as the projectile is above the ground (`while projectile.pos.y >= 0:`). Inside the loop, you must update the projectile's velocity and position. 

The great thing about using vectors is that the code is **exactly the same** as it was for 1D motion! VPython handles the x and y components automatically.

Your task is to add the two lines for numerical integration into the loop, just as you did in the previous simulation:
1.  Write the line to update `projectile.velocity` based on its acceleration.
2.  Write the line to update `projectile.pos` based on its new velocity.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/1.2-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/glowscript/acacd2fd38d4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
