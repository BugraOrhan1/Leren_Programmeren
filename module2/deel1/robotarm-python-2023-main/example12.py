from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
teller = 9
left= 8
for _ in range(9):
    robotArm.grab()
    color = robotArm.scan()
    print(color)
    if color == 'red':
        print(teller)
        for _ in range(teller): 
            robotArm.moveRight()
        
        robotArm.drop()
        for _ in range(left): 
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    teller -= 1
    left-=1 
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()