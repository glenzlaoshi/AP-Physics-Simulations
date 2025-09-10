---
title: "2.2 - Atwood Machine"
layout: default
---

## 1. Introduction to the Unit: Dynamics of Systems

This simulation builds on the core concepts of Dynamics (`F_net = m*a`). So far, we have analyzed single objects. However, many real-world scenarios involve multiple objects whose motions are connected or constrained. We call these **systems**.

An Atwood machine is a classic, simple system consisting of two masses connected by a string that passes over a pulley. Because they are connected, the motion of one mass directly affects the motion of the other. To solve for the motion of the system, we must analyze the forces on *each* mass individually and then combine their equations based on the constraint that links them.

## 2. Relevant Physics Concepts

### Tension (`T`)

Tension is the pulling force exerted by a string or rope. For the purposes of this problem, we make a few key assumptions about the string and pulley:
- The string is **massless** and does not stretch.
- The pulley is **massless** and **frictionless**.
- Under these assumptions, the tension force `T` is the **same** at all points along the string.

### Analyzing the Forces on Each Mass

Let's assume `m2` is heavier than `m1`.

- **Free-Body Diagram for `m1`:** There are two forces: `T` pulling up, and `m1*g` pulling down. The net force is `F_net1 = T - m1*g`.
- **Free-Body Diagram for `m2`:** There are two forces: `T` pulling up, and `m2*g` pulling down. The net force is `F_net2 = T - m2*g`.

### The Constraint

The string connects the two masses. This imposes a critical **constraint** on their motion: their accelerations must be equal in magnitude and opposite in direction. If `m1` accelerates upwards with `+a`, then `m2` must accelerate downwards with `-a`.

### Solving for the System's Acceleration

We can now use `F_net = m*a` for each block:
1.  `T - m1*g = m1*a`
2.  `T - m2*g = m2*(-a)`  which can be rewritten as `m2*g - T = m2*a`

This gives us two equations and two unknowns (`T` and `a`). By adding the two equations together, we can eliminate `T` and solve for `a`:

`(m2*g - T) + (T - m1*g) = m2*a + m1*a`
`g * (m2 - m1) = a * (m1 + m2)`

This gives the key result for the acceleration of the system:
**`a = g * (m2 - m1) / (m1 + m2)`**

## 3. The Simulation: Modeling the Motion

### Outline of the Simulation

The `skeleton.py` file shows two blocks (`mass1` and `mass2`) connected by strings over a pulley. Your goal is to use the formula for the system's acceleration to predict and model the motion of the blocks.

### Completing the `skeleton.py` File

#### **Task 3: Calculate Acceleration**

- **Example (Magnitude):** The main physics task is to calculate the magnitude of the system's acceleration. The formula we derived above is the key. The code to do this is:
  ```python
  a_mag = g * (mass2.m - mass1.m) / (mass1.m + mass2.m)
  ```
- **Your Task (Vectors):** The variable `a_mag` is just a number (a scalar). You need to create the full acceleration *vectors* for each block. Remember that `mass1` (the lighter one) accelerates up, while `mass2` (the heavier one) accelerates down. Write the two lines of code that set the `mass1.acceleration` and `mass2.acceleration` vector properties.

#### **Task 4: Update Motion**

Once you have the correct, constant acceleration vectors for each block, the rest of the simulation is a standard kinematics update. Inside the `while` loop, you need to update the motion for **both** blocks.

- **Your Task:** For `mass1`, write the two lines of code to update its `velocity` and `pos` properties using the standard numerical integration technique.
- **Your Task:** Do the same for `mass2`.
- **Your Task:** The skeleton file also includes lines to update the `string` visuals so they stay attached to the blocks. Make sure to uncomment these as well.

## 4. Completed Simulation

This is the final, working simulation. You can run it here to see the expected outcome.

<div id="glowscript" class="glowscript">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link type="text/css" href="https://www.glowscript.org/css/redmond/2.1/jquery-ui.custom.css" rel="stylesheet" />
<link type="text/css" href="https://www.glowscript.org/css/ide.css" rel="stylesheet" />
<script type="text/javascript" src="https://www.glowscript.org/lib/jquery/2.1/jquery.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/lib/jquery/2.1/jquery-ui.custom.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/package/glow.3.2.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/package/RSrun.3.2.min.js"></script>
<script type="text/javascript"><!--//--><![CDATA[//><!--
!function(){var o={};async function t(){"use strict";canvas;var t,e,i,l,s,r,a,c,n,p,f,y,m,u,d,h,v,_=canvas();for(t=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(o){return this.concat(o)},Array.prototype["*"]=function(o){return __array_times_number(this,o)},window.__GSlang="vpython",e=GSprint,i=range,l="__main__",s=pytype,(0,o.pythonize.strings)(),_.title="Atwood Machine",_.caption="Two masses are connected by a string over a frictionless pulley.",r=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({pos:vector(0,5,0),axis:vector(0,0,1),radius:.5,color:color.gray(.7)})]),a=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(1["-u"]()["*"](2),3,0),size:vector(1,1,1),color:color.red})]),c=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(2,1,0),size:vector(1,1,1),color:color.blue})]),n=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({radius:.05,color:color.yellow})]),p=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({radius:.05,color:color.yellow})]),f=0,y=.01,m=9.8,a.m=4,c.m=4.5,e("Mass 1 (red): "["+"](ρσ_str.format("{}",a.m))["+"](" kg")),e("Mass 2 (blue): "["+"](ρσ_str.format("{}",c.m))["+"](" kg")),u=m["*"](c.m["-"](1["*"](a.m)))["/"](a.m["+"](c.m)),e("Theoretical acceleration: "["+"](ρσ_str.format("{:.2f}",u))["+"](" m/s^2")),a.acceleration=vector(0,u,0),c.acceleration=vector(0,1["-u"]()["*"](u),0),a.velocity=vector(0,0,0),c.velocity=vector(0,0,0),d=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Position vs. Time",xtitle:"Time (s)",ytitle:"Height (m)"})]),h=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:a.color,label:"Mass 1 ("["+"](ρσ_str.format("{}",a.m))["+"](" kg)")})]),v=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:c.color,label:"Mass 2 ("["+"](ρσ_str.format("{}",c.m))["+"](" kg)")})]);f["<"](3.5);)await rate(100),a.velocity=a.velocity["+"](a.acceleration["*"](y)),c.velocity=c.velocity["+"](c.acceleration["*"](y)),a.pos=a.pos["+"](a.velocity["*"](y)),c.pos=c.pos["+"](c.velocity["*"](y)),n.pos=a.pos["+"](vector(0,.5,0)),n.axis=vector(0,5,0)["-"](n.pos),p.pos=c.pos["+"](vector(0,.5,0)),p.axis=vector(0,5,0)["-"](p.pos),f=f["+"](y),h.plot(f,a.pos.y),v.plot(f,c.pos.y);e("Simulation finished.")}t()["catch"](function(t){o.browser_send_error(t)})}();
//--><!]]>
</script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/e9ed02e66edf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  In an ideal Atwood machine (massless, frictionless pulley and string), how does the tension in the string connecting the two masses compare on either side of the pulley?
    a) The tension is greater on the side with the heavier mass.
    b) The tension is greater on the side with the lighter mass.
    c) The tension is the same on both sides.
    d) The tension is zero.

2.  If the two masses in an Atwood machine are equal (`m1 = m2`), what will be the acceleration of the system?
    a) g (9.8 m/s²)
    b) g / 2
    c) Zero.
    d) It depends on the value of the masses.

3.  A simple Atwood machine has masses `m1` and `m2`, with `m2 > m1`. What is the net force on the *entire system* of two masses?
    a) `(m1 + m2) * g`
    b) `(m2 - m1) * g`
    c) `(m1 + m2) * a`
    d) `T - m1*g`

4.  In an Atwood machine with `m2 > m1`, the tension `T` in the string is:
    a) Equal to `m1*g`.
    b) Greater than `m1*g` but less than `m2*g`.
    c) Equal to `m2*g`.
    d) Greater than `m2*g`.

5.  If you take an Atwood machine to the Moon, where the acceleration due to gravity is about 1/6th of Earth's, how will the acceleration of the system change compared to on Earth?
    a) It will be the same.
    b) It will be 6 times larger.
    c) It will be 1/6th as large.
    d) It will be zero.

### Problem-Solving Questions

1.  An Atwood machine consists of a 3 kg mass and a 5 kg mass. What is the magnitude of the acceleration of the system? (Use g = 9.8 m/s²)
    a) 1.23 m/s²
    b) 2.45 m/s²
    c) 4.9 m/s²
    d) 9.8 m/s²

2.  Using the same masses from the previous question (3 kg and 5 kg), what is the tension in the string?
    a) 29.4 N
    b) 36.8 N
    c) 49.0 N
    d) 78.4 N

3.  A 10 kg mass and a 15 kg mass are connected in an Atwood machine. How long will it take for the 15 kg mass to fall 2 meters, starting from rest? (Use g = 9.8 m/s²)
    a) 0.45 s
    b) 1.01 s
    c) 1.43 s
    d) 2.02 s

4.  In an Atwood machine, a mass `m1 = 2 kg` accelerates upwards at 2.0 m/s². What is the mass of `m2`? (Use g = 9.8 m/s²)
    a) 2.0 kg
    b) 2.5 kg
    c) 3.0 kg
    d) 3.5 kg

5.  An Atwood machine has an acceleration of `a = g/4`. What is the ratio of the two masses (`m2/m1`, assuming `m2` is the heavier mass)?
    a) 3/2
    b) 5/3
    c) 2
    d) 4

### Computational Questions

1.  In the simulation code, the acceleration is calculated as `a_mag = g * (mass2.m - mass1.m) / (mass1.m + mass2.m)`. Why is the difference of the masses in the numerator?
    a) It represents the total mass of the system.
    b) It represents the net force that causes the system to accelerate.
    c) It is a typo and should be the sum.
    d) To ensure the acceleration is always positive.

2.  The code sets `mass1.acceleration = vector(0, a_mag, 0)` and `mass2.acceleration = vector(0, -a_mag, 0)`. This is a direct implementation of which physical concept?
    a) Newton's Third Law.
    b) The conservation of energy.
    c) The constraint that the masses are connected and move together.
    d) The definition of tension.

3.  If you were to run the simulation with `mass1.m = 5` and `mass2.m = 5`, what would `a_mag` be, and what would you observe?
    a) `a_mag` would be 9.8, and the blocks would accelerate rapidly.
    b) `a_mag` would be 0, and the blocks would not move.
    c) The program would crash due to division by zero.
    d) `a_mag` would be negative, and the blocks would move in the wrong direction.

4.  The simulation updates the velocity of each block separately (e.g., `mass1.velocity = mass1.velocity + mass1.acceleration * dt`). Why is it not necessary to include tension in this part of the code?
    a) Because tension is not a real force.
    b) Because the effect of tension was already used to calculate the acceleration.
    c) Because the string is massless.
    d) Because the pulley is frictionless.

5.  What would happen if you mistakenly set both acceleration vectors to be positive: `mass1.acceleration = vector(0, a_mag, 0)` and `mass2.acceleration = vector(0, a_mag, 0)`?
    a) The simulation would appear correct, as `a_mag` is the same for both.
    b) Both blocks would accelerate upwards, and the string would appear to stretch.
    c) The blocks would accelerate in opposite directions as expected.
    d) The simulation would produce an error.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (b), 4. (b), 5. (c)
**Problem-Solving:** 1. (b), 2. (b), 3. (c), 4. (c), 5. (b)
**Computational:** 1. (b), 2. (c), 3. (b), 4. (b), 5. (b)