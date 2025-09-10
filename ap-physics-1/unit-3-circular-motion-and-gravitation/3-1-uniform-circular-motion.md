---
title: "3.1 - Uniform Circular Motion"
layout: default
---

## 1. Introduction to the Unit: Circular Motion

So far, we have studied motion in straight lines. This unit expands our understanding of dynamics to objects moving in circular paths. The key idea is a direct consequence of Newton's First Law: an object will only change its direction of motion if a net force acts on it.

For an object to move in a circle, it must be constantly changing direction. This means there must be a constant net force acting on it, directed towards the center of the circle. We call this center-seeking net force the **centripetal force**. 

It is very important to understand that centripetal force is **not** a new, fundamental force of nature. It is simply the *label* we give to the net force that causes circular motion. The actual force providing the centripetal action could be tension (like in this simulation), gravity (for a planet in orbit), or friction (for a car turning a corner).

## 2. Relevant Physics Concepts

### Uniform Circular Motion (UCM)

UCM describes motion in a perfect circle at a **constant speed**. A common point of confusion is the difference between speed and velocity. 
- **Speed** is a scalar (just a number, e.g., 5 m/s).
- **Velocity** is a vector (speed *and* direction).

In UCM, the speed is constant, but the **velocity is always changing** because the object's direction is always changing. 

### Centripetal Acceleration (`ac`)

Since velocity is changing, there must be an acceleration. For an object in UCM, this acceleration is called centripetal acceleration. 
- **Direction:** It is always directed radially inward, towards the center of the circle.
- **Magnitude:** It is given by the formula `ac = v² / r`, where `v` is the object's constant speed and `r` is the radius of the circle.

### Centripetal Force (`Fc`)

From Newton's Second Law (`F=ma`), if there is an acceleration, there must be a net force. The centripetal force is the net force required to produce the centripetal acceleration.
- **Direction:** It also always points towards the center of the circle.
- **Magnitude:** It is given by `Fc = m * ac = m * v² / r`.

## 3. The Simulation: A Ball on a String

### Outline of the Simulation

The `skeleton.py` file shows a ball attached by a "string" to a central post. The goal is to make the ball move in a circle at a constant speed. The main challenge is that, unlike our previous simulations, the acceleration is **not constant**. Its magnitude is constant, but its *direction* must change every single frame to always point at the center.

### Completing the `skeleton.py` File

#### **Task 1: Initial Velocity**

To get the motion started, the ball needs an initial velocity that is **tangential** to the circular path. If the ball starts at position `vector(5, 0, 0)`, a tangential velocity would be purely in the y-direction. Your task is to set the `ball.velocity` to an initial vector like `vector(0, 4, 0)`.

#### **Task 2 & 3: Calculating Acceleration in the Loop**

Because the direction of centripetal acceleration is always changing, you must recalculate it **inside** the `while` loop. This is the most important part of the simulation.

1.  **Magnitude (Example):** First, you need the *magnitude* of the acceleration. The formula is `ac = v² / r`. The code for this is provided as an example:
    ```python
    a_mag = speed**2 / radius
    ```

2.  **Direction (Your Task):** Next, you need the *direction* of the acceleration. The direction must always point from the ball back to the center of the circle (the origin, `vector(0,0,0)`). The ball's own position vector, `ball.pos`, points from the center to the ball. Therefore, the vector pointing from the ball *back to the center* is simply `-ball.pos`. 

    To get a pure direction vector (called a "unit vector"), we use the VPython function `norm()`. Your task is to define the direction vector `a_dir` using this logic.

3.  **Putting It Together (Your Task):** The final acceleration vector is its magnitude multiplied by its direction. Write the line of code to set `ball.acceleration` by multiplying `a_mag` and `a_dir`.

#### **Updating Motion**

- **Your Task:** Once the acceleration vector has been calculated for the current frame, you can use the same numerical integration technique from the previous units. Write the two lines of code inside the loop to update the `ball.velocity` and `ball.pos`.

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
!function(){var t={};async function e(){"use strict";canvas;var e,o,i,r,s,a,n,l,p,c,u,f,d,h,y,m,v,w,g,_=canvas();async function x(t){g=!g}for(e=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(t){return this.concat(t)},Array.prototype["*"]=function(t){return __array_times_number(this,t)},window.__GSlang="vpython",o=GSprint,i=range,r="__main__",s=pytype,(0,t.pythonize.strings)(),_.title="Uniform Circular Motion",_.caption="The green arrow is the velocity vector (tangent to the path).\nThe red arrow is the centripetal acceleration vector (points to the center).",a=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({pos:vector(0,0,0),axis:vector(0,0,1),radius:.1,color:color.gray(.5)})]),n=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(5,0,0),radius:.5,color:color.blue,make_trail:!0})]),l=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({pos:a.pos,axis:n.pos["-"](1["*"](a.pos)),radius:.05,color:color.yellow})]),p=0,c=.01,n.mass=.5,u=mag(n.pos),f=4,n.velocity=vector(0,f,0),d=Math.pow(f,2)["/"](u),h=n.mass["*"](d),o("Radius: "["+"](ρσ_str.format("{:.1f}",u))["+"](" m, Speed: ")["+"](ρσ_str.format("{:.1f}",f))["+"](" m/s")),o("Centripetal acceleration: "["+"](ρσ_str.format("{:.2f}",d))["+"](" m/s^2")),o("Required Centripetal Force (Tension): "["+"](ρσ_str.format("{:.2f}",h))["+"](" N")),y=.5,m=1,v=ρσ_interpolate_kwargs.call(this,arrow,[ρσ_desugar_kwargs({pos:n.pos,shaftwidth:.2,color:color.green,label:"Velocity"})]),w=ρσ_interpolate_kwargs.call(this,arrow,[ρσ_desugar_kwargs({pos:n.pos,shaftwidth:.2,color:color.red,label:"Acceleration"})]),await _.pause("Click to Start"),g=!0,x.__argnames__||Object.defineProperties(x,{__argnames__:{value:["evt"]},__module__:{value:null}}),_.bind("click",x);p["<"](10);)await rate(1["/"](c)),g&&(n.acceleration=1["-u"]()["*"](norm(n.pos))["*"](d),n.velocity=n.velocity["+"](n.acceleration["*"](c)),n.pos=n.pos["+"](n.velocity["*"](c)),l.axis=n.pos["-"](1["*"](a.pos)),v.pos=n.pos,w.pos=n.pos,v.axis=n.velocity["*"](y),w.axis=n.acceleration["*"](m),p=p["+"](c));o("Simulation finished.")}t.pythonize={},function(){function e(){if(e=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)o=arguments[0]?Array.prototype.slice.call(arguments):null;else{var t;o=((t=ρσ_set()).jsset.add("split"),t.jsset.add("replace"),t)}o&&(e=e.difference(set(o)));var e,o,i,r=e;for(var s of r="function"==typeof r[Symbol.iterator]?r instanceof Map?r.keys():r:Object.keys(r))i=s,(ρσ_expr_temp=String.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]}e.__module__||Object.defineProperties(e,{__module__:{value:"pythonize"}}),t.pythonize.strings=e}(),e.__module__||Object.defineProperties(e,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},e()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/52405b4d95d5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  An object is in uniform circular motion. Which of the following statements is true?
    a) Its velocity is constant.
    b) Its acceleration is constant.
    c) Its speed is constant.
    d) The net force on it is zero.

2.  A car is traveling at a constant speed around a circular track. The net force on the car is directed:
    a) Forward, in the direction of travel.
    b) Backward, opposite the direction of travel.
    c) Toward the center of the circle.
    d) Outward, away from the center of the circle.

3.  The "centripetal force" is:
    a) A fundamental force of nature, like gravity.
    b) The force that is always directed tangent to the path of motion.
    c) The net force that is required to keep an object moving in a circle.
    d) A fictitious force that pushes an object outwards.

4.  A ball is being swung in a horizontal circle on the end of a string. If the string breaks, what path will the ball follow?
    a) It will continue to move in a circle.
    b) It will fly directly outward, away from the center.
    c) It will fly off in a straight line tangent to the circle at the point of release.
    d) It will drop straight to the ground.

5.  If an object in uniform circular motion has its speed doubled, while the radius of its path remains the same, what happens to the required centripetal force?
    a) It is cut in half.
    b) It remains the same.
    c) It is doubled.
    d) It is quadrupled.

### Problem-Solving Questions

1.  A 2 kg ball is swung in a circle of radius 1.5 m with a constant speed of 6 m/s. What is the magnitude of the centripetal acceleration?
    a) 4 m/s²
    b) 8 m/s²
    c) 12 m/s²
    d) 24 m/s²

2.  Using the information from the previous question (2 kg ball, 1.5 m radius, 6 m/s speed), what is the magnitude of the centripetal force (the tension in the string)?
    a) 12 N
    b) 24 N
    c) 36 N
    d) 48 N

3.  A 1200 kg car travels around a circular track of radius 50 m. If the force of friction providing the centripetal force is 9600 N, what is the car's speed?
    a) 8 m/s
    b) 20 m/s
    c) 50 m/s
    d) 400 m/s

4.  An object completes 10 full circles in 5 seconds, moving on a path with a radius of 2 m. What is its speed?
    a) 4π m/s
    b) 8π m/s
    c) 10π m/s
    d) 20 m/s

5.  A satellite is in a circular orbit around the Earth. It has a centripetal acceleration of 9.0 m/s². If the radius of its orbit is doubled, what must its new speed be to maintain a circular orbit with the same acceleration?
    a) It must be halved.
    b) It must be multiplied by √2.
    c) It must be doubled.
    d) It must be quadrupled.

### Computational Questions

1.  In the simulation, why must the acceleration be recalculated inside the `while` loop?
    a) Because the speed of the ball is changing.
    b) Because the radius of the circle is changing.
    c) Because the direction of the required acceleration is constantly changing.
    d) To make the simulation less efficient.

2.  The code uses `a_dir = norm(-ball.pos)` to find the direction of the acceleration. Why is the negative sign necessary?
    a) `ball.pos` is a vector from the center to the ball, but the acceleration must point from the ball to the center.
    b) To make the ball slow down.
    c) It is a convention in VPython for all circular motion.
    d) The negative sign cancels out with the negative mass.

3.  What would happen if you set the initial velocity to point directly at the center, for example `ball.velocity = vector(-4, 0, 0)`?
    a) The ball would move in a perfect circle.
    b) The ball would move back and forth in a straight line along the x-axis.
    c) The ball would remain stationary.
    d) The simulation would crash.

4.  The magnitude of acceleration is calculated as `a_mag = speed**2 / radius`. If you wanted to simulate the ball moving in a larger circle but with the same period (time per revolution), how would you need to change the initial speed?
    a) The speed would need to be decreased.
    b) The speed would need to stay the same.
    c) The speed would need to be increased.
    d) The period does not depend on speed.

5.  The simulation updates position using `ball.pos = ball.pos + ball.velocity * dt`. If `dt` is made much larger, what is the most likely error you would see in the simulation?
    a) The ball would move faster and the simulation would be smoother.
    b) The ball's path would no longer be a perfect circle; it would look more like a polygon.
    c) The ball would spiral inwards towards the center.
    d) The simulation would run much slower but remain perfectly accurate.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (c), 4. (c), 5. (d)
**Problem-Solving:** 1. (d), 2. (d), 3. (b), 4. (a), 5. (b)
**Computational:** 1. (c), 2. (a), 3. (b), 4. (c), 5. (b)
