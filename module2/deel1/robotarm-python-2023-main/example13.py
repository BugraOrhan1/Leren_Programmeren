from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1, 7)

# Jouw python instructies zet je vanaf hier:
teller = 2
left = 1

robotArm.grab()
color = robotArm.scan()
if color == "":
    pass
else :
    robotArm.moveRight()
    robotArm.drop()

while color != "":
    print(teller)
    print(left)
    for _ in range(left):
        robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()  
    for _ in range(teller):
        robotArm.moveRight()
    color = robotArm.scan() 
    robotArm.drop()   
    teller += 1
    left += 1



# Na jouw code wachten tot het sluiten van het venster:
robotArm.wait()
