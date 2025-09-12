---
title: "1.2 - Projectile Motion"
layout: default
---


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
!function(){var t={};async function e(){"use strict";canvas;var e,o,i,l,r,a,s,n,c,p,u,d,f,y,h,m,v,w,g,_,j=canvas();function P(t,e=0){return Number(t.toFixed(e))}async function b(t){w=!w}for(e=ρσ_list_decorate(["3.2","glowscript"]),Array.prototype["+"]=function(t){return this.concat(t)},Array.prototype["*"]=function(t){return __array_times_number(this,t)},window.__GSlang="vpython",o=GSprint,i=range,l="__main__",r=pytype,(0,t.pythonize.strings)(),j.title="Simulation of Projectile Motion",j.caption="A yellow ball is launched at an angle. Once at the maximum height, a red ball is thrown straight up with the same vertical speed.\nNotice they hit the ground simultaneously, showing independence of vertical and horizontal motion.",a=ρσ_interpolate_kwargs.call(this,box,[ρσ_desugar_kwargs({pos:vector(0,0,0),size:vector(45,.1,10),color:color.green})]),(s=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(1["-u"]()["*"(20)],0,0),radius:.4,color:color.yellow})])).trail=ρσ_interpolate_kwargs.call(this,attach_trail,[s].concat([ρσ_desugar_kwargs({color:color.yellow,radius:.05})])),(n=ρσ_interpolate_kwargs.call(this,sphere,[ρσ_desugar_kwargs({pos:vector(s.pos.x,0,0),radius:.4,color:color.red})])).trail=ρσ_interpolate_kwargs.call(this,attach_trail,[n].concat([ρσ_desugar_kwargs({color:color.red,radius:.05})])),c=0,p=.01,u=9.8,d=20,f=await radians(50),s.pos=vector(1["-u"]()["*"(20)],s.radius,0),s.velocity=vector(d["*"(cos(f)),d["*"(sin(f)),0),s.acceleration=vector(0,1["-u"]()["*"(u),0),n.pos=vector(1["-u"]()["*"(20)["-"](1["*"(2)["*"(n.radius)),n.radius,0),n.velocity=vector(0,d["*"(sin(f)),0),n.acceleration=vector(0,1["-u"]()["*"(u),0),o("Launching projectile with speed="["+"](ρσ_str.format("{}",d))["+"](" m/s at angle=")["+"](ρσ_str.format("{:.1f}",await degrees(f)))["+"](" degrees.")),o("Thrown red ball from ground="["+"](ρσ_str.format("{}",n.pos.y))["+"](" m.")),y=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Projectile Motion",xtitle:"Time (s)",ytitle:"Position (m)"})]),h=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.blue,label:"y_pos"})]),m=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.red,label:"x_pos"})]),v=ρσ_interpolate_kwargs.call(this,graph,[ρσ_desugar_kwargs({title:"Projectile Motion",xtitle:"Time (s)",ytitle:"Velocity (m/s)"})]),g=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.blue,label:"y_vel"})]),_=ρσ_interpolate_kwargs.call(this,gcurve,[ρσ_desugar_kwargs({color:color.red,label:"x_vel"})]),await j.pause("Click to Start"),w=!0,b.__argnames__||Object.defineProperties(b,{__argnames__:{value:["evt"]},__module__:{value:null}}),j.bind("click",b);s.pos.y[">="](0);)await rate(100),w&&(s.velocity=s.velocity["+"](s.acceleration["*"(p)),s.pos=s.pos["+"](s.velocity["*"(p)),c=c["+"](p),h.plot(c,s.pos.y),m.plot(c,s.pos.x),g.plot(c,s.velocity.y),_.plot(c,s.velocity.x));for(o("Projectile landed at t="["+"](ρσ_str.format("{:.2f}",c))["+"](" s, position=")["+"](ρσ_str.format("{}",s.pos)));n.pos.y[">="](0);)await rate(100),w&&(n.velocity=n.velocity["+"](n.acceleration["*"(p)),n.pos=n.pos["+"](n.velocity["*"(p)));o("Red ball landed at position=",n.pos)}e()["catch"](function(e){t.browser_send_error(e)})}();
//--><!]]>
</script>
</div>

## 5. Student Workspace

Use the editor below to complete the `skeleton.py` file. You can edit the code and run it directly in your browser to test your work.

<iframe src="https://trinket.io/embed/glowscript/acacd2fd38d4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## 6. Check Your Understanding

Test your knowledge with these multiple-choice questions.

### Conceptual Questions

1.  A cannonball is fired from a cannon at an angle of 45 degrees above the horizontal. If we ignore air resistance, what is the acceleration of the cannonball during its flight?
    a) Zero.
    b) A constant horizontal acceleration.
    c) A constant vertical acceleration, pointing downwards.
    d) An acceleration that changes depending on the ball's velocity.

2.  A hunter shoots an arrow horizontally from a height of 1.5 m. At the exact same moment, an identical arrow is dropped from the same height. Which arrow hits the ground first? (Ignore air resistance.)
    a) The arrow shot horizontally.
    b) The arrow that was dropped.
    c) They both hit the ground at the same time.
    d) It depends on how fast the arrow was shot.

3.  For a projectile launched at an angle, which of the following quantities is zero at the highest point of its trajectory?
    a) Horizontal velocity.
    b) Vertical velocity.
    c) Horizontal acceleration.
    d) Both b and c.

4.  At what angle should a projectile be launched to achieve the maximum horizontal range? (Assume no air resistance and a flat launch/landing surface.)
    a) 30 degrees.
    b) 45 degrees.
    c) 60 degrees.
    d) 90 degrees.

5.  Which of the following statements about the horizontal and vertical components of projectile motion is true?
    a) The horizontal velocity changes due to gravity.
    b) The vertical acceleration is always zero.
    c) The horizontal motion and vertical motion are independent of each other.
    d) The horizontal and vertical displacements are always equal.

### Problem-Solving Questions

1.  A ball is thrown with an initial velocity of 20 m/s at an angle of 30 degrees above the horizontal. What are the initial horizontal (vx) and vertical (vy) components of its velocity?
    a) vx = 10 m/s, vy = 17.3 m/s
    b) vx = 17.3 m/s, vy = 10 m/s
    c) vx = 20 m/s, vy = 20 m/s
    d) vx = 0 m/s, vy = 20 m/s

2.  A stone is thrown horizontally with a speed of 10 m/s from the top of a 49 m high cliff. How far from the base of the cliff does the stone land? (Use g = 9.8 m/s²)
    a) 10 m
    b) 31.3 m
    c) 49 m
    d) 100 m

3.  A projectile is fired with an initial vertical velocity of 30 m/s. How long does it take to reach the highest point of its trajectory? (Use g = 9.8 m/s²)
    a) 1.5 s
    b) 3.1 s
    c) 9.8 s
    d) 30 s

4.  A football is kicked from the ground at an angle of 60 degrees with an initial speed of 20 m/s. What is the total time the football is in the air? (Use g = 9.8 m/s²)
    a) 1.8 s
    b) 2.0 s
    c) 3.5 s
    d) 4.1 s

5.  A projectile has an initial horizontal velocity of 15 m/s and an initial vertical velocity of 20 m/s. What is its speed after 2 seconds? (Use g = 9.8 m/s²)
    a) 15.0 m/s
    b) 15.2 m/s
    c) 20.4 m/s
    d) 35.0 m/s

### Computational Questions

1.  In the VPython simulation, the projectile's acceleration is set as `projectile.acceleration = vector(0, -9.8, 0)`. Why is the x-component of this vector zero?
    a) Because the projectile is not moving horizontally.
    b) To make the simulation run faster.
    c) Because gravity only acts in the vertical direction (ignoring air resistance).
    d) It is a mistake; the x-component should be 9.8.

2.  The simulation loop continues `while projectile.pos.y >= 0`. What does this condition represent in the context of the physics simulation?
    a) It runs as long as the projectile's speed is positive.
    b) It runs as long as the projectile is on or above the ground.
    c) It runs until the projectile reaches its maximum height.
    d) It runs for a fixed number of seconds.

3.  If you wanted to simulate projectile motion on the Moon, where the acceleration due to gravity is about 1/6th of Earth's, how would you modify the code?
    a) Change `projectile.velocity` to be 1/6th of its initial value.
    b) Change `dt` to `dt / 6`.
    c) Change `projectile.acceleration` to `vector(0, -9.8 / 6, 0)`.
    d) Change the `while` loop condition to `while projectile.pos.y >= -6`.

4.  The code `projectile.velocity = projectile.velocity + projectile.acceleration * dt` is used to update the velocity. Why is this an approximation of the true motion?
    a) Because it incorrectly assumes acceleration is constant.
    b) Because it calculates the new velocity based on the acceleration over a discrete time step `dt`, not continuously.
    c) Because VPython vectors are not precise enough for physics.
    d) Because it doesn't account for the projectile's mass.

5.  To calculate the initial velocity components, the code uses `sin(theta)` and `cos(theta)`. What would happen if you forgot to convert the launch angle `theta` from degrees to radians before using these functions?
    a) The simulation would run correctly, as Python's math functions handle both.
    b) The initial velocity components would be calculated incorrectly, leading to a wrong trajectory.
    c) The program would produce a syntax error.
    d) The horizontal motion would be correct, but the vertical motion would be wrong.

---
### Answer Key
**Conceptual:** 1. (c), 2. (c), 3. (d), 4. (b), 5. (c)
**Problem-Solving:** 1. (b), 2. (b), 3. (b), 4. (c), 5. (b)
**Computational:** 1. (c), 2. (b), 3. (c), 4. (b), 5. (b)
