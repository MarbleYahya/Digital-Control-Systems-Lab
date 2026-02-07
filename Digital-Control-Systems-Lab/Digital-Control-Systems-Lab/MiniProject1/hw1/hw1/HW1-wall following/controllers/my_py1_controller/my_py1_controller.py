"""my_PYTHON_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
leftMotor =robot.getDevice('left wheel motor')
rightMotor =robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(.5*MAX_SPEED)
rightMotor.setVelocity(.5*MAX_SPEED)

ps=[]
psNames=['ps0','ps1','ps2','ps3','ps4','ps5','ps6','ps7']
for i in range(8):
   ps.append(robot.getDevice(psNames[i]))
   ps[i].enable(timestep)
# Main loop:
# - perform simulation steps until Webots is stopping the controller

while robot.step(timestep) != -1:
    psValues=[]
    for i in range(8):
        psValues.append(ps[i].getValue())
        
    #print(psValues)
    leftWall =ps[5].getValue()
    leftCenter=ps[6].getValue()
    frontWall= ps[7].getValue()
    
    left_speed= MAX_SPEED  
    right_speed= MAX_SPEED 
    

    if frontWall>90:
          left_speed= MAX_SPEED  
          right_speed= -MAX_SPEED
          
    else:
           if leftWall>90:
             left_speed= MAX_SPEED  
             right_speed= MAX_SPEED
           if leftCenter>90:
             left_speed= MAX_SPEED  
             right_speed= MAX_SPEED/8
           else:
             left_speed= MAX_SPEED/8  
             right_speed= MAX_SPEED
       
    
    leftMotor.setVelocity(left_speed)
    rightMotor.setVelocity(right_speed)    
     
    
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

# Enter here exit cleanup code.