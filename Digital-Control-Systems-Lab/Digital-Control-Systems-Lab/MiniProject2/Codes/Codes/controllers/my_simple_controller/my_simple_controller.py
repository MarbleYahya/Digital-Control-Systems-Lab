
import time
def delay(ms):
    initTime = robot.getTime()      # Store starting time (in seconds)
    while robot.step(timestep) != -1:
        if (robot.getTime() - initTime) * 1000.0 > ms: # If time elapsed (converted into ms) is greater than value passed in
            break






from controller import Robot

MAX_SPEED = 6.28
BASE_SPEED = 0.4 * MAX_SPEED

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

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

face=("top")
def dir_translator(face,destination):

    if(destination=='right'):
       if (face=='top'):
          return[1,0]
       elif(face=='right'):
          return[0,-1]
       elif (face =='left'):
          return[0,1]
       elif (face=="down"):
          return[-1,0]
    if(destination=='left'):
       if (face=='top'):
          return[-1,0]
       elif(face=='right'):
          return[0,1]
       elif (face =='left'):
          return[0,-1]
       elif (face=='down'):
          return[1,0]      
    if(destination=='top'):
       if (face=='top'):
          return[0,1]
       elif(face=='right'):
          return[1,0]
       elif (face =='left'):
          return[-1,0]
       elif (face=='down'):
          return[0,-1] 
    if(destination=='down'):
       if (face=='top'):
          return[0,-1]
       elif(face=='right'):
          return[-1,0]
       elif (face =='left'):
          return[1,0]
       elif (face=='down'):
          return[0,1]    


def dir_face(face,destination):
    if(destination=='right'):
       if (face=='top'):
          return('right')
       elif(face=='right'):
          return("down")
       elif (face =='left'):
          return('top')
       elif (face=="down"):
          return('left')
    if(destination=='left'):
       if (face=='top'):
          return('left')
       elif(face=='right'):
          return('top')
       elif (face =='left'):
          return('down')
       elif (face=='down'):
          return('right')      
    if(destination=='top'):
       if (face=='top'):
          return('top')
       elif(face=='right'):
          return('right')
       elif (face =='left'):
          return('left')
       elif (face=='down'):
          return('down') 
    if(destination=='down'):
       if (face=='top'):
          return('down')
       elif(face=='right'):
          return('left')
       elif (face =='left'):
          return('right')
       elif (face=='down'):
          return('top')    
          
          
def converter(current,face,destination): 
    a =  dir_translator(face,destination)
    a[0] += current[0]
    a[1] += current[1]
    return a


def move_backward(path,face):
   print("kkkk")
   print(path)
   j=((path[-1][0])-(path[-2][0]))
   k=((path[-1][1])-(path[-2][1]))
   print(j)
   print(k)
   if [j,k ]== [0,1]:
      if (face=='top'):
         return('down')
      elif(face=='right'):
         return('right') 
      elif (face =='left'):
         return('left')
      elif (face=="down"): 
         return('top')    
   if [j,k] == [0,-1]:
      if (face=='top'):
         return('top')
      elif(face=='right'):
         return('left') 
      elif (face =='left'):
         return('right')
      elif (face=="down"): 
         return("down") 
   if [j,k] == [1,0]:
      if (face=='top'):
         return('left')
      elif(face=='right'):
         return("down") 
      elif (face =='left'):
         return('top')
      elif (face=="down"): 
         return('right') 
   if[j,k ]== [-1,0]:
      if (face=='top'):
         return('right')
      elif(face=='right'):
         return('top') 
      elif (face =='left'):
         return("down")
      elif (face=="down"): 
         return('left')
         
         
         
def move_direction_node(curcell,face):
   print("kkkk")
   print(path)
   j=((path[-1][0])-(curcell[0]))
   k=((path[-1][1])-(curcell[1]))
   print(j)
   print(k)
   if [j,k ]== [0,1]:
      if (face=='top'):
         return('down')
      elif(face=='right'):
         return('right') 
      elif (face =='left'):
         return('left')
      elif (face=="down"): 
         return('top')    
   if [j,k] == [0,-1]:
      if (face=='top'):
         return('top')
      elif(face=='right'):
         return('left') 
      elif (face =='left'):
         return('right')
      elif (face=="down"): 
         return("down") 
   if [j,k] == [1,0]:
      if (face=='top'):
         return('left')
      elif(face=='right'):
         return("down") 
      elif (face =='left'):
         return('top')
      elif (face=="down"): 
         return('right') 
   if[j,k ]== [-1,0]:
      if (face=='top'):
         return('right')
      elif(face=='right'):
         return('top') 
      elif (face =='left'):
         return("down")
      elif (face=="down"): 
         return('left')
         
         
def okpath(curcell,face,path,explored,destination):
    move_destination_node_path('top')
    if (frontWall<90 and converter(curcell,face,'top')  not in explored): 
        childcell= converter(curcell,face,'top') 
        explored.append(childcell)
    else:
        childcell= converter(curcell,face,'top')
    
    path.append(childcell)
    face=dir_face('top',face)
    move_destination(move_backward(path,face))
    face=dir_face(face,(move_backward(path,face)))
    
    
    move_destination_node_path('right')
    if (rightWall<90 and converter(curcell,face,'right')  not in explored): 
        childcell= converter(curcell,face,'right') 
        explored.append(childcell)
    else:
        childcell= converter(curcell,face,'right')
    
    path.append(childcell)
    face=dir_face('right',face)
    move_destination(move_backward(path,face))
    face=dir_face(face,(move_backward(path,face)))
    
    
    
    move_destination_node_path("down")
    if (behindWall<90 and converter(curcell,face,"down")  not in explored): 
        childcell= converter(curcell,face,"down") 
        explored.append(childcell)
    else:
        childcell= converter(curcell,face,"down")
    
    path.append(childcell)
    face=dir_face("down",face)
    move_destination(move_backward(path,face))
    face=dir_face(face,(move_backward(path,face)))
    
    
    
    move_destination_node_path('left')
    if (leftWall<90 and converter(curcell,face,'left')  not in explored): 
        childcell= converter(curcell,face,'left') 
        explored.append(childcell)
    else:
        childcell= converter(curcell,face,'left')
    
    path.append(childcell)
    face=dir_face('left',face)
    move_destination(move_backward(path,face))
    face=dir_face(face,(move_backward(path,face)))
    return  [explored,path]
    
    

   
           
def move_destination(destination) :         
      if(destination=='right'):
        leftMotor.setVelocity(.5 * MAX_SPEED)
        rightMotor.setVelocity(-.5 * MAX_SPEED)
        delay(750)
        leftMotor.setVelocity(.5 * MAX_SPEED)
        rightMotor.setVelocity(.5 * MAX_SPEED)
        delay(4000)
        leftMotor.setVelocity(0 * MAX_SPEED)
        rightMotor.setVelocity(0 * MAX_SPEED) 
           
      if(destination=='left'): 
          leftMotor.setVelocity(-.5 * MAX_SPEED)
          rightMotor.setVelocity(.5 * MAX_SPEED)
          delay(750)
          leftMotor.setVelocity(.5 * MAX_SPEED)
          rightMotor.setVelocity(.5 * MAX_SPEED)
          delay(4000)
          leftMotor.setVelocity(0 * MAX_SPEED)
          rightMotor.setVelocity(0 * MAX_SPEED) 
            
      if(destination=='top') : 
        leftMotor.setVelocity(.5 * MAX_SPEED)
        rightMotor.setVelocity(.5 * MAX_SPEED)
        delay(4000)
        leftMotor.setVelocity(0 * MAX_SPEED)
        rightMotor.setVelocity(0 * MAX_SPEED)
        
      if(destination=='down') :
        leftMotor.setVelocity(.5 * MAX_SPEED)
        rightMotor.setVelocity(-.5 * MAX_SPEED)
        delay(1500)
        leftMotor.setVelocity(.5 * MAX_SPEED)
        rightMotor.setVelocity(.5 * MAX_SPEED)
        delay(4000)
        leftMotor.setVelocity(0 * MAX_SPEED)
        rightMotor.setVelocity(0 * MAX_SPEED)
        
        
               
def sence():


  while robot.step(timestep) != -1:
    
    psValues=[]
    for i in range(8):
        psValues.append(ps[i].getValue())
    
    #print(psValues)
    
    leftWall =ps[5].getValue()
    behindWall=ps[4].getValue()
    frontWall= ps[7].getValue()
    rightWall =ps[2].getValue()
    print(psValues)
    return [leftWall,rightWall,behindWall,frontWall]                    
# Main loop:
# - perform simulation steps until Webots is stopping the controller

# Enter here exit cleanup code.
start=[0,0]
explored=[start]
path=[start]
curcell=start
temp_notWall=[False,False,False,False]

while len(explored)< 1000:
          #curcell=path.pop()
    print('mmmmmmmm')
          
    a =  sence()
    leftWall  =  a[0]
    rightWall = a[1]
    behindWall  = a[2] 
    frontWall  =  a[3]
          
          
               
                
    #top      
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(1600)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED)
    a =  sence()
    leftWall  =  a[0]
    rightWall = a[1]
    behindWall  = a[2] 
    frontWall  =  a[3]
    if frontWall<90:
       temp_notWall[0]=True
    else:
       temp_notWall[0]=False
    
    leftMotor.setVelocity(-.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(1600)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED)
        
        
    #r      
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(750)
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(1500)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED) 
    a =  sence()
    leftWall  =  a[0]
    rightWall = a[1]
    behindWall  = a[2] 
    frontWall  =  a[3]  
    if frontWall<90:
       temp_notWall[1]=True
    else:
       temp_notWall[1]=False
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(1500)
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)   
          
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(1600)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED)
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(800)
    
    
    #d
    leftMotor.setVelocity(-.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(1300)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED)
    a =  sence()
    leftWall  =  a[0]
    rightWall = a[1]
    behindWall  = a[2] 
    frontWall  =  a[3]
    if behindWall<90:
       temp_notWall[3]=True
    else:
       temp_notWall[3]=False
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(1300)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED)
    
   #l
    leftMotor.setVelocity(-.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(750)
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(1400)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED) 
    a =  sence()
    leftWall  =  a[0]
    rightWall = a[1]
    behindWall  = a[2] 
    frontWall  =  a[3]
    if frontWall<90:
       temp_notWall[2]=True
    else:
       temp_notWall[2]=False
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(-.5 * MAX_SPEED)
    delay(1500)
    leftMotor.setVelocity(.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(1400)
    leftMotor.setVelocity(0 * MAX_SPEED)
    rightMotor.setVelocity(0 * MAX_SPEED)
    leftMotor.setVelocity(-.5 * MAX_SPEED)
    rightMotor.setVelocity(.5 * MAX_SPEED)
    delay(750)                    
                   
          
    print(temp_notWall)         
    print  (face) 
    print(len(explored))
    print(explored)
          #b=okpath(curcell,face,path,explored,destination)
          #explored  =  b[0]
          #face =b[1]
    if (temp_notWall[0] and converter(curcell,face,'top')  not in explored): 
     
                 
                 
                    
                 move_destination('top')
                 childcell= converter(curcell,face,'top') 
                 explored.append(childcell)
                 path.append(childcell)
                 face=dir_face('top',face)
                 curcell=  childcell
          
    elif (temp_notWall[1] and converter(curcell,face,'right') not in explored):
                
                 
                 
                 move_destination('right')
                 childcell= converter(curcell,face,'right') 
                 explored.append(childcell)
                 path.append(childcell)
                 face=dir_face('right',face)
                 curcell=  childcell   
              
    elif (temp_notWall[2] and converter(curcell,face,'left') not in explored):
           
                 
                 
                 
                 move_destination('left')
                 childcell= converter(curcell,face,'left') 
                 explored.append(childcell)
                 path.append(childcell)
                 face=dir_face('left',face)
                 curcell=  childcell
             
    elif( temp_notWall[3] and converter(curcell,face,'down') not in explored): 
                
                 move_destination('down')
                 childcell= converter(curcell,face,'down') 
                 explored.append(childcell)
                 path.append(childcell)
                 face=dir_face('down',face)
                 curcell=  childcell
            
    else:
                
                move_destination(move_backward(path,face))
                face=dir_face(face,(move_backward(path,face)))
                path.pop(-1)
                curcell= path[-1]
                curcell=  childcell  

          
          
          
          

















          
          
          
          
