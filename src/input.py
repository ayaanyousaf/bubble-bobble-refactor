from dataclasses import dataclass

@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool


    
