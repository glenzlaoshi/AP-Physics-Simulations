---
title: "3.1 - LR Circuit"
layout: default
---


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

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  An inductor in a circuit opposes changes in:
    a) Voltage.
    b) Resistance.
    c) Current.
    d) Charge.

2.  At the exact moment a switch is closed in a simple LR circuit (with a battery), the inductor acts like:
    a) A broken wire (infinite resistance).
    b) A simple wire (zero resistance).
    c) A capacitor.
    d) A battery.

3.  After the switch in an LR circuit has been closed for a very long time (`t >> τ`), the inductor acts like:
    a) A broken wire (infinite resistance).
    b) A simple wire (zero resistance).
    c) A capacitor.
    d) A battery.

4.  The time constant for an LR circuit is `τ = L/R`. If you double the inductance `L`, how does this affect the time it takes for the current to build up?
    a) It takes half the time.
    b) It takes the same amount of time.
    c) It takes twice as long.
    d) It takes four times as long.

5.  The energy in an inductor is stored in:
    a) Its electric field.
    b) Its magnetic field.
    c) Its resistive components.
    d) The moving charges themselves.

### Problem-Solving Questions

1.  The current in an LR circuit is given by `I(t) = I_max * (1 - e^(-t/τ))`. What is the voltage across the inductor `V_L(t)`?
    a) `V_L(t) = I_max * R * e^(-t/τ)`
    b) `V_L(t) = I_max * R * (1 - e^(-t/τ))`
    c) `V_L(t) = -L * I_max * e^(-t/τ)`
    d) `V_L(t) = L * I_max / τ * (1 - e^(-t/τ))`

2.  An LR circuit has a 12V battery, a 3 H inductor, and a 6 Ω resistor. What is the maximum possible current in the circuit?
    a) 0.5 A
    b) 2.0 A
    c) 4.0 A
    d) 72 A

3.  For the circuit in the previous question (L=3H, R=6Ω), what is the time constant `τ`?
    a) 0.5 s
    b) 2.0 s
    c) 18 s
    d) 0.17 s

4.  The current in an LR circuit is `I(t) = 4.0 * (1 - e^(-t/2.0)) A`. What is the initial rate of change of the current, `dI/dt` at `t=0`?
    a) 0 A/s
    b) 2.0 A/s
    c) 4.0 A/s
    d) 8.0 A/s

5.  An inductor with `L = 50 mH` has a current flowing through it given by `I(t) = 2t² + 3t`. What is the magnitude of the self-induced EMF `V_L` at `t = 2 s`?
    a) 0.25 V
    b) 0.40 V
    c) 0.55 V
    d) 0.70 V

### Computational Questions

1.  The simulation calculates the rate of change of current during the decay phase using `dI_dt = -I * R / L`. This is a rearrangement of which fundamental equation?
    a) `V = IR`
    b) `V = Q/C`
    c) `V_batt - IR - L(dI/dt) = 0`
    d) `-IR - L(dI/dt) = 0` (Kirchhoff's rule for the decay loop)

2.  The simulation updates the current using `I = I + dI_dt * dt`. This numerical integration method is known as:
    a) The analytical solution.
    b) Gauss's Law.
    c) Euler's method.
    d) The cross product.

3.  In the energizing phase, the initial value of `dI/dt` is `V_batt / L`. Why?
    a) Because at t=0, the current `I` is zero, so the `IR` term in the loop rule is zero.
    b) Because the resistance `R` is zero at the beginning.
    c) Because the inductance `L` is infinite at the beginning.
    d) Because the battery voltage is zero at the beginning.

4.  If you were to increase the resistance `R` in the simulation, how would this affect the time constant `τ` and the maximum current `I_max`?
    a) `τ` decreases, `I_max` decreases.
    b) `τ` decreases, `I_max` increases.
    c) `τ` increases, `I_max` decreases.
    d) `τ` increases, `I_max` increases.

5.  The simulation plots the current `I` versus time `t`. For the energizing phase, the initial slope of this graph should be ________, and the final slope should be ________.
    a) zero, maximum
    b) maximum, zero
    c) constant, constant
    d) zero, zero

---
### Answer Key
**Conceptual:** 1. (c), 2. (a), 3. (b), 4. (c), 5. (b)
**Problem-Solving:** 1. (a), 2. (b), 3. (a), 4. (b), 5. (c)
**Computational:** 1. (d), 2. (c), 3. (a), 4. (a), 5. (b)
