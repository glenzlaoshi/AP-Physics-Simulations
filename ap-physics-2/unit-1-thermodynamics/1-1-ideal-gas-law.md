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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  According to the kinetic theory of gases, the absolute temperature of an ideal gas is directly proportional to:
    a) The average momentum of the gas particles.
    b) The average kinetic energy of the gas particles.
    c) The number of particles in the container.
    d) The volume of the container.

2.  If you increase the temperature of a sealed, rigid container of gas, what happens to the pressure inside?
    a) It decreases.
    b) It remains the same.
    c) It increases.
    d) It depends on the type of gas.

3.  The "Ideal Gas" model is most accurate under which conditions?
    a) High temperature and high pressure.
    b) High temperature and low pressure.
    c) Low temperature and high pressure.
    d) Low temperature and low pressure.

4.  You have two containers of ideal gas at the same temperature. Container A has twice the volume of Container B. How does the average kinetic energy of particles in A compare to B?
    a) The average KE in A is twice that in B.
    b) The average KE in A is half that in B.
    c) The average KE is the same in both.
    d) It cannot be determined without knowing the pressure.

5.  The pressure exerted by a gas on the walls of its container is a direct result of:
    a) The gravitational force on the particles.
    b) The repulsive forces between particles.
    c) The particles sticking to the walls.
    d) The change in momentum of particles as they collide with the walls.

### Problem-Solving Questions

1.  A container of volume 2.0 m³ holds an ideal gas at a pressure of 1.0 x 10⁵ Pa and a temperature of 300 K. How many moles (`n`) of gas are in the container? (Use R = 8.31 J/(mol·K))
    a) 40.1 mol
    b) 80.2 mol
    c) 120.3 mol
    d) 160.4 mol

2.  If the absolute temperature of an ideal gas is doubled and its volume is halved, what happens to its pressure?
    a) It is quartered.
    b) It is halved.
    c) It is doubled.
    d) It is quadrupled.

3.  What is the average kinetic energy of a gas particle at a temperature of 400 K? (Use k = 1.38e-23 J/K)
    a) 2.76e-21 J
    b) 5.52e-21 J
    c) 8.28e-21 J
    d) 1.10e-20 J

4.  A piston holds 0.5 m³ of an ideal gas at a pressure of 2.0 x 10⁵ Pa. If the gas is compressed isothermally (at constant temperature) to a volume of 0.2 m³, what is the new pressure?
    a) 2.0 x 10⁵ Pa
    b) 4.0 x 10⁵ Pa
    c) 5.0 x 10⁵ Pa
    d) 8.0 x 10⁴ Pa

5.  A rigid container of gas has its pressure tripled. What is the ratio of the final temperature to the initial temperature (T_final / T_initial)?
    a) 1/3
    b) 1
    c) 3
    d) 9

### Computational Questions

1.  In the simulation, pressure is calculated by first finding the total change in momentum of particles colliding with the walls. Why is this necessary?
    a) Because pressure is defined as the total momentum of the gas.
    b) Because the average force on the wall is the total change in momentum divided by the time interval.
    c) Because temperature is related to momentum.
    d) To ensure the collisions are elastic.

2.  The simulation calculates temperature using `T = (2/3) * KE_avg / k`. This equation shows that temperature is a measure of the ___________ of the gas particles.
    a) Average potential energy.
    b) Total kinetic energy.
    c) Average kinetic energy.
    d) Total momentum.

3.  If you were to modify the simulation to double the mass of each particle but keep their initial speeds the same, what would be the immediate effect on the calculated temperature?
    a) It would be halved.
    b) It would remain the same.
    c) It would be doubled.
    d) It would be quadrupled.

4.  The simulation models perfectly elastic collisions with the walls. If the collisions were instead inelastic (particles lose energy when they hit the wall), what would you expect to happen to the temperature of the gas over time?
    a) It would increase.
    b) It would decrease.
    c) It would remain constant.
    d) It would fluctuate randomly.

5.  The code calculates the change in momentum for a particle hitting the right-hand wall as `2 * m * vx`. This is because the particle's momentum changes from `m*vx` to `m*(-vx)`. The change in momentum *delivered to the wall* is:
    a) Zero.
    b) `-2 * m * vx`
    c) `+2 * m * vx`
    d) `m * vx`

---
### Answer Key
**Conceptual:** 1. (b), 2. (c), 3. (b), 4. (c), 5. (d)
**Problem-Solving:** 1. (b), 2. (d), 3. (c), 4. (c), 5. (c)
**Computational:** 1. (b), 2. (c), 3. (c), 4. (b), 5. (c)