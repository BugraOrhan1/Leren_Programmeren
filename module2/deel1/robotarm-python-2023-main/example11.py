from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
for _ in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()