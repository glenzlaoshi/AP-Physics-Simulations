---
title: "6.2 - Pendulum"
layout: default
---


## 1. Introduction to the Unit: SHM (continued)

This simulation explores another classic oscillating system: the simple pendulum. A simple pendulum consists of a point mass (the "bob") suspended from a pivot by a massless string or rod. 

Like the mass-spring system, a pendulum swings back and forth about an equilibrium position. A key question we will investigate is whether this motion is truly **Simple Harmonic Motion (SHM)**. Recall that the strict condition for SHM is that the restoring force must be directly proportional to the object's displacement (`F ∝ -x`). We will see that a pendulum only meets this condition approximately, and only for small angles.

## 2. Relevant Physics Concepts

### The Restoring Force of a Pendulum

Two forces act on the pendulum bob: the tension `T` from the string, and the force of gravity `Fg = mg`.

To understand the motion, we break the gravity vector into two components:
1.  A component parallel to the string (`mg*cos(θ)`), which is cancelled out by the tension force.
2.  A component **tangential** to the circular path of the swing (`mg*sin(θ)`). 

This tangential component is the **restoring force**. It is what is always trying to pull the bob back to its lowest point (the equilibrium position). 

`F_restore = -mg * sin(θ)`

The negative sign is crucial; it indicates the force is always in the opposite direction of the angular displacement `θ`.

### The Small Angle Approximation

Is the pendulum's motion SHM? The restoring force is `F = -mg*sin(θ)`. This is proportional to `sin(θ)`, not to the displacement `θ` itself. Therefore, strictly speaking, a pendulum does **not** undergo true SHM.

However, for small angles (typically less than 15°), the value of `sin(θ)` is very close to the value of `θ` (when `θ` is measured in radians). This is known as the **small angle approximation**.

So, for small angles only, we can say: `F_restore ≈ -mg*θ`. Since `mg` is constant, the restoring force is *approximately* proportional to the displacement, and the motion is very close to being SHM.

### The Period of a Simple Pendulum

Using the small angle approximation, we can derive a formula for the period of a simple pendulum:

**`T = 2π * sqrt(L / g)`**

-   `L` is the length of the pendulum.
-   `g` is the acceleration due to gravity.

Notice that for small angles, the period does **not** depend on the mass of the bob or on the amplitude of the swing.

## 3. The Simulation: Analyzing the Swing

### Outline of the Simulation

The `intermediate.py` file already contains the code to make a pendulum swing. It correctly calculates the restoring force and updates the motion without using the small angle approximation. Your task is to analyze this motion to see when the small angle approximation is valid.

### Completing the `intermediate.py` File

#### **Task 1: Graph the Motion**

- **Your Task:** Just as with the mass-spring system, the first step in analysis is to plot the motion. Before the `while` loop, create a `graph` and a `gcurve`. Inside the loop, add the line to plot the pendulum's angle `theta` versus time `t`.

#### **Task 2: Measure the Period**

- **Your Task:** Run the simulation with the initial small angle (20 degrees). Look at the graph you created and measure the time between the first two peaks. This is your **measured period**.

#### **Task 3: Compare with Theory**

- **Example (The Formula):** The theoretical period *using the small angle approximation* is `T = 2π * sqrt(L / g)`. The code to calculate this is:
  ```python
  T_theory = 2 * pi * sqrt(rod.L / g)
  ```
- **Analysis:** Compare the period you measured from the graph with this `T_theory`. For the small 20-degree angle, they should be very close.

#### **Task 4: Test the Approximation**

- **Your Task:** This is the key conceptual step. Go back to the top of the code and change the initial angle from `radians(20)` to a large angle, like `radians(80)`.
- **Your Task:** Run the simulation again and measure the period from the new graph.
- **Analysis:** Is the new measured period still close to `T_theory`? You will find that for large angles, the actual period is noticeably **longer** than the period predicted by the small angle formula. This shows the limit of the approximation.

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
!function(){var e={};async function t(){"use strict";canvas;var t,i,o,l,r,a,n,s,p,c,f,u,d,m,_,y,g,h,v,w,A,b,k,x,L,P,S,z,j,T,M,C=canvas();async function D(e){k=!k}for(t=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(e){return this.concat(e)},Array.prototype["*"]=function(e){return __array_times_number(this,e)},window.__GSlang="vpython",i=GSprint,o=range,l="__main__",r=pytype,(0,e.pythonize.strings)(),C.title="Simple Pendulum Motion",a=vector(0,3,0),n=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:a,radius:.1,color:color.gray(.5)})]),s=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({radius:.5,color:color.blue,make_trail:!0})]),p=ρσ_interpolate_kwargs.call(this,cylinder,[ρσ_desugar_kwargs({pos:a,radius:.05,color:color.yellow})]),c=0,f=.01,u=9.8,s.m=1,p.L=4,_=m=await radians(d=30),y=0,s.pos=a["+"](vector(p.L["*"](sin(_)),1["-u"]()["*"](p.L)["*"](cos(_)),0)),p.axis=s.pos["-"](1["*"](a)),g=2["*"](pi)["*"](sqrt(p.L["/"](u))),h=sqrt(u["/"](p.L)),C.caption="Initial Angle: "["+"](ρσ_str.format("{}",d))["+"](" degrees. Small Angle Approx. Period: ")["+"](ρσ_str.format("{:.2f}",g))["+"](" s"),v=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Angle vs. Time",xtitle:"Time (s)",ytitle:"Angle (rad)"})]),w=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.blue,label:"Simulation Angle"})]),A=_,b=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.black,label:"A*cos(omega*t)"})]),await C.pause("Click to Start"),k=!0,D.__argnames__||Object.defineProperties(D,{__argnames__:{value:["evt"]},__module__:{value:null}}),C.bind("click",D);c["<"](2["*"](g));)await rate(100),k&&(x=1["-u"]()["*"](u["/"](p.L))["*"](sin(_)),y=y["+"](x["*"](f)),_=_["+"](y["*"](f)),s.pos=a["+"](vector(p.L["*"](sin(_)),1["-u"]()["*"](p.L)["*"](cos(_)),0)),p.axis=s.pos["-"](1["*"](a)),w.plot(c,_),L=A["*"](cos(h["*"](c))),b.plot(c,L),c=c["+"](f));i("Simulation finished."),i("Theoretical Period (Small Angle Approx): "["+"](ρσ_str.format("{:.2f}",g))["+"](" s")),S=ρσ_getitem(ρσ_getitem(P=w.data,0),0);var G=range(10,len(P));for(var I of G="function"==typeof G[Symbol.iterator]?G instanceof Map?G.keys():G:Object.keys(G))if(ρσ_getitem(ρσ_getitem(P,T=I),1)["<"](ρσ_getitem(ρσ_getitem(P,T["-"](1["*"](1))),1))&&ρσ_getitem(ρσ_getitem(P,T["-"](1["*"](2))),1)["<"](ρσ_getitem(ρσ_getitem(P,T["-"](1["*"](1))),1))){j=(z=ρσ_getitem(ρσ_getitem(P,T["-"](1["*"](1))),0))["-"](1["*"](S)),i("Measured Period from graph: "["+"](ρσ_str.format("{:.2f}",j))["+"](" s"));break}M=abs(j["-"](1["*"](g)))["/"](g)["*"](100),i("Difference from small angle approx: "["+"](ρσ_str.format("{:.2f}",M))["+"]("%"))}e.pythonize={},function(){function t(){if(t=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)i=arguments[0]?Array.prototype.slice.call(arguments):null;else{var e;i=((e=ρσ_set()).jsset.add("split"),e.jsset.add("replace"),e)}i&&(t=t.difference(set(i)));var t,i,o,l=t;for(var r of l="function"==typeof l[Symbol.iterator]?l instanceof Map?l.keys():l:Object.keys(l))o=r,(ρσ_expr_temp=String.prototype)["number"==typeof o&&o<0?ρσ_expr_temp.length+o:o]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof o&&o<0?ρσ_expr_temp.length+o:o]}t.__module__||Object.defineProperties(t,{__module__:{value:"pythonize"}}),e.pythonize.strings=t}(),t.__module__||Object.defineProperties(t,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},t()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/92bcc34898ba" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  The motion of a simple pendulum is considered Simple Harmonic Motion (SHM) only when:
    a) The mass of the bob is very small.
    b) The length of the string is very long.
    c) The pendulum is in a vacuum.
    d) The angle of swing is small.

2.  If you take a pendulum from Earth to the Moon, where gravity is weaker, what will happen to its period?
    a) The period will increase.
    b) The period will decrease.
    c) The period will remain the same.
    d) The period will become zero.

3.  Two pendulums are created. Pendulum A has a 1 kg bob and a 1 m long string. Pendulum B has a 2 kg bob and a 1 m long string. How do their periods compare when they are swung at small angles?
    a) Period of A is greater than B.
    b) Period of B is greater than A.
    c) Their periods are equal.
    d) It cannot be determined without knowing the amplitude.

4.  The restoring force for a pendulum is provided by:
    a) The tension in the string.
    b) The entire force of gravity (`mg`).
    c) The component of gravity perpendicular to the swing path.
    d) The component of gravity tangential to the swing path.

5.  A student performs an experiment and finds that the period of her pendulum is longer than the one predicted by the formula `T = 2π * sqrt(L / g)`. What is the most likely reason for this discrepancy?
    a) The mass of the bob was too heavy.
    b) The length of the string was measured incorrectly.
    c) The amplitude of the swing was too large.
    d) The local value of `g` was smaller than expected.

### Problem-Solving Questions

1.  What is the period of a simple pendulum with a length of 2.45 m on Earth? (Use g = 9.8 m/s²)
    a) 1.57 s
    b) 3.14 s
    c) 6.28 s
    d) 9.8 s

2.  A pendulum has a period of 4.0 s. What is the length of the pendulum? (Use g = 9.8 m/s²)
    a) 1.6 m
    b) 2.5 m
    c) 4.0 m
    d) 15.8 m

3.  A pendulum with a length of 1.0 m is taken to a planet where its period is found to be 5.0 s. What is the acceleration due to gravity (`g`) on this planet?
    a) 1.58 m/s²
    b) 2.5 m/s²
    c) 3.95 m/s²
    d) 9.8 m/s²

4.  A pendulum of length `L` has a period `T`. What must be done to the length of the pendulum to double its period?
    a) The length must be halved.
    b) The length must be doubled.
    c) The length must be quadrupled.
    d) The length must be multiplied by sqrt(2).

5.  A pendulum bob is released from rest at a height of 0.1 m above its lowest point. What is the speed of the bob at the bottom of its swing? (Use g = 9.8 m/s²)
    a) 0.99 m/s
    b) 1.4 m/s
    c) 1.96 m/s
    d) 9.8 m/s

### Computational Questions

1.  The simulation calculates the restoring force on the pendulum. For it to be true SHM, this force must be proportional to `theta`. Instead, the true restoring force is proportional to:
    a) `cos(theta)`
    b) `sin(theta)`
    c) `tan(theta)`
    d) `theta²`

2.  The simulation asks you to compare the measured period for a large angle (e.g., 80 degrees) to the theoretical period from the formula `T = 2π * sqrt(L / g)`. What do you expect to find?
    a) The measured period will be shorter than the theoretical period.
    b) The measured period will be longer than the theoretical period.
    c) The measured period will be exactly the same as the theoretical period.
    d) The simulation will crash at large angles.

3.  The "small angle approximation" works because for small angles (in radians), `sin(theta)` is approximately equal to:
    a) `cos(theta)`
    b) `1`
    c) `theta`
    d) `0`

4.  If you were to add a line `print(bob.pos.x, bob.velocity.x)` inside the simulation loop, where would you expect `bob.velocity.x` to be zero?
    a) At the lowest point of the swing (`x=0`).
    b) At the highest points of the swing (the endpoints).
    c) The velocity is never zero.
    d) The velocity is always constant.

5.  To correctly calculate the theoretical period in the simulation code, which variables are needed for the formula `T = 2π * sqrt(L / g)`?
    a) `bob.mass` and `g`
    b) `rod.L` and `g`
    c) `bob.mass` and `rod.L`
    d) `initial_angle` and `g`

---
### Answer Key
**Conceptual:** 1. (d), 2. (a), 3. (c), 4. (d), 5. (c)
**Problem-Solving:** 1. (b), 2. (c), 3. (a), 4. (c), 5. (b)
**Computational:** 1. (b), 2. (b), 3. (c), 4. (b), 5. (b)
