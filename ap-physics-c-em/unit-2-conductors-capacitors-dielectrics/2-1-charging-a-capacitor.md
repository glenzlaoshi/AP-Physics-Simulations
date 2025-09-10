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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The current in a charging RC circuit is given by `I(t) = I_0 * e^(-t/τ)`. What does the initial current `I_0` represent?
    a) The current after one time constant.
    b) The final, steady-state current.
    c) The current through the capacitor only.
    d) The current at the moment the switch is closed (t=0).

2.  For a charging RC circuit, the differential equation derived from Kirchhoff's loop rule is `V_batt - R(dQ/dt) - Q/C = 0`. What does the term `R(dQ/dt)` represent?
    a) The voltage across the capacitor.
    b) The voltage across the resistor.
    c) The total energy stored in the circuit.
    d) The time constant.

3.  After a capacitor has been charging for a very long time (`t >> τ`), the current in the circuit approaches zero. Why?
    a) The battery has run out of energy.
    b) The resistor has dissipated all the energy.
    c) The voltage across the capacitor becomes equal and opposite to the battery's EMF, opposing further current flow.
    d) The capacitance increases to infinity.

4.  The time constant `τ = RC` determines the rate of charging. A larger time constant means:
    a) The capacitor charges more quickly.
    b) The capacitor charges more slowly.
    c) The final charge on the capacitor is greater.
    d) The initial current is greater.

5.  During the discharging of an RC circuit, the rate at which the charge leaves the capacitor (`-dQ/dt`) is:
    a) Constant.
    b) Directly proportional to the resistance `R`.
    c) Directly proportional to the charge `Q` remaining on the capacitor.
    d) Inversely proportional to the time constant `τ`.

### Problem-Solving Questions

1.  The charge on a charging capacitor is given by `Q(t) = C*V_batt*(1 - e^(-t/RC))`. What is the expression for the current `I(t)`?
    a) `I(t) = C*V_batt * e^(-t/RC)`
    b) `I(t) = (V_batt/R) * e^(-t/RC)`
    c) `I(t) = V_batt / R`
    d) `I(t) = - (V_batt / R) * t * e^(-t/RC)`

2.  An RC circuit has R = 1000 Ω and C = 400 μF. If the circuit is charged with a 12 V battery, what is the current at `t = 0.4` seconds? (Note: `τ = 0.4 s`)
    a) 12 mA
    b) 7.6 mA
    c) 4.4 mA
    d) 0 A

3.  A 50 μF capacitor is discharged through a 200 Ω resistor. The charge on the capacitor as a function of time is `Q(t) = Q_0 * e^(-t/0.01)`. What is the current in the circuit at t = 0.02 s?
    a) `I = -Q_0 * (100) * e^(-2)`
    b) `I = -Q_0 * (0.01) * e^(-2)`
    c) `I = Q_0 * e^(-2)`
    d) `I = -Q_0 * e^(-2)`

4.  At what time, in terms of the time constant `τ`, will the charge on a charging capacitor reach 90% of its maximum value?
    a) `t = -τ * ln(0.9)`
    b) `t = τ * ln(0.1)`
    c) `t = -τ * ln(0.1)`
    d) `t = τ`

5.  The energy stored in a capacitor is `U = Q²/ (2C)`. What is the rate at which energy is being stored in a charging capacitor (`dU/dt`) as a function of current `I` and charge `Q`?
    a) `I*Q / C`
    b) `I²R`
    c) `I*Q / (2C)`
    d) `Q/C`

### Computational Questions

1.  The simulation calculates the current at each time step using `I = (V_batt - Vc) / R`. This algebraic expression is a direct representation of:
    a) The solution to the RC circuit differential equation.
    b) The RC circuit differential equation itself, rearranged.
    c) The definition of capacitance.
    d) The formula for the time constant.

2.  The simulation updates the charge using `Q = Q + I * dt`. This is a numerical approximation of which calculus relationship?
    a) `I = dQ/dt`
    b) `V = IR`
    c) `Q = CV`
    d) `τ = RC`

3.  In the discharging phase, the current is calculated as `I = Vc / R`. If you were to write the full differential equation for this phase, it would be:
    a) `R(dQ/dt) + Q/C = V_batt`
    b) `R(dQ/dt) + Q/C = 0`
    c) `R(dQ/dt) - Q/C = 0`
    d) `dQ/dt = -Q`

4.  If you decrease the time step `dt` in the simulation, how will this affect the accuracy of the numerical solution?
    a) The accuracy will decrease.
    b) The accuracy will not change.
    c) The accuracy will increase, providing a result closer to the true exponential curve.
    d) The simulation will run faster but be less accurate.

5.  The simulation plots the voltage across the capacitor, `Vc`. According to the charging equation `Vc(t) = V_batt*(1 - e^(-t/τ))`, the initial slope of this graph at t=0 should be:
    a) Zero.
    b) `V_batt / τ`
    c) `V_batt`
    d) Infinite.

---
### Answer Key
**Conceptual:** 1. (d), 2. (b), 3. (c), 4. (b), 5. (c)
**Problem-Solving:** 1. (b), 2. (c), 3. (a), 4. (c), 5. (a)
**Computational:** 1. (b), 2. (a), 3. (b), 4. (c), 5. (b)
