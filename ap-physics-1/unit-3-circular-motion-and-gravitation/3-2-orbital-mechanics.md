---
title: "3.2 - Orbital Mechanics"
layout: default
---


## 1. Introduction to the Unit: Gravitation

This topic is a perfect, real-world application of the principles of uniform circular motion. The force that keeps a satellite or a planet in its orbit is **gravity**. By understanding Newton's Law of Universal Gravitation, we can determine exactly how fast a satellite must travel to stay in a stable orbit.

In this unit, we see that the centripetal force (`Fc`) required to keep an object in a circular path is not a new force, but is in fact being **provided by** the gravitational force (`Fg`). By setting these two equal to each other, we can unlock the physics of orbital motion.

## 2. Relevant Physics Concepts

### Newton's Law of Universal Gravitation

Every object with mass in the universe attracts every other object with mass. The magnitude of this gravitational force is given by:

`Fg = G * (M * m) / r²`

-   `G` is the Universal Gravitational Constant (`6.67e-11 N·m²/kg²`).
-   `M` and `m` are the masses of the two objects.
-   `r` is the distance between the centers of the two objects.

The force is always attractive and acts along the line connecting the two objects.

### Orbital Speed for a Circular Orbit

For a satellite of mass `m` to have a stable circular orbit around a planet of mass `M`, the gravitational force must be providing the exact amount of centripetal force required.

-   Centripetal Force required: `Fc = m * v² / r`
-   Gravitational Force provided: `Fg = G * M * m / r²`

Setting them equal: `Fc = Fg`

`m * v² / r = G * M * m / r²`

Notice that the mass of the satellite (`m`) cancels from both sides! This means the required orbital speed does not depend on how heavy the satellite is. Solving for `v`, we get the speed required for a circular orbit:

**`v = sqrt(G * M / r)`**

### Types of Orbits

-   If a satellite's speed is exactly `v = sqrt(G*M/r)`, it will have a **perfectly circular orbit**.
-   If its speed is **less** than this value, gravity will be stronger than the required centripetal force, and the satellite will be pulled inwards in a decaying spiral.
-   If its speed is **greater** than this value, it will have enough energy to move further away from the planet, resulting in an **elliptical orbit**.

## 3. The Simulation: Satellite in Orbit

### Outline of the Simulation

The `skeleton.py` file shows a satellite in space near a larger planet. Your goal is to calculate the force of gravity acting on the satellite and use it to model the satellite's orbital path. Because the distance `r` and the direction of the force can change (especially in non-circular orbits), the force must be recalculated inside the animation loop.

### Completing the `skeleton.py` File

#### **Task 1: Set Initial Velocity**

To achieve a stable circular orbit, the satellite must start with a very specific tangential velocity. Your first task is to calculate this speed using the formula derived above.

- **Your Task:** Calculate the required speed, `v_circular`, using the formula `v = sqrt(G * M / r)`. The code provides all the necessary variables (`G`, `planet.m`, and `radius`).
- **Your Task:** Once you have the speed, you must create the initial velocity *vector*. The velocity must be tangential to the orbit. If the satellite starts on the positive x-axis, this tangential velocity will be in the positive y-direction. Write the line of code to set `satellite.velocity`.

#### **Task 2: Calculate Gravitational Force**

This must be done *inside* the `while` loop.

- **Example (The `r` vector):** The force calculation depends on the vector `r` that points from the object being pulled (the satellite) to the object doing the pulling (the planet). The code for this is given as an example:
  ```python
  r_vector = planet.pos - satellite.pos
  ```
- **Your Task (Magnitude and Direction):** From `r_vector`, you need two things: its magnitude (`r_mag`) and its direction (`r_hat`). Write the two lines of code to calculate these using the VPython functions `mag()` and `norm()`.
- **Your Task (Force Vector):** Now, calculate the magnitude of the gravitational force, `F_mag`, using Newton's Law of Gravitation. Then, combine the magnitude with the direction unit vector `r_hat` to get the final force vector, `F_gravity`.

#### **Task 3: Update Motion**

- **Your Task:** This part should be familiar. Once you have the net force (`F_gravity`), you must use it to find the satellite's acceleration (`a = F/m`). Remember to use the satellite's mass, `satellite.m`.
- **Your Task:** After finding the acceleration, write the two standard lines of code to update the `satellite.velocity` and `satellite.pos` over the time step `dt`.

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
!function(){var t={};async function e(){"use strict";canvas;var e,i,o,a,r,n,l=canvas();async function s(t){n=!n}async function p(t,e){var o,a,r,s,p,c,u,f,m,d,y,v,h,w;for(l.title="Orbital Mechanics Demonstration",l.caption="Current Simulation: "["+"](ρσ_str.format("{}",e))["+"](""),o=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(0,0,0),radius:1e6,color:color.blue})]),a=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(5e6,0,0),radius:3e5,color:color.yellow,make_trail:!0})]),r=ρσ_interpolate_kwargs.call(this,label,[ρσ_desugar_kwargs({pos:a.pos["+"](vector(0,1e6,0)),text:e,box:!1,opacity:0})]),s=0,p=5,c=667e-13,o.m=6e24,a.m=1e3,u=mag(a.pos),f=sqrt(c["*"](o.m)["/"](u)),a.velocity=vector(0,f["*"](t),0),i("\n--- Running: "["+"](ρσ_str.format("{}",e))["+"](" ---")),i("Initial speed: "["+"](ρσ_str.format("{:.2f}",mag(a.velocity)))["+"](" m/s")),m=2["*"](pi)["*"](u)["/"](f);s["<"](m["*"](1.5))&&mag(a.pos)[">"](o.radius)&&mag(a.pos)["<"](2.5["*"](u));)await rate(500),n&&(y=mag(d=o.pos["-"](1["*"](a.pos))),v=norm(d),w=(h=c["*"](o.m)["*"](a.m)["/"](Math.pow(y,2)))["*"](v),a.acceleration=w["/"](a.m),a.velocity=a.velocity["+"](a.acceleration["*"](p)),a.pos=a.pos["+"](a.velocity["*"](p)),s=s["+"](p));i("Simulation segment finished."),await sleep(2)}e=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(t){return this.concat(t)},Array.prototype["*"]=function(t){return __array_times_number(this,t)},window.__GSlang="vpython",i=GSprint,o=range,a="__main__",r=pytype,(0,t.pythonize.strings)(),await l.pause("Click to Start"),n=!0,s.__argnames__||Object.defineProperties(s,{__argnames__:{value:["evt"]},__module__:{value:null}}),l.bind("click",s),p.__argnames__||Object.defineProperties(p,{__argnames__:{value:["initial_v_factor","label_text"]},__module__:{value:null}}),await p(.7,"Too Slow: Orbit Decays"),await p(1,"Correct Speed: Circular Orbit"),await p(1.4,"Too Fast: Elliptical Orbit"),await p(1.8,"Much Faster: Escape Trajectory"),l.caption="All simulations complete."}t.pythonize={},function(){function e(){if(e=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)i=arguments[0]?Array.prototype.slice.call(arguments):null;else{var t;i=((t=ρσ_set()).jsset.add("split"),t.jsset.add("replace"),t)}i&&(e=e.difference(set(i)));var e,i,o,a=e;for(var r of a="function"==typeof a[Symbol.iterator]?a instanceof Map?a.keys():a:Object.keys(a))o=r,(ρσ_expr_temp=String.prototype)["number"==typeof o&&o<0?ρσ_expr_temp.length+o:o]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof o&&o<0?ρσ_expr_temp.length+o:o]}e.__module__||Object.defineProperties(e,{__module__:{value:"pythonize"}}),t.pythonize.strings=e}(),e.__module__||Object.defineProperties(e,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},e()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/a508cfc93571" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The speed required for a satellite to maintain a stable circular orbit depends on which of the following?
    a) The mass of the satellite.
    b) The mass of the planet and the orbital radius.
    c) The mass of the satellite and the mass of the planet.
    d) The radius of the orbit only.

2.  If a satellite in a stable circular orbit suddenly slows down, what will happen to its path?
    a) It will move into a larger circular orbit.
    b) It will move into an elliptical orbit.
    c) It will begin to spiral inward towards the planet.
    d) It will continue in the same circular orbit.

3.  According to Newton's Law of Universal Gravitation, if you double the distance between the centers of two objects, the gravitational force between them will be:
    a) Four times stronger.
    b) Two times stronger.
    c) Half as strong.
    d) One-quarter as strong.

4.  Planet A has twice the mass of Planet B. A satellite orbits each planet at the same orbital radius. How does the orbital speed of the satellite around Planet A (`vA`) compare to its speed around Planet B (`vB`)?
    a) `vA = vB`
    b) `vA = 2 * vB`
    c) `vA = sqrt(2) * vB`
    d) `vA = vB / 2`

5.  For a satellite in a stable circular orbit, the force of gravity is:
    a) Greater than the required centripetal force.
    b) Less than the required centripetal force.
    c) Equal to the required centripetal force.
    d) Tangent to the orbital path.

### Problem-Solving Questions

(Use G = 6.67e-11 N·m²/kg²)

1.  A 1000 kg satellite is in a circular orbit around the Earth (Mass = 5.97e24 kg) at a radius of 7.0e6 m. What is the magnitude of the gravitational force on the satellite?
    a) 8090 N
    b) 8.09 N
    c) 5.68e9 N
    d) 5680 N

2.  Using the information from the previous question, what is the required orbital speed for this satellite?
    a) 7540 m/s
    b) 5680 m/s
    c) 5.97e3 m/s
    d) 7.0e6 m/s

3.  A satellite orbits a planet of mass `M` at a radius `r`. If another satellite with twice the mass orbits the same planet at the same radius, what is its orbital period compared to the first satellite?
    a) It is half the period.
    b) It is the same.
    c) It is twice the period.
    d) It is four times the period.

4.  An asteroid has an orbital speed of 15,000 m/s around a star with a mass of 2.0e30 kg. What is the radius of its circular orbit?
    a) 5.9e11 m
    b) 8.9e9 m
    c) 1.3e26 m
    d) 4.4e15 m

5.  What is the centripetal acceleration of the International Space Station, which orbits at a radius of approximately 6.8e6 m from Earth's center? (Earth Mass = 5.97e24 kg)
    a) 9.8 m/s²
    b) 8.6 m/s²
    c) 0 m/s²
    d) 1.6 m/s²

### Computational Questions

1.  In the simulation, the gravitational force must be recalculated inside the loop. Why is this necessary for an accurate simulation, especially for non-circular orbits?
    a) Because the mass of the planet is changing.
    b) Because the gravitational constant G changes.
    c) Because both the distance and the direction of the force vector change as the satellite moves.
    d) It is not necessary; the force is constant.

2.  The code calculates the vector from the satellite to the planet using `r_vector = planet.pos - satellite.pos`. What would happen if this were reversed to `satellite.pos - planet.pos`?
    a) The simulation would be unaffected.
    b) The force would be repulsive instead of attractive, pushing the satellite away.
    c) The magnitude of the force would be wrong.
    d) The simulation would run slower.

3.  To achieve a perfect circular orbit, the initial velocity is set to `satellite.velocity = vector(0, v_circular, 0)`. Why is this velocity purely in the y-direction?
    a) Because the satellite starts on the y-axis.
    b) Because the satellite starts on the x-axis, and the velocity must be tangential to the circular path.
    c) To make the satellite move towards the planet.
    d) It is an arbitrary choice; any direction would work.

4.  If you set the initial speed in the simulation to be *less* than the calculated `v_circular`, what trajectory would you expect to see?
    a) A larger circular orbit.
    b) A stable elliptical orbit.
    c) A spiral path moving inward towards the planet.
    d) A straight line path away from the planet.

5.  The acceleration is calculated as `satellite.acceleration = F_gravity / satellite.m`. This line of code demonstrates that:
    a) The satellite's acceleration is independent of its own mass.
    b) Heavier satellites accelerate faster.
    c) The acceleration depends only on the planet's mass.
    d) The acceleration is constant throughout the orbit.

---
### Answer Key
**Conceptual:** 1. (b), 2. (c), 3. (d), 4. (c), 5. (c)
**Problem-Solving:** 1. (a), 2. (a), 3. (b), 4. (a), 5. (b)
**Computational:** 1. (c), 2. (b), 3. (b), 4. (c), 5. (a)
