from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for _ in range(6):
    robotArm.grab()
    for _ in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range(8):
        robotArm.moveLeft()
robotArm.grab()
for _ in range(8):
    robotArm.moveRight()
robotArm.drop()


robotArm.wait()