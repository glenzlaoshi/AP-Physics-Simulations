---
title: "3.1 - Uniform Circular Motion"
layout: default
---

## 1. Introduction to the Unit: Circular Motion

So far, we have studied motion in straight lines. This unit expands our understanding of dynamics to objects moving in circular paths. The key idea is a direct consequence of Newton's First Law: an object will only change its direction of motion if a net force acts on it.

For an object to move in a circle, it must be constantly changing direction. This means there must be a constant net force acting on it, directed towards the center of the circle. We call this center-seeking net force the **centripetal force**. 

It is very important to understand that centripetal force is **not** a new, fundamental force of nature. It is simply the *label* we give to the net force that causes circular motion. The actual force providing the centripetal action could be tension (like in this simulation), gravity (for a planet in orbit), or friction (for a car turning a corner).

## 2. Relevant Physics Concepts

### Uniform Circular Motion (UCM)

UCM describes motion in a perfect circle at a **constant speed**. A common point of confusion is the difference between speed and velocity. 
- **Speed** is a scalar (just a number, e.g., 5 m/s).
- **Velocity** is a vector (speed *and* direction).

In UCM, the speed is constant, but the **velocity is always changing** because the object's direction is always changing. 

### Centripetal Acceleration (`ac`)

Since velocity is changing, there must be an acceleration. For an object in UCM, this acceleration is called centripetal acceleration. 
- **Direction:** It is always directed radially inward, towards the center of the circle.
- **Magnitude:** It is given by the formula `ac = v² / r`, where `v` is the object's constant speed and `r` is the radius of the circle.

### Centripetal Force (`Fc`)

From Newton's Second Law (`F=ma`), if there is an acceleration, there must be a net force. The centripetal force is the net force required to produce the centripetal acceleration.
- **Direction:** It also always points towards the center of the circle.
- **Magnitude:** It is given by `Fc = m * ac = m * v² / r`.

## 3. The Simulation: A Ball on a String

### Outline of the Simulation

The `skeleton.py` file shows a ball attached by a "string" to a central post. The goal is to make the ball move in a circle at a constant speed. The main challenge is that, unlike our previous simulations, the acceleration is **not constant**. Its magnitude is constant, but its *direction* must change every single frame to always point at the center.

### Completing the `skeleton.py` File

#### **Task 1: Initial Velocity**

To get the motion started, the ball needs an initial velocity that is **tangential** to the circular path. If the ball starts at position `vector(5, 0, 0)`, a tangential velocity would be purely in the y-direction. Your task is to set the `ball.velocity` to an initial vector like `vector(0, 4, 0)`.

#### **Task 2 & 3: Calculating Acceleration in the Loop**

Because the direction of centripetal acceleration is always changing, you must recalculate it **inside** the `while` loop. This is the most important part of the simulation.

1.  **Magnitude (Example):** First, you need the *magnitude* of the acceleration. The formula is `ac = v² / r`. The code for this is provided as an example:
    ```python
    a_mag = speed**2 / radius
    ```

2.  **Direction (Your Task):** Next, you need the *direction* of the acceleration. The direction must always point from the ball back to the center of the circle (the origin, `vector(0,0,0)`). The ball's own position vector, `ball.pos`, points from the center to the ball. Therefore, the vector pointing from the ball *back to the center* is simply `-ball.pos`. 

    To get a pure direction vector (called a "unit vector"), we use the VPython function `norm()`. Your task is to define the direction vector `a_dir` using this logic.

3.  **Putting It Together (Your Task):** The final acceleration vector is its magnitude multiplied by its direction. Write the line of code to set `ball.acceleration` by multiplying `a_mag` and `a_dir`.

#### **Updating Motion**

- **Your Task:** Once the acceleration vector has been calculated for the current frame, you can use the same numerical integration technique from the previous units. Write the two lines of code inside the loop to update the `ball.velocity` and `ball.pos`.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations/program/3.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/52405b4d95d5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
