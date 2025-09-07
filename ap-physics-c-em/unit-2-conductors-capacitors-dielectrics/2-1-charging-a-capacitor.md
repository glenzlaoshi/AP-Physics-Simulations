---
title: "2.1 - Charging a Capacitor"
layout: default
---


## 1. Introduction to the Unit: Electric Circuits

This unit introduces **electric circuits**: paths that allow electric current to flow. We will analyze circuits built from a few key components:
-   **Voltage Source (like a battery):** Provides the electromotive force (EMF), or "push," to move charges.
-   **Resistor (`R`):** A component that resists the flow of current. Governed by **Ohm's Law** (`V = IR`).
-   **Capacitor (`C`):** A component that stores charge and electric energy.

While circuits with only resistors and batteries are typically in a "steady state," the introduction of capacitors creates time-dependent behavior. The current and voltage in an RC circuit change over time as the capacitor charges or discharges.

## 2. Relevant Physics Concepts

### Capacitors

A capacitor stores an amount of charge `Q` that is proportional to the voltage `V` across it. The constant of proportionality is its capacitance, `C`.

`Q = C * V`  or, rearranged,  `V = Q / C`

This relationship is key: the voltage across a capacitor is determined by how much charge is currently stored on its plates.

### The RC Circuit: Charging

Imagine a series circuit with a battery (`V_batt`), a resistor (`R`), and an uncharged capacitor (`C`). When you close the switch, current begins to flow.

-   We can analyze this using **Kirchhoff's Loop Rule**: the sum of voltage changes around a closed loop must be zero.
    `V_batt - V_resistor - V_capacitor = 0`
-   Using Ohm's Law (`V_resistor = IR`) and the capacitor definition (`V_capacitor = Q/C`), we get:
    `V_batt - IR - Q/C = 0`
-   Solving for the current `I` at any instant gives:
    `I = (V_batt - Q/C) / R`

This equation tells a story: Initially, the capacitor is uncharged (`Q=0`), so the current is at its maximum (`I = V_batt / R`). As charge `Q` builds up on the capacitor, its voltage `Q/C` increases, which opposes the battery and causes the current `I` to decrease. The process stops when the capacitor is fully charged and the current becomes zero.

### The RC Circuit: Discharging

Now imagine we take the battery out and connect the charged capacitor directly to the resistor. The capacitor now acts as the voltage source.

-   The loop rule is simpler: `-V_resistor - V_capacitor = 0`, which means `V_capacitor = -V_resistor` (the voltage drop across the resistor is equal to the capacitor's voltage).
-   The current is now: `I = V_capacitor / R = (Q/C) / R`
-   As charge flows out of the capacitor, `Q` decreases, which causes `Vc` to decrease, which in turn causes the current `I` to decrease. Both the voltage and current decay exponentially to zero.

### The Time Constant (`τ`)

The speed of the charging or discharging process is characterized by the **time constant, tau (`τ`)**.

`τ = R * C`

In one time constant, a capacitor charges to about 63% of its maximum voltage, or discharges down to about 37% of its initial voltage.

## 3. The Simulation: Charging and Discharging

### Outline of the Simulation

The `intermediate.py` file correctly models the **charging phase** of the RC circuit. It uses the loop rule to calculate the current at each time step, updates the charge on the capacitor, and plots the results. Your task is to add a second `while` loop to model the **discharging phase** that happens after the battery is removed.

### Completing the `intermediate.py` File

#### **Implementing the Discharging Phase**

Your task is to write a new `while` loop that continues where the first one left off. Inside this loop, you must model the physics of the discharging capacitor.

- **Example (The Loop Rule):** For the discharging phase, the battery is gone. The current is now driven only by the capacitor's own voltage. The relationship is `I = Vc / R`. The code to calculate the capacitor's voltage, `Vc = Q / C`, is the same as before.

- **Your Task (Current):** Inside your new `while` loop, write the line of code to calculate the current `I`. It should be based on the capacitor's current voltage `Vc` and the resistance `R`.

- **Your Task (Charge Update):** During discharging, the capacitor is *losing* charge. The amount of charge that flows out in a small time step is `dQ = I * dt`. Write the line of code to **subtract** this `dQ` from the total charge `Q` stored on the capacitor.

- **Your Task (Plotting):** To see the results, you must add the `.plot()` commands inside your new loop. Write the two lines to plot the `Vc` and `I` values on their respective curves (`Vc_curve` and `I_curve`).

When you run the completed code, you should see the classic exponential curves: voltage and current rise during charging, and then both decay exponentially during discharging.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-CEM/program/2.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/05c9ca4635e8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>