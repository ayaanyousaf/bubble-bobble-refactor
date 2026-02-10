from pgzero.builtins import keyboard

# Is the space bar currently being pressed down?
space_down = False

# Has the space bar just been pressed? i.e. gone from not being pressed, to being pressed
def space_pressed():
    global space_down
    if keyboard.space:
        if space_down:
            # Space was down previous frame, and is still down
            return False
        else:
            # Space wasn't down previous frame, but now is
            space_down = True
            return True
    else:
        space_down = False
        return False