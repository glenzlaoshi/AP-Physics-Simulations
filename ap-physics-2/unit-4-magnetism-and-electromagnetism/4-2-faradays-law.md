---
title: "4.2 - Faraday's Law"
layout: default
---


## 1. Introduction to the Unit: Electromagnetism

This topic unifies the concepts of electricity and magnetism into **electromagnetism**. We have seen that moving charges (currents) create magnetic fields. The brilliant discovery by Michael Faraday was that the reverse is also true, but with a twist: a **changing** magnetic field can create an electric current.

This phenomenon is called **electromagnetic induction**, and it is the operating principle behind electric generators, transformers, and many other modern technologies. It reveals a deep and fundamental connection between electric and magnetic fields: a change in one can create the other.

## 2. Relevant Physics Concepts

### Magnetic Flux (`ΦB`)

Just as electric flux was a measure of the amount of electric field passing through an area, **magnetic flux** is a measure of the amount of magnetic field passing through a loop of wire.

`ΦB = B_perp * A = B * A * cos(θ)`

-   `B` is the magnitude of the magnetic field.
-   `A` is the area of the loop.
-   `θ` is the angle between the magnetic field `B` and the normal (perpendicular) direction to the area `A`.

To induce a current, the magnetic flux through the loop must be **changing**.

### Faraday's Law of Induction

This is the key law of induction. It states that the induced electromotive force (EMF, which is essentially a voltage) in a wire loop is equal to the negative of the **rate of change of the magnetic flux** through it.

`EMF = -N * (dΦB / dt)`

-   `N` is the number of turns in the coil of wire.
-   `dΦB / dt` is the rate at which the magnetic flux is changing over time.

This means you can create a voltage (and thus a current, if the loop is a closed circuit) by changing the magnetic field strength, changing the area of the loop, or changing the angle between the loop and the field. In our simulation, we will change the flux by moving a magnet closer to and farther away from the coil.

### Lenz's Law

What does the negative sign in Faraday's Law mean? It represents **Lenz's Law**, which tells us the direction of the induced current. Lenz's Law states:

**The direction of the induced current will be such that the magnetic field it creates opposes the change in magnetic flux.**

This is a statement of conservation of energy—nature's way of saying "you can't get something for nothing." 
-   If the magnetic flux through a loop is increasing, the induced current will create its own magnetic field in the opposite direction to fight the increase.
-   If the magnetic flux is decreasing, the induced current will create its own magnetic field in the same direction to try to keep the flux from dropping.

## 3. The Simulation: A Magnet and a Coil

### Outline of the Simulation

The `intermediate.py` file shows a bar magnet moving towards a coil of wire. The code already calculates the magnetic flux (`flux_new`) through the coil at each time step by approximating the magnet's field. Your task is to use the rate of change of this flux to calculate the induced EMF in the coil according to Faraday's Law.

### Completing the `intermediate.py` File

Your task is to calculate the `EMF` inside the animation loop.

- **Example (Change in Flux):** To find the rate of change, `dΦB / dt`, we first need to find the change in flux between one time step and the next, `dΦB`. The code to do this is given as an example. It uses a variable `flux_old` to remember the flux from the previous step.
  ```python
  dFlux = flux_new - flux_old
  ```

- **Your Task (Calculate EMF):** Now, apply Faraday's Law, `EMF = -N * (dΦB / dt)`. You can approximate the rate of change `dΦB / dt` as `dFlux / dt`. Write the line of code to calculate the `EMF` using `N`, `dFlux`, and the time step `dt`. Remember to include the crucial negative sign from the formula.

- **Your Task (Plot EMF):** The simulation has a graph already set up. Add the line of code to plot the `EMF` you just calculated versus time `t` on the `emf_curve`.

- **Your Task (Update `flux_old`):** At the very end of the loop, you must prepare for the next calculation. The flux that is "new" in this step will be "old" in the next one. Write the line of code that updates the value of `flux_old` to be equal to `flux_new`.

When you run the code, you should see that an EMF is generated only when the flux is changing. It will be positive when the magnet moves one way, and negative when it moves the other way.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/4.2-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/3042f67faf23" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  A current can be induced in a closed loop of wire by:
    a) A constant magnetic field.
    b) A changing magnetic field.
    c) A constant electric field.
    d) A stationary charge.

2.  Lenz's Law is a consequence of the conservation of:
    a) Charge.
    b) Mass.
    c) Momentum.
    d) Energy.

3.  A bar magnet is pushed towards a loop of wire with its North pole facing the loop. The induced current in the loop will create a magnetic field with a North pole that:
    a) Points towards the bar magnet to attract it.
    b) Points towards the bar magnet to repel it.
    c) Points perpendicular to the bar magnet's motion.
    d) Is zero.

4.  Which of the following actions will NOT induce a current in a loop of wire?
    a) Rotating the loop in a uniform magnetic field.
    b) Changing the area of the loop in a uniform magnetic field.
    c) Moving the loop at a constant velocity through a uniform magnetic field.
    d) Moving a magnet closer to the loop.

5.  A wire loop is in a uniform magnetic field. The magnetic flux through the loop is at a maximum when the angle between the magnetic field and the normal to the loop's area is:
    a) 0 degrees.
    b) 45 degrees.
    c) 90 degrees.
    d) 180 degrees.

### Problem-Solving Questions

1.  A square loop of wire with a side length of 0.2 m is in a uniform magnetic field of 1.5 T that is perpendicular to the loop. What is the magnetic flux through the loop?
    a) 0.03 Wb
    b) 0.06 Wb
    c) 0.3 Wb
    d) 1.5 Wb

2.  The magnetic flux through a coil of 100 turns changes from 0.02 Wb to 0.07 Wb in 0.5 seconds. What is the magnitude of the induced EMF in the coil?
    a) 1 V
    b) 5 V
    c) 10 V
    d) 14 V

3.  A circular loop of wire with a radius of 0.1 m is in a magnetic field that is increasing at a rate of 0.5 T/s. The field is perpendicular to the loop. What is the magnitude of the induced EMF?
    a) 0.005 V
    b) 0.016 V
    c) 0.031 V
    d) 0.05 V

4.  A magnet is dropped through a vertical copper ring. As the magnet passes through the ring, the induced current will:
    a) Always be in the same direction.
    b) Be in one direction as the magnet approaches and the opposite direction as it leaves.
    c) Be zero because the ring is not a complete circuit.
    d) Be zero because gravity is not a magnetic force.

5.  A 50-turn coil has a magnetic flux of `ΦB = (0.1t² + 0.05t)` through it, where t is in seconds. What is the magnitude of the induced EMF at t = 2 s?
    a) 2.5 V
    b) 22.5 V
    c) 45 V
    d) 50 V

### Computational Questions

1.  The simulation calculates the induced EMF using `EMF = -N * dFlux / dt`. This is a direct implementation of:
    a) Coulomb's Law.
    b) Ohm's Law.
    c) Faraday's Law of Induction.
    d) The Lorentz Force Law.

2.  In the simulation, `dFlux` is calculated as `flux_new - flux_old`. This represents:
    a) The total magnetic flux.
    b) The change in magnetic flux between two consecutive time steps.
    c) The average magnetic flux.
    d) The magnetic field strength.

3.  Why is an EMF only generated in the simulation when the magnet is moving?
    a) Because the magnet's charge is only active when moving.
    b) Because the magnetic flux (`ΦB`) is only changing when the magnet's position changes.
    c) Because the number of turns `N` is zero when the magnet is stationary.
    d) This is a flaw; an EMF should always be present.

4.  The simulation code must update the variable `flux_old = flux_new` at the end of the loop. What is the purpose of this line?
    a) To calculate the total flux.
    b) To prepare for the calculation of `dFlux` in the *next* iteration of the loop.
    c) To set the flux to zero.
    d) To convert the flux to a different unit.

5.  If you were to reverse the direction of the magnet's velocity in the simulation, what would happen to the induced EMF?
    a) It would become zero.
    b) Its magnitude would double.
    c) Its sign would flip.
    d) It would remain exactly the same.

---
### Answer Key
**Conceptual:** 1. (b), 2. (d), 3. (b), 4. (c), 5. (a)
**Problem-Solving:** 1. (b), 2. (c), 3. (b), 4. (b), 5. (b)
**Computational:** 1. (c), 2. (b), 3. (b), 4. (b), 5. (c)
