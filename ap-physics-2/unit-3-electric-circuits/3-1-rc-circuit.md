---
title: "3.1 - RC Circuit"
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

<iframe src="https://glowscript.org/#/user/cglenz/folder/APSimulations-2/program/3.1-complete.py" width="320" height="340"></iframe>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/37de0b54f79f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  In a simple RC circuit that is charging, what is the current in the circuit at the exact moment the switch is closed (t=0)?
    a) Zero.
    b) At its maximum value, `V_batt / R`.
    c) Half of its maximum value.
    d) It depends on the capacitance.

2.  After a charging RC circuit has been connected for a very long time (many time constants), what is the voltage across the capacitor?
    a) Zero.
    b) Half the battery voltage.
    c) Equal to the battery voltage.
    d) It depends on the resistance.

3.  When a fully charged capacitor is discharged through a resistor, the current in the circuit:
    a) Is constant until the capacitor is fully discharged.
    b) Increases over time.
    c) Decreases exponentially over time.
    d) Is always zero.

4.  The time constant (`τ = RC`) of an RC circuit represents the time it takes for a charging capacitor's voltage to reach approximately what percentage of the battery voltage?
    a) 37%
    b) 50%
    c) 63%
    d) 100%

5.  If you increase the resistance in a discharging RC circuit, how does this affect the time it takes for the capacitor to discharge?
    a) It discharges faster.
    b) It discharges slower.
    c) It has no effect on the discharge time.
    d) It depends on the initial voltage.

### Problem-Solving Questions

1.  What is the time constant of a circuit with a 100 Ω resistor and a 50 μF capacitor?
    a) 0.002 s
    b) 0.005 s
    c) 0.5 s
    d) 2.0 s

2.  A 10 V battery is connected to a 5 Ω resistor and an uncharged 2 F capacitor. What is the initial current in the circuit when the switch is closed?
    a) 0.5 A
    b) 2.0 A
    c) 10 A
    d) 50 A

3.  A capacitor is charged to 12 V and then connected to a resistor. After one time constant has passed, what is the approximate voltage across the capacitor?
    a) 0 V
    b) 4.4 V
    c) 6.0 V
    d) 7.6 V

4.  A 20 μF capacitor is charged to hold 400 μC of charge. What is the voltage across the capacitor?
    a) 0.05 V
    b) 8 V
    c) 20 V
    d) 8000 V

5.  In a charging RC circuit with a 9V battery, the voltage across the resistor is measured to be 3V at a certain instant. What is the voltage across the capacitor at that same instant?
    a) 3 V
    b) 6 V
    c) 9 V
    d) 12 V

### Computational Questions

1.  In the simulation of a charging circuit, the current is calculated as `I = (V_batt - Vc) / R`. This is a direct application of:
    a) Ohm's Law alone.
    b) The capacitor charge equation `Q=CV`.
    c) Kirchhoff's Loop Rule.
    d) The definition of the time constant.

2.  For the discharging phase, the current is calculated as `I = Vc / R`. Why is the `V_batt` term missing from this equation?
    a) Because the battery has been removed from the circuit for the discharging phase.
    b) Because the resistor's value has changed.
    c) It is a mistake in the simulation logic.
    d) Because the current is flowing in the opposite direction.

3.  The simulation updates the charge on the capacitor during discharging using `Q = Q - I * dt`. Why is the `I*dt` term subtracted?
    a) To make the simulation run faster.
    b) Because the current is negative.
    c) Because charge is flowing *out of* the capacitor, decreasing its total stored charge.
    d) Because the voltage is decreasing.

4.  If you were to double the capacitance `C` in the simulation, how would this affect the time constant `τ` and the initial charging current `I_initial`?
    a) `τ` would double, `I_initial` would be halved.
    b) `τ` would be halved, `I_initial` would double.
    c) `τ` would double, `I_initial` would be unchanged.
    d) `τ` would be unchanged, `I_initial` would be halved.

5.  The simulation plots `Vc` (voltage across the capacitor) and `I` (current) versus time. For the charging phase, the `Vc` curve should ________ and the `I` curve should ________.
    a) increase exponentially, decrease exponentially
    b) decrease exponentially, increase exponentially
    c) remain constant, decrease linearly
    d) increase linearly, remain constant

---
### Answer Key
**Conceptual:** 1. (b), 2. (c), 3. (c), 4. (c), 5. (b)
**Problem-Solving:** 1. (b), 2. (b), 3. (b), 4. (c), 5. (b)
**Computational:** 1. (c), 2. (a), 3. (c), 4. (c), 5. (a)
