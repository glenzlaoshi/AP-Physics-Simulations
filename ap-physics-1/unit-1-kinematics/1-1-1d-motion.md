
---
title: "1.1 - 1D Motion"
layout: default
---

## 1. Introduction to the Unit: Kinematics

Welcome to the study of motion! Kinematics is the branch of physics that describes how objects move, without getting into the reasons *why* they move. It's the language we use to talk about motion. Before we can analyze the forces that cause a car to accelerate (which is called **Dynamics**), we first need a precise way to describe the car's position, its velocity, and its acceleration. This unit provides the foundational concepts and equations for describing motion in one dimension (a straight line).

## 2. Relevant Physics Concepts

### Position, Velocity, and Acceleration

- **Position (`x`):** An object's location at a specific point in time. In VPython, this is a **vector**, which has both a magnitude and a direction (e.g., `vector(5, 0, 0)` means 5 meters along the x-axis).
- **Velocity (`v`)::** The rate at which an object's position changes. It is also a vector, representing both the object's **speed** and its **direction**.
- **Acceleration (`a`):** The rate at which an object's velocity changes. An object is accelerating if it is speeding up, slowing down, or changing direction. It is also a vector.

### Key Kinematic Equations (for constant acceleration)

When an object's acceleration is constant, we can use a set of simple equations to relate position, velocity, acceleration, and time.
1.  `v_f = v_i + a*t`  (Final velocity = initial velocity + acceleration × time)
2.  `Δx = v_i*t + 0.5*a*t²` (Displacement = initial velocity × time + one-half × acceleration × time squared)
3.  `v_f² = v_i² + 2*a*Δx` (Final velocity squared = initial velocity squared + 2 × acceleration × displacement)

### Simulating Motion: Numerical Integration

How does a computer simulate smooth motion? It can't! Instead, it calculates the state of an object at a specific moment, then uses the laws of physics to figure out where the object will be a tiny fraction of a second later. It does this over and over again, very quickly, creating the illusion of smooth motion. This step-by-step calculation is called **numerical integration**.

We use a small **time step (`dt`)**, for example, 0.01 seconds. In each step, we update the object's properties:
1.  `new_velocity = old_velocity + acceleration * dt` (This is just a rearranged version of `a = dv/dt`)
2.  `new_position = old_position + new_velocity * dt` (This is just a rearranged version of `v = dx/dt`)

This two-step update process is the heart of our physics simulation.

## 3. The Simulation: Making the Car Move

### Outline of the Simulation

The `skeleton.py` file sets up a visual scene with a blue "car" and a green "road". The car has properties like `car.pos`, `car.velocity`, and `car.acceleration`. Your goal is to add the physics logic inside the animation loop to make the car move according to the principles of kinematics.

### Completing the `skeleton.py` File

The skeleton file has comments labeled `--- STUDENT TASK ---`. Here is how to approach them.

#### **VPython Objects and Properties**

In VPython, everything is an object. The car is an object, and its position is a property of that object. You can access and change properties using a dot (`.`). For example, to set the car's velocity to 2 m/s in the x-direction, you would write:
```python
car.velocity = vector(2, 0, 0)
```

#### **The Animation Loop**

The simulation happens inside a `while` loop.
```python
while car.pos.x < 10:
    rate(100)
    # ... physics code goes here ...
```
- The `while car.pos.x < 10:` line means "keep repeating the code inside this loop as long as the car's x-position is less than 10." This is our stopping condition.
- `rate(100)` tells the computer to not run the loop more than 100 times per second. This slows the calculation down to a speed that we can see, creating a smooth animation.

#### **Implementing the Physics**

Your main task is to implement the numerical integration steps inside the loop. This involves translating the physics equations into code.

1.  **Update Velocity (Your Task):** The first physical relationship is that acceleration changes velocity. The equation is `new_velocity = old_velocity + acceleration * dt`. Following the example for position below, can you write the line of code that updates `car.velocity`?

2.  **Update Position (Example):** The second relationship is that velocity changes position. To update the car's position, you would write the following line. It takes the car's current position (`car.pos`), and updates it by adding the small distance it would travel (`car.velocity * dt`) in the time step `dt`.
    ```python
    # New_Position = Old_Position + Velocity * dt
    car.pos = car.pos + car.velocity * dt
    ```

3.  **Update Time (Your Task):** The simulation's clock doesn't advance on its own. You must add a line of code to update the time variable `t` by the time step `dt`.

By adding these lines in the correct order inside the `while` loop, you are telling the simulation how the car's state should evolve over time according to the laws of physics.

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

!function(){var t={};async function o(){"use strict";canvas;var o,e,i,l,n,a,r,s,c,p,u,f,y,d,h=canvas();function v(t,o=0){return Number(t.toFixed(o))}async function m(t){d=!d}for(o=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(t){return this.concat(t)},Array.prototype["*"]=function(t){return __array_times_number(this,t)},window.__GSlang="vpython",e=GSprint,i=range,l="__main__",n=pytype,(0,t.pythonize.strings)(),h.title="Simulation of 1D Motion: Constant Velocity and Constant Acceleration",h.caption="Below the simulation, graphs show position, velocity, and acceleration vs. time.",a=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(0,1["-u"]()["*"](.5),0),size:vector(20,.1,4),color:color.green})]),r=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(1["-u"]()["*"](9),0,0),size:vector(1,.5,.75),color:color.blue})]),ρσ_interpolate_kwargs.call(this,attach_trail,[r].concat([ρσ_desugar_kwargs({color:color.yellow,radius:.05})])),s=0,c=.01,e("Starting Part 1: Constant Velocity"),r.velocity=vector(2,0,0),r.acceleration=vector(0,0,0),p=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Motion Graphs",xtitle:"Time (s)",ytitle:"Value"})]),u=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.blue,label:"Position (m)"})]),f=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.red,label:"Velocity (m/s)"})]),y=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.purple,label:"Acceleration (m/s^2)"})]),await h.pause("Click to Start"),d=!0,m.__argnames__||Object.defineProperties(m,{__argnames__:{value:["evt"]},__module__:{value:null}}),h.bind("click",m);s["<"](2);)await rate(100),d&&(r.pos=r.pos["+"](r.velocity["*"](c)),s=s["+"](c),u.plot(s,r.pos.x),f.plot(s,r.velocity.x),y.plot(s,r.acceleration.x));for(e("End of Part 1. Position:",r.pos),e("---"),e("Starting Part 2: Constant Acceleration"),r.acceleration=vector(5,0,0);r.pos.x["<"](10);)await rate(100),d&&(r.velocity=r.velocity["+"](r.acceleration["*"](c)),r.pos=r.pos["+"](r.velocity["*"](c)),s=s["+"](c),u.plot(s,r.pos.x),f.plot(s,r.velocity.x),y.plot(s,r.acceleration.x));e("End of Part 2. Final Position:",r.pos),e("Final Velocity:",r.velocity),e("Simulation finished.")}t.pythonize={},function(){function o(){if(o=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)e=arguments[0]?Array.prototype.slice.call(arguments):null;else{var t;e=((t=ρσ_set()).jsset.add("split"),t.jsset.add("replace"),t)}e&&(o=o.difference(set(e)));var o,e,i,l=o;for(var n of l="function"==typeof l[Symbol.iterator]?l instanceof Map?l.keys():l:Object.keys(l))i=n,(ρσ_expr_temp=String.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]}o.__module__||Object.defineProperties(o,{__module__:{value:"pythonize"}}),t.pythonize.strings=o}(),o.__module__||Object.defineProperties(o,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},o()})}();

//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/f851b40dd418" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  An object's velocity is zero at a particular instant. What can be said about its acceleration at that instant?
    a) It must be zero.
    b) It must be non-zero.
    c) It could be zero or non-zero.
    d) It must be negative.

2.  The slope of a position-time graph represents:
    a) Acceleration
    b) Velocity
    c) Displacement
    d) Time

3.  If an object has a constant, non-zero acceleration, its velocity-time graph will be:
    a) A horizontal line.
    b) A vertical line.
    c) A straight line with a non-zero slope.
    d) A curved line.

4.  A car is moving to the right and its brakes are applied, causing it to slow down. Which of the following statements about its motion is correct?
    a) Its velocity is positive and its acceleration is positive.
    b) Its velocity is positive and its acceleration is negative.
    c) Its velocity is negative and its acceleration is positive.
    d) Its velocity is negative and its acceleration is negative.

5.  The area under a velocity-time graph represents:
    a) Acceleration
    b) Position
    c) Displacement
    d) Average velocity

### Problem-Solving Questions

1.  A ball is dropped from rest from a height of 20 m. Approximately how long does it take to hit the ground? (Use g = 9.8 m/s²)
    a) 1.0 s
    b) 2.0 s
    c) 4.1 s
    d) 9.8 s

2.  A car starts from rest and accelerates at 4 m/s² for 5 seconds. What is its final velocity?
    a) 4 m/s
    b) 5 m/s
    c) 20 m/s
    d) 100 m/s

3.  An object is thrown upwards with an initial velocity of 19.6 m/s. What is the maximum height it reaches? (Use g = 9.8 m/s²)
    a) 9.8 m
    b) 19.6 m
    c) 39.2 m
    d) 2.0 m

4.  A train slows down from 30 m/s to 10 m/s in 10 seconds. What is its acceleration?
    a) -2 m/s²
    b) 2 m/s²
    c) -4 m/s²
    d) 4 m/s²

5.  A car travels 100m in 10s, starting from rest, with constant acceleration. What is the magnitude of its acceleration?
    a) 1 m/s²
    b) 2 m/s²
    c) 5 m/s²
    d) 10 m/s²

### Computational Questions

1.  In the simulation's animation loop, the position of the object is updated using `car.pos = car.pos + car.velocity * dt`. Why is `dt` used instead of `t`?
    a) `dt` represents the final time, while `t` is the elapsed time.
    b) `t` would make the object jump to a final position, while `dt` updates the position incrementally for a smooth animation.
    c) `dt` is a typo and should be `t`.
    d) Using `t` is computationally more expensive.

2.  If you run the simulation for an object with constant positive velocity and then run it again with the same velocity but a `dt` value that is twice as large, how will the animation change?
    a) The object will move faster and the animation will be smoother.
    b) The object will move at the same simulated speed, but the animation will be choppier (less smooth).
    c) The object will move slower.
    d) The simulation will crash.

3.  You want to simulate an object accelerating from rest. Which line of code inside the `while` loop would correctly update the velocity over a small time step `dt`?
    a) `car.velocity = car.velocity + car.acceleration`
    b) `car.velocity = car.velocity + car.acceleration * dt`
    c) `car.velocity = car.acceleration * t`
    d) `car.velocity = car.acceleration`

4.  What is the purpose of the `rate(100)` function call inside the animation loop?
    a) It sets the object's acceleration rate to 100 m/s².
    b) It ensures the loop runs exactly 100 times.
    c) It limits the animation to a maximum of 100 frames per second.
    d) It calculates the rate of change of velocity.

5.  You adapt the simulation to model a ball thrown vertically upwards, with the positive y-direction being upwards. What should the `car.acceleration` vector be set to for this model?
    a) `vector(0, 9.8, 0)`
    b) `vector(0, -9.8, 0)`
    c) `vector(0, 0, 0)`
    d) `vector(car.mass * 9.8, 0, 0)`

---
### Answer Key
**Conceptual:** 1. (c), 2. (b), 3. (c), 4. (b), 5. (c)
**Problem-Solving:** 1. (b), 2. (c), 3. (b), 4. (a), 5. (b)
**Computational:** 1. (b), 2. (b), 3. (b), 4. (c), 5. (b)
