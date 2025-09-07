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