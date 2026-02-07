# Digital-Control-Systems-Lab
Mini Project 1 — Maze Navigation and Line Following with PID Control
Objective

Design an integrated autonomous robotic system that explores the maze, finds the line-following zones, completes the tracking tasks, and finally returns to the start position using feedback control.

Description

Starting from a designated initial position, the robot must navigate through the maze to locate two line-following zones.
Each zone contains a black line on a white background.

After entering a zone, the robot should:

detect the line using ground sensors

follow the path accurately

handle curves and deviations

exit the zone and return to the maze

After finishing both zones, the robot must navigate back to the starting point.

A PID controller is used to achieve stable and precise motion for straight driving, turning, and line tracking.
Sensor feedback from encoders and ground sensors continuously corrects motor speeds.

Success Criteria

The robot successfully discovers both line-following zones.

Line tracking is smooth and stable.

Closed-loop PID control is used instead of open-loop timing.

The robot returns to the initial starting position.

The system runs autonomously without manual help.

Deliverables

Complete code implementation.

PID controller class.

Integration of control with maze navigation.

Documentation explaining algorithms and tuning.

Video demonstration of the mission.
