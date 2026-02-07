# Digital-Control-Systems-Lab


Autonomous navigation, maze exploration, and PID-based control of an e-puck robot in Webots.

This repository contains the implementation of two major laboratory mini-projects developed for the **Computer Controlled Systems** course at **Amirkabir University of Technology**.

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

# Mini Project 2 — Maze Traversal using Search Algorithms

## Objective
To implement and evaluate classical search algorithms for complete maze exploration using an autonomous mobile robot.

## System Description
The robot must traverse the environment, visit all reachable cells, and return to the starting position without human intervention.

The maze is modeled as a graph where nodes represent cells and edges correspond to feasible transitions.

One of the following algorithms is employed:

- **Depth-First Search (DFS):** Deep exploration with systematic backtracking.
- **Breadth-First Search (BFS):** Level-wise exploration ensuring structured coverage.

During navigation, the robot builds an internal map using real-time sensor measurements.

## Algorithmic Approach
The implementation includes:

- environment perception  
- visited-state tracking  
- decision making at intersections  
- backtracking or queue-based expansion depending on the strategy  

## Success Criteria
- Complete coverage of accessible areas.
- Correct real-time execution.
- Reliable autonomous navigation.
- Return to the initial position.

## Deliverables
- Implementation of BFS or DFS.
- Webots controller integration.
- Documentation of methodology and results.

---

---

## 🛠 Technologies Used

- **Python**
- **Webots R2023b**
- e-puck robot model
- Feedback control & estimation methods

---


