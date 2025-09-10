---
title: "2.1 - Forces on an Inclined Plane"
layout: default
---

## 1. Introduction to the Unit: Dynamics

In the previous unit, Kinematics, we learned how to describe motion (position, velocity, acceleration). Now, in Dynamics, we explore *why* things move the way they do. The cause of any change in motion is a **force**—a push or a pull.

This unit is built upon **Newton's Three Laws of Motion**, which are the foundation of classical mechanics:
1.  **First Law (Inertia):** An object in motion stays in motion, and an object at rest stays at rest, unless acted upon by a net external force.
2.  **Second Law (F=ma):** The net force acting on an object is equal to the object's mass times its acceleration (`F_net = m*a`). This is the central equation of dynamics.
3.  **Third Law (Action-Reaction):** For every action, there is an equal and opposite reaction.

By identifying all the forces acting on an object and using `F_net = m*a`, we can predict its resulting motion.

## 2. Relevant Physics Concepts

### Common Forces
- **Gravity (`Fg` or `W`):** The force of the Earth pulling on an object. Its magnitude is `mg`, and it **always points straight down**.
- **Normal Force (`Fn`):** A contact force from a surface that prevents an object from passing through it. The normal force is always directed **perpendicular** (or "normal") to the surface.
- **Friction (`Ff`):** A contact force that opposes motion or attempted motion between surfaces. The force of kinetic (sliding) friction is calculated as `Fk = μk * Fn`, where `μk` is the coefficient of kinetic friction.

### The Inclined Plane Problem

Analyzing forces on an inclined plane is a classic physics problem. The key trick is to **tilt your coordinate system**. Instead of the usual horizontal and vertical axes, we set our axes so that:
- The **x-axis** is parallel to the surface of the incline.
- The **y-axis** is perpendicular to the surface of the incline.

### Resolving the Force of Gravity

Because we've tilted our coordinate system, the force of gravity (which still points straight down) is now at an angle to our new axes. We must break it down into its x and y components in this new system.

If the incline has an angle `theta`:
- The component of gravity **perpendicular** to the plane is `Fg_perp = mg * cos(theta)`.
- The component of gravity **parallel** to the plane is `Fg_parallel = mg * sin(theta)`.

This is the most important step. The `Fg_parallel` component is what tries to pull the block down the ramp, while the `Fg_perp` component is what the Normal Force has to push against.

## 3. The Simulation: The Sliding Block

### Outline of the Simulation

The `skeleton.py` file shows a block resting on a tilted surface. Your goal is to correctly calculate all the forces acting on the block in a tilted coordinate system. The vector sum of these forces (`F_net`) will determine the block's acceleration down the ramp.

### Completing the `skeleton.py` File

#### **Force Calculation**

1.  **Gravitational Force (`Fg`):** This is the easiest force, but also the one that causes the most confusion! In the simulation's *un-tilted* world coordinates, it always points straight down. The skeleton file provides this for you: `Fg = vector(0, -block.m * g, 0)`.

2.  **Normal Force (`Fn`):** The normal force must perfectly balance the perpendicular component of gravity. Its magnitude is `Fn_mag = mg * cos(angle)`. The skeleton file provides a direction vector for you called `normal_direction`. Your task is to combine the magnitude and direction to create the final normal force vector, `Fn`.

3.  **Frictional Force (`Fk`):** The magnitude of kinetic friction is `Fk_mag = μk * Fn_mag`. Since the block will slide *down* the ramp, the friction force must oppose this motion and point *up* the ramp. The skeleton provides a `friction_direction` vector. Your task is to calculate the magnitude and combine it with the direction to create the friction force vector, `Fk`.

4.  **Net Force (`F_net`):** The net force is the vector sum of all the forces you just defined. Write the line of code to add the three force vectors (`Fg`, `Fn`, and `Fk`) together.

#### **Applying Newton's Second Law**

- **Acceleration (Example):** Once you have the net force, you can find the acceleration using Newton's Second Law. The code for this is:
  ```python
  block.acceleration = F_net / block.m
  ```
- **Updating Motion (Your Task):** Now that you have the block's (constant) acceleration, you must add the two familiar lines of code for numerical integration inside the `while` loop to update the block's `velocity` and `pos` over each time step `dt`.

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
!function(){var e={};async function t(){"use strict";canvas;var t,o,i,s,a,l,n,r,c,p,u,f,h,d,m,y,_,g,v,w,x,z,b,j,k,P=canvas();async function A(e){k=!k}for(t=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(e){return this.concat(e)},Array.prototype["*"]=function(e){return __array_times_number(this,e)},window.__GSlang="vpython",o=GSprint,i=range,s="__main__",a=pytype,(0,e.pythonize.strings)(),P.title="Forces on an Inclined Plane",P.caption="The simulation shows the force vectors acting on the block.",l=await radians(25),n=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(0,1["-u"]()["*"](.65),0),size:vector(12,.2,4),color:color.blue})]),ρσ_interpolate_kwargs.call(n,n.rotate,[ρσ_desugar_kwargs({angle:l,axis:vector(0,0,1)})]),(r=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(n.size.x["*"](.5)["*"](cos(l)),n.size.x["*"](.5)["*"](sin(l)),0),size:vector(1,1,1),color:color.red})])).pos=vec(n.size.x["*"](.5)["-"](1["*"](.8))["*"](cos(l)),n.size.x["*"](.5)["-"](1["*"](.8))["*"](sin(l)),0),ρσ_interpolate_kwargs.call(r,r.rotate,[ρσ_desugar_kwargs({angle:l,axis:vector(0,0,1)})]),c=0,p=.001,u=9.8,r.mass=1,f=.35,r.velocity=vector(0,0,0),h=1["-u"]()["*"](vector(cos(l),sin(l),0)),d=vector(sin(1["-u"]()["*"](l)),cos(1["-u"]()["*"](l)),0),m=vector(0,1["-u"]()["*"](r.mass)["*"](u),0),_=(y=r.mass["*"](u)["*"](cos(l)))["*"](d),g=f["*"](y),v=1["-u"]()["*"](g)["*"](h),w=m["+"](_)["+"](v),r.acceleration=w["/"](r.mass),x=.8,(z=ρσ_interpolate_kwargs.call(this,arrow,[ρσ_desugar_kwargs({color:color.yellow,shaftwidth:.1})])).pos=r.pos,z.axis=_["*"](x),(b=ρσ_interpolate_kwargs.call(this,arrow,[ρσ_desugar_kwargs({color:color.green,shaftwidth:.1})])).pos=r.pos,b.axis=m["*"](x),(j=ρσ_interpolate_kwargs.call(this,arrow,[ρσ_desugar_kwargs({color:color.orange,shaftwidth:.1})])).pos=r.pos,j.axis=v["*"](x),o("Angle: "["+"](ρσ_str.format("{:.1f}",await degrees(l)))["+"](" degrees")),o("Net Force: "["+"](ρσ_str.format("{}",w))["+"]("")),o("Acceleration: "["+"](ρσ_str.format("{}",r.acceleration))["+"]("")),await P.pause("Click to Start"),k=!0,A.__argnames__||Object.defineProperties(A,{__argnames__:{value:["evt"]},__module__:{value:null}}),P.bind("click",A);r.pos.x[">"](1["-u"]()["*"](5.25));)await rate(1["/"](p)),k&&(r.velocity=r.velocity["+"](r.acceleration["*"](p)),r.pos=r.pos["+"](r.velocity["*"](p)),c=c["+"](p),z.pos=r.pos,b.pos=r.pos,j.pos=r.pos);o("Simulation finished."),o("Final velocity: "["+"](ρσ_str.format("{:.2f}",r.velocity.mag))["+"](" m/s"))}e.pythonize={},function(){function t(){if(t=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)o=arguments[0]?Array.prototype.slice.call(arguments):null;else{var e;o=((e=ρσ_set()).jsset.add("split"),e.jsset.add("replace"),e)}o&&(t=t.difference(set(o)));var t,o,i,s=t;for(var a of s="function"==typeof s[Symbol.iterator]?s instanceof Map?s.keys():s:Object.keys(s))i=a,(ρσ_expr_temp=String.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]}t.__module__||Object.defineProperties(t,{__module__:{value:"pythonize"}}),e.pythonize.strings=t}(),t.__module__||Object.defineProperties(t,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},t()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/802926b2c58c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  A block rests on an inclined plane without sliding. The force of static friction must be equal in magnitude to:
    a) The force of gravity on the block.
    b) The normal force on the block.
    c) The component of gravity parallel to the incline.
    d) The component of gravity perpendicular to the incline.

2.  As the angle of an inclined plane is increased, what happens to the normal force acting on a block resting on it?
    a) It increases.
    b) It decreases.
    c) It remains the same.
    d) It depends on the coefficient of friction.

3.  A block is sliding down a frictionless inclined plane. Its acceleration is:
    a) g (9.8 m/s²).
    b) Zero.
    c) Less than g.
    d) Greater than g.

4.  According to Newton's Third Law, the "reaction" force to the Earth's gravitational pull on a block is:
    a) The normal force from the incline on the block.
    b) The friction force on the block.
    c) The block's gravitational pull on the Earth.
    d) The component of gravity parallel to the incline.

5.  If a block is pushed up an inclined plane at a constant velocity, the net force on the block is:
    a) Zero.
    b) Equal to the pushing force.
    c) Equal to the force of friction.
    d) Equal to the force of gravity.

### Problem-Solving Questions

1.  A 5 kg block rests on an incline with an angle of 30 degrees. What is the magnitude of the normal force on the block? (Use g = 9.8 m/s²)
    a) 24.5 N
    b) 42.4 N
    c) 49.0 N
    d) 98.0 N

2.  For the same 5 kg block on a 30-degree incline, what is the magnitude of the component of gravity acting parallel to the incline? (Use g = 9.8 m/s²)
    a) 24.5 N
    b) 42.4 N
    c) 49.0 N
    d) 0 N

3.  A 10 kg block is on a frictionless ramp angled at 20 degrees. What is the acceleration of the block down the ramp? (Use g = 9.8 m/s²)
    a) 3.35 m/s²
    b) 9.21 m/s²
    c) 9.8 m/s²
    d) 0 m/s²

4.  A 2 kg block slides down a 25-degree incline. The coefficient of kinetic friction between the block and the surface is 0.2. What is the magnitude of the friction force? (Use g = 9.8 m/s²)
    a) 3.55 N
    b) 4.14 N
    c) 8.28 N
    d) 17.8 N

5.  Using the information from the previous question (2 kg block, 25-degree incline, μk = 0.2), what is the net force on the block?
    a) 3.55 N
    b) 4.73 N
    c) 8.28 N
    d) 11.8 N

### Computational Questions

1.  In the simulation, the coordinate system is tilted. Why is this a useful strategy for solving inclined plane problems?
    a) It makes the force of gravity align with an axis.
    b) It makes the acceleration of the block align with an axis, simplifying the application of F=ma.
    c) It is required by the VPython library for all simulations.
    d) It eliminates the need to consider the friction force.

2.  The code calculates the normal force magnitude as `Fn_mag = block.m * g * cos(angle)`. This is the magnitude of the component of gravity that is:
    a) Parallel to the incline.
    b) Perpendicular to the incline.
    c) In the direction of motion.
    d) Equal to the total force of gravity.

3.  To find the net force, the simulation code adds three vectors: `F_net = Fg + Fn + Fk`. Why is it essential that these are added as vectors and not just as magnitudes?
    a) Because the forces point in different directions.
    b) Because VPython requires all forces to be vectors.
    c) To make the calculation more complex.
    d) It is not essential; adding magnitudes would give the same result.

4.  The simulation calculates acceleration using `block.acceleration = F_net / block.m`. If you were to double the mass of the block (`block.m`) but keep all other parameters (angle, friction) the same, how would the block's acceleration change?
    a) It would double.
    b) It would be cut in half.
    c) It would remain the same.
    d) It would decrease, but not be cut in half.

5.  The simulation updates velocity with `block.velocity = block.velocity + block.acceleration * dt`. If you commented out this line but kept the position update `block.pos = block.pos + block.velocity * dt`, what would the block's motion look like?
    a) The block would not move at all.
    b) The block would move down the ramp with constant velocity.
    c) The block would still accelerate down the ramp.
    d) The simulation would crash.

---
### Answer Key
**Conceptual:** 1. (c), 2. (b), 3. (c), 4. (c), 5. (a)
**Problem-Solving:** 1. (b), 2. (a), 3. (a), 4. (a), 5. (b)
**Computational:** 1. (b), 2. (b), 3. (a), 4. (d), 5. (b)
