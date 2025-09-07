---
title: "2.2 - Atwood Machine"
layout: default
---
# Information: Atwood Machine

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
!function(){var o={};async function t(){"use strict";canvas;var t,e,i,l,s,r,a,c,n,p,f,y,m,u,d,h,v,_=canvas();for(t=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(o){return this.concat(o)},Array.prototype["*"]=function(o){return __array_times_number(this,o)},window.__GSlang="vpython",e=GSprint,i=range,l="__main__",s=pytype,(0,o.pythonize.strings)(),_.title="Atwood Machine",_.caption="Two masses are connected by a string over a frictionless pulley.",r=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({pos:vector(0,5,0),axis:vector(0,0,1),radius:.5,color:color.gray(.7)})]),a=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(1["-u"]()["*"](2),3,0),size:vector(1,1,1),color:color.red})]),c=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(2,1,0),size:vector(1,1,1),color:color.blue})]),n=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({radius:.05,color:color.yellow})]),p=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({radius:.05,color:color.yellow})]),f=0,y=.01,m=9.8,a.m=4,c.m=4.5,e("Mass 1 (red): "["+"](ρσ_str.format("{}",a.m))["+"](" kg")),e("Mass 2 (blue): "["+"](ρσ_str.format("{}",c.m))["+"](" kg")),u=m["*"](c.m["-"](1["*"](a.m)))["/"](a.m["+"](c.m)),e("Theoretical acceleration: "["+"](ρσ_str.format("{:.2f}",u))["+"](" m/s^2")),a.acceleration=vector(0,u,0),c.acceleration=vector(0,1["-u"]()["*"](u),0),a.velocity=vector(0,0,0),c.velocity=vector(0,0,0),d=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Position vs. Time",xtitle:"Time (s)",ytitle:"Height (m)"})]),h=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:a.color,label:"Mass 1 ("["+"](ρσ_str.format("{}",a.m))["+"](" kg)")})]),v=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:c.color,label:"Mass 2 ("["+"](ρσ_str.format("{}",c.m))["+"](" kg)")})]);f["<"](3.5);)await rate(100),a.velocity=a.velocity["+"](a.acceleration["*"](y)),c.velocity=c.velocity["+"](c.acceleration["*"](y)),a.pos=a.pos["+"](a.velocity["*"](y)),c.pos=c.pos["+"](c.velocity["*"](y)),n.pos=a.pos["+"](vector(0,.5,0)),n.axis=r.pos["-"](1["*"](n.pos)),p.pos=c.pos["+"](vector(0,.5,0)),p.axis=r.pos["-"](1["*"](p.pos)),h.plot(f,a.pos.y),v.plot(f,c.pos.y),f=f["+"](y);e("Simulation finished."),e("Final velocity of mass 1: "["+"](ρσ_str.format("{:.2f}",a.velocity.y))["+"](" m/s")),e("Final velocity of mass 2: "["+"](ρσ_str.format("{:.2f}",c.velocity.y))["+"](" m/s"))}o.pythonize={},function(){function t(){if(t=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)e=arguments[0]?Array.prototype.slice.call(arguments):null;else{var o;e=((o=ρσ_set()).jsset.add("split"),o.jsset.add("replace"),o)}e&&(t=t.difference(set(e)));var t,e,i,l=t;for(var s of l="function"==typeof l[Symbol.iterator]?l instanceof Map?l.keys():l:Object.keys(l))i=s,(ρσ_expr_temp=String.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]}t.__module__||Object.defineProperties(t,{__module__:{value:"pythonize"}}),o.pythonize.strings=t}(),t.__module__||Object.defineProperties(t,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},t()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/e9ed02e66edf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
