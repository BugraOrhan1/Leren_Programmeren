from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for _ in range(7):
    robotArm.moveRight()


for _ in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if _ <=6: 
        robotArm.moveLeft()
        robotArm.moveLeft()

  
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()