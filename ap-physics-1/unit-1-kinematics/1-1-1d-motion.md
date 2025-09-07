---
title: "1.1 - 1D Motion"
layout: default
---
# Information: 1D Motion

## 1. Introduction to the Unit: Kinematics

Welcome to the study of motion! Kinematics is the branch of physics that describes how objects move, without getting into the reasons *why* they move. It's the language we use to talk about motion. Before we can analyze the forces that cause a car to accelerate (which is called **Dynamics**), we first need a precise way to describe the car's position, its velocity, and its acceleration. This unit provides the foundational concepts and equations for describing motion in one dimension (a straight line).

## 2. Relevant Physics Concepts

### Position, Velocity, and Acceleration

- **Position (`x`):** An object's location at a specific point in time. In VPython, this is a **vector**, which has both a magnitude and a direction (e.g., `vector(5, 0, 0)` means 5 meters along the x-axis).
- **Velocity (`v`):** The rate at which an object's position changes. It is also a vector, representing both the object's **speed** and its **direction**.
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
!function(){var t={};async function e(){"use strict";canvas;var e,o,i,l,r,a,s,n,c,p,u,y,f,d,h,m,v,g,w,_=canvas();function j(t,e=0){return Number(t.toFixed(e))}for(e=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(t){return this.concat(t)},Array.prototype["*"]=function(t){return __array_times_number(this,t)},window.__GSlang="vpython",o=GSprint,i=range,l="__main__",r=pytype,(0,t.pythonize.strings)(),_.title="Simulation of Projectile Motion",_.caption="A yellow ball is launched at an angle. A red ball is dropped at the same time.\nNotice they hit the ground simultaneously, showing independence of vertical and horizontal motion.",a=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(0,1["-u"]()["*"](.5),0),size:vector(45,.1,10),color:color.green})]),(s=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(1["-u"]()["*"](20),0,0),radius:.4,color:color.yellow})])).trail=ρσ_interpolate_kwargs.call(this,attach_trail,[s].concat([ρσ_desugar_kwargs({color:color.yellow,radius:.05})])),(n=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(s.pos.x,15,0),radius:.4,color:color.red})])).trail=ρσ_interpolate_kwargs.call(this,attach_trail,[n].concat([ρσ_desugar_kwargs({color:color.red,radius:.05})])),c=0,p=.01,u=9.8,y=25,f=await radians(50),s.pos=vector(1["-u"]()["*"](20),.4,0),s.velocity=vector(y["*"](cos(f)),y["*"](sin(f)),0),s.acceleration=vector(0,1["-u"]()["*"](u),0),n.pos=vector(1["-u"]()["*"](20),15,0),n.velocity=vector(0,0,0),n.acceleration=vector(0,1["-u"]()["*"](u),0),o("Launching projectile with speed="["+"](ρσ_str.format("{}",y))["+"](" m/s at angle=")["+"](ρσ_str.format("{:.1f}",await degrees(f)))["+"](" degrees.")),o("Dropping red ball from height="["+"](ρσ_str.format("{}",n.pos.y))["+"](" m.")),d=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Projectile Motion",xtitle:"Time (s)",ytitle:"Value"})]),h=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.yellow,label:"Projectile Y-Position (m)"})]),m=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.red,label:"Projectile Y-Velocity (m/s)"})]),v=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.blue,label:"Projectile X-Position (m)"})]);s.pos.y[">="](0)||n.pos.y[">="](0);)await rate(100),s.pos.y[">="](0)&&(s.velocity=s.velocity["+"](s.acceleration["*"](p)),s.pos=s.pos["+"](s.velocity["*"](p)),h.plot(c,s.pos.y),m.plot(c,s.velocity.y),v.plot(c,s.pos.x)),n.pos.y[">="](0)&&(n.velocity=n.velocity["+"](n.acceleration["*"](p)),n.pos=n.pos["+"](n.velocity["*"](p))),c=c["+"](p);o("Simulation finished."),o("Projectile landed at x = "["+"](ρσ_str.format("{:.2f}",s.pos.x))["+"](" m after ")["+"](ρσ_str.format("{:.2f}",c))["+"](" s")),g=y["*"](sin(f))["+"](sqrt(Math.pow(y["*"](sin(f)),2)["+"](2["*"](u)["*"](s.pos.y))))["/"](u),w=y["*"](cos(f))["*"](g),o("Theoretical time: "["+"](ρσ_str.format("{:.2f}",g))["+"](" s"))}t.pythonize={},function(){function e(){if(e=set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" ")),arguments.length)o=arguments[0]?Array.prototype.slice.call(arguments):null;else{var t;o=((t=ρσ_set()).jsset.add("split"),t.jsset.add("replace"),t)}o&&(e=e.difference(set(o)));var e,o,i,l=e;for(var r of l="function"==typeof l[Symbol.iterator]?l instanceof Map?l.keys():l:Object.keys(l))i=r,(ρσ_expr_temp=String.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]=(ρσ_expr_temp=ρσ_str.prototype)["number"==typeof i&&i<0?ρσ_expr_temp.length+i:i]}e.__module__||Object.defineProperties(e,{__module__:{value:"pythonize"}}),t.pythonize.strings=e}(),e.__module__||Object.defineProperties(e,{__module__:{value:null}}),$(function(){window.__context={glowscript_container:$("#glowscript").removeAttr("id")},e()})}();
//--><!]]></script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/68e87bb52311" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
