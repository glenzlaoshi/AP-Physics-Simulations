---
title: "1.1 - Ideal Gas Law"
layout: default
---


## 1. Introduction to the Unit: Thermodynamics

Thermodynamics is the branch of physics that deals with heat, work, and temperature, and their relation to energy and the physical properties of matter. A key part of thermodynamics is understanding the behavior of gases.

In this simulation, we will explore the **Ideal Gas Law**, which describes the relationship between the macroscopic properties of a gas: Pressure, Volume, and Temperature. We will use the **Kinetic Theory of Gases**, a microscopic model, to see how the collective actions of individual gas particles give rise to these large-scale properties.

An **Ideal Gas** is a simplified theoretical model of a gas in which we assume the particles themselves have no volume and do not interact with each other except through perfectly elastic collisions. This model works very well for real gases under many conditions.

## 2. Relevant Physics Concepts

### The Kinetic Theory of Gases

This theory connects the motion of individual particles to the macroscopic properties we can measure.

-   **Pressure (`P`):** In the model, pressure is caused by the force of countless gas particles colliding with the walls of the container. The pressure depends on how many particles there are, how fast they are moving, and the size of the container.

-   **Temperature (`T`):** In the model, temperature is a direct measure of the **average kinetic energy** of the gas particles. A higher temperature means the particles have a higher average speed. The relationship is:
    `KE_avg = (3/2)kT`
    where `k` is the Boltzmann constant.

### The Ideal Gas Law

This law is an equation of state that relates the four macroscopic gas variables. It is one of the most important equations in thermodynamics.

`PV = nRT`  or, in terms of individual particles,  `PV = NkT`

-   `P` is the absolute pressure of the gas.
-   `V` is the volume the gas occupies.
-   `N` is the total number of gas particles.
-   `k` is the Boltzmann constant (`1.38e-23 J/K`).
-   `T` is the absolute temperature in Kelvin.

This equation shows, for example, that if you keep the temperature constant and decrease the volume of a gas, its pressure must increase because the particles will collide with the walls more frequently.

## 3. The Simulation: A Box of Gas

### Outline of the Simulation

The `intermediate.py` file shows a number of particles moving randomly inside a box. They are already programmed to have perfectly elastic collisions with the walls. Your task is to add the physics calculations to measure the gas's macroscopic properties (Pressure and Temperature) from the microscopic motions of these particles.

### Completing the `intermediate.py` File

#### **Task 1: Calculate Pressure**

Pressure is force per unit area (`P = F/A`). The force on a wall is the total momentum transferred to it by particle collisions, per unit time (`F = Δp / Δt`).

- **Example (Momentum Transfer):** When a single particle hits the right-hand wall (at `x=L/2`), its x-velocity reverses from `vx` to `-vx`. The change in the particle's own momentum is `p_final - p_initial = m*(-vx) - m*(vx) = -2*m*vx`. By Newton's Third Law, the impulse (change in momentum) delivered **to the wall** is the opposite of this: `+2*m*vx`.

- **Your Task (Total Momentum Transfer):** Inside the `if` statement that checks for a wall collision, you need to add the momentum transferred to a running total. A variable `total_delta_p` is created for this purpose before the loop. Add a line to update this variable every time a particle hits a wall.

- **Your Task (Pressure Calculation):** After the loop finishes, you can calculate the average force on the walls (`F_avg = total_delta_p / t`) and then the pressure (`Pressure = F_avg / Area`). The total area of the box is `6 * L²`. Write the code to perform this calculation.

#### **Task 2: Calculate Temperature**

Temperature is a measure of the average kinetic energy of the particles.

- **Your Task:** Inside the main `for` loop that iterates through the particles, you need to calculate the kinetic energy (`KE = 0.5*m*v²`) for each particle `p`. Add this value to a running total, `total_ke`. (Note: `mag2(p.velocity)` is a VPython shortcut for `v²`).

- **Your Task:** After the loop, calculate the average kinetic energy: `KE_avg = total_ke / N`. Then, use the formula `T = (2/3) * KE_avg / k` to find the temperature of the gas in Kelvin.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/1.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/ac4c11afee7e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
