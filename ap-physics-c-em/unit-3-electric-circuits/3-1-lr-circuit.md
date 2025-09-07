---
title: "3.1 - LR Circuit"
layout: default
---
# Information: The LR Circuit

## 1. Introduction to the Unit: Circuits with Inductors

This unit introduces a new circuit component: the **inductor (`L`)**. While a capacitor stores energy in an electric field and opposes changes in **voltage**, an inductor stores energy in a **magnetic field** and opposes changes in **current**. 

Just as with RC circuits, adding an inductor to a circuit creates time-dependent behavior. The analysis of these circuits relies on applying Kirchhoff's Loop Rule, but now with a new term to account for the voltage across the inductor.

## 2. Relevant Physics Concepts

### Inductors and Self-Inductance

An inductor is typically a coil of wire. When current `I` flows through the coil, it generates a magnetic field `B` and thus a magnetic flux `ΦB` through the coil itself.

If the current attempts to change, the magnetic flux changes. By Faraday's Law of Induction, this changing flux induces an EMF (a voltage) in the coil. This phenomenon is called **self-inductance**. 

The direction of this self-induced EMF, according to Lenz's Law, is always such that it **opposes the change in current**. This makes an inductor a sort of "current inertia." The voltage across an inductor is given by:

`V_L = -L * (dI/dt)`

-   `L` is the inductance, a property of the coil measured in **Henrys (H)**.
-   `dI/dt` is the rate of change of the current.

### The LR Circuit: Energizing

Consider a series circuit with a battery (`V_batt`), a resistor (`R`), and an inductor (`L`). When the switch is closed, the current tries to increase from zero.

-   The inductor immediately creates a back-EMF `V_L` that opposes this increase, so the current does not jump to its maximum value instantly.
-   **Kirchhoff's Loop Rule:** `V_batt - V_resistor - V_inductor = 0`. Using the formulas for each component, this becomes: `V_batt - I*R - L*(dI/dt) = 0`.
-   Rearranging to find the rate of change of current gives: `dI/dt = (V_batt - I*R) / L`.
-   This equation shows that initially (`I=0`), the current grows fastest. As `I` increases, its rate of growth `dI/dt` slows down. The current asymptotically approaches a maximum value of `I_max = V_batt / R`.

### The LR Circuit: Decaying

If we now remove the battery and short the circuit, the magnetic field in the inductor starts to collapse. This collapse induces an EMF that tries to keep the current flowing.

-   The loop rule is now: `-I*R - L*(dI/dt) = 0`, or `-I*R - L*(dI/dt) = 0`.
-   The rate of change of current is: `dI/dt = -I*R / L`.
-   The current now decays exponentially from its maximum value down to zero.

### The Time Constant (`τ`)

The characteristic time for this energizing or decaying process is the **time constant, tau (`τ`)**.

`τ = L / R`

## 3. The Simulation: Current Buildup and Decay

### Outline of the Simulation

The `intermediate.py` file correctly models the **energizing phase** of an LR circuit. It uses the loop rule to calculate `dI/dt` and then numerically integrates to find the current `I` as it builds up over time. Your task is to add a second `while` loop to model the **de-energizing (decaying) phase**.

### Completing the `intermediate.py` File

Your task is to write a new `while` loop that continues after the first one finishes, modeling the decay of the current.

- **Example (The Loop Rule):** For the de-energizing phase, the battery is gone. The loop rule becomes `-I*R - L*(dI/dt) = 0`. The key physics is to solve this for the rate of change of current:
  `dI/dt = -I*R / L`

- **Your Task (dI/dt):** Inside your new `while` loop, write the line of code to calculate `dI_dt` based on the inductor's current `I` at that moment, the resistance `R`, and the inductance `L`.

- **Your Task (Update Current):** The change in current in a small time step is `dI = dI_dt * dt`. Write the line of code to update the total current `I` by adding this `dI` to it. Since `dI_dt` will be negative, this will correctly decrease the current.

- **Your Task (Plotting):** Add the `.plot()` command inside your new loop to continue drawing the `I_curve` during this decay phase.

When you run the completed code, you should see the classic exponential curve for an LR circuit: the current rises and flattens out, then decays back down to zero when the battery is removed.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CEM/program/3.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/06e0cd755e58" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>