from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for _ in range(5):
    robotArm.moveRight()
robotArm.drop()

for _ in range(4):
        robotArm.moveLeft()
robotArm.grab()
for _ in range(5):
        robotArm.moveRight()
robotArm.drop()
for _ in range(5):
        robotArm.moveLeft()
robotArm.grab()
for _ in range(5):
        robotArm.moveRight()
robotArm.drop()
for _ in range(4):
        robotArm.moveLeft()
robotArm.grab()
for _ in range(5):
        robotArm.moveRight()
robotArm.drop()
for _ in range(2):
    for _ in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for _ in range(5):
        robotArm.moveRight()
    robotArm.drop() 
for _ in range(4):
        robotArm.moveLeft()
robotArm.grab()
for _ in range(5):
        robotArm.moveRight()
robotArm.drop()
for _ in range(3):
    for _ in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for _ in range(5):
        robotArm.moveRight()
    robotArm.drop() 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()