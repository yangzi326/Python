# maze game

def turn_right():
    for i in range(3):
        turn_left()
        
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
