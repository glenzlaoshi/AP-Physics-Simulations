---
title: "1.2 - Projectile Motion"
layout: default
---
# Information: 2D Projectile Motion

## 1. Introduction to the Unit: 2D Kinematics

This topic builds directly on 1D Kinematics. Instead of moving in a straight line, objects can now move in a two-dimensional plane (e.g., both horizontally and vertically). 

The single most important concept in 2D kinematics is the **independence of perpendicular motion**. This powerful idea means we can analyze the horizontal (x-direction) motion of an object completely separately from its vertical (y-direction) motion. The two components do not affect each other. The only thing they share is time (`t`).

The classic example of this is **projectile motion**: the motion of an object that is thrown or launched into the air and moves under the influence of gravity alone.

## 2. Relevant Physics Concepts

### The Independence of Motion

Imagine firing a cannonball from a cliff. Its motion can be broken down into two parts:

1.  **Horizontal (x-direction):** After the initial launch, there are no horizontal forces (we ignore air resistance). This means there is **zero horizontal acceleration**. The cannonball's horizontal velocity, `vx`, never changes.
2.  **Vertical (y-direction):** The only force acting on the cannonball is gravity, which pulls it straight down. This means there is a **constant downward acceleration**, `g` (approximately 9.8 m/s²). The vertical velocity, `vy`, is constantly changing.

### Equations for Projectile Motion

Because we can separate the components, we just use the 1D kinematic equations from the previous unit for each direction.

| Horizontal (x) Motion | Vertical (y) Motion |
| :--- | :--- |
| `ax = 0` | `ay = -g` |
| `vx = constant` | `vy_f = vy_i - g*t` |
| `x = x_i + vx*t` | `y = y_i + vy_i*t - 0.5*g*t²` |

### Initial Velocity Components

Typically, a projectile is launched with an initial speed `v0` at an angle `theta` above the horizontal. To analyze the motion, we must first break this initial velocity vector into its x and y components using trigonometry.

-   `vx_i = v0 * cos(theta)`
-   `vy_i = v0 * sin(theta)`

These initial components are then used in the kinematic equations above.

## 3. The Simulation: Modeling the Trajectory

### Outline of the Simulation

The `skeleton.py` file sets up a scene with a "projectile" (a sphere). Your goal is to use the principles of 2D kinematics to calculate the projectile's trajectory. You will give it an initial velocity and then, inside an animation loop, tell the computer how gravity affects its motion over time.

### Completing the `skeleton.py` File

#### **Task 1 & 2: Initial Velocity Components**

Before the simulation starts, you must calculate the initial x and y components of the projectile's velocity from the given speed `v0` and angle `theta`.

- **A Note on Angles:** Computer math functions like `cos()` and `sin()` expect angles to be in **radians**, not degrees. The skeleton file already converts the angle for you using `radians(45)`.

- **Example (x-component):** To calculate the initial x-velocity, you would write:
  ```python
  vx = v0 * cos(theta)
  ```
- **Your Task (y-component):** Following the example above, write the line of code to calculate the initial y-velocity, `vy`.

Once you have `vx` and `vy`, you can create the initial velocity vector for the VPython object:
`projectile.velocity = vector(vx, vy, 0)`

#### **Task 3: Define Acceleration**

After the projectile is launched, what is its acceleration? The only force is gravity. Therefore, the acceleration is constant and points downwards. Your task is to set the `projectile.acceleration` property to the correct vector value.

#### **Task 4: Update Motion in the Loop**

The animation loop runs as long as the projectile is above the ground (`while projectile.pos.y >= 0:`). Inside the loop, you must update the projectile's velocity and position. 

The great thing about using vectors is that the code is **exactly the same** as it was for 1D motion! VPython handles the x and y components automatically.

Your task is to add the two lines for numerical integration into the loop, just as you did in the previous simulation:
1.  Write the line to update `projectile.velocity` based on its acceleration.
2.  Write the line to update `projectile.pos` based on its new velocity.

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
!function(){var t={};async function e(){"use strict";canvas;var e,o,i,l,r,a,s,n,c,p,u,y,f,d,h,m,v,g,w,_=canvas();function j(t,e=0){return Number(t.toFixed(e))}for(e=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(t){return this.concat(t)},Array.prototype["*"]=function(t){return __array_times_number(this,t)},window.__GSlang="vpython",o=GSprint,i=range,l="__main__",r=pytype,(0,t.pythonize.strings)(),_.title="Simulation of Projectile Motion",_.caption="A yellow ball is launched at an angle. A red ball is dropped at the same time.\nNotice they hit the ground simultaneously, showing independence of vertical and horizontal motion.",a=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(0,1["-u"]()["*"](.5),0),size:vector(45,.1,10),color:color.green})]),(s=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(1["-u"]()["*"](20),0,0),radius:.4,color:color.yellow})])).trail=ρσ_interpolate_kwargs.call(this,attach_trail,[s].concat([ρσ_desugar_kwargs({color:color.yellow,radius:.05})])),(n=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(s.pos.x,15,0),radius:.4,color:color.red})])).trail=ρσ_interpolate_kwargs.call(this,attach_trail,[n].concat([ρσ_desugar_kwargs({color:color.red,radius:.05})])),c=0,p=.01,u=9.8,y=25,f=await radians(50),s.pos=vector(1["-u"]()["*"](20),.4,0),s.velocity=vector(y["*"](cos(f)),y["*"](sin(f)),0),s.acceleration=vector(0,1["-u"]()["*"](u),0),n.pos=vector(1["-u"]()["*"](20),15,0),n.velocity=vector(0,0,0),n.acceleration=vector(0,1["-u"]()["*"](u),0),o("Launching projectile with speed="["+"](ρσ_str.format("{}",y))["+"](" m/s at angle=")["+"](ρσ_str.format("{:.1f}",await degrees(f)))["+"](" degrees.")),o("Dropping red ball from height="["+"](ρσ_str.format("{}",n.pos.y))["+"](" m.")),d=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Projectile Motion",xtitle:"Time (s)",ytitle:"Value"})]),h=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.yellow,label:"Projectile Y-Position (m)"})]),m=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.red,label:"Projectile Y-Velocity (m/s)"})]),v=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.blue,label:"Projectile X-Position (m)"})]);s.pos.y[">="](0)||n.pos.y[">="](0);)await rate(100),s.pos.y[">="](0)&&(s.velocity=s.velocity["+"](s.acceleration["*"](p)),s.pos=s.pos["+"](s.velocity["*"](p)),h.plot(c,s.pos.y),m.plot(c,s.velocity.y),v.plot(c,s.pos.x)),n.pos.y[">="](0)&&(n.velocity=n.velocity["+"](n.acceleration["*"](p)),n.pos=n.pos["+"](n.velocity["*"](p))),c=c["+"](p);o("Simulation finished."),o("Projectile landed at x = "["+"](ρσ_str.format("{:.2f}",s.pos.x))["+"](" m after ")["+"](ρσ_str.format("{:.2f}",c))["+"](" s")),g=y["*"](sin(f))["+"](sqrt(Math.pow(y["*"](sin(f)),2)["+"](2["*"](u)["*"](s.pos.y))))["/"](u),w=y["*"](cos(f))["*"](g),o("Theoretical time: "["+"](ρσ_str.format("{:.2f}",g))["+"](" s"))}t.pythonize={},function(){function e(){if(e=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)o=arguments[0]?Array.prototype.slice.call(arguments):null;else{var t;o=((t=ρσ_set()).jsset.add("split"),t.jsset.add("replace"),t)}o&&(e=e.difference(set(o)));var e,o,i,l=e;for(var r of l="function"==typeof l[Symbol.iterator]?l instanceof Map?l.keys():l:Object.keys(l))i=r,(ρσ_expr_temp=String.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]}e.__module__||Object.defineProperties(e,{__module__:{value:"pythonize"}}),t.pythonize.strings=e}(),e.__module__||Object.defineProperties(e,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},e()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/acacd2fd38d4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
