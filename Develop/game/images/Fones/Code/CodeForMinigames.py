def Helicopter (direction):
    print(direction)







actionToNow = open("Helicopter/Actions/ActionToNow.txt")
actions = actionToNow.read()

for numberAfAction in range(1, 4):
    action = actions[0 - numberAfAction]

    if (action == 'R'):
        Helicopter(0)
    elif (action == 'L'):
        Helicopter(1)
    elif (action == 'U'):
        Helicopter(2)
    elif (action == 'D'):
        Helicopter(3)
    else:
        Helicopter(4)