# Digital-Control-Systems-Lab


Autonomous navigation, maze exploration, and PID-based control of an e-puck robot in Webots.

This repository contains the implementation of two major laboratory mini-projects developed for the **Computer Controlled Systems** course .

The projects focus on combining **robotics**, **search algorithms**, and **feedback control systems** in a simulated environment.

---

## 🧠 Skills Demonstrated

- Autonomous robotic navigation  
- BFS & DFS search strategies  
- PID controller design and tuning  
- Sensor-based feedback control  
- Line following and trajectory correction  
- Working with encoders and proximity sensors  
- Modular controller implementation in Python  
- Simulation in Webots  

---

---

# Mini Project 1 — Maze Navigation and Line Following with PID Control

## Objective
To design a fully autonomous system capable of navigating inside a maze, detecting line-following zones, accurately tracking the lines using closed-loop control, and returning to the starting point.

## System Description
The robot begins at a predefined starting position and explores the maze to locate **two line-following areas**.  
Each zone includes a black path on a white surface.

Upon entering a zone, the robot must:

- detect the line via ground sensors  
- compute tracking error  
- apply PID correction to wheel speeds  
- follow the path until completion  
- exit back into the maze  

After completing both zones, the robot navigates back to its initial location.

The system relies on continuous feedback from:

- ground sensors  
- wheel encoders  
- proximity sensors  

to guarantee robust and stable behavior.

## Control Strategy
A reusable **PID controller** is implemented and utilized for:

- straight motion regulation  
- turning maneuvers  
- heading correction  
- line following  

Motor commands are continuously updated according to the measured error.

## Success Criteria
- Detection of both line-following zones.
- Smooth and accurate tracking performance.
- Proper use of closed-loop control.
- Fully autonomous execution.
- Successful return to the start point.

## Deliverables
- Full Python controller implementation.
- PID class and parameter tuning.
- Integrated navigation and tracking logic.
- Technical documentation.
- Demonstration video.

---

---

# Mini Project 2 — Maze Traversal using Search Algorithms and Line Following

## Objective
To implement autonomous maze exploration combined with accurate line-following behavior using feedback control strategies.

## System Description
The robot must navigate inside the maze, discover two dedicated line-following zones, complete the tracking tasks, and finally return to the starting point without human intervention.

The environment is treated as a graph in which cells correspond to nodes and feasible movements define edges.  
During exploration, the robot incrementally builds knowledge of the environment using onboard sensors.

When a line-following zone is reached, the robot must:

- detect the black line on a white background  
- compute the lateral tracking error  
- apply PID-based velocity corrections  
- follow the line until the segment is completed  
- exit the zone and resume maze navigation  

## Algorithmic Approach
The system integrates:

- maze traversal using **BFS** or **DFS**  
- visited-state management  
- decision making at intersections  
- transition between exploration mode and line-following mode  
- path memory for returning to the start position  

## Success Criteria
- Successful exploration of reachable maze areas.
- Detection and completion of both line-following zones.
- Stable and accurate PID-based tracking.
- Fully autonomous operation.
- Correct return to the starting point.

## Deliverables
- Implementation of search and navigation algorithms.
- PID-based line-following controller.
- Integration within the Webots simulation.
- Documentation of methodology and results.

---


