def delay(ms):
    initTime = robot.getTime()      # Store starting time (in seconds)
    while robot.step(timestep) != -1:
        if (robot.getTime() - initTime) * 1000.0 > ms: # If time elapsed (converted into ms) is greater than value passed in
            break

    
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()
def run_robot():
    pass
    
path=[]

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

#leftMotor.setPosition(10.0)
#rightMotor.setPosition(10.0)

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
# # set up the motor speeds at 10% of the MAX_SPEED.
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# initialize sensors
gs = []
gsNames = ['gs0', 'gs1', 'gs2']
for i in range(3):
    gs.append(robot.getDevice(gsNames[i]))
    gs[i].enable(timestep)

ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(timestep)

# encoders
encoder = []
encoderNames = ['left wheel sensor', 'right wheel sensor']
for i in range(2):
    encoder.append(robot.getDevice(encoderNames[i]))
    encoder[i].enable(timestep)

oldEncoderValues = []
OnLine = False
paved=0
once =True
def read_sensors():
    global right_obstacle, left_obstacle, front_obstacle,line_center,line_left,line_right
    gsValues = []
    for i in range(3):
        gsValues.append(gs[i].getValue())
    
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    line_right = gsValues[0]
    line_center = gsValues[1]
    line_left = gsValues[2]
     
    encoderValues = []
    for i in range(2):
        encoderValues.append(encoder[i].getValue())    # [rad]
        
    # Update old encoder values if not done before
    if len(oldEncoderValues) < 2:
        for i in range(2):
            oldEncoderValues.append(encoder[i].getValue())   

        
    # detect obstacles
    right_obstacle = psValues[0] > 80.0 or psValues[1] > 80.0 or psValues[2] > 80.0
    left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0 or psValues[7] > 80.0
    front_obstacle=psValues[0].getValue()>80 or psValues[7].getValue()>80

def turnRight():
    global path,pre_left_obstacle
    print("right")
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(750)
    moveforward()
    if not Back:
        path.append("l")
    pre_left_obstacle=True
    
    

def Turnback():
        global once
        print("back")
        leftMotor.setVelocity(-.5 * MAX_SPEED)
        rightMotor.setVelocity(-.5 * MAX_SPEED)
        delay(750)
        once=False


def TurnLeft():
    global path, pre_right_obstacle
    print("left")
    leftMotor.setVelocity(-.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(750) 
    pre_right_obstacle=True
    if not Back:
        path.append("r")
    moveforward()


    

def moveforward():
    global path
    print("moveforward")
    leftMotor.setVelocity(MAX_SPEED)
    rightMotor.setVelocity(MAX_SPEED)
    delay(750) 
    if not Back:   
        path.append("b")

def direction_chooser():
    global paved
    if not OnLine and paved==0:
        x=comparator()
        match x:
            case "l":
                TurnLeft()
            case "mf":
                if not front_obstacle:
                    moveforward()
                elif front_obstacle:
                    turnRight()
    elif OnLine and paved==1 :
        x=comparator()
        match x:
            case "r":
                turnRight()
            case "mf":
                if not front_obstacle:
                    moveforward()
                else:
                    TurnLeft()
    elif paved !=2:
        paved+=1
        Line()
    else:
        turnBack()
    


def moveahead():
    print("moveahead")
    leftMotor.setVelocity(MAX_SPEED)
    rightMotor.setVelocity(MAX_SPEED)
    delay(750)
def comparator():
    if pre_left_obstacle:
        if not left_obstacle:
            pre_left_obstacle=False
            return "l" 
    elif pre_right_obstacle:
        if not right_obstacle:
            pre_right_obstacle=False
            return "r"
    else:
        return "mf"

def Line():
    pass
def turnBack():
    global Back
    Back=True
    if once:
        Turnback()
    for directions in range(len(path)):
        x=path.pop()
        moves(x)

    
def moves(x):
    global end
    if len(path)==0:
        match x:
            case "b":
                moveforward()
            case "l":
                TurnLeft()
            case "r":
                turnRight()
    else :
        end=True
# Main loop:
while robot.step(timestep) != -1:
    # Read the sensors:
    read_sensors()
    #choose the direction
    if not end:
        direction_chooser()
    else:
        break

    

leftMotor.setVelocity(0)
rightMotor.setVelocity(0)